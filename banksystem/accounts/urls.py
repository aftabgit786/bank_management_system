from django.urls import path

from . import views


urlpatterns = [
    path('', views.GetBankAllAccountAPIView.as_view(), name='accounts'),
    path('<int:pk>/', views.GetBankAccountViaIdsAPIView.as_view(), name='accounts-details'),
]
