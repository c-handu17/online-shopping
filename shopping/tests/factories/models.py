import factory.django
from shopping.models import *


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    name = factory.Sequence(lambda n=1: f'User {n}')
    userName = factory.Sequence(lambda n=1: f'User {n}')
    age = 20


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n=1: f'User {n}')
    price = 500
    description = "Philips Light"
    category = 'ELECTRONICS'
    brand = 'PHILIPS'


class CartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cart
    user_id = factory.SubFactory(UserFactory)
    product_id = factory.SubFactory(ProductFactory)