from django.db.models import Count

from .models import Bank


def get_user_banks(request):
    user = request.user
    user_bank_context = Bank.objects.filter(bank_accounts__user=user).annotate(accounts_count=Count('bank_accounts'))

    return user_bank_context
