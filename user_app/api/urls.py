from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

from user_app.api.views import logout_view, RegistrationView


urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    # path("register/", registration_view, name="register"),
    path("register/", RegistrationView.as_view(), name="register"),
    path("logout/", logout_view, name="register"),
]
