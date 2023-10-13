from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from shopping.interactors.dtos import *
from shopping.storages.storage_implementation import StorageImplementation
from shopping.presenters.presenter_implementation import PresenterImplementation
from shopping.interactors.add_to_cart_interactor import AddToCartInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_body = kwargs['request_data']
    user_id = kwargs['user']
    add_to_cart_dto = AddToCartDTO(
        user_id=user_id,
        product_id=request_body['product_id']
    )
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = AddToCartInteractor(storage=storage)
    return interactor.add_to_cart_wrapper(presenter=presenter, add_to_cart_dto=add_to_cart_dto)

