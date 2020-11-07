from django.db import models
from species.models import Breed, Specie


class Pet(models.Model):
    SIZES = (("P", "Pequeno"), ("M", "Médio"), ("G", "Grande"))
    GENDERS = (("F", "Fêmea"), ("M", "Macho"))
    picture = models.ImageField(upload_to="pets/images/")
    name = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, null=True)
    color = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS)
    size = models.CharField(max_length=1, choices=SIZES)
    breed = models.ForeignKey(Breed, on_delete=models.DO_NOTHING)
    specie = models.ForeignKey(Specie, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
