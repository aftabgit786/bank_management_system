from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    dob = models.DateField(null=True)
    city = models.CharField(max_length=150)
