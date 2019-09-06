# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.18
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from launchdarkly_api.api_client import ApiClient


class CustomRolesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_custom_role(self, custom_role_key, **kwargs):  # noqa: E501
        """Delete a custom role by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_custom_role(custom_role_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str custom_role_key: The custom role key. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_custom_role_with_http_info(custom_role_key, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_custom_role_with_http_info(custom_role_key, **kwargs)  # noqa: E501
            return data

    def delete_custom_role_with_http_info(self, custom_role_key, **kwargs):  # noqa: E501
        """Delete a custom role by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_custom_role_with_http_info(custom_role_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str custom_role_key: The custom role key. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['custom_role_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_custom_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'custom_role_key' is set
        if ('custom_role_key' not in params or
                params['custom_role_key'] is None):
            raise ValueError("Missing the required parameter `custom_role_key` when calling `delete_custom_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'custom_role_key' in params:
            path_params['customRoleKey'] = params['custom_role_key']  # noqa: E501

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
            '/roles/{customRoleKey}', 'DELETE',
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

    def get_custom_role(self, custom_role_key, **kwargs):  # noqa: E501
        """Get one custom role by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_role(custom_role_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str custom_role_key: The custom role key. (required)
        :return: CustomRole
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_custom_role_with_http_info(custom_role_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_custom_role_with_http_info(custom_role_key, **kwargs)  # noqa: E501
            return data

    def get_custom_role_with_http_info(self, custom_role_key, **kwargs):  # noqa: E501
        """Get one custom role by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_role_with_http_info(custom_role_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str custom_role_key: The custom role key. (required)
        :return: CustomRole
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['custom_role_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_custom_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'custom_role_key' is set
        if ('custom_role_key' not in params or
                params['custom_role_key'] is None):
            raise ValueError("Missing the required parameter `custom_role_key` when calling `get_custom_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'custom_role_key' in params:
            path_params['customRoleKey'] = params['custom_role_key']  # noqa: E501

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
            '/roles/{customRoleKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomRole',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_custom_roles(self, **kwargs):  # noqa: E501
        """Return a complete list of custom roles.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_roles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CustomRoles
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_custom_roles_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_custom_roles_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_custom_roles_with_http_info(self, **kwargs):  # noqa: E501
        """Return a complete list of custom roles.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_roles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CustomRoles
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_custom_roles" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/roles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomRoles',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_custom_role(self, custom_role_key, patch_delta, **kwargs):  # noqa: E501
        """Modify a custom role by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_custom_role(custom_role_key, patch_delta, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str custom_role_key: The custom role key. (required)
        :param list[PatchOperation] patch_delta: Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/' (required)
        :return: CustomRole
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_custom_role_with_http_info(custom_role_key, patch_delta, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_custom_role_with_http_info(custom_role_key, patch_delta, **kwargs)  # noqa: E501
            return data

    def patch_custom_role_with_http_info(self, custom_role_key, patch_delta, **kwargs):  # noqa: E501
        """Modify a custom role by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_custom_role_with_http_info(custom_role_key, patch_delta, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str custom_role_key: The custom role key. (required)
        :param list[PatchOperation] patch_delta: Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/' (required)
        :return: CustomRole
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['custom_role_key', 'patch_delta']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_custom_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'custom_role_key' is set
        if ('custom_role_key' not in params or
                params['custom_role_key'] is None):
            raise ValueError("Missing the required parameter `custom_role_key` when calling `patch_custom_role`")  # noqa: E501
        # verify the required parameter 'patch_delta' is set
        if ('patch_delta' not in params or
                params['patch_delta'] is None):
            raise ValueError("Missing the required parameter `patch_delta` when calling `patch_custom_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'custom_role_key' in params:
            path_params['customRoleKey'] = params['custom_role_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'patch_delta' in params:
            body_params = params['patch_delta']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/roles/{customRoleKey}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomRole',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_custom_role(self, custom_role_body, **kwargs):  # noqa: E501
        """Create a new custom role.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_custom_role(custom_role_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomRoleBody custom_role_body: New role or roles to create. (required)
        :return: CustomRole
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_custom_role_with_http_info(custom_role_body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_custom_role_with_http_info(custom_role_body, **kwargs)  # noqa: E501
            return data

    def post_custom_role_with_http_info(self, custom_role_body, **kwargs):  # noqa: E501
        """Create a new custom role.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_custom_role_with_http_info(custom_role_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomRoleBody custom_role_body: New role or roles to create. (required)
        :return: CustomRole
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['custom_role_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_custom_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'custom_role_body' is set
        if ('custom_role_body' not in params or
                params['custom_role_body'] is None):
            raise ValueError("Missing the required parameter `custom_role_body` when calling `post_custom_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'custom_role_body' in params:
            body_params = params['custom_role_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/roles', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomRole',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
