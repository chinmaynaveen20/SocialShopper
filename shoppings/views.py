from django.shortcuts import render, redirect, get_object_or_404
from .models import Shopping


def user_home(request, status = "pr"):
    if request.user.is_authenticated:
        shoppings = Shopping.objects.all().filter(
            status = status.upper()
        )
        context = {"shoppings": shoppings}
        return render(request, "home.html", context)

    else:
        return redirect("home")


def shopping_home(request, shopping_id):
    if request.user.is_authenticated:
        if request.method == "POST" :
            shopping = get_object_or_404(Shopping, pk = shopping_id)
            context = {"shopping": shopping}
            return render(request, "shopping_detail.html", context)
