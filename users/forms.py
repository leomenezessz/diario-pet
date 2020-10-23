from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Ex.: Lully@13"}),
        error_messages={"required": "O nome do usuário não pode estar vazio."}
    )
    email = forms.EmailField(
        label="Email",
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Ex.: email@gmail.com"}),
        error_messages={"required": "O email precisa ser preenchido."}
    )

    password = forms.CharField(
        label="Senha",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Ex.: GHJlP*&"}),
        error_messages={"required": "A senha precisa ser informada."}
    )

    repeat_password = forms.CharField(
        label="Repetir senha",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Ex.: GHJlP*&"}),
        error_messages={"required": "A senha repetida precisa ser informada."}
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
