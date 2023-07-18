from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Bank


class GetBanks(TemplateView):
    template_name = 'class_based/banks.html'

    def get(self, request):
        user = request.user
        get_context_data = Bank.objects.filter(bank_accounts__user=user).annotate(accounts_count=Count('bank_accounts'))

        return self.render_to_response({'banks': get_context_data})


def get_banks(request):
    user = request.user
    get_context_data = Bank.objects.filter(bank_accounts__user=user).annotate(accounts_count=Count('bank_accounts'))

    return render(request, 'function_based/banks.html', {'banks': get_context_data})
