from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from users.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User
from users.models import UserProfile


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

            UserProfile(user=user).save()

            auth_user = auth.authenticate(
                username=username,
                password=password,
            )

            if auth_user is not None:
                auth.login(request, auth_user)
                return render(request, "users/home.html", {"user": auth_user})

        for field in form.errors:
            form[field].field.widget.attrs['class'] = "form-control is-invalid"

        return render(request, "users/register.html", {"form": form})
    else:
        return render(request, "users/register.html", {"form": UserRegisterForm()})


@login_required
def home(request):
    return render(request, "users/home.html")


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            auth.login(request, user)
            return render(request, "users/home.html", {"user": user})

        for field in form.errors:
            form[field].field.widget.attrs['class'] = "form-control is-invalid"

        return render(request, "users/login.html", {"form": form})
    else:
        return render(request, "users/login.html", {"form": UserLoginForm()})


@login_required
def logout(request):
    auth.logout(request)
    return render(request, "users/login.html", {"form": UserLoginForm()})


@login_required
def profile(request):
    pets = UserProfile.objects.get(user=request.user).pets.all()
    return render(request, "users/profile.html", {"pets": pets})
