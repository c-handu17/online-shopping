# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AddToCartAPITestCase.test_case body'] = {
    'http_status_code': 404,
    'res_status': 'PRODUCT_NOT_EXISTS',
    'response': 'Product Not Exists'
}

snapshots['TestCase01AddToCartAPITestCase.test_case status_code'] = '404'
