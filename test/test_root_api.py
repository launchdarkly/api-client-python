# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 4.0.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import launchdarkly_api
from launchdarkly_api.api.root_api import RootApi  # noqa: E501
from launchdarkly_api.rest import ApiException


class TestRootApi(unittest.TestCase):
    """RootApi unit test stubs"""

    def setUp(self):
        self.api = launchdarkly_api.api.root_api.RootApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_root(self):
        """Test case for get_root

        """
        pass


if __name__ == '__main__':
    unittest.main()
