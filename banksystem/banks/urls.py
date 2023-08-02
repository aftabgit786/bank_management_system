from django.urls import path

from . import views


urlpatterns = [
    path('', views.GetBanksAPIView.as_view(), name='banks-class'),
]
