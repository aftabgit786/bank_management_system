from django.shortcuts import render
from .models import Bank


def banks(request):
    user = request.user
    user_banks = Bank.objects.filter(bank_accounts__user=user)

    return render(request, 'bank.html', {'banks': user_banks})
