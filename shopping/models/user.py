from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    userName = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()