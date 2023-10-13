# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetProductsAPITestCase.test_case body'] = {
    'products': [
        {
            'description': 'Philips Light',
            'id': 1,
            'name': 'User 0',
            'price': 500.0
        }
    ],
    'total_count': 1
}

snapshots['TestCase01GetProductsAPITestCase.test_case status_code'] = '200'
