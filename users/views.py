from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.shortcuts import render
from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from django.contrib.auth.models import User
from users.models import UserProfile


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            name = form.cleaned_data["first_name"]
            email = form.cleaned_data["email"]

            user = User.objects.create_user(
                email=email,
                username=username,
                password=password,
                first_name=name,
            )

            user.save()

            UserProfile(user=user).save()

            auth_user = auth.authenticate(
                username=username,
                password=password,
            )

            if auth_user is not None:
                auth.login(request, auth_user)
                return home(request)

        for field in form.errors:
            form[field].field.widget.attrs["class"] = "form-control is-invalid"

        return render(request, "users/register.html", {"form": form})
    else:
        return render(request, "users/register.html", {"form": UserRegisterForm()})


@login_required
def home(request):
    user_profile = UserProfile.objects.get(id=request.user.id)
    return render(request, "users/home.html", {"user": user_profile})


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            auth.login(request, user)
            return home(request)

        for field in form.errors:
            form[field].field.widget.attrs["class"] = "form-control is-invalid"

        return render(request, "users/login.html", {"form": form})
    else:
        return render(request, "users/login.html", {"form": UserLoginForm()})


@login_required
def logout(request):
    auth.logout(request)
    return render(request, "users/login.html", {"form": UserLoginForm()})


@login_required
def profile(request):
    user_id = request.user.id
    user_profile = UserProfile.objects.get(id=user_id)
    pets = UserProfile.objects.get(user=user_id).pets.all()
    return render(
        request, "users/profile.html", {"pets": pets, "profile": user_profile}
    )


@login_required
def update(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            profile_data = UserProfile.objects.get(user=request.user.id)
            profile_data.user.email = form.cleaned_data["email"]
            profile_data.user.first_name = form.cleaned_data["first_name"]
            profile_data.user.last_name = form.cleaned_data["second_name"]
            profile_data.user.save()

            if request.FILES:
                profile_data.picture.delete()
                profile_data.picture = request.FILES.get("picture")

            profile_data.cellphone = form.cleaned_data["cellphone"]
            profile_data.birthday = form.cleaned_data["birthday"]
            profile_data.address = form.cleaned_data["address"]
            profile_data.save()
            return profile(request)
    else:
        profile_data = UserProfile.objects.get(user=request.user.id)
        user = {
            "email": profile_data.user.email,
            "first_name": profile_data.user.first_name,
            "second_name": profile_data.user.last_name,
        }
        user.update(model_to_dict(profile_data))
        form = UserUpdateForm(user)
        return render(request, "users/update.html", {"form": form})
