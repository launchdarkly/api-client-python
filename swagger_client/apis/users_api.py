# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API

    OpenAPI spec version: 2.0.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class UsersApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete_user(self, project_key, environment_key, user_key, **kwargs):
        """
        Delete a user by ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_user(project_key, environment_key, user_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key (required)
        :param str user_key: The user's key (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_user_with_http_info(project_key, environment_key, user_key, **kwargs)
        else:
            (data) = self.delete_user_with_http_info(project_key, environment_key, user_key, **kwargs)
            return data

    def delete_user_with_http_info(self, project_key, environment_key, user_key, **kwargs):
        """
        Delete a user by ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_user_with_http_info(project_key, environment_key, user_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key (required)
        :param str user_key: The user's key (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'user_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params) or (params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `delete_user`")
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params) or (params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `delete_user`")
        # verify the required parameter 'user_key' is set
        if ('user_key' not in params) or (params['user_key'] is None):
            raise ValueError("Missing the required parameter `user_key` when calling `delete_user`")


        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']
        if 'user_key' in params:
            path_params['userKey'] = params['user_key']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['Token']

        return self.api_client.call_api('/users/{projectKey}/{environmentKey}/{userKey}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_search_users(self, project_key, environment_key, **kwargs):
        """
        Search users in LaunchDarkly based on their last active date, or a search query.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_search_users(project_key, environment_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key (required)
        :param str q: Search query
        :param float limit: Pagination limit
        :param float offset: Specifies the first item to return in the collection
        :param float after: A unix epoch time in milliseconds specifying the maximum last time a user requested a feature flag
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_search_users_with_http_info(project_key, environment_key, **kwargs)
        else:
            (data) = self.get_search_users_with_http_info(project_key, environment_key, **kwargs)
            return data

    def get_search_users_with_http_info(self, project_key, environment_key, **kwargs):
        """
        Search users in LaunchDarkly based on their last active date, or a search query.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_search_users_with_http_info(project_key, environment_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key (required)
        :param str q: Search query
        :param float limit: Pagination limit
        :param float offset: Specifies the first item to return in the collection
        :param float after: A unix epoch time in milliseconds specifying the maximum last time a user requested a feature flag
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'q', 'limit', 'offset', 'after']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_search_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params) or (params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_search_users`")
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params) or (params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `get_search_users`")


        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'after' in params:
            query_params.append(('after', params['after']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['Token']

        return self.api_client.call_api('/user-search/{projectKey}/{environmentKey}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Users',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_user(self, project_key, environment_key, user_key, **kwargs):
        """
        Get a user by key.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user(project_key, environment_key, user_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key (required)
        :param str user_key: The user's key (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_user_with_http_info(project_key, environment_key, user_key, **kwargs)
        else:
            (data) = self.get_user_with_http_info(project_key, environment_key, user_key, **kwargs)
            return data

    def get_user_with_http_info(self, project_key, environment_key, user_key, **kwargs):
        """
        Get a user by key.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_with_http_info(project_key, environment_key, user_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key (required)
        :param str user_key: The user's key (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'user_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params) or (params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_user`")
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params) or (params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `get_user`")
        # verify the required parameter 'user_key' is set
        if ('user_key' not in params) or (params['user_key'] is None):
            raise ValueError("Missing the required parameter `user_key` when calling `get_user`")


        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']
        if 'user_key' in params:
            path_params['userKey'] = params['user_key']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['Token']

        return self.api_client.call_api('/users/{projectKey}/{environmentKey}/{userKey}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='User',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_users(self, project_key, environment_key, **kwargs):
        """
        List all users in the environment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_users(project_key, environment_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key (required)
        :param float limit: Pagination limit
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_users_with_http_info(project_key, environment_key, **kwargs)
        else:
            (data) = self.get_users_with_http_info(project_key, environment_key, **kwargs)
            return data

    def get_users_with_http_info(self, project_key, environment_key, **kwargs):
        """
        List all users in the environment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_users_with_http_info(project_key, environment_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key (required)
        :param float limit: Pagination limit
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'limit']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params) or (params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_users`")
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params) or (params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `get_users`")


        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['Token']

        return self.api_client.call_api('/users/{projectKey}/{environmentKey}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Users',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
