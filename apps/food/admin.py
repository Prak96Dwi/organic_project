""" food/admin.py """
from django.contrib import admin
from .models import (
	Food, FoodCategory, Review,
)


class FoodAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'price', 'weight', 'discount',
					 'image', 'featured', 'average_rate', 'availability')

admin.site.register(Food, FoodAdmin)


class FoodCategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'image')

admin.site.register(FoodCategory, FoodCategoryAdmin)


class ReviewAdmin(admin.ModelAdmin):
	list_display = ('reviewer', 'food', 'review_text', 'rate')

admin.site.register(Review, ReviewAdmin)
