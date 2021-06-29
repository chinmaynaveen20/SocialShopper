from django.shortcuts import render, redirect

def user_home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect("home")

