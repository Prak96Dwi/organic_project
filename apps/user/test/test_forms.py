""" apps/user/test/test_forms.py """
from django.test import TestCase
from apps.user.forms import UserLoginForm, RegistrationForm
from apps.user.models import Customer


class RegistrationFormTestCase(TestCase):
    """
    Registration form testcase class
    """

    def setUp(self):
        """
        data to fill in form field
        """
        self.fullname = "John Doe" 
        self.email = 'john@gmail.com'
        self.address = 'F-38 Dindayal Nagar, Ratlam, [M.P]'
        self.phone = '+916260336626'
        self.country = 'IN'
        self.state = 'Madhya Pradesh'
        self.district = 'Ratlam'
        self.password = 'Myadmin123'


    def test_form_validity(self):
        """
        test form validity
        """
        data = {
            'full_name' : self.fullname,
            'email' : self.email,
            'address' : self.address,
            'phone' : self.phone,
            'country' : self.country,
            'state' : self.state,
            'district'  : self.district,
            'password1' : self.password,
            'password2' : self.password
        }
        form = RegistrationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_not_valid(self):
        """
        test form not valid
        """
        data = {
            'full_name' : self.fullname,
            'address' : self.address,
            'mobile_number' : self.mobile_number,
            'country' : self.country,
            'state' : self.state,
            'district'  : self.district,
            'password1' : self.password,
            'password2' : self.password
        }
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validity_with_empty_full_name_field(self):
        """
        test form validity with empty full name field
        """
        data = {
            'full_name'  : '',
            'email' : self.email,
            'address' : self.address,
            'mobile_number' : self.mobile_number,
            'country' : self.country,
            'state' : self.state,
            'district'  : self.district,
            'password1' : self.password,
            'password2' : self.password
        }
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validity_with_empty_email_field(self):
        """
        test form validity with emapty  email field
        """
        data = {
            'full_name'  : self.fullname,
            'email' : '',
            'address' : self.address,
            'mobile_number' : self.mobile_number,
            'country' : self.country,
            'state' : self.state,
            'district'  : self.district,
            'password1' : self.password,
            'password2' : self.password
        }
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validity_with_empty_address_field(self):
        """
        test form validity with empty address field
        """
        data = {
            'full_name'  : self.fullname,
            'email' : self.email,
            'address' : '',
            'mobile_number' : self.mobile_number,
            'country' : self.country,
            'state' : self.state,
            'district'  : self.district,
            'password1' : self.password,
            'password2' : self.password
        }
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validity_with_empty_mobile_number_field(self):
        """
        test form validity with empty mobile number field
        """
        data = {
            'full_name'  : self.fullname,
            'email' : self.email,
            'address' : self.address,
            'mobile_number' : '',
            'country' : self.country,
            'state' : self.state,
            'district'  : self.district,
            'password1' : self.password,
            'password2' : self.password
        }
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validity_with_mobilenumber_greater_than_ten_digit(self):
        """
        test form validity with mobile number greater then ten digit
        """
        data = {
            'full_name'  : self.fullname,
            'email' : self.email,
            'address' : self.address,
            'mobile_number' : '626033662626',
            'country' : self.country,
            'state' : self.state,
            'district'  : self.district,
            'password1' : self.password,
            'password2' : self.password
        }
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validity_with_mobilenumber_less_than_ten_digit(self):
        """
        test form validity with mobile number less then ten digit
        """
        data = {
            'full_name'  : self.fullname,
            'email' : self.email,
            'address' : self.address,
            'mobile_number' : '62603366',
            'country' : self.country,
            'state' : self.state,
            'district'  : self.district,
            'password1' : self.password,
            'password2' : self.password
        }
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validity_with_empty_country_field(self):
        """
        test form validity with empty county field
        """
        data = {
            'full_name'  : self.fullname,
            'email' : self.email,
            'address' : self.address,
            'mobile_number' : self.mobile_number,
            'country' : '',
            'state' : self.state,
            'district'  : self.district,
            'password1' : self.password,
            'password2' : self.password
        }
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validity_with_empty_state_field(self):
        """
        test form validity with empty state field
        """
        data = {
            'full_name'  : self.fullname,
            'email' : self.email,
            'address' : self.address,
            'mobile_number' : self.mobile_number,
            'country' : self.country,
            'state' : '',
            'district'  : self.district,
            'password1' : self.password,
            'password2' : self.password
        }
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validity_with_empty_district_field(self):
        """
        test form validity with empty district field
        """
        data = {
            'full_name'  : self.fullname,
            'email' : self.email,
            'address' : self.address,
            'mobile_number' : self.mobile_number,
            'country' : self.country,
            'state' : self.state,
            'district'  : '',
            'password1' : self.password,
            'password2' : self.password
        }
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validity_with_empty_password_field(self):
        """
        test form validity with empty password field
        """
        data = {
            'full_name'  : self.fullname,
            'email' : self.email,
            'address' : self.address,
            'mobile_number' : self.mobile_number,
            'country' : self.country,
            'state' : self.state,
            'district'  : self.district,
            'password1' : '',
            'password2' : ''
        }
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validity_with_password_less_than_eight_characters(self):
        """
        test form validity with password less than eight characters
        """
        data = {
            'full_name'  : self.fullname,
            'email' : self.email,
            'address' : self.address,
            'mobile_number' : self.mobile_number,
            'country' : self.country,
            'state' : self.state,
            'district'  : self.district,
            'password1' : 'admin',
            'password2' : 'admin'
        }
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validity_with_password_greater_than_fifteen_characters(self):
        """
        test form validity with password greater than fifteen characters
        """
        data = {
            'full_name'  : self.fullname,
            'email' : self.email,
            'address' : self.address,
            'mobile_number' : self.mobile_number,
            'country' : self.country,
            'state' : self.state,
            'district'  : self.district,
            'password1' : 'adminAdmin1233455',
            'password2' : 'adminAdmin1233455'
        }
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validity_with_password_unequal_to_confirm_password(self):
        """
        test form validity with password unequal to confirm password
        """
        data = {
            'full_name'  : self.fullname,
            'email' : self.email,
            'address' : self.address,
            'mobile_number' : self.mobile_number,
            'country' : self.country,
            'state' : self.state,
            'district'  : self.district,
            'password1' : 'Myadmin123',
            'password2' : 'Myadmin12345'
        }
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors.get('password2'), ['The two password fields didn’t match.'])


