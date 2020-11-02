from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import TextInput


class UserRegisterForm(forms.Form):
    username = forms.CharField(
        label="Username: ",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control "}),
        error_messages={"required": "O nome do usuário não pode estar vazio."},
    )
    email = forms.EmailField(
        label="Email: ",
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control "}),
        error_messages={"required": "O email precisa ser preenchido."},
    )

    password = forms.CharField(
        label="Senha: ",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control "}),
        error_messages={"required": "A senha precisa ser informada."},
    )

    repeat_password = forms.CharField(
        label="Repetir senha: ",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control "}),
        error_messages={"required": "A senha repetida precisa ser informada."},
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            self.add_error("username", f"O usuário {username} já existe.")
        return username

    def clean(self):
        password = self.cleaned_data.get("password")
        repeated_password = self.cleaned_data.get("repeat_password")

        if password != repeated_password:
            self.add_error("repeat_password", "As senhas devem ser iguais.")


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=TextInput(attrs={"class": "form-control "}),
        error_messages={"required": "O nome do usuário precisa ser informado."},
    )

    password = forms.CharField(
        max_length=100,
        required=True,
        widget=TextInput(attrs={"class": "form-control", "type": "password"}),
        error_messages={"required": "A senha precisa ser informada."},
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if not User.objects.filter(username=username).exists():
            self.add_error("username", "Usuário não cadastrado.")
            return

        if not authenticate(username=username, password=password):
            self.add_error("password", "Usuário ou senha inválidos.")
            return
