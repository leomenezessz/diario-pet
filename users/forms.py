from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput


class UserRegisterForm(forms.Form):
    picture = forms.ImageField(label="Foto de perfil")
    first_name = forms.CharField(
        label="Primeiro nome",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: Lully"}),
    )
    second_name = forms.CharField(
        label="Segundo nome",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: Santos"}),
    )
    email = forms.EmailField(
        label="Email",
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Ex.: email@gmail.com"}),
    )
    password = forms.CharField(
        label="Senha",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Ex.: GHJlP*&"}),
    )
    cellphone = forms.CharField(
        label="Telefone ou celular",
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: (DDD) + Número"}),
    )
    birthday = forms.DateField(
        label="Data de aniversário",
        input_formats=["%d/%m/%Y"],
        required=True,
        widget=DateTimePickerInput(
            format="%d/%m/%Y",
            attrs={"placeholder": "Informa a data de seu aniversário"},
        ),
    )
    address = forms.CharField(
        label="Endereço",
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: Rua Pinheiros, 199"}),
    )
