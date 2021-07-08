from django.db import models

from accounts.models import AppUser


class Shopping(models.Model):

    PROPOSED = "PR"
    ACTIVE = "AC"
    COMPLETED = "CO"
    status_choices = (
        (PROPOSED, "proposed"), (ACTIVE, "active"), (COMPLETED, "completed")
    )

    shopper = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=status_choices, default=PROPOSED)
    total_amount = models.FloatField()
    venues = models.CharField(max_length=30)
    datetime = models.DateTimeField()

    def __str__(self):
      return   f"{self.shopper} {self.status} {self.datetime}"

