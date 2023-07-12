from django.shortcuts import render
from .models import Account


def accounts(request, bank_name):
    user = request.user
    accounts_data = Account.objects.filter(user=user, bank__name=bank_name)

    return render(request, 'accounts.html', {'account': accounts_data})
