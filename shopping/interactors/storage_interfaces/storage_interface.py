from abc import abstractmethod
from shopping.interactors.dtos import *


class StorageInterface:
    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def get_all_products_using_query_params(self, query_params_dto: ProductsWithQueryParamsDTO):
        pass

    @abstractmethod
    def validate_product_id(self, product_id: int):
        pass

    @abstractmethod
    def add_to_cart(self, add_to_cart_dto: AddToCartDTO):
        pass

    @abstractmethod
    def delete_cart_items(self):
        pass

    @abstractmethod
    def validate_cart_items(self):
        pass

    @abstractmethod
    def get_user_cart_items(self):
        pass