# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.9.1
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import launchdarkly_api
from launchdarkly_api.api.relay_proxy_configurations_api import RelayProxyConfigurationsApi  # noqa: E501
from launchdarkly_api.rest import ApiException


class TestRelayProxyConfigurationsApi(unittest.TestCase):
    """RelayProxyConfigurationsApi unit test stubs"""

    def setUp(self):
        self.api = launchdarkly_api.api.relay_proxy_configurations_api.RelayProxyConfigurationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_relay_proxy_config(self):
        """Test case for delete_relay_proxy_config

        Delete a relay proxy configuration by ID.  # noqa: E501
        """
        pass

    def test_get_relay_proxy_config(self):
        """Test case for get_relay_proxy_config

        Get a single relay proxy configuration by ID.  # noqa: E501
        """
        pass

    def test_get_relay_proxy_configs(self):
        """Test case for get_relay_proxy_configs

        Returns a list of relay proxy configurations in the account.  # noqa: E501
        """
        pass

    def test_patch_relay_proxy_config(self):
        """Test case for patch_relay_proxy_config

        Modify a relay proxy configuration by ID.  # noqa: E501
        """
        pass

    def test_post_relay_auto_config(self):
        """Test case for post_relay_auto_config

        Create a new relay proxy config.  # noqa: E501
        """
        pass

    def test_reset_relay_proxy_config(self):
        """Test case for reset_relay_proxy_config

        Reset a relay proxy configuration's secret key with an optional expiry time for the old key.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()