from django.shortcuts import redirect
from django.views.generic import TemplateView

from .forms import signup_form, login_form


class SignupPage(TemplateView):
    template_name = 'signup.html'

    def post(self, request):
        signup_form(request)

        return redirect('login-class')


class LoginPage(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        login_form(request)

        return redirect('banks-class')
