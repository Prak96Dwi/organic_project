""" apps/food/views.py """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.cache import never_cache
from django.conf import settings

from taggit.models import Tag

from .forms import FoodInsertForm, FoodCategoryForm
from .models import (
	Food, FoodCategory, Review
)

from apps.blog.models import Blog, BlogCategory


def index(request):
	"""
	This function will display the dashboard to user
	"""
	food_categories = FoodCategory.objects.get_queryset()
	featured_foods = Food.objects.featured_foods()
	latest_blogs = Blog.objects.latest_blogs()

	return render(
		request,
		'food/index.html', {
			'categories': food_categories,
			'foods': featured_foods,
			'blogs': latest_blogs
		}
	)


def admin_dashboard(request):
	"""
	This function will display the admin dashboard
	"""

	return render(request, 'admin/admin_dashboard.html', {})


@login_required(login_url='user_login_form')
def food_form(request):
	"""
	This function will display the food insert form 
	to the user
	"""
	if request.method == "POST":
		food_form = FoodInsertForm(request.POST, request.FILES)
		if food_form.is_valid():
			food = food_form.save()
			food.resize_food_image()
		return redirect('index')
	else:
		food_form = FoodInsertForm()
	return render(request, 'food/food_form.html', {'form': food_form})


@login_required(login_url='user_login_form')
def food_list_page(request):
	"""
	This function will display the list of
	food data to admin
	"""
	foods = Food.objects.get_queryset()
	return render(request, 'food/food_list.html', {'foods': foods})


@login_required(login_url='user_login_form')
def food_edit_form(request, id):
	"""
	This function will display the food object edit form
	to the user

	Params:
	1. id : int
	    Food object id

	Returns:
	1. food detail of that particular food.
	2. all food categoires
	3. Food editing  form

	"""
	food = get_object_or_404(Food, pk=id)
	food_categories = FoodCategory.objects.get_queryset()
	if request.method == "POST":
		form = FoodInsertForm(request.POST, instance=food)
		if form.is_valid():
			form.save()
			return redirect('food_edit_form_view')
	else:
		form = FoodInsertForm(instance=food)
	context = {'form': form, 'categories': food_categories}

	return render(request, 'food/food_edit_form.html', context)


@login_required(login_url='user_login_form')
def category_form_view(request):
	"""
	This function will display the category form
	to the admin

	"""
	if request.method == 'POST':
		food_category_form = FoodCategoryForm(request.POST, request.FILES)
		if food_category_form.is_valid():
			food_category_form.save()
			return redirect('food_form_view')
	else:
		food_category_form = FoodCategoryForm()

	return render(request, 'category/category_form.html', {'form': food_category_form})


def category_list_view(request):
	"""
	This function is used to display the food
	category list to the admin.

	"""
	categories = FoodCategory.objects.get_queryset()
	return render(request, 'category/food_category_list.html', {'categories': categories})


def category_edit_form(request, id):
	"""
	This function is used to display the category edit form.

	Arguments
	-----------
	id : int
	    Food category object id.

	"""

	food_category = get_object_or_404(FoodCategory, pk=id)

	if request.method == 'POST':
		food_category.name = request.POST.get('category_name')
		food_category.image = request.FILES.get('cat_image')
		food_category.save()

		return redirect('category_list_view')

	return render(request, 'category/food_category_edit_form.html', {'food_category':food_category})


