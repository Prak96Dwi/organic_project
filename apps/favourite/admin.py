""" apps/favourite/admin.py """
from django.contrib import admin
from .models import FoodLiked


class FoodLikedAdmin(admin.ModelAdmin):
	list_display = ('client', 'food', 'likes')

admin.site.register(FoodLiked, FoodLikedAdmin)
