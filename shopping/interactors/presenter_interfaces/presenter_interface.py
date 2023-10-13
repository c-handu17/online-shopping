from abc import abstractmethod
from shopping.interactors.dtos import *


class PresenterInterface:
    @abstractmethod
    def get_all_products_response(self, all_products_response_dto: ProductResponseDTO):
        pass

    @abstractmethod
    def get_add_to_cart_response(self, cart_id: int):
        pass

    @abstractmethod
    def delete_cart_items_response(self, deleted: str):
        pass

    @abstractmethod
    def raise_no_cart_items(self):
        pass

    @abstractmethod
    def raise_product_not_exist(self):
        pass