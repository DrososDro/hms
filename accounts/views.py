from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import authenticated_user, unauthenticated_user

# Create your views here.


@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        try:
            user = authenticate(
                request,
                username=request.POST["username"],
                password=request.POST["password"],
            )
            login(request, user)
            messages.success(request, "You Successfuly login")
            return redirect("home")

        except Exception:
            messages.error(request, "Emair or password are invalid")

    return render(request, "accounts/register_login.html")


@authenticated_user
def logout_user(request):
    logout(request)
    messages.success(request, "Successfuly logout")
    return redirect("login")
