from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.index, name='home'),
    path('', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
]
