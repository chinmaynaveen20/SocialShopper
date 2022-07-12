from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from shoppings.models import Shopping
from .models import AppUser

# Create your views here.
def home(request):
    return render(request, "login.html")

def login(request):
    if request.method == "POST" :
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect("user_home")
        else:
            return render(request, "login.html")

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect("user_home")

def mytrips(request, status="pr"):
    if request.user.is_authenticated:
        context = {}
        user= AppUser.objects.filter(user = request.user)
        user = list(user)[0]
        trips = Shopping.objects.filter(
            shopper = user,
            status = status.upper()
        )
        context["shoppings"] = trips
        context["status"] = status
        return render(request, "mytrips.html", context)

