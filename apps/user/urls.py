""" apps/user/urls.py """
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from apps.user import views # pylint: disable=import-error


urlpatterns = [
    path('registration/form/',
        views.RegistrationFormView.as_view(),
        name='user_registration_form'
    ),

    path('login/form/',
        views.LoginFormView.as_view(),
        name='user_login_form'
    ),

    path('logout/',
        views.LogoutView.as_view(),
        name='user_logout_form'
    ),

    path('change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='commons/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'
    ),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'
    ),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'
    ),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'
    )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
