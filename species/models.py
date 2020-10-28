from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Specie(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()
    breed = models.ManyToManyField(Breed)

    def __str__(self):
        return self.name
