from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
