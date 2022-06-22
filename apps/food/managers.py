""" apps/food/manager.py 
    
    This modules contains some model manager classes

    * class : FoodManager
    * class : FoodCategoryManager
    * class : ReviewManager

"""
from django.db.models import (
    Manager,
    Max,
    Min,
    Avg
)


class FoodManager(Manager):
    """
    food model manager class

    This class contains some methods which is used to retrieve
    objects.

    """

    # ==================================================================================
    def get_queryset(self):
        """
        Returns all the objects of the FoodManager class.

        """
        return super().get_queryset().filter(availability=True)

    # =================================================================================
    def featured_foods(self):
        """
        Returns food products which are featured as True.

        """
        return self.get_queryset().filter(featured=True)

    # =================================================================================
    def foods_by_category(self, category):
        """
        Returns food products of particular category.

        """
        return self.get_queryset().filter(category=category)

    # =================================================================================
    def maximum_food_products_price(self):
        """
        Returns maximum food products price.

        """
        return self.get_queryset().aggregate(Max('price'))

    # =================================================================================
    def minimum_food_products_price(self):
        """
        Returns minimum food products price.

        """
        return self.get_queryset().aggregate(Min('price'))

    # =================================================================================
    def maximum_food_products_weight(self):
        """
        Returns maximum weight of food products registered.

        """
        return self.get_queryset().aggregate(Max('weight'))

    # ================================================================================
    def minimum_food_products_weight(self):
        """
        Returns maximum weight of food products registered.

        """
        return self.get_queryset().aggregate(Min('weight'))

    # ================================================================================
    def food_of_specific_price_category_and_weight(
        self,
        price,
        category,
        weight
    ):
        """
        Returns food product of specific price, category and weight.

        """
        return self.get_queryset().filter(
            price__lte=price[1:],
            category__in=category,
            weight__lte=weight[:len(weight)-2]
        )


class FoodCategoryManager(Manager):
    """
    food model manager class

    This class contains some methods which is used to retrieve
    objects.

    """

    def get_queryset(self):
        """
        Returns all the objects of the FoodManager class.

        """
        return super().get_queryset()


class ReviewManager(Manager):
    """
    Review model manager class

    This class contains some methods which is used to retrieve
    objects.

    """

    # =================================================================================
    def get_queryset(self):
        """
        Returns all the objects of the FoodManager class.

        """
        return super().get_queryset()

    # ================================================================================
    def food_product_review(self, food):
        """
        Returns review of particular food product.

        """
        return self.get_queryset().filter(food=food)

    # ================================================================================
    def average_rate_of_food_product_reviews(self, food_product_reviews):
        """
        Returns average rate of food product reviews.

        """
        average_rate = food_product_reviews.aggregate(average_rate=Avg('rate'))
        return average_rate['average_rate']
