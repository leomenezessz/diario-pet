from django.contrib.auth.models import User
from django.db import models
from pets.models import Pet


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    objects = models.Manager()
    picture = models.ImageField(upload_to="users/images/")
    second_name = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=20, default="")
    birthday = models.DateField(auto_now=True)
    address = models.CharField(max_length=200)
    pets = models.ManyToManyField(Pet)

    def __str__(self):
        return str(self.user)