class LoginFormTestCase(TestCase):
    """
    Login form test case
    """

    def create_customer(self):
        """
        create customer object
        """
        self.fullname1 = "Sen Doe"
        self.email1 = 'sen_doe@gmail.com'
        self.address1 = 'F-38 Dindayal Nagar, Ratlam, [M.P]'
        self.mobile_number1 = '6260336626'
        self.country1 = 'India'
        self.state1 = 'Madhya Pradesh'
        self.district1 = 'Ratlam'
        self.password1 = 'Myadmin123'

        # Create customer user object
        Customer.objects.create_user(
            full_name=self.fullname1,
            email=self.email1,
            address=self.address1,
            mobile_number=self.mobile_number1,
            country=self.country1,
            state=self.state1,
            district=self.district1,
            password=self.password1,
            is_active=True,
            staff=True,
            admin=True
        )

    def setUp(self):
        """
        create customer login data
        """
        self.create_customer()

        self.email = 'sen_doe@gmail.com'
        self.password =  'Myadmin123'

        self.data = {
            'email' : self.email,
            'password' : self.password
        }

    def test_login_form_validity(self):
        """
        test login  form validity
        """
        form = UserLoginForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_login_form_email_field_authentication(self):
        """
        test login form email field authentication
        """
        data1 = {
            'email' : 'john_doe@gmail.com',
            'password' : 'Myadmin123'
        }
        form = UserLoginForm(data=data1)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors.get('email'), ['Email is invalid'])
