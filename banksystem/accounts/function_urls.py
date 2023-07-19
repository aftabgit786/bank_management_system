from django.urls import path

from . import views


urlpatterns = [
    path('<int:bank_id>/', views.get_bank_accounts, name='accounts-function'),
]
