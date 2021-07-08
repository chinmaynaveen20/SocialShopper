from django.db import models

from accounts.models import AppUser
from shoppings.models import Shopping

class ShoppingRequest(models.Model):

    REQUESTED = "RE"
    APPROVED = "AP"
    DENIED = "DE"
    CANCELED = "CA"

    status_choices = (
        (REQUESTED, "requested"), (APPROVED, "approved"), (DENIED, "denied"), (CANCELED, "canceled")
    )

    shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE, related_name= "requests")
    requester = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(max_length=2, choices=status_choices, default = REQUESTED)

    def __str__(self):
        return f"{self.requester} {self.amount} {self.status}"


class Item(models.Model):

    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30, null=True)
    quantity = models.CharField(max_length=30)
    price = models.FloatField()
    shopping_request = models.ForeignKey(ShoppingRequest, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return f"{self.name} {self.quantity} {self.price} {self.shopping_request}"