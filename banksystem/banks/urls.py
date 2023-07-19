from django.urls import path

from . import views


urlpatterns = [
    path('class/', views.GetBanks.as_view(), name='banks-class'),
    path('function/', views.get_banks, name='banks-function'),
]
