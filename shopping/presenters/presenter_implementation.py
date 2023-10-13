from shopping.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from shopping.interactors.dtos import *
from shopping.constants.exception_messages import *
from shopping.constants.enums import StatusCode


class PresenterImplementation(PresenterInterface, HTTPResponseMixin):
    def get_all_products_response(self, products_response_dto: ProductResponseDTO):
        products_list = []
        for product in products_response_dto.products:
            product_dict = {
                "id": product.product_id,
                "name": product.name,
                "price": product.price,
                "description": product.description,
            }
            products_list.append(product_dict)
        products_dict = {
            "products": products_list,
            "total_count": products_response_dto.products_count
        }
        return self.prepare_200_success_response(response_dict=products_dict)

    def raise_product_not_exist(self, *args, **kwargs):
        response_dict = {
            "response": PRODUCT_NOT_EXISTS[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": PRODUCT_NOT_EXISTS[1],
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def get_add_to_cart_response(self, cart_id: int):
        cart_id_dict = {'cart_id': cart_id}
        return self.prepare_200_success_response(response_dict=cart_id_dict)

    def delete_cart_items_response(self, deleted: str):
        delete_message_dict = {"message": deleted}
        return self.prepare_200_success_response(response_dict=delete_message_dict)
