from django.test import TestCase, Client, RequestFactory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from food.models import CategoryData
from django.urls import reverse
from django.conf import settings
import os




class IndexPageTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.index_url = reverse('index')

	def test_index_page(self):
		response = self.client.get(self.index_url)
		self.assertEqual(response.status_code, 200)

	def test_index_template(self):
		response = self.client.get(self.index_url)
		self.assertTemplateUsed(response, 'food/index.html')


class RegistrationFormTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.registration_url = reverse('user-reg-form')

	def test_register_form_page(self):
		response = self.client.get(self.registration_url)
		self.assertEqual(response.status_code, 200)

	def test_register_form_template(self):
		response = self.client.get(self.registration_url)
		self.assertEqual(response.templates[0].name, 'accounts/register_form.html')
		self.assertTemplateUsed(response, 'accounts/register_form.html')

	def test_register_form_function_name(self):
		response = self.client.get(self.registration_url)
		self.assertEqual(response.resolver_match.func.__name__, 'registration_form')

	def test_register_form_function_url_path(self):
		response = self.client.get(self.registration_url)
		self.assertEqual(response.request['PATH_INFO'], '/reg/form/')

	def test_registration_form_method_type(self):
		response = self.client.get(self.registration_url)
		self.assertEqual(response.request['REQUEST_METHOD'], 'GET')


class LoginFormTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.login_page_url = reverse('user-log-form')

	def test_login_form_page(self):
		response = self.client.get(self.login_page_url)
		self.assertEqual(response.status_code, 200)

	def test_login_form_template(self):
		response = self.client.get(self.login_page_url)
		self.assertEqual(response.templates[0].name, 'accounts/login.html')
		self.assertTemplateUsed(response, 'accounts/login.html')

	def test_login_form_function_name(self):
		response = self.client.get(self.login_page_url)
		self.assertEqual(response.resolver_match.func.__name__, 'login_form')

	def test_login_form_function_url_path(self):
		response = self.client.get(self.login_page_url)
		self.assertEqual(response.request['PATH_INFO'], '/log/form/')

	def test_login_form_method_type(self):
		response = self.client.get(self.login_page_url)
		self.assertEqual(response.request['REQUEST_METHOD'], 'GET')


class FoodFormTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.food_form_page_url = reverse('food-form-view')

	def test_food_form_page(self):
		response = self.client.get(self.food_form_page_url)
		self.assertEqual(response.status_code, 302)

	# def test_food_form_template(self):
	# 	response = self.client.get(self.food_form_page_url)
	# 	self.assertEqual(response.templates[0].name, 'food/food_insert.html')
	# 	self.assertTemplateUsed(response, 'food/food_insert.html')

	def test_food_form_function_name(self):
		response = self.client.get(self.food_form_page_url)
		self.assertEqual(response.resolver_match.func.__name__, 'food_form')

	def test_food_form_function_url_path(self):
		response = self.client.get(self.food_form_page_url)
		self.assertEqual(response.request['PATH_INFO'], '/food/form/')

	def test_food_form_method_type(self):
		response = self.client.get(self.food_form_page_url)
		self.assertEqual(response.request['REQUEST_METHOD'], 'GET')


class CategoryAddFormTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.category_add_form_page_url = reverse('category-add-form')

	def test_category_add_form_page(self):
		response = self.client.get(self.category_add_form_page_url)
		self.assertEqual(response.status_code, 302)

	# def test_food_form_template(self):
	# 	response = self.client.get(self.category_add_form_page_url)
	# 	self.assertEqual(response.templates[0].name, 'food/food_insert.html')
	# 	self.assertTemplateUsed(response, 'food/food_insert.html')

	def test_category_add_form_function_name(self):
		response = self.client.get(self.category_add_form_page_url)
		self.assertEqual(response.resolver_match.func.__name__, 'category_form_view')

	def test_category_add_form_function_url_path(self):
		response = self.client.get(self.category_add_form_page_url)
		self.assertEqual(response.request['PATH_INFO'], '/cat/form/')

	def test_category_add_method_type(self):
		response = self.client.get(self.category_add_form_page_url)
		self.assertEqual(response.request['REQUEST_METHOD'], 'GET')


class CategoryListTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.category_list_url = reverse('category-list-view')

	def test_category_list_page(self):
		response = self.client.get(self.category_list_url)
		self.assertEqual(response.status_code, 200)

	def test_category_list_template(self):
		response = self.client.get(self.category_list_url)
		self.assertEqual(response.templates[0].name, 'category/category_list.html')
		self.assertTemplateUsed(response, 'category/category_list.html')

	def test_category_list_function_name(self):
		response = self.client.get(self.category_list_url)
		self.assertEqual(response.resolver_match.func.__name__, 'category_list_view')

	def test_category_list_function_url_path(self):
		response = self.client.get(self.category_list_url)
		self.assertEqual(response.request['PATH_INFO'], '/cat/list/')

	def test_category_list_method_type(self):
		response = self.client.get(self.category_list_url)
		self.assertEqual(response.request['REQUEST_METHOD'], 'GET')


# class CategoryEditFormTestCase(TestCase):

# 	def setUp(self):
# 		self.client = Client()
# 		file_path = os.path.join(settings.BASE_DIR, 'media/myphoto.jpg')
# 		with open(file_path, 'rb') as file:
# 			data = {
# 				'name': 'New Test Image',
# 				'file': file
# 			}
# 		self.category_data_object = CategoryData.objects.create(category = 'Fresh Fruits',
# 																cat_image = data)
# 		self.category_edit_form_url = reverse('category-edit-form', 
# 											  kwargs = {'id': self.category_data_object.id})

# 	def test_food_dedit_form_page(self):
# 		response = self.client.get(self.category_edit_form_url)
# 		self.assertEqual(response.status_code, 200)
# 		self.assertTemplateUsed(response, 'category/cat_edit_form.html')


class ShoppingCartPageTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.shopping_cart_page_url = reverse('shopping-cart-page')

	def test_shopping_cart_page(self):
		response = self.client.get(self.shopping_cart_page_url)
		self.assertEqual(response.status_code, 302)

	# def test_shopping_cart_template(self):
	# 	response = self.client.get(self.shopping_cart_page_url)
	# 	self.assertEqual(response.templates[0].name, 'food/shoping-cart.html')
	# 	self.assertTemplateUsed(response, 'food/shoping-cart.html')

	def test_shopping_cart_function_name(self):
		response = self.client.get(self.shopping_cart_page_url)
		self.assertEqual(response.resolver_match.func.__name__, 'shoping_cart_page')

	def test_shopping_cart_function_url_path(self):
		response = self.client.get(self.shopping_cart_page_url)
		self.assertEqual(response.request['PATH_INFO'], '/shop/cart/')

	def test_shopping_cart_method_type(self):
		response = self.client.get(self.shopping_cart_page_url)
		self.assertEqual(response.request['REQUEST_METHOD'], 'GET')


class BlogViewPageTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.blog_view_page_url = reverse('blog-view-page')

	def test_blog_view_page(self):
		response = self.client.get(self.blog_view_page_url)
		self.assertEqual(response.status_code, 200)

	def test_blog_view_page_template(self):
		response = self.client.get(self.blog_view_page_url)
		self.assertEqual(response.templates[0].name, 'blog/blog.html')
		self.assertTemplateUsed(response, 'blog/blog.html')

	def test_blog_view_function_name(self):
		response = self.client.get(self.blog_view_page_url)
		self.assertEqual(response.resolver_match.func.__name__, 'blog_page')

	def test_blog_view_function_url_path(self):
		response = self.client.get(self.blog_view_page_url)
		self.assertEqual(response.request['PATH_INFO'], '/blog/page/')

	def test_blog_view_method_type(self):
		response = self.client.get(self.blog_view_page_url)
		self.assertEqual(response.request['REQUEST_METHOD'], 'GET')


class BlogPostFormPageTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.blog_post_form_page_url = reverse('blog-post-form-view')

	def test_blog_post_form_page(self):
		response = self.client.get(self.blog_post_form_page_url)
		self.assertEqual(response.status_code, 200)

	def test_blog_post_form_template(self):
		response = self.client.get(self.blog_post_form_page_url)
		self.assertEqual(response.templates[0].name, 'blog/blog_post_form.html')
		self.assertTemplateUsed(response, 'blog/blog_post_form.html')

	def test_blog_post_form_function_name(self):
		response = self.client.get(self.blog_post_form_page_url)
		self.assertEqual(response.resolver_match.func.__name__, 'blog_post_form')

	def test_blog_post_form_function_url_path(self):
		response = self.client.get(self.blog_post_form_page_url)
		self.assertEqual(response.request['PATH_INFO'], '/blog/post/form/')

	def test_blog_post_form_method_type(self):
		response = self.client.get(self.blog_post_form_page_url)
		self.assertEqual(response.request['REQUEST_METHOD'], 'GET')


class BlogCategoryFormPageTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.blog_category_form_page_url = reverse('blog-cat-form-view')

	def test_food_dedit_form_page(self):
		response = self.client.get(self.blog_category_form_page_url)
		self.assertEqual(response.status_code, 200)

	def test_blog_category_form_template(self):
		response = self.client.get(self.blog_category_form_page_url)
		self.assertEqual(response.templates[0].name, 'blog/blog_category_form.html')
		self.assertTemplateUsed(response, 'blog/blog_category_form.html')

	def test_blog_post_form_function_name(self):
		response = self.client.get(self.blog_category_form_page_url)
		self.assertEqual(response.resolver_match.func.__name__, 'blog_category_form')

	def test_blog_post_form_function_url_path(self):
		response = self.client.get(self.blog_category_form_page_url)
		self.assertEqual(response.request['PATH_INFO'], '/blog/cat/form/')

	def test_blog_post_form_method_type(self):
		response = self.client.get(self.blog_category_form_page_url)
		self.assertEqual(response.request['REQUEST_METHOD'], 'GET')


# class BlogDetailPageTestCase(TestCase):

# 	def setUp(self):
# 		self.d = Client()
# 		self.blog_detail_page_url = reverse('blog-detail-page-view')

# 	def test_food_dedit_form_page(self):
# 		response = self.d.get(self.blog_detail_page_url)
# 		self.assertEqual(response.status_code, 200)
# 		self.assertTemplateUsed(response, 'blog/blog-details.html')


class UsersBlogListPageTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.users_blog_list_url = reverse('users-blog-list-view')

	def test_users_blog_list_page(self):
		response = self.client.get(self.users_blog_list_url)
		self.assertEqual(response.status_code, 200)

	def test_users_blog_list_template(self):
		response = self.client.get(self.users_blog_list_url)
		self.assertEqual(response.templates[0].name, 'blog/users_blog_list.html')
		self.assertTemplateUsed(response, 'blog/users_blog_list.html')

	def test_users_blog_list_function_name(self):
		response = self.client.get(self.users_blog_list_url)
		self.assertEqual(response.resolver_match.func.__name__, 'users_blog_list_function')

	def test_users_blog_list_function_url_path(self):
		response = self.client.get(self.users_blog_list_url)
		self.assertEqual(response.request['PATH_INFO'], '/user/blog/')

	def test_users_blog_list_method_type(self):
		response = self.client.get(self.users_blog_list_url)
		self.assertEqual(response.request['REQUEST_METHOD'], 'GET')


class ContactPageTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.contact_page_url = reverse('contact-view-page')

	def test_contact_page(self):
		response = self.client.get(self.contact_page_url)
		self.assertEqual(response.status_code, 302)

	# def test_users_blog_list_template(self):
	# 	response = self.client.get(self.contact_page_url)
	# 	self.assertEqual(response.templates[0].name, 'core/contact.html')
	# 	self.assertTemplateUsed(response, 'core/contact.html')

	def test_users_blog_list_function_name(self):
		response = self.client.get(self.contact_page_url)
		self.assertEqual(response.resolver_match.func.__name__, 'contact_page')

	def test_users_blog_list_function_url_path(self):
		response = self.client.get(self.contact_page_url)
		self.assertEqual(response.request['PATH_INFO'], '/contact/page/')

	def test_users_blog_list_method_type(self):
		response = self.client.get(self.contact_page_url)
		self.assertEqual(response.request['REQUEST_METHOD'], 'GET')


class ProductLikePageTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.product_like_page_url = reverse('products-like-page')

	def test_product_like_page(self):
		response = self.client.get(self.product_like_page_url)
		self.assertEqual(response.status_code, 302)

	# def test_users_blog_list_template(self):
	# 	response = self.client.get(self.contact_page_url)
	# 	self.assertEqual(response.templates[0].name, 'food/fav_product.html')
	# 	self.assertTemplateUsed(response, 'food/fav_product.html')

	def test_product_like_function_name(self):
		response = self.client.get(self.product_like_page_url)
		self.assertEqual(response.resolver_match.func.__name__, 'product_likes_page')

	def test_product_like_function_url_path(self):
		response = self.client.get(self.product_like_page_url)
		self.assertEqual(response.request['PATH_INFO'], '/like/page/')

	def test_product_like_method_type(self):
		response = self.client.get(self.product_like_page_url)
		self.assertEqual(response.request['REQUEST_METHOD'], 'GET')


class CheckoutPageTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.checkout_page_url = reverse('checkout-view-page')

	def test_checkout_page(self):
		response = self.client.get(self.checkout_page_url)
		self.assertEqual(response.status_code, 302)

	# def test_checkout_template(self):
	# 	response = self.client.get(self.checkout_page_url)
	# 	self.assertEqual(response.templates[0].name, 'food/checkout.html')
	# 	self.assertTemplateUsed(response, 'food/checkout.html')

	def test_checkout_function_name(self):
		response = self.client.get(self.checkout_page_url)
		self.assertEqual(response.resolver_match.func.__name__, 'checkout_page')

	def test_checkout_function_url_path(self):
		response = self.client.get(self.checkout_page_url)
		self.assertEqual(response.request['PATH_INFO'], '/check/page/')

	def test_checkout_method_type(self):
		response = self.client.get(self.checkout_page_url)
		self.assertEqual(response.request['REQUEST_METHOD'], 'GET')


class ShopGridPageTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.shop_grid_page_url = reverse('shop-grid-page', kwargs = {'range': 'h2l'})

	def test_shop_grid_page(self):
		response = self.client.get(self.shop_grid_page_url)
		self.assertEqual(response.status_code, 200)

	def test_shop_grid_template(self):
		response = self.client.get(self.shop_grid_page_url)
		self.assertEqual(response.templates[0].name, 'food/shop-grid.html')
		self.assertTemplateUsed(response, 'food/shop-grid.html')

	def test_shop_grid_function_name(self):
		response = self.client.get(self.shop_grid_page_url)
		self.assertEqual(response.resolver_match.func.__name__, 'shop_grid_page')

	def test_shop_grid_function_url_path(self):
		response = self.client.get(self.shop_grid_page_url)
		self.assertEqual(response.request['PATH_INFO'], '/shop/grid/h2l/')

	def test_shop_grid_method_type(self):
		response = self.client.get(self.shop_grid_page_url)
		self.assertEqual(response.request['REQUEST_METHOD'], 'GET')


class FoodOrderListPageViewTestCase(TestCase):

	def setUp(self):
		self.client = Client()
		self.food_order_list_page_url = reverse('food-order-list')

	def test_food_order_list_page(self):
		response = self.client.get(self.food_order_list_page_url)
		self.assertEqual(response.status_code, 200)

	def test_food_order_list_template(self):
		response = self.client.get(self.food_order_list_page_url)
		self.assertEqual(response.templates[0].name, 'admin/food_order_data_list.html')
		self.assertTemplateUsed(response, 'admin/food_order_data_list.html')

	def test_food_order_list_function_name(self):
		response = self.client.get(self.food_order_list_page_url)
		self.assertEqual(response.resolver_match.func.__name__, 'food_order_list_page_view')

	def test_food_order_list_function_url_path(self):
		response = self.client.get(self.food_order_list_page_url)
		self.assertEqual(response.request['PATH_INFO'], '/admn/order/list/')

	def test_food_order_list_method_type(self):
		response = self.client.get(self.food_order_list_page_url)
		self.assertEqual(response.request['REQUEST_METHOD'], 'GET')














































