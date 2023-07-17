from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Account


class GetBankAccount(TemplateView):
    template_name = 'accounts.html'

    def get(self, request, bank_id):
        user = request.user
        get_context_data = Account.objects.filter(user=user, bank_id=bank_id)

        return self.render_to_response({'accounts': get_context_data})


def get_bank_accounts(request, bank_id):
    user = request.user
    get_context_data = Account.objects.filter(user=user, bank_id=bank_id)

    return render(request, 'accounts.html', {'accounts': get_context_data})
