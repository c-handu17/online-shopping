from django.db import models
from .user import User


class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    pincode = models.IntegerField()