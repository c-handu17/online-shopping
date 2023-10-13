import factory
from shopping.interactors.dtos import AddToCartResponseDTO, ProductDTO, ProductResponseDTO
import json


class ProductResponseDTOFactory(factory.Factory):
    class Meta:
        model = ProductDTO

    product_id = factory.Sequence(lambda n: n)
    name = "Light"
    price = 500
    description = "Philips"


class ProductResponseDTOFactory_list(factory.Factory):
    class Meta:
        model = ProductResponseDTO
    products = factory.List([factory.SubFactory(ProductResponseDTOFactory)for _ in range(4)])
    products_count = 0


class ProductDTOEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ProductDTO):
            # Convert the ProductDTO object to a dictionary
            return {
                'product_id': obj.product_id,
                'name': obj.name,
                'price': obj.price,
                'description': obj.description,
            }
        return super().default(obj)


class AddToCartResponseDTOFactory(factory.Factory):
    class Meta:
        model = AddToCartResponseDTO
    cart_id = 1
