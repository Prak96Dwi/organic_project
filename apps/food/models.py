""" apps/food/models.py

    This module contains some non-abstract concrete model classes

    * class : Food
    * class : FoodCategory
    * class : Review

    and contains some Model manager classes

    * class : FoodManager 
    * class : FoodCategoryManager
    * class : ReviewManager

"""
from django.db.models import (
    CASCADE,
    Model,
    CharField,
    IntegerField,
    BooleanField,
    ForeignKey,
    ManyToManyField,
    FloatField,
    ImageField
)
from django.contrib.auth import get_user_model
from django.conf import settings

from .managers import (
    FoodManager,
    FoodCategoryManager,
    ReviewManager
)
from PIL import Image


class Food(Model):
    """
    Food data model
    """
    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'

    # Name of food product
    name = CharField(max_length=100)
    
    # Category of food product
    category = CharField(max_length=50)

    # Price of food product
    price = FloatField()

    # Weight of food product
    weight = FloatField()

    # Description of food product
    detail = CharField(max_length=1000, null=True)

    # Discount in food product
    discount = FloatField(null=True)
    
    # Food Product Image
    image = ImageField(upload_to='product/', null=True)
    
    # If food product is special
    featured = BooleanField(default=False, null=False)
    
    # Available of food product i.e. it is available in stock or not
    availability = BooleanField(default=True)
    
    # Average rate of the rates given by the users to the particular product.
    average_rate = FloatField(null=True)

    objects = FoodManager()


    def save(self, *args, **kwargs):
        """
        Receives clean data of food object and 
        saves it.
        """
        super().save(*args,  **kwargs)

    #==========================================================================================
    def resize_food_image(self):
        """
        Resize food image 1:1 resolution
        """
        # Open image using self
        # If profile picture is uploaded by user
        food_image = Image.open(self.image.path) # pylint: disable=no-member
        food_image_resolution = (settings.FOOD_IMAGE_WIDTH, settings.FOOD_IMAGE_HEIGHT)
        food_image.thumbnail(food_image_resolution)
        # saving image at the same path
        food_image.save(self.image.path)  # pylint: disable=no-member

    #==========================================================================================
    def get_uncategories(self) -> str:
        """
        Get categories in desired format
        
        Returns
        --------
        1. category names in lower case

        """
        categories = FoodCategory.objects.filter(name=self.name)
        return ' '.join([category.name.lower().replace(' ', '-') for category in categories])

    #==========================================================================================
    def calculate_discount_price(self) -> int:
        """Calculate discount price  of  food product
        
        Returns
        --------
        discount price of food product

        """
        discount_price = self.price - (self.price * (self.discount/100))
        return discount_price


    def __str__(self) -> str:
        """ string representation of food instance """
        return f'{self.name}'


class FoodCategory(Model):
    """
    Food Category Data  model
    """
    class Meta:
        verbose_name = 'FoodCategory'
        verbose_name_plural = 'FoodCategories'

    # Name of food category
    name = CharField(max_length=100)
    
    # Image of food category
    image = ImageField(upload_to='category/', null=True)

    objects = FoodCategoryManager()


    def __str__(self):
        """ string representation of FoodCategory instance """
        return f'{self.name}'


    def save(self, *args, **kwargs):
        """
        saves food object
        """
        super().save(*args,  **kwargs)
        # resize food category image
        self.resize_food_category_image()

    #==========================================================================================
    def resize_food_category_image(self):
        """
        resize food category image 1:1 resolution
        """
        # Open image using self
        if self.image:
            # If profile picture is uploaded by user
            image = Image.open(self.image.path) # pylint: disable=no-member
            food_image_resolution = (settings.FOOD_CATEGORY_IMAGE_WIDTH, settings.FOOD_CATEGORY_IMAGE_HEIGHT)
            image.thumbnail(food_image_resolution)
            # saving image at the same path
            image.save(self.image.path)  # pylint: disable=no-member
        pass

    #========================================================================================
    def get_formatted_name(self) -> str:
        """Returns food category formatted name
        
        Coverts food category name is lowercase letter and empty space with -
        
        Returns
        -------
        food category name in lower case letters

        """
        return self.name.lower().replace(' ', '-')


class Review(Model):
    """
    Review data model
    """

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    # User who review food object
    reviewer = ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=CASCADE,
        related_name='customer'
    )

    # Food object which is reviewed
    food = ForeignKey(
        Food,
        on_delete=CASCADE,
        related_name='food_data'
    )

    # Rating of particular food product
    rate = FloatField(null=True)

    # Review text of particular food product
    review_text = CharField(max_length=500, null=True)

    objects = ReviewManager()

    def __str__(self):
        """ string representation of Review instance """
        return f'{self.reviewer.email}'
