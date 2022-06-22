""" apps/cart/models.py 

This module contains some non-abstract classes
   * class : CartItem
   * class : Cart

"""

from django.conf import settings
from django.db.models import (
    Model,
    CASCADE,
    ForeignKey,
    IntegerField,
    PositiveIntegerField,
    OneToOneField,
    ManyToManyField
)
from apps.food.models import Food # pylint: disable=import-error


class CartItem(Model):
    """
    cartitem model
    """
    class Meta:
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'

    QUANTITY = 1

    # Buyer who buys a product
    buyer = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name='buyer'
    )
    
    # Forieignkey of particular food in a buyers cart
    food = ForeignKey(
        Food, 
        null=False, 
        blank=False, 
        on_delete=CASCADE
    )

    # Quantity of a particular food in a buyers cart
    quantity = IntegerField(
        default=QUANTITY,
        null=False,
        blank=True
    )

    # Price of a particular food in buyers cart as per quantity
    food_price = PositiveIntegerField(null=False)

    def __str__(self) -> str:
        """ string representation of CartItem instance """
        return f'{self.buyer}'

    #=========================================================================================
    def updating_cart_item_quantity_and_price(self, food_object):
        """
        updating cart item quantity and price

        Parameters:
        1. food_object
           description  - Food object
        """
        self.quantity = food_object['value']
        self.food_price = self.food.price * int(food_object['value']) # pylint: disable=no-member
        self.save()

    #========================================================================================
    def delete_cart_item(self):
        """Deletes cart item object """
        self.delete()


class Cart(Model):
    """
    Cart model class
    """
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    # instance of user who holds a cart
    user = OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name='cart_user'
    )

    # Products info included in the cart by a particular user
    products = ManyToManyField(CartItem)

    # Number of Food Products included in the cart by the user 
    number_of_products = IntegerField(
        default=0,
        null=False
    )

    # Sum of price of products which are included in a cart by the user
    sum_of_products_price = PositiveIntegerField(
        default=0,
        null=False
    )

    # ======================================================================================
    def adding_cart_item_in_cart(self, cart_item):
        """
        This method add cart item in cart

        Params:
        cart_item - cart item object
        """
        self.products.add(cart_item) # pylint: disable=no-member
        self.number_of_products += 1
        self.sum_of_products_price += cart_item.food_price
        self.save()

    # ======================================================================================
    def get_number_of_products_from_cart(self) -> int:
        """
        get number of products from cart

        Returns
        --------
        number of products of cart
        
        """
        return self.number_of_products

    # ======================================================================================
    def get_sum_of_products_price_from_cart(self) -> int:
        """
        get sum of products price from cart

        Returns
        --------
        1. sum  of products price of cart

        """
        return self.sum_of_products_price

    # ======================================================================================
    def remove_cart_item_from_cart(self, cart_item):
        """
        Removing cart item from cart and also decreasing number of
        products from cart

        Parameters
        -----------
        cart_item - object
            Cart item object

        """
        cart_item_products_list = list(self.products.all()) # pylint: disable=no-member
        cart_item_products_list.remove(cart_item) # pylint: disable=no-member
        self.products.set(cart_item_products_list) # pylint: disable=no-member
        # Decreasing number_of_products from cart
        self.number_of_products -= 1
        # Subtracting product price from cart
        self.sum_of_products_price -= cart_item.food.price
        self.save()

    # ==========================================================================================
    def update_cart_after_updating_food_order(self):
        """
        This method updates number of products and sum 
        of products price to zero.

        """
        self.number_of_products = 0
        self.sum_of_products_price = 0
        self.save()
