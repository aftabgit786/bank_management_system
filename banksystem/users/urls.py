from django.urls import path

from . import views


urlpatterns = [
    path('login/home/', views.home, name='home'),
    path('', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
]
