from django.urls import path

from . import views


urlpatterns = [
    path('', views.SignupPage.as_view(), name='signup-class'),
    path('class/login/', views.LoginPage.as_view(), name='login-class'),
    path('function/', views.signup_page, name='signup-function'),
    path('function/login/', views.login_page, name='login-function'),
]
