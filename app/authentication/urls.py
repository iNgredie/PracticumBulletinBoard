from django.urls import path

from authentication.views import RegisterFormView

urlpatterns = [
    path('register', RegisterFormView.as_view(), name="register"),
]