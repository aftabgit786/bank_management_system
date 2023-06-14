from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, redirect

from .models import User


def signup_page(request):
    if request.method == "POST":
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

            return redirect('login/')
        return HttpResponse('Please provide all fields')

    return render(request, 'signup.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('home/')

            return HttpResponse('Invalid username or password')

        return HttpResponse('Please provide both username and password')

    return render(request, 'login.html')


def home(request):

    return HttpResponse('Welcome to the user profile')
