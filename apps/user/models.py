""" apps/user/models.py

This module contains some non-abstract classes
    * class : Customer
    * class : Profile

"""
# Third Party modules
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image

# Core Django modules
from django.db import models
from django.contrib.auth.models import  (
    AbstractBaseUser, BaseUserManager
)
from django_countries.fields import CountryField
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from apps.cart.models import Cart # pylint: disable=import-error

# Native app modules
from .managers import CustomerManager


class Customer(AbstractBaseUser):
    """
    Table of Customer model inheriting AbstractUser
    """
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    # Full name of a registered user
    full_name = models.CharField(
        max_length=259,
        help_text=_("Full Name")
    )

    # Email of a registered user
    email = models.EmailField(
        max_length=50,
        unique=True,
        help_text=_("Email")
    )

    # Address of a registered user
    address = models.CharField(
        max_length=500,
        null=True,
        help_text=_("Address")
    )

    # User Country CharField
    country = CountryField(
        max_length=50, blank_label='(Select country)'
    )

    # User phone number
    phone = PhoneNumberField(
        blank=True, help_text=_("Contact phone number")
    )

    # State of a registered user
    state = models.CharField(
        max_length=259,
        null=True,
        help_text=_("Customer State")
    )

    # District of a user
    district = models.CharField(
        max_length=259,
        null=True,
        help_text=_("Customer District")
    )

    # type = models.CharField(max_length=50, null=False, help_text=_("User Type"))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False) # a superuser

    objects = CustomerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    #======================================================================================
    def get_short_name(self) -> str:
        # The user is identified by their email address
        return self.email

    def __str__(self) -> str:
        """ string representation of Customer instance """
        return f'{self.full_name}'

    def save(self, *args, **kwargs): # pylint: disable=arguments-differ
        """
        save cleaned data of user object
        """
        # self.full_clean()
        super().save(*args, **kwargs)

    #========================================================================================
    def has_perm(self, perm, obj=None) -> bool:
        """ has permission """
        return self.is_admin

    def has_module_perms(self, app_label) -> str:
        """ has module permission """
        return self.is_admin


#=======================================================================================
class Profile(models.Model):
    """
    Profile model class
    """
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    user = models.OneToOneField(Customer, on_delete=models.CASCADE, null=False)
    full_name = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=259, null=True)
    residential_address = models.CharField(max_length=259, null=True)
    country = CountryField(
        max_length=4, blank_label='(Select country)'
    )
    # User phone number
    phone = PhoneNumberField(
        blank=True, help_text=_("Contact phone number")
    )
    # User phone number
    alternative_phone = PhoneNumberField(
        blank=True, help_text=_("Alternative Contact phone number"), null=True
    )
    state = models.CharField(max_length=259, null=True)
    district = models.CharField(max_length=259, null=True)
    gender = models.CharField(max_length=50, null=True)
    profile_picture = models.ImageField(upload_to='profile/', null=True)


    def __str__(self) -> str:
        """ print method """
        return f'{self.full_name}'

    # ===================================================================================
    def resize_profile_picture(self):
        """Resize profile picture is 1:1 resolution using Pillow

        This method resize profile picture of customer when he/she upload its image
        
        Parameters
        ------------
        profile_picture : image file
            profile picture of customer

        """
        # Open image using self
        if self.profile_picture:
            # If profile picture is uploaded by user
            image = Image.open(self.profile_picture.path) # pylint: disable=no-member
            image_resolution = (settings.PROFILE_PICTURE_WIDTH, settings.PROFILE_PICTURE_HEIGHT)
            image.thumbnail(image_resolution)
            # saving image at the same path
            image.save(self.profile_picture.path)  # pylint: disable=no-member
        pass
