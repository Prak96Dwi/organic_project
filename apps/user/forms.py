"""  apps/user/forms.py """
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django import forms
from apps.user.models import Customer # pylint: disable=import-error
from phonenumber_field.formfields import PhoneNumberField
from django_countries.widgets import CountrySelectWidget


class UserLoginForm(forms.Form):
    """
    User Login Form class
    """
    email = forms.EmailField(label="Email",
                            widget=forms.EmailInput(
                                                attrs = {
                                                'class' : 'form-control emailctn'
                                                }
                                            )
                            )
    password = forms.CharField(label="Password",
                            widget=forms.PasswordInput(
                                                attrs = {
                                                'class': 'form-control pass3'
                                                }
                                            )
                            )

    def clean_email(self):
        """
        This method validated form field email
        """
        email = self.cleaned_data.get('email')

        # Retrieving user data if it exist
        user = Customer.objects.filter(email=email).first()

        if not user:
            raise ValidationError(_('Email is invalid'), code='invalid')

        return email


class RegistrationForm(UserCreationForm):
    """
    Registration Form class
    """
    full_name = forms.CharField(label="Full Name", max_length=100,
                                widget = forms.TextInput(
                                    attrs = {
                                    'class' : 'form-control fullnm'
                                    }
                                )
                            )
    address = forms.CharField(label="Address", max_length=100,
                                widget = forms.Textarea(
                                    attrs = {
                                    'class' : 'form-control pass1'
                                    }
                                )
                            )
    # country = forms.CharField(label="Country Name", max_length=50,
    #                             widget = CountrySelectWidget(
    #                             attrs = {
    #                                 'class' : 'form-control pass1'
    #                                 }
    #                             )
    #                         )
    phone = PhoneNumberField(max_length=50,
                            widget = forms.NumberInput(
                                    attrs = {
                                    'class' : 'form-control pass1'
                                    }
                            )
                        )
    state = forms.CharField(label="State", max_length=52,
                                widget = forms.TextInput(
                                    attrs = {
                                    'class' : 'form-control pass1'
                                    }
                                )
                            )
    district = forms.CharField(label="District", max_length=50,
                                widget = forms.TextInput(
                                    attrs = {
                                    'class' : 'form-control pass1'
                                    }
                                )
                            )
    password1 = forms.CharField(label="Password", max_length=100,
                                widget = forms.PasswordInput(
                                    attrs = {
                                    'class' : 'form-control pass1'
                                    }
                                )
                            )
    password2 = forms.CharField(label="Confirm Password", max_length=100,
                                widget = forms.PasswordInput(
                                    attrs = {
                                    'class': 'form-control pass2'
                                    }
                                )
                            )

    class Meta: # pylint: disable=too-few-public-methods
        """
        UserLogin meta class
        """
        model = Customer
        fields = ['full_name', 'email', 'address', 'country', 'phone', 
                    'state', 'district']
        widgets = {
            'email'   : forms.EmailInput(attrs={'class' : 'form-control emailctn'}),
        }

    def clean(self):
        """Validating registration form fields

        If the form fields are invalid then it will raise
        validation error specified.

        Arguments
        ----------
        user_password : str
            password of a custom user 
        user_confirm_password : str
            confirm password of a custom user

        Raises
        --------
        ValidationError
            Raises when user password and confirm password is not matching


        Returns 
        ---------
        form field cleaned data
        """

        # data from the form is fetched using super function
        super().clean()

        # extracting password and confirm password from register form
        user_password = self.cleaned_data.get('password1')
        user_confirm_password = self.cleaned_data.get('password2')

        if user_password != user_confirm_password:
            raise ValidationError(_('Confirm Password is not matching'), code='invalid')

        return self.cleaned_data

    def clean_password1(self):
        """Validating password field

        Password field of registration form should have maximum 15 and minimum 8 characters

        Arguments
        -----------
        user_password : str
            password of a user

        Raises
        -----------
        ValidationError
              When user input less than 8 characters and more than 15 characters.

        Return
        ----------
        user_password form field

        """

        # Retreiving password from registration form field
        user_password = self.cleaned_data.get('password1')

        if len(user_password) <= 8: # If password length is less the eight
            raise ValidationError(_('Password should be greater than 8 characters'), code='invalid')
        if len(user_password) >= 15: # If password length is more than specified value
            raise ValidationError(_('Password should be less than 15 characters'), code='invalid')
        return user_password

    def clean_full_name(self):
        """Validating full name of user

        If full_name is not entered by user

        Attributes
        -----------
        full_name : str, optional
            full_name of user

        Raises
        ----------
        ValidationError
            When full_name variable is None or not entered in form

        Return
        ---------
        full_name field

        """
        full_name = self.cleaned_data.get('full_name')
        if not full_name:
            raise ValidationError(_('Full name should not be empty'))
        return full_name



