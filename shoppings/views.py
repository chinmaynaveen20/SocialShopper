from django.shortcuts import render, redirect, get_object_or_404
from .models import Shopping
from shoppings_requests.models import ShoppingRequest
from accounts.models import AppUser
from django.contrib.auth.decorators import login_required
from datetime import datetime

def user_home(request, status = "pr"):
    if request.user.is_authenticated:
        user = AppUser.objects.filter(user = request.user)
        user = list(user)[0]
        shoppings = Shopping.objects.filter(
            status = status.upper()
        ).exclude(shopper = user)
        context = {"shoppings": shoppings, "status" : status.lower()}
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


def add_sr(request):
    if request.user.is_authenticated:
        if request.method == "POST" :
            print("Adding a Shopping request")


@login_required()
def add_shopping(request):
    if request.method == "POST":
        venue = request.POST["venue"]
        date = request.POST["date"]
        time = request.POST["time"]
        datetime_str = date + " " + time
        dt = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
        print(dt)
        shopper = AppUser.objects.filter(user=request.user)
        shopper = list(shopper)[0]
        shopping = Shopping(
            shopper = shopper,
            venues = venue,
            datetime = dt,
            total_amount = 0
        )
        shopping.save()
        return redirect("tripList")