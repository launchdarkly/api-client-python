# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 5.3.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import launchdarkly_api
from launchdarkly_api.api.audit_log_api import AuditLogApi  # noqa: E501
from launchdarkly_api.rest import ApiException


class TestAuditLogApi(unittest.TestCase):
    """AuditLogApi unit test stubs"""

    def setUp(self):
        self.api = launchdarkly_api.api.audit_log_api.AuditLogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_audit_log_entries(self):
        """Test case for get_audit_log_entries

        Get a list of all audit log entries. The query parameters allow you to restrict the returned results by date ranges, resource specifiers, or a full-text search query.  # noqa: E501
        """
        pass

    def test_get_audit_log_entry(self):
        """Test case for get_audit_log_entry

        Use this endpoint to fetch a single audit log entry by its resouce ID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
