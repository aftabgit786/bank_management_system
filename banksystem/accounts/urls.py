from django.urls import path
from .views import GetBankAccount


urlpatterns = [
    path('<int:bank_id>/', GetBankAccount.as_view(), name='accounts'),
]
