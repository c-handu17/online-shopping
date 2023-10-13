from shopping.interactors.storage_interfaces.storage_interface import StorageInterface
from shopping.models import Product, User, Cart
from shopping.interactors.dtos import *
from shopping.exceptions.custom_exceptions import *


class StorageImplementation(StorageInterface):
    def get_all_products(self):
        products = list(Product.objects.all())
        products_count = Product.objects.all().count()
        products_list = []
        for each_product in products:
            product_dto = ProductDTO(
                product_id=each_product.id,
                name=each_product.name,
                price=each_product.price,
                description=each_product.description,
            )
            products_list.append(product_dto)
        products_response_dto = ProductResponseDTO(products=products_list,
                                                   products_count=products_count)
        return products_response_dto

    def get_all_products_using_query_params(self, query_params_dto: ProductsWithQueryParamsDTO):
        category = query_params_dto.category
        brand = query_params_dto.brand
        sort_by = query_params_dto.sort_by
        sort_value = query_params_dto.sort_value
        products = Product.objects.all()

        if category:
            products = products.filter(category=category)
        if brand:
            products = products.filter(brand=brand)
        if sort_by and sort_value:
            if sort_value == 'ASC':
                products = products.order_by(sort_by.lower())
            elif sort_value == 'DESC':
                products = products.order_by(f'-{sort_by.lower()}')

        products_list = []
        for each_product in products:
            product_dto = ProductDTO(
                product_id=each_product.id,
                name=each_product.name,
                price=each_product.price,
                description=each_product.description,
            )
            products_list.append(product_dto)

        products_count = products.count()
        products_response_dto = ProductResponseDTO(products=products_list,
                                                   products_count=products_count)

        return products_response_dto

    def validate_product_id(self, product_id: int):
        is_exists_flag = Product.objects.filter(id=product_id).exists()
        if not is_exists_flag:
            raise ProductNotExists

    def add_to_cart(self, add_to_cart_dto: AddToCartDTO):
        product_id = add_to_cart_dto.product_id
        user_id = add_to_cart_dto.user_id
        product = Product.objects.get(id=product_id)
        add_item_to_cart = Cart.objects.create(user_id=user_id, product_id=product)
        return add_item_to_cart.id

    def delete_cart_items(self):
        cart = Cart.objects.all()
        cart.delete()
        return "Deleted Successfully"

    def get_user_cart_items(self):
        cart = Cart.objects.select_related('product_id').all()
        products_count = 0
        products_list = []
        for each_product in cart:
            products_count += 1
            product = each_product.product_id
            product_dto = ProductDTO(
                product_id=product.id,
                name=product.name,
                price=product.price,
                description=product.description,
            )
            products_list.append(product_dto)
        products_response_dto = ProductResponseDTO(products=products_list,
                                                   products_count=products_count)
        return products_response_dto
