from shopping.interactors.storage_interfaces.storage_interface import StorageInterface
from shopping.presenters.presenter_implementation import PresenterImplementation
from shopping.interactors.dtos import *
from shopping.exceptions.custom_exceptions import *


class AddToCartInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_to_cart_wrapper(self, presenter: PresenterImplementation, add_to_cart_dto: AddToCartDTO):
        try:
            cart_id = self.add_to_cart(add_to_cart_dto=add_to_cart_dto)
            return presenter.get_add_to_cart_response(cart_id)
        except ProductNotExists:
            return presenter.raise_product_not_exist()

    def add_to_cart(self, add_to_cart_dto: AddToCartDTO):
        product_id = add_to_cart_dto.product_id
        self.storage.validate_product_id(product_id=product_id)
        cart_id = self.storage.add_to_cart(add_to_cart_dto=add_to_cart_dto)
        return cart_id
