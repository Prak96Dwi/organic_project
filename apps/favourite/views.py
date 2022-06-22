""" apps/favourite/views.py """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from apps.food.models import Food

from .models import FoodLiked


@login_required(login_url='user_login_form')
def favourite_product_page(request):
	"""
	This function is used to display the favourite
	products page of a particular client
	"""
	try:
		food_liked = FoodLiked.objects.filter(client=request.user)
	except FoodLiked.DoesNotExist:
		likes = {"products": "You have not liked any food item"}

	return render(request, 'favourite/favourite_product.html', {'likes': food_liked})


def ajax_add_food_as_liked(request):
	""" 
	AJAX method for adding
	the food as liked for a particular user
	"""
	# check if requested user is_authenticated or not
	if not request.user.is_authenticated:
		choices = ("Please create an account",)
		return JsonResponse(choices, safe=False)

	# Retreive food object from food_id
	food_id = request.GET.get('food_id')
	food = get_object_or_404(Food, id=food_id)

	# Retreive food liked list of requested user
	food_liked_list = list(FoodLiked.objects.filter(users_liked_this_product__in=[request.user]))
	for food_liked in food_liked_list:
		# check particular food is liked by requested user or not
		if food_liked.food == food:
			choices = ("You have already Liked this fruit", str(len(food_liked_list)))

			return JsonResponse(choices, safe=False)

	try:
		# check if users  food_liked object exist then.
		food_liked = get_object_or_404(FoodLiked, client=request.user, food=food)
		food_liked.added_as_user_liked_this_product(request)
		food_liked.increasing_number_of_likes_of_particular_food()
		food_liked.get_number_of_likes()
		food_liked.save()
	except FoodLiked.DoesNotExist:
		# if food_liked object of particular request user is not exist
		# then food_liked object will be created
		food_liked = FoodLiked.objects.create(
			client=request.user,
			food=food,
			number_of_likes=1
		)
		food_liked.added_as_user_liked_this_product(request)

	food_liked_count_by_user = len(FoodLiked.objects.filter(client=request.user))
	choices = ("Added as Liked", str(food_liked_count_by_user))
	return JsonResponse(choices, safe=False)


def ajax_food_products_likes(request):
	"""
	AJAX method for getting the number of
	likes of particular user
	"""
	if request.user.is_authenticated:
		food_liked = FoodLiked.objects.filter(client=request.user)
	else:
		food_liked = []
	choices = (len(food_liked),)

	return JsonResponse(choices, safe=False)


def ajax_food_likes_delete(request):
	"""
	ajax function for food likes delete
	"""
	food_liked = FoodLiked.objects.get(id=request.GET.get('id'))
	food_liked.delete()
	food_liked_count = FoodLiked.objects.filter(client=request.user)
	choices = ("Food is removed from favourite page", str(food_liked_count))

	return JsonResponse(choices, safe=False)
