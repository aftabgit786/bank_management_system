from django.db.models import Count
from django.views.generic import TemplateView

from .models import Bank


class GetBanks(TemplateView):
    template_name = 'banks.html'

    def get(self, request):
        user = request.user
        user_banks = Bank.objects.filter(bank_accounts__user=user).annotate(accounts_count=Count('bank_accounts'))

        return self.render_to_response({'banks': user_banks})
