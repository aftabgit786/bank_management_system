from django.views.generic import TemplateView

from .models import Account


class GetBankAccount(TemplateView):
    template_name = 'accounts.html'

    def get(self, request, bank_id):
        user = request.user
        accounts_data = Account.objects.filter(user=user, bank_id=bank_id)

        return self.render_to_response({'accounts': accounts_data})
