from django.urls import path

from . import views


urlpatterns = [
    path('<int:bank_id>/', views.GetBankAccount.as_view(), name='accounts-class'),

]