def shop_details_page(request, id):
	"""
	This function is used to display the information 
	of particular product

	Params:
	1. id : int
	    Food object id.

	"""
	# Retreiving food object from given food food_id
	food = get_object_or_404(Food, pk=id)

	# Retreiving review objects of particular food object
	food_product_reviews = Review.objects.food_product_review(food)

	# Retreiving food objects of particular food category
	food_product_of_particular_category = Food.objects.foods_by_category(food.category)

	# Retreiving product average rate of food products
	product_average_rate = Review.objects.average_rate_of_food_product_reviews(
		food_product_reviews
	)

	if request.method == 'POST':
		food_review = request.POST.get('revew_data')
		Review.objects.create(
			reviewer=request.user,
			food=food,
			review_text=food_review
		)

		return redirect('product_detail_page', id=food.id)

	context = {
		'food': food,
		'foods': food_product_of_particular_category,
		'reviews': food_product_reviews, 
		'number_of_reviews': len(food_product_reviews),
		'average_rate': product_average_rate
	}
	return render(request, 'food/shop_details.html', context)


@login_required(login_url='user_login_form')
@never_cache
def checkout_page(request):
	"""
	This function is used to display the
	checkout page to a particular client.

	"""
	cart = get_object_or_404(Cart, user=request.user)
	shipping = Shipping.objects.all()

	if cart.sum_of_products_price == 0:
		return redirect('shopping_cart_page')

	context = {
		'cart_details': cart,
		'shipping_data': shipping
	}
	return render(request, 'food/checkout.html', context)


def shop_grid_page(request, range=settings.HIGH_TO_LOW):
	"""
	This page is used to display the shop grid
	page to the user

	In Get request, price, weight and categories list is retreived
	if length of price, category and weight is not zero.  

	"""
	if request.method == 'GET':
		price = request.GET.get('mprice')
		weight = request.GET.get('wei')
		category = request.GET.getlist('cats')

		if (len(category) and len(price) and len(weight)) != 0:
			foods = Food.objects.food_of_specific_price_category_and_weight(
				price,
				category,
				weight
			)
			food_price_ordering_choice = settings.HIGH_TO_LOW			
		else:
			category = request.GET.get('cat', 'Fresh Fruit')
			food_of_particular_category = Food.objects.foods_by_category(category)

			if range == settings.HIGH_TO_LOW:
				foods = food_of_particular_category.order_by('-price')
				food_price_ordering_choice = settings.HIGH_TO_LOW
			else:
				foods = food_of_particular_category.order_by('price')
				food_price_ordering_choice = settings.LOW_TO_HIGH

	# Retrieving Category
	food_categories = FoodCategory.objects.all()
	# Creates Paginator objects
	paginator = Paginator(foods, 5)
	page_number = request.GET.get('page', 1)
	discount_foods = Food.objects.exclude(discount='0')

	try:
		page = paginator.get_page(page_number)  # returns the desired page object
	except PageNotAnInteger:
		# if page_number is not an integer then assign the first page
		page = paginator.page(1)
	except EmptyPage:
		# if page is empty then return last page,
		page = paginator.page(paginator.num_pages)

	maximum_price_value = Food.objects.maximum_food_products_price()
	minimum_price_value = Food.objects.minimum_food_products_price()
	maximum_weight = Food.objects.maximum_food_products_weight()
	minimum_weight = Food.objects.minimum_food_products_weight()

	context = {
		'number_of_foods': len(foods),
		'pages' : page, 
		'discount_foods' : discount_foods,
		'max_price' : str(maximum_price_value['price__max']),
		'min_price' : str(minimum_price_value['price__min']),
		'max_weight' : str(maximum_weight['weight__max']),
		'filter_choice' : food_price_ordering_choice,
		'food_categories' : food_categories
	}
	return render(request, 'food/shop_grid.html', context)


@login_required(login_url='user_login_form')
def contact_page(request):
	"""
	This function is used to display the contact page
	to the user
	"""
	return render(request, 'food/contact.html', {})


def food_order_list_page_view(request):
	"""
	This function display the list
	of food order to the client
	"""
	orders = Order.objects.all()
	return render(request, 'admin/food_order_data_list.html', {'ordered_data': orders})


def thank_you_page(request):
	"""
	This function is used to display the
	thank you page to the client when the client successfully
	make payment and checkout from website.

	"""
	return render(request, 'admin/thank_you_page.html', {})
