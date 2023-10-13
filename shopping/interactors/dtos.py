from dataclasses import dataclass
from typing import List


@dataclass
class ProductDTO:
    product_id: int
    name: str
    price: int
    description: str


@dataclass
class ProductResponseDTO:
    products: List[ProductDTO]
    products_count: int


@dataclass
class ProductsWithQueryParamsDTO:
    category: str = "Electronics"
    brand: str = "Philips"
    sort_by: str = "Price"
    sort_value: str = "ASC"


@dataclass
class AddToCartDTO:
    user_id: str = 1
    product_id: int = 1


@dataclass
class UserDTO:
    name: str
    userName: str
    age: int


@dataclass
class AddToCartResponseDTO:
    cart_id: int
