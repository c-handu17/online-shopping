from shopping.interactors.storage_interfaces.storage_interface import StorageInterface
from shopping.models import Product
from shopping.presenters.presenter_implementation import PresenterImplementation
from shopping.interactors.dtos import *


class GetProductsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_product_details_wrapper(self, presenter: PresenterImplementation, query_params_dto: ProductsWithQueryParamsDTO, is_query_params_flag):
        if not is_query_params_flag:
            products = self.storage.get_all_products()
            return presenter.get_all_products_response(products)
        else:
            products = self.storage.get_all_products_using_query_params(query_params_dto=query_params_dto)
            return presenter.get_all_products_response(products)
