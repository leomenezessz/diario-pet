from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import TextInput, CharField, DateField


class UserRegisterForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control "}),
        error_messages={"required": "O nome do usuário não pode estar vazio."},
    )
    first_name = CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        error_messages={"required": "É necessário informar o primeiro nome."},
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control "}),
        error_messages={"required": "O email precisa ser preenchido."},
    )

    password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control "}),
        error_messages={"required": "A senha precisa ser informada."},
    )

    repeat_password = forms.CharField(
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


class UserUpdateForm(forms.Form):
    picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={"class": "file-field", "type": "file"}),
    )
    first_name = CharField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    second_name = CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control "})
    )
    birthday = DateField(required=False, widget=forms.SelectDateWidget())
    address = CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control "}),
        error_messages={"required": "O email precisa ser preenchido."},
    )
    cellphone = CharField(
        required=False, widget=forms.TextInput(attrs={"class": "form-control"})
    )
