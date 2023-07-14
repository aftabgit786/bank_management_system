from django.shortcuts import render
from .models import Account


def get_bank_accounts(request, bank_id):
    user = request.user
    accounts_data = Account.objects.filter(user=user, bank_id=bank_id)
    total_accounts = accounts_data.count()

    return render(request, 'accounts.html', {'accounts': accounts_data, 'total_accounts': total_accounts})
