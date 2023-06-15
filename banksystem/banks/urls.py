from django.urls import path

from . import views


urlpatterns = [
    path('', views.banks, name='banks'),
]
