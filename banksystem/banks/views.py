from django.shortcuts import render
from django.db.models import Count
from .models import Bank


def get_banks(request):
    user = request.user
    user_banks = Bank.objects.filter(bank_accounts__user=user).annotate(accounts_count=Count('bank_accounts'))

    return render(request, 'banks.html', {'banks': user_banks})
