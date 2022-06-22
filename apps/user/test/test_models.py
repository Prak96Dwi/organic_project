""" apps/user/test/test_models.py """
from django.test import TestCase
from apps.user.models import Customer
from phonenumber_field.phonenumber import PhoneNumber
from django_countries.fields import Country


class UserModelTestCase(TestCase):
    """
    User model test case
    """

    def create_customer_object(self, user_data):
        """
        create customer object
        """
        user = Customer.objects.create_user(**user_data)
        return user

    def create_super_user_for_testing(self):
        """
        create super user for testing
        """

        self.user_email = 'john_doe@gmail.com'
        self.password1 = 'Myadmin123'

        # Create customer superadmin object
        super_user_data = {
            'email' : self.user_email,
            'password' : self.password1,
            'is_active' : True,
            'is_staff' : True,
            'is_admin' : True
        }
        user = self.create_customer_object(super_user_data)
        return user

    def setUp(self):
        """
        creating object of customer before each method
        """
        self.country_code1 = '+91'
        self.mobile_number1 = '6260336626'

        self.full_name = "John Doe"
        self.email = 'john@gmail.com'
        self.address = 'F-38 Dindayal Nagar, Ratlam, [M.P]'
        self.phone = f'{self.country_code1}{self.mobile_number1}'
        self.country = 'IN'
        self.state = 'Madhya Pradesh'
        self.district = 'Ratlam'
        self.password = 'Myadmin123'

        self.user_data = {
            'full_name' : self.full_name,
            'email'    : self.email,
            'address'  : self.address,
            'phone'    : self.phone,
            'country'  : self.country,
            'state'    : self.state,
            'district' : self.district,
            'password' : self.password
        }
        # Create customer user object
        user = self.create_customer_object(self.user_data)

    def test_customer_object_created_or_not(self):
        """
        test customer object created or not
        """
        customer = Customer.objects.get(email=self.email)
        self.assertIsInstance(customer,  Customer)

    def test_customer_object_count(self):
        """
        test customer object count
        """
        customers = Customer.objects.all()
        self.assertEqual(customers.count(),  1)

    def test_customer_model_full_name_field(self):
        """
        test customer model full name  field
        """
        customer = Customer.objects.get(email=self.email)
        self.assertEqual(customer.full_name, self.full_name)

    def test_customer_model_full_name_field_with_null(self):
        """
        test customer model full name  field with null
        """
        user_data = self.user_data.copy()
        user_data['email'] = 'sona_jain@gmail.com'
        del user_data['full_name']
        test_user = self.create_customer_object(user_data)
        self.assertEqual(test_user.email, user_data['email'])
        self.assertIsInstance(test_user, Customer)

    def test_customer_model_email_field(self):
        """
        test customer model email field
        """
        customer = Customer.objects.get(email=self.email)
        self.assertEqual(customer.email, self.email)

    def test_customer_model_address_field(self):
        """
        test customer model address field
        """
        customer = Customer.objects.get(email=self.email)
        self.assertEqual(customer.address, self.address)

    def test_customer_model_address_field_with_null(self):
        """
        test customer model address field with null
        """
        user_data = self.user_data.copy()
        user_data['email'] = 'mayank_jain@gmail.com'
        del user_data['address']
        test_user = self.create_customer_object(user_data)
        self.assertEqual(test_user.email, user_data['email'])
        self.assertIsInstance(test_user, Customer)

    def test_customer_model_country_field_isinstance_or_not(self):
        """
        test customer model country field isinstance or not
        """
        customer = Customer.objects.get(email=self.email)
        self.assertIsInstance(customer.country, Country)


    def test_customer_model_country_field_code(self):
        """
        test customer model country field isinstance or not
        """
        customer = Customer.objects.get(email=self.email)
        self.assertEqual(customer.country.code, self.country)

    def test_customer_model_country_field_with_null(self):
        """
        test customer model country field with null
        """
        user_data = self.user_data.copy()
        user_data['email'] = 'sunil_soni@gmail.com'
        del user_data['country']
        test_user = self.create_customer_object(user_data)
        self.assertEqual(test_user.email, user_data['email'])
        self.assertIsInstance(test_user, Customer)

    def test_customer_model_phone_field(self):
        """
        test customer model phone field
        """
        customer = Customer.objects.get(email=self.email)
        self.assertIsInstance(customer.phone, PhoneNumber)


    def test_customer_model_phone_field_country_code(self):
        """
        test customer model phone field country code
        """
        customer = Customer.objects.get(email=self.email)
        self.assertEqual(customer.phone.country_code, int(self.country_code1))

    def test_customer_model_phone_field_mobile_number(self):
        """
        test customer model phone field mobile number
        """
        customer = Customer.objects.get(email=self.email)
        self.assertEqual(customer.phone.national_number, int(self.mobile_number1))

    def test_customer_model_phone_field_with_null(self):
        """
        test customer model phone field with null
        """
        user_data = self.user_data.copy()
        user_data['email'] = 'ravi@gmail.com'
        del user_data['phone']
        test_user = self.create_customer_object(user_data)
        self.assertEqual(test_user.email, user_data['email'])
        self.assertIsInstance(test_user, Customer)

    def test_customer_model_state_field(self):
        """
        test customer model state field
        """
        customer = Customer.objects.get(email=self.email)
        self.assertEqual(customer.state, self.state)

    def test_customer_model_state_field_with_null(self):
        """
        test customer model state field with null
        """
        user_data = self.user_data.copy()
        user_data['email'] = 'rahul@gmail.com'
        del user_data['state']
        test_user = self.create_customer_object(user_data)
        self.assertEqual(test_user.email, user_data['email'])
        self.assertIsInstance(test_user, Customer)

    def test_customer_model_district_field(self):
        """
        test customer model district field
        """
        customer = Customer.objects.get(email=self.email)
        self.assertEqual(customer.district, self.district)

    def test_customer_model_district_field_with_null(self):
        """
        test customer model district field with null
        """
        user_data = self.user_data.copy()
        user_data['email'] = 'faruk@gmail.com'
        del user_data['district']
        test_user = self.create_customer_object(user_data)
        self.assertEqual(test_user.email, user_data['email'])
        self.assertIsInstance(test_user, Customer)

    def test_customer_model_with_required_fields(self):
        """
        test customer model with required fields
        """
        user_data = {
            'fullname': "Prakhar Dwivedi",
            'email' : 'prakhardwi@gmail.com',
            'password' : 'Myadmin123'
        }
        test_user = self.create_customer_object(user_data)
        self.assertIsInstance(test_user, Customer)

    def test_customer_model_object_string_method(self):
        """
        test customer model object string method
        """
        customer = Customer.objects.get(email=self.email)
        self.assertEqual(str(customer), self.full_name)

    def test_customer_model_is_active_field_default(self):
        """
        test customer model is active field default
        """
        customer = Customer.objects.get(email=self.email)
        self.assertEqual(customer.is_active, True)

    def test_customer_model_is_staff_field_default(self):
        """
        test customer model is staff field default
        """
        customer = Customer.objects.get(email=self.email)
        self.assertEqual(customer.is_staff, False)

    def test_customer_model_object_is_admin_field_default(self):
        """
        test customer model objectt is admin field default
        """
        customer = Customer.objects.get(email=self.email)
        self.assertEqual(customer.is_admin, False)

    def test_customer_model_create_superuser_admin_field(self):
        """
        test customer model  create  superuser admin field
        """
        self.create_super_user_for_testing()
        customer = Customer.objects.get(email=self.email1)
        self.assertEqual(customer.is_admin, True)

    def test_customer_model_create_superuser_is_active_field(self):
        """
        test customer model  create superuser is active field
        """
        self.create_super_user_for_testing()
        customer = Customer.objects.get(email=self.email1)
        self.assertEqual(customer.is_active, True)

    def test_customer_model_create_superuser_staff_field(self):
        """
        test customer model create superuser staff field
        """
        self.create_super_user_for_testing()
        customer = Customer.objects.get(email=self.email1)
        self.assertEqual(customer.is_staff, True)
