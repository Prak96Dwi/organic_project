"""apps/favourite/urls.py """
from django.urls import path
from apps.favourite import views


urlpatterns = [

	path('like/page/',
        views.favourite_product_page,
        name='products_like_page'
    ),

	# AJAX function of likes
    path('ajax/liked/',
        views.ajax_add_food_as_liked,
        name='add_food_product_liked'
    ),

    path('ajax/likes/num/',
        views.ajax_food_products_likes,
        name='ajax_likes_product_number'
    ),

    path('ajax/del/likes/',
        views.ajax_food_likes_delete,
        name='ajax_food_product_delete_from_likes'
    )
]
