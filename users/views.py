from django.shortcuts import render
from users.forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        pass
    else:
        context = {"form": UserRegisterForm()}
        return render(request, "users/register.html", context)
