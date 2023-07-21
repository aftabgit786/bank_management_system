import logging

from django.shortcuts import render
from django.views.generic import TemplateView

from .utils import get_user_bank_accounts

logger = logging.getLogger('Django')


class GetBankAccount(TemplateView):
    template_name = 'accounts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        bank_id = self.kwargs.get('bank_id')
        context["accounts"] = get_user_bank_accounts(self.request, bank_id=bank_id)

        return context


def get_bank_accounts(request, bank_id):
    user_account_context = get_user_bank_accounts(request, bank_id)

    return render(request, 'accounts.html', {'accounts': user_account_context})

