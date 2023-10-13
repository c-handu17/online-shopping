# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetProducts.test_add_to_cart_with_product 1'] = {
    'cart_id': 1
}

snapshots['TestGetProducts.test_add_to_cart_with_product_not_exist Product Not Exists'] = {
    'http_status_code': 404,
    'res_status': 'PRODUCT_NOT_EXISTS',
    'response': 'Product Not Exists'
}

snapshots['TestGetProducts.test_delete_cart_items'] = {
    'message': 'Deleted Successfully'
}

snapshots['TestGetProducts.test_get_all_products 1'] = {
    'product_details': [
        {
            'description': 'Philips',
            'name': 'Light',
            'price': 500,
            'product_id': 0
        },
        {
            'description': 'Philips',
            'name': 'Light',
            'price': 500,
            'product_id': 1
        },
        {
            'description': 'Philips',
            'name': 'Light',
            'price': 500,
            'product_id': 2
        },
        {
            'description': 'Philips',
            'name': 'Light',
            'price': 500,
            'product_id': 3
        }
    ],
    'products_count': 4
}

snapshots['TestGetProducts.test_get_all_products_with_valid_query_params 1'] = {
    'product_details': [
        {
            'description': 'Philips',
            'name': 'Light',
            'price': 500,
            'product_id': 0
        },
        {
            'description': 'Philips',
            'name': 'Light',
            'price': 500,
            'product_id': 1
        },
        {
            'description': 'Philips',
            'name': 'Light',
            'price': 500,
            'product_id': 2
        },
        {
            'description': 'Philips',
            'name': 'Light',
            'price': 500,
            'product_id': 3
        }
    ],
    'products_count': 4
}

snapshots['TestGetProducts.test_get_cart_with_items 1'] = {
    'product_objects': [
        {
            'description': 'Philips',
            'name': 'Light',
            'price': 500,
            'product_id': 0
        },
        {
            'description': 'Philips',
            'name': 'Light',
            'price': 500,
            'product_id': 1
        },
        {
            'description': 'Philips',
            'name': 'Light',
            'price': 500,
            'product_id': 2
        },
        {
            'description': 'Philips',
            'name': 'Light',
            'price': 500,
            'product_id': 3
        }
    ],
    'products_total_count': 4
}

snapshots['TestGetProducts.test_get_cart_with_out_cart_items No Cart Items'] = {
    'http_status_code': 400,
    'res_status': 'NO_ITEMS_IN_CART',
    'response': 'No Items In Cart'
}
