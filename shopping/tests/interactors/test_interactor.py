import pytest
from unittest.mock import create_autospec
from shopping.interactors.delete_cart_items_interactor import *
from shopping.interactors.get_cart_interactor import *
from shopping.tests.factories.presenter_dtos import *
from shopping.tests.factories.storage_dtos import *
from django.http import HttpResponse
import json
from shopping.interactors.add_to_cart_interactor import *
from shopping.interactors.get_all_products_interactor import *
from dataclasses import asdict


class TestGetProducts:
    @pytest.fixture
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def presenter(self):
        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture
    def delete_cart_items_interactor(self, storage):
        interactor = RemoveCartItemsInteractor(storage=storage)
        return interactor

    def test_delete_cart_items(self, delete_cart_items_interactor, storage, presenter, snapshot):
        # Arrange
        storage.delete_cart_items.return_value = "Deleted Successfully"
        presenter.delete_cart_items_response.return_value = HttpResponse(json.dumps({
            "message": "Deleted Successfully"
        }))
        # Act
        response = delete_cart_items_interactor.delete_cart_items_wrapper(presenter=presenter)
        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, {"message": "Deleted Successfully"})
        presenter.delete_cart_items_response.assert_called_once_with(deleted="Deleted Successfully")

    @pytest.fixture
    def get_cart_interactor(self, storage):
        interactor = GetUserCartInteractor(storage=storage)
        return interactor

    def test_get_cart_with_items(self, get_cart_interactor, storage, presenter, snapshot):
        products_response_dto = ProductResponseDTOFactory_list()
        storage.get_user_cart_items.return_value = products_response_dto
        products_count = 0
        products_list = []
        for each_item in products_response_dto.products:
            products_count += 1
            product_id = each_item.product_id
            product_dto = ProductDTO(
                product_id=product_id,
                name=each_item.name,
                price=each_item.price,
                description=each_item.description,
            )
            products_list.append(product_dto)
        products_dict = {
            "product_objects": products_list,
            "products_total_count": products_count
        }
        presenter.get_all_products_response.return_value = HttpResponse(
            json.dumps(products_dict, cls=ProductDTOEncoder))

        # Act
        response = get_cart_interactor.get_user_cart_wrapper(presenter=presenter)

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data)

    @pytest.fixture
    def add_to_cart_interactor(self, storage):
        interactor = AddToCartInteractor(storage=storage)
        return interactor

    def test_add_to_cart_with_product_not_exist(self, storage, presenter, add_to_cart_interactor, snapshot):
        # Arrange
        storage.validate_product_id.side_effect = ProductNotExists
        presenter.raise_product_not_exist.return_value = HttpResponse(json.dumps({
            "response": PRODUCT_NOT_EXISTS[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": PRODUCT_NOT_EXISTS[1]
        }))
        # Act

        response = add_to_cart_interactor.add_to_cart_wrapper(presenter=presenter, add_to_cart_dto=AddToCartDTO())

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Product Not Exists")
        presenter.raise_product_not_exist.assert_called_once_with()

    def test_add_to_cart_with_product(self, storage, presenter, add_to_cart_interactor, snapshot):
        # Arrange
        product_request_dto = AddToCartDTOFactory()
        product_response_dto = AddToCartResponseDTOFactory()
        storage.add_to_cart.return_value = product_response_dto
        presenter.get_add_to_cart_response.return_value = HttpResponse(json.dumps(asdict(product_response_dto)))

        # Act
        response = add_to_cart_interactor.add_to_cart_wrapper(presenter=presenter, add_to_cart_dto=product_request_dto)

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data)

    @pytest.fixture
    def get_all_products_interactor(self, storage):
        storage = GetProductsInteractor(storage=storage)
        return storage

    def test_get_all_products_with_valid_query_params(self, get_all_products_interactor, storage, presenter, snapshot):
        # Arrange
        products_response_dto = ProductResponseDTOFactory_list()
        storage.get_all_products.return_value = products_response_dto
        products_list = []
        products_count = 0
        for each_product in products_response_dto.products:
            products_count += 1
            product = ProductDTO(
                product_id=each_product.product_id,
                name=each_product.name,
                price=each_product.price,
                description=each_product.description,
            )
            products_list.append(product)
        product_details = {
            "product_details": products_list,
            "products_count": products_count
        }
        query_params_dto = ProductsWithQueryParamsDTO()
        presenter.get_all_products_response.return_value = HttpResponse(json.dumps(product_details, cls=ProductDTOEncoder))

        # Act
        response = get_all_products_interactor.get_product_details_wrapper(presenter=presenter, query_params_dto=query_params_dto, is_query_params_flag=True)

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data)

    def test_get_all_products(self, get_all_products_interactor, storage, presenter, snapshot):
        # Arrange
        products_response_dto = ProductResponseDTOFactory_list()
        storage.get_all_products.return_value = products_response_dto
        products_list = []
        products_count = 0
        for each_product in products_response_dto.products:
            products_count += 1
            product_dto = ProductDTO(
                product_id=each_product.product_id,
                name=each_product.name,
                price=each_product.price,
                description=each_product.description,
            )
            products_list.append(product_dto)
        products_details = {
            "product_details": products_list,
            "products_count": products_count
        }
        query_params_dto = ProductsWithQueryParamsDTO()
        presenter.get_all_products_response.return_value = HttpResponse(json.dumps(products_details, cls=ProductDTOEncoder))

        # Act
        response = get_all_products_interactor.get_product_details_wrapper(presenter=presenter, query_params_dto=query_params_dto, is_query_params_flag=False)

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data)
