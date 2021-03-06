# Generated by Django 3.1.2 on 2020-11-07 01:52
from django.db import migrations

CAT = "Gato"
DOG = "Cachorro"

DOG_BREEDS = ["Pitbull", "Yorkshire", "Shi Tzu", "Vira-Lata", "Pastor Alemão"]
CATS_BREEDS = ["Persa", "Siamês", "Angora", "Siberiano", "Angorá"]


def add_dogs_specie_and_breeds(apps, schema_editor):
    dog_specie = apps.get_model("species", "Specie").objects.create(name=DOG)
    breed = apps.get_model("species", "Breed")
    for name in DOG_BREEDS:
        dog_breed = breed.objects.create(name=name)
        dog_specie.breed.add(dog_breed)


def add_cats_specie_and_breeds(apps, schema_editor):
    cat_specie = apps.get_model("species", "Specie").objects.create(name=CAT)
    breed = apps.get_model("species", "Breed")
    for name in CATS_BREEDS:
        cat_breed = breed.objects.create(name=name)
        cat_specie.breed.add(cat_breed)


class Migration(migrations.Migration):
    dependencies = [
        ('species', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_cats_specie_and_breeds),
        migrations.RunPython(add_dogs_specie_and_breeds)
    ]
