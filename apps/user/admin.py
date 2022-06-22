""" apps/user/admin.py """
from django.contrib import admin
from apps.user.models import Customer, Profile # pylint: disable=import-error


class CustomerAdmin(admin.ModelAdmin):
    """
    CustomerAdmin class
    """
    list_display = ('full_name', 'email', 'address', 'phone',
                    'country', 'state', 'district')

admin.site.register(Customer, CustomerAdmin)


class ProfileAdmin(admin.ModelAdmin):
    """
    ProfileAdmin class
    """
    list_display = ('user', 'full_name', 'permanent_address', 'residential_address', 
                    'country', 'phone', 'alternative_phone', 'state', 'district',
                    'gender', 'profile_picture')

admin.site.register(Profile, ProfileAdmin)
