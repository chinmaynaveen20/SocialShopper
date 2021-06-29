from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth

# Create your views here.
def home(request):
    return render(request, "login.html")

def login(request):
    if request.method == "POST" :
        email = request.POST.get("email")
        password = request.POST.get("password")

        username = "user1"
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect("user_home")

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect("user_home")

