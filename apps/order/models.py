""" apps/order/models.py

This module contains non-abstract classes
    * class : FoodItem
    * class : Order

"""

from django.db import models
from apps.food.models import  Food
from apps.shipping.models import Shipping
from django.conf import settings


class FoodItem(models.Model):
    """
    FoodItem model class
    """

    class Meta:
        verbose_name = 'FoodItem'
        verbose_name_plural = 'FoodItems'

    # Food intance which is been ordered by the user
    food = models.ForeignKey(
        Food,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    # Quantity of food item which is been ordered by the user
    quantity = models.IntegerField(default=1, null=False, blank=True)

    # Price of food product
    price = models.PositiveIntegerField(null=False)


class Order(models.Model):
    """
    Order model class
    """

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        name='user'
    )

    # Products ordered by user
    products = models.ManyToManyField(FoodItem)

    # number_of_products ordered by user
    number_of_products = models.IntegerField()

    # sum of products price ordered by user
    sum_of_products_price = models.FloatField()

    # Type of shipping that user ordered
    shipping = models.ForeignKey(Shipping,
        on_delete=models.CASCADE
    )

    # Shipping status
    shipping_status = models.CharField(max_length=100)
