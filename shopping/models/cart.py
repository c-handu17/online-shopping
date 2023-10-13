from django.db import models
from .user import User
from .product import Product


class Cart(models.Model):
    user_id = models.CharField(max_length=150)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)