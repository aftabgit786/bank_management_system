from django.shortcuts import render

from .models import Account


def accounts(request):
    data = Account.objects.all()

    return render(request, 'accounts.html', {'accounts': data})
