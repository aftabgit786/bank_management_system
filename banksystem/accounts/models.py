from django.db import models

from .choices import AccountType
from users.models import Users
from banks.models import Banks


class Accounts(models.Model):
    number = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=AccountType.choices, default=AccountType.CURRENT)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_accounts')
    bank = models.ForeignKey(Banks, on_delete=models.CASCADE, related_name='bank_accounts')

    def __str__(self):
        return self.number
