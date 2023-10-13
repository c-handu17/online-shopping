# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestPresenter.test_get_add_to_cart_response Items added in cart succesfully'] = {
    'cart_id': 1
}

snapshots['TestPresenter.test_get_all_products_response 1'] = {
    'products': [
        {
            'description': 'Philips',
            'id': 0,
            'name': 'Light',
            'price': 500
        },
        {
            'description': 'Philips',
            'id': 1,
            'name': 'Light',
            'price': 500
        }
    ],
    'total_count': 2
}

snapshots['TestPresenter.test_get_delete_cart_items_response Deleted'] = {
    'message': 'deleted Successfully'
}

snapshots['TestPresenter.test_raise_product_not_exist Product not exists'] = {
    'http_status_code': 404,
    'res_status': 'PRODUCT_NOT_EXISTS',
    'response': 'Product Not Exists'
}
