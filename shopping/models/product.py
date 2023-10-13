from django.db import models

category_choices = (
    ("ELECTRONICS", "ELECTRONICS"),
    ("CLOTHING", "CLOTHING"),
    ("KITCHEN APPLIANCES", "KITCHEN APPLIANCES"),
    ("BEAUTY PRODUCTS", "BEAUTY PRODUCTS"),
    ("BOOKS", "BOOKS")
)

brand_choices = (
    ("PHILIPS", "PHILIPS"),
    ("PUMA", "PUMA"),
    ("ELICA", "ELICA"),
    ("SUGAR", "SUGAR"),
    ("AMAZON BOOKS", "AMAZON BOOKS")
)


class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    category = models.CharField(max_length=50, choices=category_choices)
    brand = models.CharField(max_length=50, choices=brand_choices)