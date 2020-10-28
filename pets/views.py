from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from pets.forms import PetsRegisterForm
from pets.models import Pet
from species.models import Specie
from users.models import UserProfile


@login_required(login_url="/users/login/")
def register(request):
    if request.method == "POST":
        form = PetsRegisterForm(request.POST)
        if form.is_valid():
            pet = Pet(
                name=form.cleaned_data["name"],
                breed=form.cleaned_data["breed"],
                gender=form.cleaned_data["gender"],
                specie=form.cleaned_data["specie"],
            )
            pet.save()

            UserProfile.objects.get(user=request.user).pets.add(pet)
            return render(request, "users/home.html", {"user": request.user})
        return render(request, "pets/register.html", {"form": form})
    else:
        return render(request, "pets/register.html", {"form": PetsRegisterForm()})


@login_required(login_url="/users/login/")
def breeds(request):
    if request.method == "POST":
        specie = request.POST.get("specie")
        breeds_list = list()
        breeds_list.append("---------")
        for breed in Specie.objects.get(name=specie).breed.all():
            breeds_list.append(breed.name)
        return JsonResponse({"breeds": breeds_list})
