# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.6.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import launchdarkly_api
from launchdarkly_api.api.data_export_destinations_api import DataExportDestinationsApi  # noqa: E501
from launchdarkly_api.rest import ApiException


class TestDataExportDestinationsApi(unittest.TestCase):
    """DataExportDestinationsApi unit test stubs"""

    def setUp(self):
        self.api = launchdarkly_api.api.data_export_destinations_api.DataExportDestinationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_destination(self):
        """Test case for delete_destination

        Get a single data export destination by ID  # noqa: E501
        """
        pass

    def test_get_destination(self):
        """Test case for get_destination

        Get a single data export destination by ID  # noqa: E501
        """
        pass

    def test_get_destinations(self):
        """Test case for get_destinations

        Returns a list of all data export destinations.  # noqa: E501
        """
        pass

    def test_patch_destination(self):
        """Test case for patch_destination

        Perform a partial update to a data export destination.  # noqa: E501
        """
        pass

    def test_post_destination(self):
        """Test case for post_destination

        Create a new data export destination  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
