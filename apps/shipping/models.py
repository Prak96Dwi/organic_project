""" apps/shipping/models.py

This module contains some non-abstract classes
    * class : Shipping

"""
from django.db import models


class Shipping(models.Model):
    """
    Shipping model class
    """
    class Meta:
        verbose_name = 'Shipping'
        verbose_name_plural = 'Shippings'

    # Type of shipping that admin wants
    type = models.CharField(max_length=100)

    # Charge of shipping of particular type
    charge = models.FloatField()

    def __str__(self):
        """ String representation of Shipping instance """
        return f'{self.type}'
