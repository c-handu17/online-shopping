from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from shopping.views.getProducts.validator_class import ValidatorClass
from shopping.storages.storage_implementation import StorageImplementation
from shopping.presenters.presenter_implementation import PresenterImplementation
from shopping.interactors.get_all_products_interactor import GetProductsInteractor
from shopping.interactors.dtos import *


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    query_params = kwargs['query_params']
    category = query_params.get('category', None)
    brand = query_params.get('brand', None)
    sort_by = query_params.get('sort_by', None)
    sort_value = query_params.get('sort_value', None)

    query_params_dto = ProductsWithQueryParamsDTO(
        category=category,
        brand=brand,
        sort_by=sort_by,
        sort_value=sort_value
    )
    is_query_params_flag = False
    if category or brand or sort_by:
        is_query_params_flag = True

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetProductsInteractor(storage=storage)
    return interactor.get_product_details_wrapper(presenter=presenter, query_params_dto=query_params_dto, is_query_params_flag=is_query_params_flag)
