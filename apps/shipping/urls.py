""" apps/shipping/urls.py """
from django.urls import path
from apps.shipping import views


urlpatterns = [
	path('admn/ship/', 
		views.shipping_form_page,
		name='shipping_form_page'
	)
]
