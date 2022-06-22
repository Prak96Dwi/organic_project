from django.test import TestCase
from food.forms import RegForm, FoodInsertForm, FoodCategoryForm, BlogPostForm
from food.forms import ShippingForm
from io import BytesIO
from PIL import Image
from django.core.files.base import File


class UserRegisterFormTestCase(TestCase):

	def setUp(self):
		data = {
			'full_name': "Toni Stark",
			'username' : "prak2dwi",
			'email'    : 'prakhardwi1996@gmail.com',
			'addr'     : "F-38 Dindayal Nagar, Ratlam, [M.P]",
			'mobile_no': "6260336626",
			'country'  : "India",
			'state'    : "MP",
			'district' : "Ratlam",
			'password1': "Myadmin123",
			'password2': "Myadmin123" 
		}
		self.form = RegForm(data = data)

	def test_user_form(self):
		self.assertTrue(self.form.is_valid())


	def test_user_required_field(self):
		data_1 = {
			'full_name': "", 'username' : "", 'email' : "", 'addr' : "", 'mobile_no': "",
			'country' : "", 'state' : "", 'district' : "", 'password1': "", 'password2': "" 
		}
		self.form_1 = RegForm(data = data_1)
		self.assertEqual(self.form_1.errors, {
			'country': ['This field is required.'],
			'mobile_no': ['This field is required.'],
			'email': ['This field is required.'],
			'username': ['This field is required.'],
			'full_name': ['This field is required.'],
			'addr': ['This field is required.'],
			'district': ['This field is required.'],
			'state': ['This field is required.'],
			'password1': ['This field is required.'],
			'password2': ['This field is required.']
			}
		)
		self.assertFalse(self.form_1.is_valid())


	def test_user_email_field(self):
		data_1 = {
			'full_name': "Toni Stark",'username':"prak2dwi",'email':'prakhardwi19l','addr':"F-38 Dindayal Nagar, Ratlam, [M.P]",
			'mobile_no': "6260336626",'country': "India",'state': "MP",'district' : "Ratlam",
			'password1': "Myadmin123",'password2': "Myadmin123" 
		}
		self.form_1 = RegForm(data = data_1)
		self.assertEqual(self.form_1.errors, {
			'email': ['Enter a valid email address.'],
			}
		)
		self.assertFalse(self.form_1.is_valid())

	def test_user_password_field(self):
		data_1 = {
			'full_name': "Toni Stark",'username':"prak2dwi",'email':'prakhardwi1996@gmail.com',
			'addr':"F-38 Dindayal Nagar, Ratlam, [M.P]",'mobile_no': "6260336626",'country': "India",
			'state': "MP",'district' : "Ratlam",'password1': "Myadmin123",'password2': "Myadmin" 
		}
		self.form_1 = RegForm(data = data_1)
		self.assertEqual(self.form_1.errors, {
			'password2': ['The two password fields didn’t match.'],
			}
		)
		self.assertFalse(self.form_1.is_valid())


		

class FoodInsertFormTestCase(TestCase):

	def setUp(self):
		data = {
			'food_name': "WalterDisney",
			'food_category': "Fruits",
			'food_price': 34,
			'food_wgt': 200.0,
			'food_detail': "Sweet Fruits",
			'food_discount': 30,
			'featured_product': True,
			'availability': "In Stock"
		}
		self.form = FoodInsertForm(data = data)


	def test_food_insert_form(self):
		self.assertTrue(self.form.is_valid())
		self.featured_product = self.form.cleaned_data.get('featured_product')
		self.assertEqual(self.featured_product, True)


	def test_food_required_fields(self):
		data_1 = {
			'food_name': "", 'food_category' : "", 'food_price' : "", 'food_wgt' : "", 'food_detail': "",
			'food_discount' : "", 'featured_product' : "", 'availability' : ""
		}
		self.form_1 = FoodInsertForm(data={})
		self.assertFalse(self.form_1.is_valid())
		self.assertEqual(self.form_1.errors, {
			'food_name': ['This field is required.'],
			'food_category': ['This field is required.'],
			'food_price': ['This field is required.'],
			'food_wgt': ['This field is required.'],
			'food_detail': ['This field is required.'],
			'availability': ['This field is required.'],
			}
		)


class BlogPostFormTestCase(TestCase):

	def setUp(self):
		data = {
			'blog_title': "WalterDisney",
			'blog_category': "Fruits",
			'blog_body': "This blog belongs to Fruits",
		}
		self.form = BlogPostForm(data = data)

	def test_blog_post_form(self):
		self.assertTrue(self.form.is_valid())
		self.title = self.form.cleaned_data.get('blog_title')
		self.assertEqual(self.title, "WalterDisney")

	def test_blog_fields_required(self):
		data_1 = {'blog_title': "", 'blog_category': "", 'blog_body': ""}
		self.form_1 = BlogPostForm(data = data_1)
		self.assertFalse(self.form_1.is_valid())
		self.assertEqual(self.form_1.errors, {
			'blog_title': ['This field is required.'],
			'blog_category': ['This field is required.'],
			'blog_body': ['This field is required.']
			}
		)


class ShippingFormTestCase(TestCase):

	def setUp(self):
		data = {
			'shipping_type': "Flying Mode",
			'shipping_charge': 50
		}
		self.form = ShippingForm(data = data)

	def test_shipping_data(self):
		self.assertTrue(self.form.is_valid())
		self.shipping_type = self.form.cleaned_data.get('shipping_type')
		self.assertEqual(self.shipping_type, "Flying Mode")

	def test_shipping_required_fields(self):
		data_1 = {
			'shipping_type': "",
			'shipping_charge': 50
		}
		self.form_1 = ShippingForm(data = data_1)
		self.assertFalse(self.form_1.is_valid())
		self.assertEqual(self.form_1.errors, {
			'shipping_type': ['This field is required.'],
			}
		)


















