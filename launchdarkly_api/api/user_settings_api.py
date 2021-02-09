# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 5.0.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from launchdarkly_api.api_client import ApiClient


class UserSettingsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_expiring_user_targets_for_user(self, project_key, environment_key, user_key, **kwargs):  # noqa: E501
        """Get expiring dates on flags for user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_expiring_user_targets_for_user(project_key, environment_key, user_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_key: The user's key. (required)
        :return: UserTargetingExpirationOnFlagsForUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_expiring_user_targets_for_user_with_http_info(project_key, environment_key, user_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_expiring_user_targets_for_user_with_http_info(project_key, environment_key, user_key, **kwargs)  # noqa: E501
            return data

    def get_expiring_user_targets_for_user_with_http_info(self, project_key, environment_key, user_key, **kwargs):  # noqa: E501
        """Get expiring dates on flags for user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_expiring_user_targets_for_user_with_http_info(project_key, environment_key, user_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_key: The user's key. (required)
        :return: UserTargetingExpirationOnFlagsForUser
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
                    " to method get_expiring_user_targets_for_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_expiring_user_targets_for_user`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `get_expiring_user_targets_for_user`")  # noqa: E501
        # verify the required parameter 'user_key' is set
        if ('user_key' not in params or
                params['user_key'] is None):
            raise ValueError("Missing the required parameter `user_key` when calling `get_expiring_user_targets_for_user`")  # noqa: E501

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
            '/users/{projectKey}/{userKey}/expiring-user-targets/{environmentKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserTargetingExpirationOnFlagsForUser',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_flag_setting(self, project_key, environment_key, user_key, feature_flag_key, **kwargs):  # noqa: E501
        """Fetch a single flag setting for a user by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_flag_setting(project_key, environment_key, user_key, feature_flag_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_key: The user's key. (required)
        :param str feature_flag_key: The feature flag's key. The key identifies the flag in your code. (required)
        :return: UserFlagSetting
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_flag_setting_with_http_info(project_key, environment_key, user_key, feature_flag_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_flag_setting_with_http_info(project_key, environment_key, user_key, feature_flag_key, **kwargs)  # noqa: E501
            return data

    def get_user_flag_setting_with_http_info(self, project_key, environment_key, user_key, feature_flag_key, **kwargs):  # noqa: E501
        """Fetch a single flag setting for a user by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_flag_setting_with_http_info(project_key, environment_key, user_key, feature_flag_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_key: The user's key. (required)
        :param str feature_flag_key: The feature flag's key. The key identifies the flag in your code. (required)
        :return: UserFlagSetting
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'user_key', 'feature_flag_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_flag_setting" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_user_flag_setting`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `get_user_flag_setting`")  # noqa: E501
        # verify the required parameter 'user_key' is set
        if ('user_key' not in params or
                params['user_key'] is None):
            raise ValueError("Missing the required parameter `user_key` when calling `get_user_flag_setting`")  # noqa: E501
        # verify the required parameter 'feature_flag_key' is set
        if ('feature_flag_key' not in params or
                params['feature_flag_key'] is None):
            raise ValueError("Missing the required parameter `feature_flag_key` when calling `get_user_flag_setting`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']  # noqa: E501
        if 'user_key' in params:
            path_params['userKey'] = params['user_key']  # noqa: E501
        if 'feature_flag_key' in params:
            path_params['featureFlagKey'] = params['feature_flag_key']  # noqa: E501

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
            '/users/{projectKey}/{environmentKey}/{userKey}/flags/{featureFlagKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserFlagSetting',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_flag_settings(self, project_key, environment_key, user_key, **kwargs):  # noqa: E501
        """Fetch a single flag setting for a user by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_flag_settings(project_key, environment_key, user_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_key: The user's key. (required)
        :return: UserFlagSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_flag_settings_with_http_info(project_key, environment_key, user_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_flag_settings_with_http_info(project_key, environment_key, user_key, **kwargs)  # noqa: E501
            return data

    def get_user_flag_settings_with_http_info(self, project_key, environment_key, user_key, **kwargs):  # noqa: E501
        """Fetch a single flag setting for a user by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_flag_settings_with_http_info(project_key, environment_key, user_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_key: The user's key. (required)
        :return: UserFlagSettings
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
                    " to method get_user_flag_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_user_flag_settings`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `get_user_flag_settings`")  # noqa: E501
        # verify the required parameter 'user_key' is set
        if ('user_key' not in params or
                params['user_key'] is None):
            raise ValueError("Missing the required parameter `user_key` when calling `get_user_flag_settings`")  # noqa: E501

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
            '/users/{projectKey}/{environmentKey}/{userKey}/flags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserFlagSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_expiring_user_targets_for_flags(self, project_key, environment_key, user_key, semantic_patch_with_comment, **kwargs):  # noqa: E501
        """Update, add, or delete expiring user targets for a single user on all flags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_expiring_user_targets_for_flags(project_key, environment_key, user_key, semantic_patch_with_comment, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_key: The user's key. (required)
        :param object semantic_patch_with_comment: Requires a Semantic Patch representation of the desired changes to the resource. 'https://apidocs.launchdarkly.com/reference#updates-via-semantic-patches'. The addition of comments is also supported. (required)
        :return: UserTargetingExpirationOnFlagsForUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_expiring_user_targets_for_flags_with_http_info(project_key, environment_key, user_key, semantic_patch_with_comment, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_expiring_user_targets_for_flags_with_http_info(project_key, environment_key, user_key, semantic_patch_with_comment, **kwargs)  # noqa: E501
            return data

    def patch_expiring_user_targets_for_flags_with_http_info(self, project_key, environment_key, user_key, semantic_patch_with_comment, **kwargs):  # noqa: E501
        """Update, add, or delete expiring user targets for a single user on all flags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_expiring_user_targets_for_flags_with_http_info(project_key, environment_key, user_key, semantic_patch_with_comment, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_key: The user's key. (required)
        :param object semantic_patch_with_comment: Requires a Semantic Patch representation of the desired changes to the resource. 'https://apidocs.launchdarkly.com/reference#updates-via-semantic-patches'. The addition of comments is also supported. (required)
        :return: UserTargetingExpirationOnFlagsForUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'user_key', 'semantic_patch_with_comment']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_expiring_user_targets_for_flags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `patch_expiring_user_targets_for_flags`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `patch_expiring_user_targets_for_flags`")  # noqa: E501
        # verify the required parameter 'user_key' is set
        if ('user_key' not in params or
                params['user_key'] is None):
            raise ValueError("Missing the required parameter `user_key` when calling `patch_expiring_user_targets_for_flags`")  # noqa: E501
        # verify the required parameter 'semantic_patch_with_comment' is set
        if ('semantic_patch_with_comment' not in params or
                params['semantic_patch_with_comment'] is None):
            raise ValueError("Missing the required parameter `semantic_patch_with_comment` when calling `patch_expiring_user_targets_for_flags`")  # noqa: E501

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
        if 'semantic_patch_with_comment' in params:
            body_params = params['semantic_patch_with_comment']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/users/{projectKey}/{userKey}/expiring-user-targets/{environmentKey}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserTargetingExpirationOnFlagsForUser',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_flag_setting(self, project_key, environment_key, user_key, feature_flag_key, user_settings_body, **kwargs):  # noqa: E501
        """Specifically enable or disable a feature flag for a user based on their key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_flag_setting(project_key, environment_key, user_key, feature_flag_key, user_settings_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_key: The user's key. (required)
        :param str feature_flag_key: The feature flag's key. The key identifies the flag in your code. (required)
        :param UserSettingsBody user_settings_body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_flag_setting_with_http_info(project_key, environment_key, user_key, feature_flag_key, user_settings_body, **kwargs)  # noqa: E501
        else:
            (data) = self.put_flag_setting_with_http_info(project_key, environment_key, user_key, feature_flag_key, user_settings_body, **kwargs)  # noqa: E501
            return data

    def put_flag_setting_with_http_info(self, project_key, environment_key, user_key, feature_flag_key, user_settings_body, **kwargs):  # noqa: E501
        """Specifically enable or disable a feature flag for a user based on their key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_flag_setting_with_http_info(project_key, environment_key, user_key, feature_flag_key, user_settings_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param str environment_key: The environment key, used to tie together flag configuration and users under one environment so they can be managed together. (required)
        :param str user_key: The user's key. (required)
        :param str feature_flag_key: The feature flag's key. The key identifies the flag in your code. (required)
        :param UserSettingsBody user_settings_body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'environment_key', 'user_key', 'feature_flag_key', 'user_settings_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_flag_setting" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `put_flag_setting`")  # noqa: E501
        # verify the required parameter 'environment_key' is set
        if ('environment_key' not in params or
                params['environment_key'] is None):
            raise ValueError("Missing the required parameter `environment_key` when calling `put_flag_setting`")  # noqa: E501
        # verify the required parameter 'user_key' is set
        if ('user_key' not in params or
                params['user_key'] is None):
            raise ValueError("Missing the required parameter `user_key` when calling `put_flag_setting`")  # noqa: E501
        # verify the required parameter 'feature_flag_key' is set
        if ('feature_flag_key' not in params or
                params['feature_flag_key'] is None):
            raise ValueError("Missing the required parameter `feature_flag_key` when calling `put_flag_setting`")  # noqa: E501
        # verify the required parameter 'user_settings_body' is set
        if ('user_settings_body' not in params or
                params['user_settings_body'] is None):
            raise ValueError("Missing the required parameter `user_settings_body` when calling `put_flag_setting`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501
        if 'environment_key' in params:
            path_params['environmentKey'] = params['environment_key']  # noqa: E501
        if 'user_key' in params:
            path_params['userKey'] = params['user_key']  # noqa: E501
        if 'feature_flag_key' in params:
            path_params['featureFlagKey'] = params['feature_flag_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_settings_body' in params:
            body_params = params['user_settings_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/users/{projectKey}/{environmentKey}/{userKey}/flags/{featureFlagKey}', 'PUT',
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
