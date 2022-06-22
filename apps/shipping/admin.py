""" apps/shipping/admin.py """
from django.contrib import admin
from apps.shipping.models import Shipping


class ShippingAdmin(admin.ModelAdmin):
	list_display = ('type', 'charge')

admin.site.register(Shipping, ShippingAdmin)
