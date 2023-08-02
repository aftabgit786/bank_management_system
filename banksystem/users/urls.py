from django.urls import path

from . import views


urlpatterns = [
    path('', views.SignupPage.as_view(), name='signup'),
    path('login/', views.LoginPage.as_view(), name='login'),
]
