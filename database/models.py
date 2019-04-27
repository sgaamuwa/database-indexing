from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __init__(self, user_name, first_name, last_name):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return self.user_name

class Address(models.Model):
    street = models.TextField(max_length=200)
    city = models.CharField(max_length=200)
    postal_code = models.TextField(max_length=200)
    country = models.CharField(max_length=200)