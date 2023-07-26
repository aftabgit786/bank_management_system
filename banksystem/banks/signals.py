import random

from django.db.models.signals import post_save
from django.dispatch import receiver
from banks.models import Bank
from accounts.models import Account
from users.models import User


@receiver(post_save, sender=Bank)
def create_accounts_for_users(created, instance, **kwargs):
    if created:
        users = User.objects.all()
        for user in users:
            set_account_numbers = random.randint(00000000000000, 99999999999999)
            Account.objects.create(user=user, bank=instance, number=set_account_numbers)
