from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from shopping.storages.storage_implementation import *
from shopping.presenters.presenter_implementation import *
from shopping.interactors.delete_cart_items_interactor import *


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = RemoveCartItemsInteractor(storage=storage)
    return interactor.delete_cart_items_wrapper(presenter=presenter)
