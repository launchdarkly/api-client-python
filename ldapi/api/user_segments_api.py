# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.2
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ldapi.api_client import ApiClient


class UserSegmentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_user_segment(self, project_key, environment_key, user_segment_key, **kwargs):  # noqa: E501
        """Delete a user segment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_user_segment(project_key, environment_key, user_segment_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_segment_key: The user segment's key. The key identifies the user segment in your code. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_user_segment_with_http_info(project_key, environment_key, user_segment_key, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_user_segment_with_http_info(project_key, environment_key, user_segment_key, **kwargs)  # noqa: E501
            return data

    def delete_user_segment_with_http_info(self, project_key, environment_key, user_segment_key, **kwargs):  # noqa: E501
        """Delete a user segment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_user_segment_with_http_info(project_key, environment_key, user_segment_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_segment_key: The user segment's key. The key identifies the user segment in your code. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'user_segment_key']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_segment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `delete_user_segment`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `delete_user_segment`")  # noqa: E501
        # verify the required parameter 'user_segment_key' is set
        if ('user_segment_key' not in params or
                params['user_segment_key'] is None):
            raise ValueError("Missing the required parameter `user_segment_key` when calling `delete_user_segment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']  # noqa: E501
        if 'user_segment_key' in params:
            path_params['userSegmentKey'] = params['user_segment_key']  # noqa: E501

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
            '/segments/{projectKey}/{environmentKey}/{userSegmentKey}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_segment(self, project_key, environment_key, user_segment_key, **kwargs):  # noqa: E501
        """Get a single user segment by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_segment(project_key, environment_key, user_segment_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_segment_key: The user segment's key. The key identifies the user segment in your code. (required)
        :return: UserSegment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_user_segment_with_http_info(project_key, environment_key, user_segment_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_segment_with_http_info(project_key, environment_key, user_segment_key, **kwargs)  # noqa: E501
            return data

    def get_user_segment_with_http_info(self, project_key, environment_key, user_segment_key, **kwargs):  # noqa: E501
        """Get a single user segment by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_segment_with_http_info(project_key, environment_key, user_segment_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_segment_key: The user segment's key. The key identifies the user segment in your code. (required)
        :return: UserSegment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'user_segment_key']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_segment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_user_segment`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `get_user_segment`")  # noqa: E501
        # verify the required parameter 'user_segment_key' is set
        if ('user_segment_key' not in params or
                params['user_segment_key'] is None):
            raise ValueError("Missing the required parameter `user_segment_key` when calling `get_user_segment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']  # noqa: E501
        if 'user_segment_key' in params:
            path_params['userSegmentKey'] = params['user_segment_key']  # noqa: E501

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
            '/segments/{projectKey}/{environmentKey}/{userSegmentKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserSegment',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_segments(self, project_key, environment_key, **kwargs):  # noqa: E501
        """Get a list of all user segments in the given project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_segments(project_key, environment_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str tag: Filter by tag. A tag can be used to group flags across projects.
        :return: UserSegments
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_user_segments_with_http_info(project_key, environment_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_segments_with_http_info(project_key, environment_key, **kwargs)  # noqa: E501
            return data

    def get_user_segments_with_http_info(self, project_key, environment_key, **kwargs):  # noqa: E501
        """Get a list of all user segments in the given project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_segments_with_http_info(project_key, environment_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str tag: Filter by tag. A tag can be used to group flags across projects.
        :return: UserSegments
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_segments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_user_segments`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `get_user_segments`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']  # noqa: E501

        query_params = []
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501

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
            '/segments/{projectKey}/{environmentKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserSegments',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_user_segment(self, project_key, environment_key, user_segment_key, patch_only, **kwargs):  # noqa: E501
        """Perform a partial update to a user segment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.patch_user_segment(project_key, environment_key, user_segment_key, patch_only, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_segment_key: The user segment's key. The key identifies the user segment in your code. (required)
        :param list[PatchOperation] patch_only: Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/' Feature flag patches also support JSON Merge Patch format. 'https://tools.ietf.org/html/rfc7386' The addition of comments is also supported. (required)
        :return: UserSegment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.patch_user_segment_with_http_info(project_key, environment_key, user_segment_key, patch_only, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_user_segment_with_http_info(project_key, environment_key, user_segment_key, patch_only, **kwargs)  # noqa: E501
            return data

    def patch_user_segment_with_http_info(self, project_key, environment_key, user_segment_key, patch_only, **kwargs):  # noqa: E501
        """Perform a partial update to a user segment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.patch_user_segment_with_http_info(project_key, environment_key, user_segment_key, patch_only, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_segment_key: The user segment's key. The key identifies the user segment in your code. (required)
        :param list[PatchOperation] patch_only: Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/' Feature flag patches also support JSON Merge Patch format. 'https://tools.ietf.org/html/rfc7386' The addition of comments is also supported. (required)
        :return: UserSegment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'user_segment_key', 'patch_only']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_user_segment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `patch_user_segment`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `patch_user_segment`")  # noqa: E501
        # verify the required parameter 'user_segment_key' is set
        if ('user_segment_key' not in params or
                params['user_segment_key'] is None):
            raise ValueError("Missing the required parameter `user_segment_key` when calling `patch_user_segment`")  # noqa: E501
        # verify the required parameter 'patch_only' is set
        if ('patch_only' not in params or
                params['patch_only'] is None):
            raise ValueError("Missing the required parameter `patch_only` when calling `patch_user_segment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']  # noqa: E501
        if 'user_segment_key' in params:
            path_params['userSegmentKey'] = params['user_segment_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'patch_only' in params:
            body_params = params['patch_only']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/segments/{projectKey}/{environmentKey}/{userSegmentKey}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserSegment',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_user_segment(self, project_key, environment_key, user_segment_body, **kwargs):  # noqa: E501
        """Creates a new user segment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_user_segment(project_key, environment_key, user_segment_body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param UserSegmentBody user_segment_body: Create a new user segment. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_user_segment_with_http_info(project_key, environment_key, user_segment_body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_user_segment_with_http_info(project_key, environment_key, user_segment_body, **kwargs)  # noqa: E501
            return data

    def post_user_segment_with_http_info(self, project_key, environment_key, user_segment_body, **kwargs):  # noqa: E501
        """Creates a new user segment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_user_segment_with_http_info(project_key, environment_key, user_segment_body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param UserSegmentBody user_segment_body: Create a new user segment. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'user_segment_body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_user_segment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `post_user_segment`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `post_user_segment`")  # noqa: E501
        # verify the required parameter 'user_segment_body' is set
        if ('user_segment_body' not in params or
                params['user_segment_body'] is None):
            raise ValueError("Missing the required parameter `user_segment_body` when calling `post_user_segment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_segment_body' in params:
            body_params = params['user_segment_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/segments/{projectKey}/{environmentKey}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
