""" apps/cart/views.py """
import json

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.cache import never_cache

from apps.food.models import Food

from .models import CartItem, Cart


@login_required(login_url='user_login_form')
@never_cache
def shoping_cart_page(request):
	"""
	This function is used to display the shopping
	cart page to a particular client

	Renders shopping cart page
	"""
	try:
		 cart = get_object_or_404(Cart, user=request.user)
	except Cart.DoesNotExist:
		message = {"products": "You have no food item in Cart"}
		cart = {"sum_of_products_price": "0"}

	return render(request, 'cart/shoping_cart.html', {'cart_items': cart})


def ajax_add_food_product_to_cart(request):
	""" 
	AJAX method for adding
	the food in cart for a particular user

	Get request data
	1. food_id - int
	    id of food object

	2. quantity : int
	   Number of particular  food  item to include in cart

	Returns
	-------
	1. Number of  products in cart
	
	"""
	# Check whether the user is authenticated or not
	if not request.user.is_authenticated:
		choices = ("Please create an account",)
		return JsonResponse(choices, safe=False)

	# Retreive get request data
	food_id = request.GET.get('food_id')
	quantity_value = request.GET.get('quantity')

	# Retreive food object
	food = get_object_or_404(Food, pk=food_id)
	# Retreiving cart itme of particular user
	cart_item = CartItem.objects.filter(buyer=request.user, food=food)

	# Check whether the food in included in the cart of user or not
	try:
		cart = Cart.objects.get(products__in=cart_item)
		for cart_product in list(cart.products.all()):
			if cart_product.food == food:
				choices = ("You have already added this fruit in your cart", cart.number_of_products)
				return JsonResponse(choices, safe=False)
	except Cart.DoesNotExist:
		pass

	# Creating cart item object if the selected food does not exists in customer's cart
	cart_item_obj = CartItem.objects.create(buyer=request.user,
											food=food,
											quantity=quantity_value, 
											food_price=food.price * int(quantity_value))
	# Retreiving cart object of particular customer
	cart = get_object_or_404(Cart, user=request.user)
	cart.adding_cart_item_in_cart(cart_item_obj)
	number_of_product = cart.get_number_of_products_from_cart()
	choices = ("Added to Cart", number_of_product)
	return JsonResponse(choices, safe=False)


def ajax_get_cart_product_number(request):
	"""
	AJAX method for getting the number of
	products from the cart of particular user

	This function is called when the page renders

	For authenticated  user -
	Returns:
	1. number of products in cart

	For anonymous user - 
	Returns:
	1. number of  products in cart will be zero
	"""
	if request.user.is_authenticated:
		cart = get_object_or_404(Cart, user=request.user)
		choices = (cart.get_number_of_products_from_cart(), )
	else:
		choices = (0, )

	return JsonResponse(choices, safe=False)


def ajax_delete_cart_product(request):
	""" 
	AJAX method for removing the product 
	from the cart

	Params:
	1. id - 
	   type: id
       description: id of cart item

    Returns JsonResponse:
    1. number  of products in cart
    2. sum of products price included in cart
	"""
	cart_item_id = request.GET.get('id')
	# Retrieving  CartItem object
	cart_item = get_object_or_404(CartItem, pk=cart_item_id)
	# Retrieving Cart object
	cart = get_object_or_404(Cart, user=request.user)
	# Removing cart item from the cart
	cart.remove_cart_item_from_cart(cart_item)
	# Retreiving number of products from cart
	number_of_products_in_cart = cart.get_number_of_products_from_cart()
	# Retreiving sum of  products price in cart
	sum_of_products_price = cart.get_sum_of_products_price_from_cart()
	# Delete cart item
	cart_item.delete()
	choices = ("deleted cart product", str(sum_of_products_price), str(number_of_products_in_cart))

	return JsonResponse(choices, safe=False)


def ajax_update_product_from_cart(request):
	"""
	update product from cart

	Get request data
	1. food_list
	   type : json format
	   description - json format food item data including food quantity and price

	2. total_sum
	   type : int
	   description - sum of  products price

	Returns
	1. Alert box will be toggled confirming that
	   food  data is  updated.
	"""
	food_list_in_json = request.GET.get('food_list')
	total_sum = request.GET.get('total_sum')
	# Converting food_list_in_json to python list data type
	food_list_in_python = json.loads(food_list_in_json)

	for food_object in food_list_in_python:
		# Retreiving cart item
		cart_item = get_object_or_404(CartItem, pk=food_object['id'])
		cart_item.updating_cart_item_quantity_and_price(food_object)

	cart_item = get_object_or_404(CartItem, pk=food_list_in_python[0]['id'])
	obj3 = cart_item.cart_set.get()
	obj3.sum_of_products_price = int(total_sum)
	obj3.save()

	choices = ("Products information is updated", )

	return JsonResponse(choices, safe=False)
