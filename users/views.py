from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from users.forms import UserRegisterForm
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = User.objects.create_user(
                email=form.cleaned_data["email"],
                username=username,
                password=password,
            )

            user.save()

            logged_user = authenticate(
                username=username,
                password=password,
            )

            if logged_user is not None:
                return render(request, "users/home.html", {"username": logged_user.username})

        return render(request, "users/register.html", {"form": form})
    else:
        return render(request, "users/register.html", {"form": UserRegisterForm()})


@login_required
def home(request):
    return render(request, "users/home.html")
