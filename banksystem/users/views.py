from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponse, redirect
from django.views.generic import TemplateView

from .models import User


class SignupPage(TemplateView):
    template_name = 'signup.html'

    def post(self, request):
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        dob = request.POST.get('dob', '')
        city = request.POST.get('city', '')

        if all([firstname, lastname, username, password, email, dob, city]):
            user = User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                username=username,
                email=email,
                password=password,
                dob=dob,
                city=city
            )
            user.save()

            return redirect('login')

        return HttpResponse('Please provide all fields')


class LoginPage(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('banks')

            return HttpResponse('Invalid username or password')

        return HttpResponse('Please provide both username and password')
