from django.shortcuts import render, redirect, get_object_or_404
from .models import Shopping
from shoppings_requests.models import ShoppingRequest
from accounts.models import AppUser

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
            isOwner  = request.user.username == shopping.shopper.user.username
            shoppingRequests = []
            if not isOwner:
                requester = AppUser.objects.filter(user = request.user)
                requester = list(requester)[0]
                shoppingRequests = ShoppingRequest.objects.filter(
                    shopping = shopping,
                    requester = requester
                )
            context = {"shopping": shopping, "isOwner" : isOwner, "shoppingRequests" : shoppingRequests}
            return render(request, "shopping_detail.html", context)
