import json
from shopping.presenters.presenter_implementation import *
import pytest
from shopping.tests.factories.presenter_dtos import *


class TestPresenter:
    @pytest.fixture
    def presenter(self):
        presenter = PresenterImplementation()
        return presenter

    def test_raise_product_not_exist(self, presenter, snapshot):
        # Act
        actual_response = presenter.raise_product_not_exist()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Product not exists")

    def test_get_add_to_cart_response(self, presenter, snapshot):
        # Act
        actual_response = presenter.get_add_to_cart_response(1)

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Items added in cart succesfully")

    def test_get_delete_cart_items_response(self, presenter, snapshot):
        # Arrange
        actual_response = presenter.delete_cart_items_response(deleted="deleted Successfully")

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Deleted")

    def test_get_all_products_response(self, presenter, snapshot):
        product_1 = ProductResponseDTOFactory()
        product_2 = ProductResponseDTOFactory()
        products = [product_1, product_2]
        products_response_dto = ProductResponseDTOFactory_list(
            products=products, products_count=2
        )
        actual_response = presenter.get_all_products_response(products_response_dto=products_response_dto)
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data)