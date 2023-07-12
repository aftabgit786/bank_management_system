from django.shortcuts import render
from .models import Banks


def get_banks(request):
    user = request.user
    user_banks = Banks.objects.filter(bank_accounts__user=user).distinct()

    return render(request, 'banks.html', {'banks': user_banks})
