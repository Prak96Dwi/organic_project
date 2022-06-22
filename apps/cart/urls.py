""" apps/cart/urls.py """
from django.urls import path, include
from . import views


urlpatterns = [
    path('shop/cart/',
        views.shoping_cart_page,
        name='shopping_cart_page'
    ),

    # AJAX function of cart products
    path('ajax/cart/',
        views.ajax_add_food_product_to_cart,
        name='add_food_product_to_cart'
    ),

    path('ajax/cart/no/',
        views.ajax_get_cart_product_number,
        name='ajax_cart_product_number'
    ),

    path('ajax/del/cart/',
        views.ajax_delete_cart_product,
        name='ajax_delete_product_from_cart'
    ),

    path('ajax/update/product/info',
        views.ajax_update_product_from_cart,
        name='ajax_update_product_from_cart'
    )
]
