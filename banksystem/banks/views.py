from django.shortcuts import render
from .models import Bank


def get_banks(request):
    user = request.user
    total_bank_accounts = Bank.objects.filter(bank_accounts__user=user)
    user_banks = Bank.objects.filter(bank_accounts__user=user).distinct()
    total_account_counts = total_bank_accounts.count()

    return render(request, 'banks.html', {'banks': user_banks, 'total_account': total_account_counts})
