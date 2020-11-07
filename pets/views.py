from logging import getLogger

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from pets.forms import PetsRegisterForm
from pets.models import Pet
from species.models import Specie
from users.models import UserProfile


@login_required
def register(request):
    if request.method == "POST":
        form = PetsRegisterForm(request.POST)

        if form.is_valid():

            pet = Pet(
                name=form.cleaned_data["name"],
                breed=form.cleaned_data["breed"],
                gender=form.cleaned_data["gender"],
                specie=form.cleaned_data["specie"],
                birthday=form.cleaned_data["birthday"]
            )

            if request.FILES:
                pet.picture = request.FILES.get("picture")

            pet.save()

            user = UserProfile.objects.get(id=request.user.id)
            user.pets.add(pet)

            return render(request, "users/home.html", {"user": user})

        for field in form.errors:
            form[field].field.widget.attrs['class'] = "form-control is-invalid"

        return render(request, "pets/register.html", {"form": form})
    else:
        return render(request, "pets/register.html", {"form": PetsRegisterForm()})


@login_required
def breeds(request):
    if request.method == "POST":
        specie = request.POST.get("specie")
        breeds_list = []
        for breed in Specie.objects.get(name=specie).breed.all():
            breeds_list.append({breed.id: breed.name})
        return JsonResponse({"breeds": breeds_list})


@login_required
def list(request):
    pets = UserProfile.objects.get(id=request.user.id).pets.all()
    return render(request, "pets/list.html", {"pets": pets})


@login_required
def update(request):
    pets = UserProfile.objects.get(id=request.user.id).pets.all()
    return render(request, "pets/list.html", {"pets": pets})