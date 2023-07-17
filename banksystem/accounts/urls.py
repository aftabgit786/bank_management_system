from django.urls import path

from .views import *


urlpatterns = [
    path('<int:bank_id>/class', GetBankAccount.as_view(), name='accounts-class'),
    path('<int:bank_id>/function', get_bank_accounts, name='accounts-function'),

]
