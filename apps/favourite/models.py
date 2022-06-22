""" apps/favourite/models.py 

This module contains some non-abstract classes
    * class : FoodLiked

"""

from django.db import models
from django.conf import settings

from apps.food.models import Food


class FoodLiked(models.Model):
    """
    FoodLiked model class
    """
    class Meta:
        verbose_name = 'FoodLiked'
        verbose_name_plural = 'FoodLikes'

    # user instance who liked the particular food
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='client'
    )

    # food instance liked by the particular user
    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        null=True
    )

    # list of user instances who liked the particular food
    users_liked_this_product = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='likes'
    )

    # Number of likes to a particular food
    likes = models.IntegerField(
        default=0,
        null=False
    )

    def __str__(self):
        """ string representation of FoodLiked instance """
        return f'{self.client} {self.food}'

    #==============================================================================================
    def get_user_likes(self, user):
        """
        Returns users likes

        Parameters
        ----------
        user - user object
            customer object

        Returns
        -------
        users who liked this product

        """
        return self.objects.filter(users_liked_this_product__in=[user])

    #=============================================================================================
    def added_as_user_liked_this_product(self, request):
        """
        Updates as user liked this product
        
        """
        self.users_liked_this_product.add(request.user)
        self.save()

    #============================================================================================
    def increasing_number_of_likes_of_particular_food(self):
        """
        Increments number of likes of particular food
        """
        self.likes += 1
        self.save()

    #============================================================================================
    def get_number_of_likes(self) -> int:
        """
        Returns number of likes of particular food product
        
        Returns
        --------
        number of likes of particular food

        """
        return self.likes
