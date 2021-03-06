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
from launchdarkly_api.api.projects_api import ProjectsApi  # noqa: E501
from launchdarkly_api.rest import ApiException


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = launchdarkly_api.api.projects_api.ProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_project(self):
        """Test case for delete_project

        Delete a project by key. Caution-- deleting a project will delete all associated environments and feature flags. You cannot delete the last project in an account.  # noqa: E501
        """
        pass

    def test_get_project(self):
        """Test case for get_project

        Fetch a single project by key.  # noqa: E501
        """
        pass

    def test_get_projects(self):
        """Test case for get_projects

        Returns a list of all projects in the account.  # noqa: E501
        """
        pass

    def test_patch_project(self):
        """Test case for patch_project

        Modify a project by ID.  # noqa: E501
        """
        pass

    def test_post_project(self):
        """Test case for post_project

        Create a new project with the given key and name.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
