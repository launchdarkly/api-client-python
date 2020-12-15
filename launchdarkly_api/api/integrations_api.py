# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 4.0.0
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from launchdarkly_api.api_client import ApiClient


class IntegrationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_integration_subscription(self, integration_key, integration_id, **kwargs):  # noqa: E501
        """Delete an integration subscription by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_integration_subscription(integration_key, integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_key: The key used to specify the integration kind. (required)
        :param str integration_id: The integration ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_integration_subscription_with_http_info(integration_key, integration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_integration_subscription_with_http_info(integration_key, integration_id, **kwargs)  # noqa: E501
            return data

    def delete_integration_subscription_with_http_info(self, integration_key, integration_id, **kwargs):  # noqa: E501
        """Delete an integration subscription by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_integration_subscription_with_http_info(integration_key, integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_key: The key used to specify the integration kind. (required)
        :param str integration_id: The integration ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_key', 'integration_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_integration_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'integration_key' is set
        if ('integration_key' not in params or
                params['integration_key'] is None):
            raise ValueError("Missing the required parameter `integration_key` when calling `delete_integration_subscription`")  # noqa: E501
        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params or
                params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `delete_integration_subscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'integration_key' in params:
            path_params['integrationKey'] = params['integration_key']  # noqa: E501
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']  # noqa: E501

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
            '/integrations/{integrationKey}/{integrationId}', 'DELETE',
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

    def get_integration_subscription(self, integration_key, integration_id, **kwargs):  # noqa: E501
        """Get a single integration subscription by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_integration_subscription(integration_key, integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_key: The key used to specify the integration kind. (required)
        :param str integration_id: The integration ID. (required)
        :return: IntegrationSubscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_integration_subscription_with_http_info(integration_key, integration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_integration_subscription_with_http_info(integration_key, integration_id, **kwargs)  # noqa: E501
            return data

    def get_integration_subscription_with_http_info(self, integration_key, integration_id, **kwargs):  # noqa: E501
        """Get a single integration subscription by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_integration_subscription_with_http_info(integration_key, integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_key: The key used to specify the integration kind. (required)
        :param str integration_id: The integration ID. (required)
        :return: IntegrationSubscription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_key', 'integration_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_integration_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'integration_key' is set
        if ('integration_key' not in params or
                params['integration_key'] is None):
            raise ValueError("Missing the required parameter `integration_key` when calling `get_integration_subscription`")  # noqa: E501
        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params or
                params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `get_integration_subscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'integration_key' in params:
            path_params['integrationKey'] = params['integration_key']  # noqa: E501
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']  # noqa: E501

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
            '/integrations/{integrationKey}/{integrationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntegrationSubscription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_integration_subscriptions(self, integration_key, **kwargs):  # noqa: E501
        """Get a list of all configured integrations of a given kind.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_integration_subscriptions(integration_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_key: The key used to specify the integration kind. (required)
        :return: Integration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_integration_subscriptions_with_http_info(integration_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_integration_subscriptions_with_http_info(integration_key, **kwargs)  # noqa: E501
            return data

    def get_integration_subscriptions_with_http_info(self, integration_key, **kwargs):  # noqa: E501
        """Get a list of all configured integrations of a given kind.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_integration_subscriptions_with_http_info(integration_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_key: The key used to specify the integration kind. (required)
        :return: Integration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_integration_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'integration_key' is set
        if ('integration_key' not in params or
                params['integration_key'] is None):
            raise ValueError("Missing the required parameter `integration_key` when calling `get_integration_subscriptions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'integration_key' in params:
            path_params['integrationKey'] = params['integration_key']  # noqa: E501

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
            '/integrations/{integrationKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Integration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_integrations(self, **kwargs):  # noqa: E501
        """Get a list of all configured audit log event integrations associated with this account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_integrations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Integrations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_integrations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_integrations_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_integrations_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of all configured audit log event integrations associated with this account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_integrations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Integrations
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
                    " to method get_integrations" % key
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
            '/integrations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Integrations',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_integration_subscription(self, integration_key, integration_id, patch_delta, **kwargs):  # noqa: E501
        """Modify an integration subscription by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_integration_subscription(integration_key, integration_id, patch_delta, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_key: The key used to specify the integration kind. (required)
        :param str integration_id: The integration ID. (required)
        :param list[PatchOperation] patch_delta: Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/' (required)
        :return: IntegrationSubscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_integration_subscription_with_http_info(integration_key, integration_id, patch_delta, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_integration_subscription_with_http_info(integration_key, integration_id, patch_delta, **kwargs)  # noqa: E501
            return data

    def patch_integration_subscription_with_http_info(self, integration_key, integration_id, patch_delta, **kwargs):  # noqa: E501
        """Modify an integration subscription by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_integration_subscription_with_http_info(integration_key, integration_id, patch_delta, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_key: The key used to specify the integration kind. (required)
        :param str integration_id: The integration ID. (required)
        :param list[PatchOperation] patch_delta: Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/' (required)
        :return: IntegrationSubscription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_key', 'integration_id', 'patch_delta']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_integration_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'integration_key' is set
        if ('integration_key' not in params or
                params['integration_key'] is None):
            raise ValueError("Missing the required parameter `integration_key` when calling `patch_integration_subscription`")  # noqa: E501
        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params or
                params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `patch_integration_subscription`")  # noqa: E501
        # verify the required parameter 'patch_delta' is set
        if ('patch_delta' not in params or
                params['patch_delta'] is None):
            raise ValueError("Missing the required parameter `patch_delta` when calling `patch_integration_subscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'integration_key' in params:
            path_params['integrationKey'] = params['integration_key']  # noqa: E501
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']  # noqa: E501

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
            '/integrations/{integrationKey}/{integrationId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntegrationSubscription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_integration_subscription(self, integration_key, subscription_body, **kwargs):  # noqa: E501
        """Create a new integration subscription of a given kind.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_integration_subscription(integration_key, subscription_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_key: The key used to specify the integration kind. (required)
        :param SubscriptionBody subscription_body: Create a new integration subscription. (required)
        :return: IntegrationSubscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_integration_subscription_with_http_info(integration_key, subscription_body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_integration_subscription_with_http_info(integration_key, subscription_body, **kwargs)  # noqa: E501
            return data

    def post_integration_subscription_with_http_info(self, integration_key, subscription_body, **kwargs):  # noqa: E501
        """Create a new integration subscription of a given kind.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_integration_subscription_with_http_info(integration_key, subscription_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_key: The key used to specify the integration kind. (required)
        :param SubscriptionBody subscription_body: Create a new integration subscription. (required)
        :return: IntegrationSubscription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_key', 'subscription_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_integration_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'integration_key' is set
        if ('integration_key' not in params or
                params['integration_key'] is None):
            raise ValueError("Missing the required parameter `integration_key` when calling `post_integration_subscription`")  # noqa: E501
        # verify the required parameter 'subscription_body' is set
        if ('subscription_body' not in params or
                params['subscription_body'] is None):
            raise ValueError("Missing the required parameter `subscription_body` when calling `post_integration_subscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'integration_key' in params:
            path_params['integrationKey'] = params['integration_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'subscription_body' in params:
            body_params = params['subscription_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/{integrationKey}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntegrationSubscription',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
