""" apps/user/views.py """
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout

# Core Django Class-based View modules
from django.views.generic.edit import FormView
from django.views.generic.base import View, RedirectView

# Native app module
from .forms import RegistrationForm, UserLoginForm # pylint: disable=import-error


class RegistrationFormView(FormView):
    """
    This class renders registration form page in which admin can
    input the data of its employees.

    """
    template_name = 'user/registration_form.html'
    form_class = RegistrationForm
    success_url = '/login/form/'

    def form_valid(self, form):
        """
        This method is called when the request method is post and
        form data is clean.

        """
        form.save()
        return super().form_valid(form)


class LoginFormView(FormView):
    """
    Login form view
    """
    template_name = 'user/login_form.html'
    success_url = '/'
    form_class = UserLoginForm
    # redirect_field_name = REDIRECT_FIELD_NAME

    def form_valid(self, form):
        """
        If the login form is valid and input data is clean.
        Then this method will invoke

        """
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        user = authenticate(self.request, email=email, password=password)
        login(self.request, user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(RedirectView):
    """
    Provides users the ability to logout.

    """
    url = '/login/form/'

    def get(self, request, *args, **kwargs):
        """
        This method will logout the user and redirects the user
        to login form page.

        """
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
