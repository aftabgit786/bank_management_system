from django.urls import path

from . import views


urlpatterns = [
    path('', views.GetBanks.as_view(), name='banks'),
]
