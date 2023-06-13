from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=300)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    password_confirmation = models.CharField(max_length=100)
    dob = models.DateField()
    city = models.CharField(max_length=100)
