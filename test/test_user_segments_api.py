# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.14
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import launchdarkly_api
from launchdarkly_api.api.user_segments_api import UserSegmentsApi  # noqa: E501
from launchdarkly_api.rest import ApiException


class TestUserSegmentsApi(unittest.TestCase):
    """UserSegmentsApi unit test stubs"""

    def setUp(self):
        self.api = launchdarkly_api.api.user_segments_api.UserSegmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_user_segment(self):
        """Test case for delete_user_segment

        Delete a user segment.  # noqa: E501
        """
        pass

    def test_get_user_segment(self):
        """Test case for get_user_segment

        Get a single user segment by key.  # noqa: E501
        """
        pass

    def test_get_user_segments(self):
        """Test case for get_user_segments

        Get a list of all user segments in the given project.  # noqa: E501
        """
        pass

    def test_patch_user_segment(self):
        """Test case for patch_user_segment

        Perform a partial update to a user segment.  # noqa: E501
        """
        pass

    def test_post_user_segment(self):
        """Test case for post_user_segment

        Creates a new user segment.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
