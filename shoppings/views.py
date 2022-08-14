from django.shortcuts import render, redirect, get_object_or_404
from .models import Shopping
from shoppings_requests.models import ShoppingRequest, Item
from accounts.models import AppUser
from django.contrib.auth.decorators import login_required
from datetime import datetime

def user_home(request, status = "pr"):
    if request.user.is_authenticated:
        activate_trips()
        user = AppUser.objects.filter(user = request.user)
        user = list(user)[0]
        shoppings = Shopping.objects.filter(
            status = status.upper()
        ).exclude(shopper = user)
        context = {"shoppings": shoppings, "status" : status.lower()}
        return render(request, "home.html", context)

    else:
        return redirect("home")


def activate_trips():
    current_time = datetime.now()
    shoppings =  Shopping.objects.filter(
        status = "PR",
        datetime__gt = current_time
    )

    for shopping in shoppings:
        shopping.status = "AC"
        shopping.save()


def shopping_home(request, shopping_id):
    if request.user.is_authenticated:
        activate_trips()
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
            else:
                shoppingRequests = ShoppingRequest.objects.filter(
                    shopping=shopping
                )
            active_shopping = True if shopping.status == "AC" else False



            context = {"shopping": shopping, "isOwner" : isOwner, "shoppingRequests" : shoppingRequests, "active_shopping" : active_shopping}
            return render(request, "shopping_detail.html", context)


def add_sr(request, shopping_id):
    if request.user.is_authenticated:
        if request.method == "POST" :
            shopping = get_object_or_404(Shopping, pk = shopping_id)
            requester = AppUser.objects.filter(user=request.user)
            requester = list(requester)[0]
            amount = 0


            sr = ShoppingRequest(
                shopping=shopping,
                requester=requester,
                amount=amount
            )
            sr.save()
            name_1 = request.POST["name_1"]
            if len(name_1) >0:
                brand_1=request.POST["brand_1"]
                quantity_1 = request.POST["quantity_1"]
                price_1 = request.POST["price_1"]
                amount += float(price_1)
                item_1 = Item(name = name_1, brand = brand_1, price = price_1, quantity = quantity_1, shopping_request = sr)
                item_1.save()
            name_2 = request.POST["name_2"]
            if len(name_2) > 0:
                brand_2 = request.POST["brand_2"]
                quantity_2 = request.POST["quantity_2"]
                price_2 = request.POST["price_2"]
                amount += float(price_2)
                item_2 = Item(name = name_2, brand = brand_2, price = price_2, quantity = quantity_2, shopping_request = sr)
                item_2.save()

            name_3 = request.POST["name_3"]
            if len(name_3) > 0:
                brand_3 = request.POST["brand_3"]
                quantity_3 = request.POST["quantity_3"]
                price_3 = request.POST["price_3"]
                amount += float(price_3)
                item_3 = Item(name = name_3, brand = brand_3, price = price_3, quantity = quantity_3, shopping_request = sr)
                item_3.save()

            sr.amount = amount

            sr.save()
        return redirect("user_home")



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


def complete_shopping(request, shopping_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            shopping = get_object_or_404(Shopping, pk = shopping_id)
            if shopping:
                shopping.status = "CO"
                shopping.save()
                return redirect("tripList")
