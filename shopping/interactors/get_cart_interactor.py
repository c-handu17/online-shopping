from shopping.storages.storage_implementation import *
from shopping.presenters.presenter_implementation import *


class GetUserCartInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_user_cart_wrapper(self, presenter: PresenterImplementation):
        try:
            products = self.get_user_cart()
        except Exception:
            pass
        else:
            return presenter.get_all_products_response(products)

    def get_user_cart(self):
        self.storage.validate_cart_items()
        products = self.storage.get_user_cart_items()
        return products
