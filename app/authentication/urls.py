from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from authentication.decorators import check_recaptcha
from authentication.views import RegisterFormView, activate

urlpatterns = [
    # custom urls + recaptcha decorator
    path('register/', check_recaptcha(RegisterFormView.as_view()), name='register'),
    path('activate/<uidb64>/<token>',
         activate, name='activate'),
    # django.contrib.auth urls + recaptcha decorator
    path('login/', check_recaptcha(LoginView.as_view()), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # django.contrib.auth urls + recaptcha decorator
    path('password_reset/', check_recaptcha(PasswordResetView.as_view()), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]