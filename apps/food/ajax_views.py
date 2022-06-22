""" apps/food/ajax_views.py """
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import (
	Food,
	FoodCategory,
	Review
)


def ajax_get_foodname(request):
	""" 
	AJAX method for getting the name 
	of food using autocomplete jquery plugin
	"""
	foods = Food.objects.all()
	food_names_list = [food.name for food in foods]

	return JsonResponse(tuple(food_names_list), safe=False)


def ajax_search_food_product_detail(request):
	"""
	This ajax function search for food product detail
	and returns as a JsonResponse to the page to display

	Params: 
	1. food_name : name of food product
	   type  : int

	"""
	food_name = request.GET.get("food_name")
	food = get_object_or_404(Food, name=food_name)
	choices = (int(food.id), )
	return JsonResponse(choices, safe=False)


def ajax_get_categories_name(request):
	"""
	This ajax function get food  category name when we type on search bar

	"""
	food_categories = list(FoodCategory.objects.all().values('name'))

	return JsonResponse(food_categories, safe=False)


def ajax_data_on_food_filter(request):
	"""
	This ajax function returns filtered food data

	Params:
	1. price : price of food product
	   type : int
	2. category ; category of food product
	   type : str
	3. weight : weight of food product
	   type : int

	"""
	price = request.GET.get('price')
	category = request.GET.get('category')
	weight = request.GET.get('wgt')
	food_filter_data = list(Food.objects.filter(food_price__lte=price[1:], 
											   food_category=category,
											   food_wgt__lte=weight).values())
	choices = ("Food Filtered Data", )

	return JsonResponse(choices, safe=False)


def ajax_update_rate_of_product(request):
	"""
	This ajax function update rate of  product

	Params :  Get Request
	1. food_id ; id of food product
	   type : int
	2. rate : rate of food product
	   type : int

	"""
	food_id =  request.GET.get('food_id')
	number_of_rate = request.GET.get('rate')
	# Retreive food object from food id
	food = get_object_or_404(Food, pk=food_id)

	try:
		review = Review.objects.get(
			foods=food, 
			reviewer=request.user
		)
		review.rating = number_of_rate
		review.save()

	except Review.DoesNotExist:
		Review.objects.create(
			foods=food,
			reviewer=request.user, 
			rating=number_of_rate
		)
	choices = ("Added your ratings", )

	return JsonResponse(choices, safe=False)


def ajax_update_food_order_data(request):
	"""
	This fuction is called for updating food order data

	Params:  Get Request
	1. cart_details_id : cart id
	   type: int
	2. total_price : total price of particular food which we want to update
	   type: int
	3. shipping_data : shipping id
	   type: int

	"""
	cart_id = request.GET.get('cart_details_id')
	total_price = request.GET.get('total_price')
	shipping_id = request.GET.get('shipping_data')

	cart = get_object_or_404(Cart, pk=cart_id)
	food_item_list = []

	for cart_product in cart.products.all():
		food_item = FoodItem.objects.create(
				food=cart_product.food, 
				quantity=cart_product.quantity,
				price=cart_product.food_price
		)
		food_item_list.append(food_item)
		cart_product.delete()

	# Create Shipping object
	shipping = get_object_or_404(Shipping, pk=shipping_id)

	# Create Food Order object
	order = Order.objects.create(
		  user=request.user,
		  number_of_products=cart.number_of_products,
		  sum_of_products_price=total_price,
		  shipping=shipping,
		  shipping_status=shipping_status
	)
	order.order_products.set(food_item_list)

	# Update Cart object
	self.update_cart_after_updating_food_order()

	choices = ("Update food product in order", )

	return JsonResponse(choices, safe=False)


def ajax_delete_food_product_function(request):
	"""
	This function  deletes the food product

	Params: get request
	1. food_id : food product id which we want to delete
	   type : int

	"""
	food_id = request.GET.get('food_id')
	food = get_object_or_404(Food, pk=food_id)
	food.delete()
	choices = ("Delete Product ", )

	return JsonResponse(choices, safe=False)
