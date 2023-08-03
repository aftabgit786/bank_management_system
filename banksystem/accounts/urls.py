from django.urls import path

from . import views


urlpatterns = [
    path('', views.BankListAPIView.as_view(), name='accounts'),
    path('<int:pk>/', views.BankDetailAPIView.as_view(), name='accounts-details'),
    path('admin/', views.AdminBankListAPIView.as_view(), name='admin_bank_list'),
    path('admin/<int:user_id>/', views.AdminBankListAPIView.as_view(), name='admin_bank_list_by_user'),
]
