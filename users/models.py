import os
import pathlib
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from pets.models import Pet


def change_path_and_rename_picture(instance, filename):
    upload_to = f"users/images/{instance.pk}"
    extension = pathlib.Path(filename).suffix
    new_filename = f"{uuid4().__str__()}{extension}"
    return os.path.join(upload_to, new_filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    objects = models.Manager()
    cellphone = models.CharField(max_length=20, default="")
    picture = models.ImageField(upload_to=change_path_and_rename_picture, default="users/images/default.png")
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200)
    pets = models.ManyToManyField(Pet)

    def __str__(self):
        return str(self.user)
