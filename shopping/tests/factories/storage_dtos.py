import factory
from shopping.interactors.dtos import *


class ProductDTOFactory(factory.Factory):
    class Meta:
        model = ProductDTO

    product_id = factory.sequence(lambda n: n)
    name = factory.Sequence(lambda n: f'Product {n}')
    price = 500
    description = "Philips light"


class UserDTOFactory(factory.Factory):
    class Meta:
        model = UserDTO

    name = factory.Sequence(lambda n: f'User {n}')
    userName = factory.Sequence(lambda n: f'User {n}')
    age = 20


class AddToCartDTOFactory(factory.Factory):
    class Meta:
        model = AddToCartDTO
    user_id = factory.Sequence(lambda n: f'UserId {n}')
    product_id = factory.Sequence(lambda n: f'ProductId {n}')


class GetAllProductsUsingQueryParamsDTOFactory(factory.Factory):
    class Meta:
        model = ProductsWithQueryParamsDTO

    category = "ELECTRONICS"
    brand = "PHILIPS"
    sort_by = "PRICE"
    sort_value = "DESC"
