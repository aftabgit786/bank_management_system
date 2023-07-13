from django.shortcuts import render
from .models import Bank


def get_banks(request):
    user = request.user
    user_banks = Bank.objects.filter(bank_accounts__user=user)
    accounts_counts = user_banks.count()

    return render(request, 'banks.html', {'banks': user_banks.distinct(), 'total_accounts': accounts_counts})
