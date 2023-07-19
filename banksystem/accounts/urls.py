from django.urls import path

from . import views


urlpatterns = [
    path('<int:bank_id>/class/', views.GetBankAccount.as_view(), name='accounts-class'),
    path('<int:bank_id>/function/', views.get_bank_accounts, name='accounts-function'),

]
