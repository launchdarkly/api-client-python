# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 3.9.1
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from launchdarkly_api.api_client import ApiClient


class UsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_user(self, project_key, environment_key, user_key, **kwargs):  # noqa: E501
        """Delete a user by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user(project_key, environment_key, user_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_key: The user's key. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_user_with_http_info(project_key, environment_key, user_key, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_user_with_http_info(project_key, environment_key, user_key, **kwargs)  # noqa: E501
            return data

    def delete_user_with_http_info(self, project_key, environment_key, user_key, **kwargs):  # noqa: E501
        """Delete a user by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_with_http_info(project_key, environment_key, user_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_key: The user's key. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'user_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `delete_user`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `delete_user`")  # noqa: E501
        # verify the required parameter 'user_key' is set
        if ('user_key' not in params or
                params['user_key'] is None):
            raise ValueError("Missing the required parameter `user_key` when calling `delete_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']  # noqa: E501
        if 'user_key' in params:
            path_params['userKey'] = params['user_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/users/{projectKey}/{environmentKey}/{userKey}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_search_users(self, project_key, environment_key, **kwargs):  # noqa: E501
        """Search users in LaunchDarkly based on their last active date, or a search query. It should not be used to enumerate all users in LaunchDarkly-- use the List users API resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_search_users(project_key, environment_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str q: Search query.
        :param int limit: Pagination limit.
        :param int offset: Specifies the first item to return in the collection.
        :param int after: A timestamp filter, expressed as a Unix epoch time in milliseconds. All entries returned will have occurred after this timestamp.
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_search_users_with_http_info(project_key, environment_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_search_users_with_http_info(project_key, environment_key, **kwargs)  # noqa: E501
            return data

    def get_search_users_with_http_info(self, project_key, environment_key, **kwargs):  # noqa: E501
        """Search users in LaunchDarkly based on their last active date, or a search query. It should not be used to enumerate all users in LaunchDarkly-- use the List users API resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_search_users_with_http_info(project_key, environment_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str q: Search query.
        :param int limit: Pagination limit.
        :param int offset: Specifies the first item to return in the collection.
        :param int after: A timestamp filter, expressed as a Unix epoch time in milliseconds. All entries returned will have occurred after this timestamp.
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'q', 'limit', 'offset', 'after']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_search_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_search_users`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `get_search_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']  # noqa: E501

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/user-search/{projectKey}/{environmentKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Users',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user(self, project_key, environment_key, user_key, **kwargs):  # noqa: E501
        """Get a user by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user(project_key, environment_key, user_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_key: The user's key. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_with_http_info(project_key, environment_key, user_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_with_http_info(project_key, environment_key, user_key, **kwargs)  # noqa: E501
            return data

    def get_user_with_http_info(self, project_key, environment_key, user_key, **kwargs):  # noqa: E501
        """Get a user by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_with_http_info(project_key, environment_key, user_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_key: The user's key. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'user_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_user`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `get_user`")  # noqa: E501
        # verify the required parameter 'user_key' is set
        if ('user_key' not in params or
                params['user_key'] is None):
            raise ValueError("Missing the required parameter `user_key` when calling `get_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']  # noqa: E501
        if 'user_key' in params:
            path_params['userKey'] = params['user_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/users/{projectKey}/{environmentKey}/{userKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_users(self, project_key, environment_key, **kwargs):  # noqa: E501
        """List all users in the environment. Includes the total count of users. In each page, there will be up to 'limit' users returned (default 20). This is useful for exporting all users in the system for further analysis. Paginated collections will include a next link containing a URL with the next set of elements in the collection.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users(project_key, environment_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param int limit: Pagination limit.
        :param str h: This parameter is required when following \"next\" links.
        :param str scroll_id: This parameter is required when following \"next\" links.
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_users_with_http_info(project_key, environment_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_users_with_http_info(project_key, environment_key, **kwargs)  # noqa: E501
            return data

    def get_users_with_http_info(self, project_key, environment_key, **kwargs):  # noqa: E501
        """List all users in the environment. Includes the total count of users. In each page, there will be up to 'limit' users returned (default 20). This is useful for exporting all users in the system for further analysis. Paginated collections will include a next link containing a URL with the next set of elements in the collection.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users_with_http_info(project_key, environment_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param int limit: Pagination limit.
        :param str h: This parameter is required when following \"next\" links.
        :param str scroll_id: This parameter is required when following \"next\" links.
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'limit', 'h', 'scroll_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_users`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `get_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'h' in params:
            query_params.append(('h', params['h']))  # noqa: E501
        if 'scroll_id' in params:
            query_params.append(('scrollId', params['scroll_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/users/{projectKey}/{environmentKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Users',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
