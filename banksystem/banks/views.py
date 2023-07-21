import logging

from django.shortcuts import render
from django.views.generic import TemplateView

from .utils import get_user_banks

logger = logging.getLogger('Django')


class GetBanks(TemplateView):
    template_name = 'class_based/banks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["banks"] = get_user_banks(self.request)

        return context


def get_banks(request):
    context = get_user_banks(request)

    return render(request, 'function_based/banks.html', {'banks': context})
