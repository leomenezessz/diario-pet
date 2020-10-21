from django.db import models


class Pet(models.Model):
    SIZES = (("P", "Pequeno"), ("M", "Médio"), ("G", "Grande"))
    GENDERS = (("F", "Fêmea"), ("M", "Macho"))
    picture = models.ImageField(upload_to="pets/images/")
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    specie = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS)
    size = models.CharField(max_length=1, choices=SIZES)
