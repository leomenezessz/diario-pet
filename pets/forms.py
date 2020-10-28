from django import forms
from django.forms import Select
from species.models import Specie, Breed


class PetsRegisterForm(forms.Form):
    name = forms.CharField(
        label="Nome do Pet: ",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: Lully"}),
        error_messages={"required": "O nome do pet não pode estar vazio."},
    )
    gender = forms.ChoiceField(
        choices=(("F", "Fêmea"), ("M", "Macho")), label="Gênero: "
    )
    specie = forms.ModelChoiceField(
        queryset=Specie.objects.all(),
        widget=Select(attrs={"onchange": "getBreeds()"}),
        error_messages={
            "invalid_choice": "Por favor selecione uma espécie para seu pet."
        },
        label="Espécie: ",
    )
    breed = forms.ModelChoiceField(
        queryset=Breed.objects.all(),
        error_messages={"invalid_choice": "Por favor selecione uma raça para seu pet."},
        label="Raça: ",
    )
