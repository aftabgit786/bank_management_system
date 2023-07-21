import logging

from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .forms import signup_form, login_form

logger = logging.getLogger('Django')


class SignupPage(TemplateView):
    template_name = 'class_based/signup.html'

    def post(self, request):
        signup_form(request)

        return redirect('login-class')


class LoginPage(TemplateView):
    template_name = 'class_based/login.html'

    def post(self, request):
        login_form(request)

        return redirect('banks-class')


def signup_page(request):
    if request.method == "POST":
        signup_form(request)

        return redirect('login-function')

    return render(request, 'function_based/signup.html')


def login_page(request):
    if request.method == 'POST':
        login_form(request)

        return redirect('banks-function')

    return render(request, 'function_based/login.html')
