from django.urls import path

from .views import *


urlpatterns = [
    path('', SignupPage.as_view(), name='signup-class'),
    path('login/class', LoginPage.as_view(), name='login-class'),
    path('function', signup_page, name='signup-function'),
    path('login/function', login_page, name='login-function'),
]
