from django.db import models
from django.contrib.auth.models import User

class AppUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    society = models.CharField(max_length=30)
    phone = models.CharField(max_length = 20)
    shopsDone = models.IntegerField()
    shopsRequested = models.IntegerField()
    approved = models.BooleanField()

    def __str__(self):
        return f"{self.name} {self.phone} {self.email} {self.society}"
