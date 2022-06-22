""" apps/cart/admin.py """
from django.contrib import admin
from .models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
	list_display = ('user','number_of_products', 'sum_of_products_price')

admin.site.register(Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
	list_display = ('food', 'quantity')

admin.site.register(CartItem, CartItemAdmin)
