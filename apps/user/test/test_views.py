""" apps/user/test/test_views.py """
from django.test import TestCase
from apps.user.models import Customer
from apps.user import views
from django.urls import reverse


class RegisterUserViewTestCase(TestCase):
    """
    user view test case
    """
    def get_customer_user_registration_invalid_data(self):
        """
        Returns customer user registration invalid data
        """
        self.fullname = 'John Doe'
        self.email = 'john_doe@gmail.com'
        self.address = 'F-38 Dindayal Nagar, Ratlam, [M.P].'
        self.mobile_number = '6260336626'

        data = {
            'full_name' : self.fullname,
            'email'     : self.email,
            'address'   : self.address,
            'mobile_number' :  '6260336626',
            'country'   : 'India',
            'state'     : 'Madhya Pradesh',
            'district'  : 'Ratlam',
        }
        return data

    def get_customer_user_registration_data(self):
        """
        Returns customer user  registration data
        """
        user_data = self.get_customer_user_registration_invalid_data()
        user_data['password1'] = 'Myadmin123'
        user_data['password2'] = 'Myadmin123'
        return user_data

    def setUp(self):
        """
        setup method
        """
        pass

    def test_registration_form_view_function_by_name(self):
        """
        test registration form view function by name
        """
        response = self.client.get(reverse('user_registration_form'))
        self.assertEqual(response.status_code, 200)

    def test_registration_form_view_function_by_template(self):
        """
        test registration form view function by template
        """
        response = self.client.get(reverse('user_registration_form'))
        self.assertTemplateUsed(response, 'user/registration_form.html')

    def test_registration_form_view_function_by_charset(self):
        """
        test registration form view function by charset
        """
        response = self.client.get(reverse('user_registration_form'))
        self.assertEqual(response.charset, 'utf-8')

    def test_registration_form_view_function_by_content_type(self):
        """
        test registration form view function by content type
        """
        response = self.client.get(reverse('user_registration_form'))
        self.assertEqual(response.headers['Content-Type'], 'text/html; charset=utf-8')

    def test_registration_form_view_function_post_request_data(self):
        """
        test registration form view function post request data
        """
        user_data = self.get_customer_user_registration_data()
        response = self.client.post(reverse('user_registration_form'), data=user_data)
        self.assertEqual(response.status_code, 302)

    def test_registration_form_view_function_post_request_create_user(self):
        """
        test registration form view function post request create user
        """
        user_data = self.get_customer_user_registration_data()
        response = self.client.post(reverse('user_registration_form'), data=user_data)
        self.assertRedirects(response, reverse('user_login_form'))

    def test_registration_form_view_function_invalid_post_request(self):
        """
        test registration  form view function invalid post request
        """
        user_data = self.get_customer_user_registration_invalid_data()
        response = self.client.post(reverse('user_registration_form'), data=user_data)
        self.assertEqual(response.status_code, 200)

    def test_registration_form_view_function_invalid_post_request_template(self):
        """
        test registration form view function invalid post request template
        """
        user_data = self.get_customer_user_registration_invalid_data()
        response = self.client.post(reverse('user_registration_form'), data=user_data)
        self.assertTemplateUsed(response, 'user/registration_form.html')


