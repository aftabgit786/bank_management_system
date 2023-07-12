from django.urls import path
from .views import get_bank_accounts


urlpatterns = [
    path('<int:bank_id>/', get_bank_accounts, name='accounts'),
]
