from django import forms
from django.forms import Select
from species.models import Specie, Breed


class PetsRegisterForm(forms.Form):
    picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={"class": "file-field", "type": "file"}),
    )
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        error_messages={"required": "O nome do pet não pode estar vazio."},
    )
    gender = forms.ChoiceField(
        choices=(("F", "Fêmea"), ("M", "Macho")),
        widget=forms.Select(attrs={"class": "custom-select custom-select-sm"}),
    )
    specie = forms.ModelChoiceField(
        queryset=Specie.objects.all(),
        initial=0,
        widget=Select(
            attrs={"onchange": "getBreeds()", "class": "custom-select custom-select-sm"}
        ),
        error_messages={
            "invalid_choice": "Por favor selecione uma espécie para seu pet."
        },
    )
    breed = forms.ModelChoiceField(
        queryset=Breed.objects.all(),
        initial=0,
        error_messages={"invalid_choice": "Por favor selecione uma raça para seu pet."},
        widget=Select(attrs={"class": "custom-select custom-select-sm"}),
    )
    birthday = forms.DateField(required=True, widget=forms.SelectDateWidget())
