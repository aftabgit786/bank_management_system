from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, redirect

from .models import User


def signup_page(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        username = request.POST.get('username', '')

        password = request.POST.get('password', '')
        password_confirmation = request.POST.get('password_confirmation', '')

        email = request.POST.get('email', '')
        dob = request.POST.get('dob', '')
        city = request.POST.get('city', '')

        if firstname == '' or lastname == '' or username == ''\
                or password == '' or email == '' or dob == '' or city == '':

            return HttpResponse('Please fill in all fields')

        if password != password_confirmation:

            return HttpResponse('Passwords do not match')

        user = User(first_name=firstname, last_name=lastname, username=username, email=email,
                    password=password, password_confirmation=password_confirmation, dob=dob, city=city)
        user.save()

        return redirect('login/')

    return render(request, 'signup.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:

            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('home/')

        return HttpResponse('Invalid username or password')

    return render(request, 'login.html')


def index(request):

    return HttpResponse('Welcome to the user profile')
