# your django admin
from shopping.models import Product, Cart, User, Address
from django.contrib import admin

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(User)
admin.site.register(Address)
