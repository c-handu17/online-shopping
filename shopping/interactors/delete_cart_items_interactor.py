from shopping.storages.storage_implementation import *
from shopping.presenters.presenter_implementation import *


class RemoveCartItemsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def delete_cart_items_wrapper(self, presenter: PresenterImplementation):
        try:
            deleted_message = self.storage.delete_cart_items()
        except Exception:
            pass
        else:
            return presenter.delete_cart_items_response(deleted=deleted_message)
