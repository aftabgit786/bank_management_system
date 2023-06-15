from django.shortcuts import render, HttpResponse

from .models import Bank


def banks(request):
    data = Bank.objects.all()

    return render(request, 'bank.html', {'banks': data})
