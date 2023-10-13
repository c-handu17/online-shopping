import pytest
from shopping.storages.storage_implementation import *
from shopping.tests.factories.models import *
from shopping.tests.factories.storage_dtos import *
from shopping.models import *


class TestStorageImplementation:
    @pytest.fixture
    def storage(self):
        storage = StorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_validate_product_id(self, storage):
        product_id = 1
        with pytest.raises(ProductNotExists):
            storage.validate_product_id(product_id=product_id)

    @pytest.mark.django_db
    def test_add_to_cart(self, storage):
        # Arrange
        user = UserFactory()
        product = ProductFactory()
        add_to_cart_dto = AddToCartDTOFactory(user_id=str(user.id), product_id=product.id)

        # Act
        cart_id = storage.add_to_cart(add_to_cart_dto=add_to_cart_dto)

        # Assert
        cart = Cart.objects.get(id=cart_id)
        assert cart.user_id == add_to_cart_dto.user_id
        assert cart.product_id.id == add_to_cart_dto.product_id

    @pytest.mark.django_db
    def test_delete_cart_items(self, storage):
        storage.delete_cart_items()
        assert Cart.objects.all().count() == 0

    @pytest.mark.django_db
    def test_get_all_products(self, storage):
        # Arrange
        product = ProductFactory()

        # Act
        response = storage.get_all_products()

        # Assert
        response_product_ids = [product.product_id for product in response.products]
        assert response_product_ids == [product.id]

    @pytest.mark.django_db
    def test_get_all_products_using_query_params(self, storage):
        # Arrange
        product = ProductFactory()
        query_params_dto = GetAllProductsUsingQueryParamsDTOFactory

        # Act
        response = storage.get_all_products_using_query_params(query_params_dto=query_params_dto)

        # Assert
        response_product_ids = [product.product_id for product in response.products]
        assert response_product_ids == [product.id]