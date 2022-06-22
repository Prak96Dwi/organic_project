""" apps/food/tests/test_models.py """
from django.test import TestCase
from food.models import FoodData, CategoryData
import datetime


class FoodDataModelTestCase(TestCase):

	def setUp(self):
		self.food_object = baker.make(FoodData, food_name = "WaterOrange", food_category = "Fresh Fruit",
										food_price = 40.0, food_discount = 10.0)

	def test_food_data_model(self):
		self.assertIsInstance(self.food_object, FoodData)

	def test_food_name_field(self):
		self.assertEqual(str(self.food_object), "WaterOrange")

	def test_food_data_discount_price(self):
		self.assertEqual(self.food_object.calculatate_discount_price(), 36.0)


class CategoryDataTest(TestCase):

	def setUp(self):
		self.cat_data = CategoryData.objects.create(category = 'Fresh Fruits')

	def test_category_data_model(self):
		self.assertTrue(isinstance(self.cat_data, CategoryData))

	def test_category_name_field(self):
		self.assertEqual(self.cat_data.category, "Fresh Fruits")

	def test_category_formatted_name(self):
		self.assertEqual(self.cat_data.get_formatted_name(), 'fresh-fruits')
