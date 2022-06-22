""" apps/user/test/test_views.py """
from django.test import TestCase
from apps.user.models import Customer
from apps.user import views
from django.urls import reverse


class RegisterUserUrlTestCase(TestCase):
	"""
	user view test case
	"""

	def setUp(self):
		"""
		setup method
		"""
		pass

	def test_registration_form_view_function_by_desired_location(self):
		"""
		test registration form view function by desired location
		"""
		response = self.client.get('/reg/form/')
		self.assertEqual(response.status_code, 200)

	def test_registration_form_view_function_by_invalid_desired_location(self):
		"""
		test registration form view function by invalid desired location
		"""
		response = self.client.get('reg/form/')
		self.assertEqual(response.status_code, 404)

	def test_registration_form_view_function_by_name(self):
		"""
		test registration form view function by name
		"""
		response = self.client.get(reverse('user_registration_form'))
		self.assertEqual(response.status_code, 200)


class LoginViewTestCase(TestCase):
	"""
	user view test case
	"""

	def setUp(self):
		"""
		setup method
		"""
		pass

	def test_login_form_view_function_by_desired_location(self):
		"""
		test logiin form  view function by desired location
		"""
		response = self.client.get('/log/form/')
		self.assertEqual(response.status_code, 200)

	def test_login_form_view_function_by_invalid_desired_location(self):
		"""
		test login form view function by invalid desired  location
		"""
		response = self.client.get('log/form/')
		self.assertEqual(response.status_code, 404)

	def test_login_form_view_function_by_name(self):
		"""
		test login form view function by name
		"""
		response = self.client.get(reverse('user_login_form'))
		self.assertEqual(response.status_code, 200)


class LogoutViewTestCase(TestCase):
	"""
	user view test case
	"""

	def setUp(self):
		"""
		setup method
		"""
		pass

	def test_logout_form_view_function_by_desired_location(self):
		"""
		test logout form  view function by desired location
		"""
		response = self.client.get('/logout/view/')
		self.assertEqual(response.status_code, 302)

	def test_logout_form_view_function_by_invalid_desired_location(self):
		"""
		test logout form view function by invalid desired  location
		"""
		response = self.client.get('logout/view/')
		self.assertEqual(response.status_code, 404)

	def test_logout_form_view_function_by_name(self):
		"""
		test logout form view function by name
		"""
		response = self.client.get(reverse('user_logout_form'))
		self.assertEqual(response.status_code, 302)
