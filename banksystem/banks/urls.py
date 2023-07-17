from django.urls import path

from .views import *


urlpatterns = [
    path('class', GetBanks.as_view(), name='banks-class'),
    path('function', get_banks, name='banks-function'),
]
