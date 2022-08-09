from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from shoppings.models import Shopping
from .models import AppUser
from django.contrib.auth.models import User

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

def signup(request):
    if request.method == "POST":
        username = request.POST["user_username"]
        password = request.POST["user_password"]
        name = request.POST["user_name"]
        email = request.POST["user_email"]
        society = request.POST["user_society"]
        phoneNumber = request.POST["user_phone"]
        user = User.objects.create_user(username = username, password = password)
        appUser = AppUser(
            user=user,
            name =name,
            email = email,
            society = society,
            phone = phoneNumber,
            shopsDone = 0,
            shopsRequested = 0,
            approved = True
        )
        appUser.save()
        return redirect("home")


def signupPage(request):
    return render(request, "signup.html")

