from django.db import models

from .choices import Types
from users.models import User
from banks.models import Bank


class Account(models.Model):
    number = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=Types.choices, default=Types.CURRENT)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_accounts')
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='bank_accounts')

    def __str__(self):
        return self.number
