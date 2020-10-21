from django.db import models
from pets.models import Pet


class User(models.Model):
    picture = models.ImageField(upload_to="users/images/")
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cellphone = models.IntegerField()
    birthday = models.DateField()
    address = models.CharField(max_length=200)
    pets = models.ManyToManyField(Pet)
