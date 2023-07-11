from django.urls import path
from .views import accounts


urlpatterns = [
    path('<str:bank_name>/', accounts, name='bank-accounts'),
]