class ProfileEditForm(forms.ModelForm):
    """
    Registration Form class
    """
    full_name = forms.CharField(label="Full Name", max_length=100,
                                widget = forms.TextInput(
                                    attrs = {
                                    'class' : 'form-control fullnm'
                                    }
                                )
                            )

    address = forms.CharField(label="Address", max_length=100,
                                widget = forms.Textarea(
                                    attrs = {
                                    'class' : 'form-control pass1'
                                    }
                                )
                            )
    mobile_number = forms.CharField(label="Mobile Number", max_length=100,
                                widget = forms.NumberInput(
                                    attrs = {
                                    'class' : 'form-control pass1'
                                    }
                                )
                            )

    country = forms.CharField(label="Country Name", max_length=50,
                                widget = forms.TextInput(
                                    attrs = {
                                    'class' : 'form-control pass1'
                                    }
                                )
                            )
    state = forms.CharField(label="State", max_length=52,
                                widget = forms.TextInput(
                                    attrs = {
                                    'class' : 'form-control pass1'
                                    }
                                )
                            )
    district = forms.CharField(label="District", max_length=50,
                                widget = forms.TextInput(
                                    attrs = {
                                    'class' : 'form-control pass1'
                                    }
                                )
                            )
    profile_picture = forms.ImageField(label='Upload Image', required=False,
                                widget=forms.FileInput(
                                    attrs={
                                    'class': 'form-control',
                                    'required': False,
                                    }
                                )
                            )

    class Meta: # pylint: disable=too-few-public-methods
        """
        UserLogin meta class
        """
        model = Customer
        fields = ['full_name', 'email', 'address', 'mobile_number',
                   'country', 'state', 'district']
        widgets = {
            'email'   : forms.EmailInput(attrs={'class' : 'form-control emailctn'}),
        }

    def clean_profile_picture(self):
        """Validating profile picture field

        If profile picture exist and does not have image format in jpeg or jpg.
        Then, it raises validation error.

        Attributes
        -----------
        profile_image : image file
            profile picture uploaded by the user

        Raises
        ----------
        ValidationError
            When image extension is not in jpeg or jpg

        Return
        ---------
        image
            profile image of user

        """

        profile_image = self.cleaned_data.get('profile_picture')
        if profile_image is not None:
            # If profile image is uploaded
            image_format = profile_image.content_type.split('/')[1]
            if image_format not in ('jpeg', 'jpg'):
                raise ValidationError(_('Image format should be in jpg or jpeg'))
        return profile_image

    def clean_mobile_number(self):
        """Validating mobile number

        If mobile number doesn't contain country code before mobile number then
        Validation error is raised.

        Attributes
        ------------
        mobile_number : str
            Mobile number entered by the user along with country code

        Raises
        -----------
        ValidationError
            If the entered mobile number is equal to 10 or less.
            If mobile number does not exists.

        Return
        ---------
        mobile number form field

        """
        mobile_number = self.cleaned_data.get('mobile_number')
        if not mobile_number:
             raise ValidationError(_('Please enter mobile number along with country code'))
        if len(mobile_number) <= 10:
            raise ValidationError(_('Please enter country code before mobile_number'), code='invalid')

        return mobile_number

    def clean_full_name(self):
        """Validating fullname of user

        If fullname is not entered the validation error is raised.

        Variable
        ----------
        full_name : str
            fullname of custom user

        Raises
        ---------
        ValidationError
             When full nsme is empty

        Return
        --------
        full_name form field
        
        """
        full_name = self.cleaned_data.get('full_name')

        if not full_name:
            raise ValidationError(_('Full name should not be empty'))

        return full_name