class LoginFormViewTestCase(TestCase):
    """
    login form view test case
    """

    def get_login_data(self):
        """
        Returns login data
        """
        data = {
            'email': 'johndoe@gmail.com',
            'password' : 'Myadmin123'
        }
        return data

    def get_login_invalid_password(self):
        """
        Returns login data
        """
        data = {
            'email': 'johndoe@gmail.com',
            'password' : 'Myadmin12345'
        }
        return data

    def get_login_invalid_email(self):
        """
        Returns login data
        """
        data = {
            'email': 'john@gmail.com',
            'password' : 'Myadmin123'
        }
        return data

    def setUp(self):
        """
        setup method
        """
        self.fullname = "John Doe"
        self.email = 'johndoe@gmail.com'
        self.address = 'F-38 Dindayal Nagar, Ratlam, [M.P]'
        self.mobile_number = '6260336626'
        self.country = 'India'
        self.state = 'Madhya Pradesh'
        self.district = 'Ratlam'
        self.password = 'Myadmin123'

        # Create customer user object
        Customer.objects.create_user(
            full_name=self.fullname,
            email=self.email,
            address=self.address,
            mobile_number=self.mobile_number,
            country=self.country,
            state=self.state,
            district=self.district,
            password=self.password
        )

    def test_login_form_view_function_by_name(self):
        """
        test login form view function by name
        """
        response = self.client.get(reverse('user_login_form'))
        self.assertEqual(response.status_code, 200)

    def test_login_form_view_function_by_template(self):
        """
        test login form view function by template
        """
        response = self.client.get(reverse('user_login_form'))
        self.assertTemplateUsed(response, 'user/login_form.html')

    def test_login_form_view_function_post_request(self):
        """
        test login form view function post request
        """
        response = self.client.get(reverse('user_login_form'))
        self.assertTemplateUsed(response, 'user/login_form.html')

    def test_login_form_view_function_post_request_by_login_redirect(self):
        """
        test login form  view  function post request by login redirect
        """
        login_data = self.get_login_data()
        response = self.client.post(reverse('user_login_form'), login_data)
        self.assertRedirects(response, reverse('index'))

    def test_login_form_view_function_post_request_by_login_status_code(self):
        """
        test login  form view function post request by login status code
        """
        login_data = self.get_login_data()
        response = self.client.post(reverse('user_login_form'), login_data)
        self.assertEqual(response.status_code, 302)

    def test_login_form_view_function_post_request_by_login_status_code(self):
        """
        test login form view function post request by login status code
        """
        login_data = self.get_login_invalid_password()
        response = self.client.post(reverse('user_login_form'), login_data)
        self.assertEqual(response.status_code, 200)

    def test_login_form_view_function_post_request_by_invalid_password(self):
        """
        test login form view functipn post request by invalid password
        """
        login_data = self.get_login_invalid_password()
        response = self.client.post(reverse('user_login_form'), login_data)
        self.assertEqual(response.status_code, 200)

    def test_login_form_view_function_post_request_by_invalid_email_status_code(self):
        """
        test login form  view function post request by invalid email status code
        """
        login_data = self.get_login_invalid_email()
        response = self.client.post(reverse('user_login_form'), login_data)
        self.assertEqual(response.status_code, 200)

    def test_login_form_view_function_post_request_by_invalid_email_template(self):
        """
        test login form view function post request by invalid email template
        """
        login_data = self.get_login_invalid_email()
        response = self.client.post(reverse('user_login_form'), login_data)
        self.assertTemplateUsed(response, 'user/login_form.html')

    def test_login_form_view_function_post_request_by_invalid_email(self):
        """
        test login form view function post request by invalid email
        """
        login_data = self.get_login_invalid_email()
        response = self.client.post(reverse('user_login_form'), login_data)
        self.assertEqual(response.charset, 'utf-8')

    def test_login_form_view_function_post_request_by_invalid_email(self):
        """
        test login form view  function post request by invalid email
        """
        login_data = self.get_login_invalid_email()
        response = self.client.post(reverse('user_login_form'), login_data)
        self.assertEqual(response.headers['Content-Type'], 'text/html; charset=utf-8')


class LogoutViewTestCase(TestCase):
    """
    logout view test case class
    """

    def create_user_data(self):
        """
        create custom user data
        """
        self.fullname = "John Doe"
        self.email = 'johndoe@gmail.com'
        self.address = 'F-38 Dindayal Nagar, Ratlam, [M.P]'
        self.mobile_number = '6260336626'
        self.country = 'India'
        self.state = 'Madhya Pradesh'
        self.district = 'Ratlam'
        self.password = 'Myadmin123'

        # Create customer user object
        Customer.objects.create_user(
            full_name=self.fullname,
            email=self.email,
            address=self.address,
            mobile_number=self.mobile_number,
            country=self.country,
            state=self.state,
            district=self.district,
            password=self.password
        )

    def setUp(self):
        """
        setup method
        """
        self.create_user_data()
        response = self.client.login(email=self.email, password=self.password)

    def test_logout_view_url_redirect(self):
        """
        test logout view url redirect
        """
        response = self.client.get(reverse('user_logout_form'))
        self.assertRedirects(response, reverse('user_login_form'))

    def test_logout_view_url_status_code(self):
        """
        test logout view url status code
        """
        response = self.client.get(reverse('user_logout_form'))
        self.assertEqual(response.status_code, 302)
