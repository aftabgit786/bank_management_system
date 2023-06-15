from django.shortcuts import render, HttpResponse

from .models import Bank


def banks(request):
    bank = Bank.objects.all()
    return render(request, 'bank.html', {'banks': bank})
