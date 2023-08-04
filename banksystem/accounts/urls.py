from django.urls import path

from . import views


urlpatterns = [
    path('', views.BankListAPIView.as_view(), name='accounts'),
    path('<int:pk>/', views.BankDetailAPIView.as_view(), name='accounts-details'),
    path('list/', views.AdminBankListAPIView.as_view(), name='admin_bank_list'),
]
