""" apps/food/urls.py """
# Django Core modules
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, ajax_views


urlpatterns = [
    path('', views.index, name='index'),

    # Admin Dashboard
    path('admn/dashboard/', 
        views.admin_dashboard,
        name='admin_dashboard_page'
    ),

    path('admn/thank/',
        views.thank_you_page,
        name='thank_you_page'
    ),

    path('admn/order/list/',
        views.food_order_list_page_view,
        name='food_order_list'
    ),

    # Food Product URL path
    path('food/form/',
        views.food_form,
        name='food_form_view'
    ),

    path('food/edit/',
        views.food_list_page,
        name='food_edit_form_view'
    ),

    path('fd/edit/form/<int:id>/',
        views.food_edit_form,
        name='food_edit_form'
    ),

    # Category URL path
    path('cat/form/',
        views.category_form_view,
        name='category_add_form'
    ),

    path('cat/list/',
        views.category_list_view,
        name='category_list_view'
    ),

    path('cat/edit/<int:id>/',
        views.category_edit_form,
        name='category_edit_form'
    ),


    # URL path for product detail page
    path('food/detail/<int:id>/',
        views.shop_details_page,
        name='product_detail_page'
    ),


    path('check/page/',
        views.checkout_page,
        name='checkout_view_page'
    ),

    path('shop/grid/<str:range>/',
        views.shop_grid_page,
        name='shop_grid_page'
    ),

    path('contact/page/',
        views.contact_page,
        name='contact_view_page'
    ),

    path('ajax/food/delete/',
        ajax_views.ajax_delete_food_product_function,
        name='delete_food_product'
    ),

    # AJAX get food name using autocomplete
    path('ajax/food/',
        ajax_views.ajax_get_foodname,
        name="get_food_product_name"
    ),

    path('ajax/food/search/',
        ajax_views.ajax_search_food_product_detail,
        name='search_food_product_detail'
    ),

    path('ajax/cat/name/',
        ajax_views.ajax_get_categories_name,
        name='ajax_get_categories_name'
    ),

    path('ajax/filtered/food/',
        ajax_views.ajax_data_on_food_filter,
        name='ajax_on_food_filter'
    ),
    
    path('ajsx/update/rate/',
        ajax_views.ajax_update_rate_of_product,
        name='add_food_product_rate'
    ),
    
    path('ajax/update/orders/',
        ajax_views.ajax_update_food_order_data,
        name='ajax_update_product_in_order'
    ),
    
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
							document_root=settings.MEDIA_ROOT)
