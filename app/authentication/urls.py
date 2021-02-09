from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path

from authentication.decorators import check_recaptcha
from authentication.views import RegisterFormView, activate

urlpatterns = [
    # custom urls + recaptcha decorator
    path(
        "accounts/register/",
        check_recaptcha(RegisterFormView.as_view()),
        name="register",
    ),
    path("accounts/activate/<uidb64>/<token>", activate, name="activate"),
    # django.contrib.auth urls + recaptcha decorator
    path("accounts/login/", check_recaptcha(LoginView.as_view()), name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    # django.contrib.auth urls + recaptcha decorator
    path(
        "accounts/password_reset/",
        check_recaptcha(PasswordResetView.as_view()),
        name="password_reset",
    ),
    path(
        "accounts/password_reset/done/",
        PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "accounts/reset/done/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
