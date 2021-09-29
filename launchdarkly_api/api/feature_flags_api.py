# -*- coding: utf-8 -*-

"""
    LaunchDarkly REST API

    # Overview  ## Authentication  All REST API resources are authenticated with either [personal or service access tokens](https://docs.launchdarkly.com/home/account-security/api-access-tokens), or session cookies. Other authentication mechanisms are not supported. You can manage personal access tokens on your [Account settings](https://app.launchdarkly.com/settings/tokens) page.  LaunchDarkly also has SDK keys, mobile keys, and client-side IDs that are used by our server-side SDKs, mobile SDKs, and client-side SDKs, respectively. **These keys cannot be used to access our REST API**. These keys are environment-specific, and can only perform read-only operations (fetching feature flag settings).  | Auth mechanism                                                                                  | Allowed resources                                                                                     | Use cases                                          | | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------- | | [Personal access tokens](https://docs.launchdarkly.com/home/account-security/api-access-tokens) | Can be customized on a per-token basis                                                                | Building scripts, custom integrations, data export | | SDK keys                                                                                        | Can only access read-only SDK-specific resources and the firehose, restricted to a single environment | Server-side SDKs, Firehose API                     | | Mobile keys                                                                                     | Can only access read-only mobile SDK-specific resources, restricted to a single environment           | Mobile SDKs                                        | | Client-side ID                                                                                  | Single environment, only flags marked available to client-side                                        | Client-side JavaScript                             |  > #### Keep your access tokens and SDK keys private > > Access tokens should _never_ be exposed in untrusted contexts. Never put an access token in client-side JavaScript, or embed it in a mobile application. LaunchDarkly has special mobile keys that you can embed in mobile apps. If you accidentally expose an access token or SDK key, you can reset it from your [Account Settings](https://app.launchdarkly.com/settings#/tokens) page. > > The client-side ID is safe to embed in untrusted contexts. It's designed for use in client-side JavaScript.  ### Via request header  The preferred way to authenticate with the API is by adding an `Authorization` header containing your access token to your requests. The value of the `Authorization` header must be your access token.  Manage personal access tokens from the [Account Settings](https://app.launchdarkly.com/settings/tokens) page.  ### Via session cookie  For testing purposes, you can make API calls directly from your web browser. If you're logged in to the application, the API will use your existing session to authenticate calls.  If you have a [role](https://docs.launchdarkly.com/home/team/built-in-roles) other than Admin, or have a [custom role](https://docs.launchdarkly.com/home/team/custom-roles) defined, you may not have permission to perform some API calls. You will receive a `401` response code in that case.  > ### Modifying the Origin header causes an error > > LaunchDarkly validates that the Origin header for any API request authenticated by a session cookie matches the expected Origin header. The expected Origin header is `https://app.launchdarkly.com`. > > If the Origin header does not match what's expected, LaunchDarkly returns an error. This error can prevent the LaunchDarkly app from working correctly. > > Any browser extension that intentionally changes the Origin header can cause this problem. For example, the `Allow-Control-Allow-Origin: *` Chrome extension changes the Origin header to `http://evil.com` and causes the app to fail. > > To prevent this error, do not modify your Origin header. > > LaunchDarkly does not require origin matching when authenticating with an access token, so this issue does not affect normal API usage.  ## Representations  All resources expect and return JSON response bodies. Error responses will also send a JSON body. Read [Errors](#section/Errors) for a more detailed description of the error format used by the API.  In practice this means that you always get a response with a `Content-Type` header set to `application/json`.  In addition, request bodies for `PUT`, `POST`, `REPORT` and `PATCH` requests must be encoded as JSON with a `Content-Type` header set to `application/json`.  ### Summary and detailed representations  When you fetch a list of resources, the response includes only the most important attributes of each resource. This is a _summary representation_ of the resource. When you fetch an individual resource (for example, a single feature flag), you receive a _detailed representation_ containing all of the attributes of the resource.  The best way to find a detailed representation is to follow links. Every summary representation includes a link to its detailed representation.  ### Links and addressability  The best way to navigate the API is by following links. These are attributes in representations that link to other resources. The API always uses the same format for links:  - Links to other resources within the API are encapsulated in a `_links` object. - If the resource has a corresponding link to HTML content on the site, it is stored in a special `_site` link.  Each link has two attributes: an href (the URL) and a type (the content type). For example, a feature resource might return the following:  ```json {   \"_links\": {     \"parent\": {       \"href\": \"/api/features\",       \"type\": \"application/json\"     },     \"self\": {       \"href\": \"/api/features/sort.order\",       \"type\": \"application/json\"     }   },   \"_site\": {     \"href\": \"/features/sort.order\",     \"type\": \"text/html\"   } } ```  From this, you can navigate to the parent collection of features by following the `parent` link, or navigate to the site page for the feature by following the `_site` link.  Collections are always represented as a JSON object with an `items` attribute containing an array of representations. Like all other representations, collections have `_links` defined at the top level.  Paginated collections include `first`, `last`, `next`, and `prev` links containing a URL with the respective set of elements in the collection.  ## Updates  Resources that accept partial updates use the `PATCH` verb, and support the [JSON Patch](http://tools.ietf.org/html/rfc6902) format. Some resources also support the [JSON Merge Patch](https://tools.ietf.org/html/rfc7386) format. In addition, some resources support optional comments that can be submitted with updates. Comments appear in outgoing webhooks, the audit log, and other integrations.  ### Updates via JSON Patch  [JSON Patch](http://tools.ietf.org/html/rfc6902) is a way to specify the modifications to perform on a resource. For example, in this feature flag representation:  ```json {     \"name\": \"New recommendations engine\",     \"key\": \"engine.enable\",     \"description\": \"This is the description\",     ... } ```  You can change the feature flag's description with the following patch document:  ```json [{ \"op\": \"replace\", \"path\": \"/description\", \"value\": \"This is the new description\" }] ```  JSON Patch documents are always arrays. You can specify multiple modifications to perform in a single request. You can also test that certain preconditions are met before applying the patch:  ```json [   { \"op\": \"test\", \"path\": \"/version\", \"value\": 10 },   { \"op\": \"replace\", \"path\": \"/description\", \"value\": \"The new description\" } ] ```  The above patch request tests whether the feature flag's `version` is `10`, and if so, changes the feature flag's description.  Attributes that aren't editable, like a resource's `_links`, have names that start with an underscore.  ### Updates via JSON Merge Patch  The API also supports the [JSON Merge Patch](https://tools.ietf.org/html/rfc7386) format, as well as the [Update feature flag](/tag/Feature-flags#operation/patchFeatureFlag) resource.  JSON Merge Patch is less expressive than JSON Patch but in many cases, it is simpler to construct a merge patch document. For example, you can change a feature flag's description with the following merge patch document:  ```json {   \"description\": \"New flag description\" } ```  ### Updates with comments  You can submit optional comments with `PATCH` changes. The [Update feature flag](/tag/Feature-flags#operation/patchFeatureFlag) resource supports comments.  To submit a comment along with a JSON Patch document, use the following format:  ```json {   \"comment\": \"This is a comment string\",   \"patch\": [{ \"op\": \"replace\", \"path\": \"/description\", \"value\": \"The new description\" }] } ```  To submit a comment along with a JSON Merge Patch document, use the following format:  ```json {   \"comment\": \"This is a comment string\",   \"merge\": { \"description\": \"New flag description\" } } ```  ### Updates via semantic patches  The API also supports the Semantic patch format. A semantic `PATCH` is a way to specify the modifications to perform on a resource as a set of executable instructions.  JSON Patch uses paths and a limited set of operations to describe how to transform the current state of the resource into a new state. Semantic patch allows you to be explicit about intent using precise, custom instructions. In many cases, semantic patch instructions can also be defined independently of the current state of the resource. This can be useful when defining a change that may be applied at a future date.  For example, in this feature flag configuration in environment Production:  ```json {     \"name\": \"Alternate sort order\",     \"kind\": \"boolean\",     \"key\": \"sort.order\",    ...     \"environments\": {         \"production\": {             \"on\": true,             \"archived\": false,             \"salt\": \"c29ydC5vcmRlcg==\",             \"sel\": \"8de1085cb7354b0ab41c0e778376dfd3\",             \"lastModified\": 1469131558260,             \"version\": 81,             \"targets\": [                 {                     \"values\": [                         \"Gerhard.Little@yahoo.com\"                     ],                     \"variation\": 0                 },                 {                     \"values\": [                         \"1461797806429-33-861961230\",                         \"438580d8-02ee-418d-9eec-0085cab2bdf0\"                     ],                     \"variation\": 1                 }             ],             \"rules\": [],             \"fallthrough\": {                 \"variation\": 0             },             \"offVariation\": 1,             \"prerequisites\": [],             \"_site\": {                 \"href\": \"/default/production/features/sort.order\",                 \"type\": \"text/html\"             }        }     } } ```  You can add a date you want a user to be removed from the feature flag's user targets. For example, “remove user 1461797806429-33-861961230 from the user target for variation 0 on the Alternate sort order flag in the production environment on Wed Jul 08 2020 at 15:27:41 pm”. This is done using the following:  ```json {   \"comment\": \"update expiring user targets\",   \"instructions\": [     {       \"kind\": \"removeExpireUserTargetDate\",       \"userKey\": \"userKey\",       \"variationId\": \"978d53f9-7fe3-4a63-992d-97bcb4535dc8\"     },     {       \"kind\": \"updateExpireUserTargetDate\",       \"userKey\": \"userKey2\",       \"variationId\": \"978d53f9-7fe3-4a63-992d-97bcb4535dc8\",       \"value\": 1587582000000     },     {       \"kind\": \"addExpireUserTargetDate\",       \"userKey\": \"userKey3\",       \"variationId\": \"978d53f9-7fe3-4a63-992d-97bcb4535dc8\",       \"value\": 1594247266386     }   ] } ```  Here is another example. In this feature flag configuration:  ```json {   \"name\": \"New recommendations engine\",   \"key\": \"engine.enable\",   \"environments\": {     \"test\": {       \"on\": true     }   } } ```  You can change the feature flag's description with the following patch document as a set of executable instructions. For example, “add user X to targets for variation Y and remove user A from targets for variation B for test flag”:  ```json {   \"comment\": \"\",   \"instructions\": [     {       \"kind\": \"removeUserTargets\",       \"values\": [\"438580d8-02ee-418d-9eec-0085cab2bdf0\"],       \"variationId\": \"852cb784-54ff-46b9-8c35-5498d2e4f270\"     },     {       \"kind\": \"addUserTargets\",       \"values\": [\"438580d8-02ee-418d-9eec-0085cab2bdf0\"],       \"variationId\": \"1bb18465-33b6-49aa-a3bd-eeb6650b33ad\"     }   ] } ```  > ### Supported semantic patch API endpoints > > - [Update feature flag](/tag/Feature-flags#operation/patchFeatureFlag) > - [Update expiring user targets on feature flag](/tag/Feature-flags#operation/patchExpiringUserTargets) > - [Update expiring user target for flags](/tag/User-settings#operation/patchExpiringFlagsForUser) > - [Update expiring user targets on segment](/tag/Segments#operation/patchExpiringUserTargetsForSegment)  ## Errors  The API always returns errors in a common format. Here's an example:  ```json {   \"code\": \"invalid_request\",   \"message\": \"A feature with that key already exists\",   \"id\": \"30ce6058-87da-11e4-b116-123b93f75cba\" } ```  The general class of error is indicated by the `code`. The `message` is a human-readable explanation of what went wrong. The `id` is a unique identifier. Use it when you're working with LaunchDarkly support to debug a problem with a specific API call.  ### HTTP Status - Error Response Codes  | Code | Definition        | Desc.                                                                                       | Possible Solution                                                | | ---- | ----------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | | 400  | Bad Request       | A request that fails may return this HTTP response code.                                    | Ensure JSON syntax in request body is correct.                   | | 401  | Unauthorized      | User doesn't have permission to an API call.                                                | Ensure your SDK key is good.                                     | | 403  | Forbidden         | User does not have permission for operation.                                                | Ensure that the user or access token has proper permissions set. | | 409  | Conflict          | The API request could not be completed because it conflicted with a concurrent API request. | Retry your request.                                              | | 429  | Too many requests | See [Rate limiting](/#section/Rate-limiting).                                               | Wait and try again later.                                        |  ## CORS  The LaunchDarkly API supports Cross Origin Resource Sharing (CORS) for AJAX requests from any origin. If an `Origin` header is given in a request, it will be echoed as an explicitly allowed origin. Otherwise, a wildcard is returned: `Access-Control-Allow-Origin: *`. For more information on CORS, see the [CORS W3C Recommendation](http://www.w3.org/TR/cors). Example CORS headers might look like:  ```http Access-Control-Allow-Headers: Accept, Content-Type, Content-Length, Accept-Encoding, Authorization Access-Control-Allow-Methods: OPTIONS, GET, DELETE, PATCH Access-Control-Allow-Origin: * Access-Control-Max-Age: 300 ```  You can make authenticated CORS calls just as you would make same-origin calls, using either [token or session-based authentication](#section/Authentication). If you’re using session auth, you should set the `withCredentials` property for your `xhr` request to `true`. You should never expose your access tokens to untrusted users.  ## Rate limiting  We use several rate limiting strategies to ensure the availability of our APIs. Rate-limited calls to our APIs will return a `429` status code. Calls to our APIs will include headers indicating the current rate limit status. The specific headers returned depend on the API route being called. The limits differ based on the route, authentication mechanism, and other factors. Routes that are not rate limited may not contain any of the headers described below.  > ### Rate limiting and SDKs > > LaunchDarkly SDKs are never rate limited and do not use the API endpoints defined here. LaunchDarkly uses a different set of approaches, including streaming/server-sent events and a global CDN, to ensure availability to the routes used by LaunchDarkly SDKs. > > The client-side ID is safe to embed in untrusted contexts. It's designed for use in client-side JavaScript.  ### Global rate limits  Authenticated requests are subject to a global limit. This is the maximum number of calls that can be made to the API per ten seconds. All personal access tokens on the account share this limit, so exceeding the limit with one access token will impact other tokens. Calls that are subject to global rate limits will return the headers below:  | Header name                    | Description                                                                      | | ------------------------------ | -------------------------------------------------------------------------------- | | `X-Ratelimit-Global-Remaining` | The maximum number of requests the account is permitted to make per ten seconds. | | `X-Ratelimit-Reset`            | The time at which the current rate limit window resets in epoch milliseconds.    |  We do not publicly document the specific number of calls that can be made globally. This limit may change, and we encourage clients to program against the specification, relying on the two headers defined above, rather than hardcoding to the current limit.  ### Route-level rate limits  Some authenticated routes have custom rate limits. These also reset every ten seconds. Any access tokens hitting the same route share this limit, so exceeding the limit with one access token may impact other tokens. Calls that are subject to route-level rate limits will return the headers below:  | Header name                   | Description                                                                                           | | ----------------------------- | ----------------------------------------------------------------------------------------------------- | | `X-Ratelimit-Route-Remaining` | The maximum number of requests to the current route the account is permitted to make per ten seconds. | | `X-Ratelimit-Reset`           | The time at which the current rate limit window resets in epoch milliseconds.                         |  A _route_ represents a specific URL pattern and verb. For example, the [Delete environment](/tag/Environments#operation/deleteEnvironment) endpoint is considered a single route, and each call to delete an environment counts against your route-level rate limit for that route.  We do not publicly document the specific number of calls that can be made to each endpoint per ten seconds. These limits may change, and we encourage clients to program against the specification, relying on the two headers defined above, rather than hardcoding to the current limits.  ### IP-based rate limiting  We also employ IP-based rate limiting on some API routes. If you hit an IP-based rate limit, your API response will include a `Retry-After` header indicating how long to wait before re-trying the call. Clients must wait at least `Retry-After` seconds before making additional calls to our API, and should employ jitter and backoff strategies to avoid triggering rate limits again.  ## OpenAPI (Swagger)  We have a [complete OpenAPI (Swagger) specification](https://app.launchdarkly.com/api/v2/openapi.json) for our API.  You can use this specification to generate client libraries to interact with our REST API in your language of choice.  This specification is supported by several API-based tools such as Postman and Insomnia. In many cases, you can directly import our specification to ease use in navigating the APIs in the tooling.  ## Client libraries  We auto-generate multiple client libraries based on our OpenAPI specification. To learn more, visit [GitHub](https://github.com/search?q=topic%3Alaunchdarkly-api+org%3Alaunchdarkly&type=Repositories).  ## Method Overriding  Some firewalls and HTTP clients restrict the use of verbs other than `GET` and `POST`. In those environments, our API endpoints that use `PUT`, `PATCH`, and `DELETE` verbs will be inaccessible.  To avoid this issue, our API supports the `X-HTTP-Method-Override` header, allowing clients to \"tunnel\" `PUT`, `PATCH`, and `DELETE` requests via a `POST` request.  For example, if you wish to call one of our `PATCH` resources via a `POST` request, you can include `X-HTTP-Method-Override:PATCH` as a header.  ## Beta resources  We sometimes release new API resources in **beta** status before we release them with general availability.  Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.  We try to promote resources into general availability as quickly as possible. This happens after sufficient testing and when we're satisfied that we no longer need to make backwards-incompatible changes.  We mark beta resources with a \"Beta\" callout in our documentation, pictured below:  > ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](/#section/Beta-resources).  ### Using beta resources  To use a beta resource, you must include a header in the request. If you call a beta resource without this header, you'll receive a `403` response.  Use this header:  ``` LD-API-Version: beta ```  ## Versioning  We try hard to keep our REST API backwards compatible, but we occasionally have to make backwards-incompatible changes in the process of shipping new features. These breaking changes can cause unexpected behavior if you don't prepare for them accordingly.  Updates to our REST API include support for the latest features in LaunchDarkly. We also release a new version of our REST API every time we make a breaking change. We provide simultaneous support for multiple API versions so you can migrate from your current API version to a new version at your own pace.  ### Setting the API version per request  You can set the API version on a specific request by sending an `LD-API-Version` header, as shown in the example below:  ``` LD-API-Version: 20191212 ```  The header value is the version number of the API version you'd like to request. The number for each version corresponds to the date the version was released. In the example above the version `20191212` corresponds to December 12, 2019.  ### Setting the API version per access token  When creating an access token, you must specify a specific version of the API to use. This ensures that integrations using this token cannot be broken by version changes.  Tokens created before versioning was released have their version set to `20160426` (the version of the API that existed before versioning) so that they continue working the same way they did before versioning.  If you would like to upgrade your integration to use a new API version, you can explicitly set the header described above.  > ### Best practice: Set the header for every client or integration > > We recommend that you set the API version header explicitly in any client or integration you build. > > Only rely on the access token API version during manual testing.   # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@launchdarkly.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from launchdarkly_api.api_client import ApiClient, Endpoint as _Endpoint
from launchdarkly_api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from launchdarkly_api.model.expiring_user_target_get_response import ExpiringUserTargetGetResponse
from launchdarkly_api.model.expiring_user_target_patch_response import ExpiringUserTargetPatchResponse
from launchdarkly_api.model.feature_flag import FeatureFlag
from launchdarkly_api.model.feature_flag_body import FeatureFlagBody
from launchdarkly_api.model.feature_flag_status_across_environments import FeatureFlagStatusAcrossEnvironments
from launchdarkly_api.model.feature_flag_statuses import FeatureFlagStatuses
from launchdarkly_api.model.feature_flags import FeatureFlags
from launchdarkly_api.model.flag_copy_config_post import FlagCopyConfigPost
from launchdarkly_api.model.flag_status_rep import FlagStatusRep
from launchdarkly_api.model.patch_with_comment import PatchWithComment


class FeatureFlagsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __copy_feature_flag(
            self,
            proj_key,
            feature_flag_key,
            flag_copy_config_post,
            **kwargs
        ):
            """Copy feature flag  # noqa: E501

            The includedActions and excludedActions define the parts of the flag configuration that are copied or not copied. By default, the entire flag configuration is copied.  You can have either `includedActions` or `excludedActions` but not both.  Valid `includedActions` and `excludedActions` include:  - `updateOn` - `updatePrerequisites` - `updateTargets` - `updateRules` - `updateFallthrough` - `updateOffVariation`    The `source` and `target` must be JSON objects if using curl, specifying the environment key and (optional) current flag configuration version in that environment. For example:  ```json {   \"key\": \"production\",   \"currentVersion\": 3 } ```  If target is specified as above, the API will test to ensure that the current flag version in the `production` environment is `3`, and reject attempts to copy settings to `production` otherwise. You can use this to enforce optimistic locking on copy attempts.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.copy_feature_flag(proj_key, feature_flag_key, flag_copy_config_post, async_req=True)
            >>> result = thread.get()

            Args:
                proj_key (str): The project key.
                feature_flag_key (str): The feature flag's key. The key identifies the flag in your code.
                flag_copy_config_post (FlagCopyConfigPost):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                FeatureFlag
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['proj_key'] = \
                proj_key
            kwargs['feature_flag_key'] = \
                feature_flag_key
            kwargs['flag_copy_config_post'] = \
                flag_copy_config_post
            return self.call_with_http_info(**kwargs)

        self.copy_feature_flag = _Endpoint(
            settings={
                'response_type': (FeatureFlag,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projKey}/{featureFlagKey}/copy',
                'operation_id': 'copy_feature_flag',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'proj_key',
                    'feature_flag_key',
                    'flag_copy_config_post',
                ],
                'required': [
                    'proj_key',
                    'feature_flag_key',
                    'flag_copy_config_post',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'proj_key':
                        (str,),
                    'feature_flag_key':
                        (str,),
                    'flag_copy_config_post':
                        (FlagCopyConfigPost,),
                },
                'attribute_map': {
                    'proj_key': 'projKey',
                    'feature_flag_key': 'featureFlagKey',
                },
                'location_map': {
                    'proj_key': 'path',
                    'feature_flag_key': 'path',
                    'flag_copy_config_post': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__copy_feature_flag
        )

        def __delete_feature_flag(
            self,
            proj_key,
            key,
            **kwargs
        ):
            """Delete feature flag  # noqa: E501

            Delete a feature flag in all environments. Use with caution: only delete feature flags your application no longer uses.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_feature_flag(proj_key, key, async_req=True)
            >>> result = thread.get()

            Args:
                proj_key (str): The project key.
                key (str): The feature flag's key. The key identifies the flag in your code.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['proj_key'] = \
                proj_key
            kwargs['key'] = \
                key
            return self.call_with_http_info(**kwargs)

        self.delete_feature_flag = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projKey}/{key}',
                'operation_id': 'delete_feature_flag',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'proj_key',
                    'key',
                ],
                'required': [
                    'proj_key',
                    'key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'proj_key':
                        (str,),
                    'key':
                        (str,),
                },
                'attribute_map': {
                    'proj_key': 'projKey',
                    'key': 'key',
                },
                'location_map': {
                    'proj_key': 'path',
                    'key': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_feature_flag
        )

        def __get_expiring_user_targets(
            self,
            proj_key,
            env_key,
            flag_key,
            **kwargs
        ):
            """Get expiring user targets for feature flag  # noqa: E501

            Get a list of user targets on a feature flag that are scheduled for removal.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_expiring_user_targets(proj_key, env_key, flag_key, async_req=True)
            >>> result = thread.get()

            Args:
                proj_key (str): The project key.
                env_key (str): The environment key.
                flag_key (str): The feature flag key.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ExpiringUserTargetGetResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['proj_key'] = \
                proj_key
            kwargs['env_key'] = \
                env_key
            kwargs['flag_key'] = \
                flag_key
            return self.call_with_http_info(**kwargs)

        self.get_expiring_user_targets = _Endpoint(
            settings={
                'response_type': (ExpiringUserTargetGetResponse,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projKey}/{flagKey}/expiring-user-targets/{envKey}',
                'operation_id': 'get_expiring_user_targets',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'proj_key',
                    'env_key',
                    'flag_key',
                ],
                'required': [
                    'proj_key',
                    'env_key',
                    'flag_key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'proj_key':
                        (str,),
                    'env_key':
                        (str,),
                    'flag_key':
                        (str,),
                },
                'attribute_map': {
                    'proj_key': 'projKey',
                    'env_key': 'envKey',
                    'flag_key': 'flagKey',
                },
                'location_map': {
                    'proj_key': 'path',
                    'env_key': 'path',
                    'flag_key': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_expiring_user_targets
        )

        def __get_feature_flag(
            self,
            proj_key,
            key,
            **kwargs
        ):
            """Get feature flag  # noqa: E501

            Get a single feature flag by key. By default, this returns the configurations for all environments. You can filter environments with the `env` query parameter. For example, setting `env=production` restricts the returned configurations to just the `production` environment.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_feature_flag(proj_key, key, async_req=True)
            >>> result = thread.get()

            Args:
                proj_key (str): The project key
                key (str): The feature flag key

            Keyword Args:
                env (str): Filter configurations by environment. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                FeatureFlag
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['proj_key'] = \
                proj_key
            kwargs['key'] = \
                key
            return self.call_with_http_info(**kwargs)

        self.get_feature_flag = _Endpoint(
            settings={
                'response_type': (FeatureFlag,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projKey}/{key}',
                'operation_id': 'get_feature_flag',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'proj_key',
                    'key',
                    'env',
                ],
                'required': [
                    'proj_key',
                    'key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'proj_key':
                        (str,),
                    'key':
                        (str,),
                    'env':
                        (str,),
                },
                'attribute_map': {
                    'proj_key': 'projKey',
                    'key': 'key',
                    'env': 'env',
                },
                'location_map': {
                    'proj_key': 'path',
                    'key': 'path',
                    'env': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_feature_flag
        )

        def __get_feature_flag_status(
            self,
            proj_key,
            env_key,
            key,
            **kwargs
        ):
            """Get feature flag status  # noqa: E501

            Get the status for a particular feature flag.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_feature_flag_status(proj_key, env_key, key, async_req=True)
            >>> result = thread.get()

            Args:
                proj_key (str): The project key
                env_key (str): The environment key
                key (str): The feature flag key

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                FlagStatusRep
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['proj_key'] = \
                proj_key
            kwargs['env_key'] = \
                env_key
            kwargs['key'] = \
                key
            return self.call_with_http_info(**kwargs)

        self.get_feature_flag_status = _Endpoint(
            settings={
                'response_type': (FlagStatusRep,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flag-statuses/{projKey}/{envKey}/{key}',
                'operation_id': 'get_feature_flag_status',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'proj_key',
                    'env_key',
                    'key',
                ],
                'required': [
                    'proj_key',
                    'env_key',
                    'key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'proj_key':
                        (str,),
                    'env_key':
                        (str,),
                    'key':
                        (str,),
                },
                'attribute_map': {
                    'proj_key': 'projKey',
                    'env_key': 'envKey',
                    'key': 'key',
                },
                'location_map': {
                    'proj_key': 'path',
                    'env_key': 'path',
                    'key': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_feature_flag_status
        )

        def __get_feature_flag_status_across_environments(
            self,
            proj_key,
            key,
            **kwargs
        ):
            """Get flag status across environments  # noqa: E501

            Get the status for a particular feature flag across environments.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_feature_flag_status_across_environments(proj_key, key, async_req=True)
            >>> result = thread.get()

            Args:
                proj_key (str): The project key
                key (str): The feature flag key

            Keyword Args:
                env (str): Optional environment filter. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                FeatureFlagStatusAcrossEnvironments
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['proj_key'] = \
                proj_key
            kwargs['key'] = \
                key
            return self.call_with_http_info(**kwargs)

        self.get_feature_flag_status_across_environments = _Endpoint(
            settings={
                'response_type': (FeatureFlagStatusAcrossEnvironments,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flag-status/{projKey}/{key}',
                'operation_id': 'get_feature_flag_status_across_environments',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'proj_key',
                    'key',
                    'env',
                ],
                'required': [
                    'proj_key',
                    'key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'proj_key':
                        (str,),
                    'key':
                        (str,),
                    'env':
                        (str,),
                },
                'attribute_map': {
                    'proj_key': 'projKey',
                    'key': 'key',
                    'env': 'env',
                },
                'location_map': {
                    'proj_key': 'path',
                    'key': 'path',
                    'env': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_feature_flag_status_across_environments
        )

        def __get_feature_flag_statuses(
            self,
            proj_key,
            env_key,
            **kwargs
        ):
            """List feature flag statuses  # noqa: E501

            Get a list of statuses for all feature flags. The status includes the last time the feature flag was requested, as well as a state, which is one of the following:  - `new`: the feature flag was created within the last seven days, and has not been requested yet - `active`: the feature flag was requested by your servers or clients within the last seven days - `inactive`: the feature flag was created more than seven days ago, and hasn't been requested by your servers or clients within the past seven days - `launched`: one variation of the feature flag has been rolled out to all your users for at least 7 days   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_feature_flag_statuses(proj_key, env_key, async_req=True)
            >>> result = thread.get()

            Args:
                proj_key (str): The project key
                env_key (str): Filter configurations by environment

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                FeatureFlagStatuses
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['proj_key'] = \
                proj_key
            kwargs['env_key'] = \
                env_key
            return self.call_with_http_info(**kwargs)

        self.get_feature_flag_statuses = _Endpoint(
            settings={
                'response_type': (FeatureFlagStatuses,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flag-statuses/{projKey}/{envKey}',
                'operation_id': 'get_feature_flag_statuses',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'proj_key',
                    'env_key',
                ],
                'required': [
                    'proj_key',
                    'env_key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'proj_key':
                        (str,),
                    'env_key':
                        (str,),
                },
                'attribute_map': {
                    'proj_key': 'projKey',
                    'env_key': 'envKey',
                },
                'location_map': {
                    'proj_key': 'path',
                    'env_key': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_feature_flag_statuses
        )

        def __get_feature_flags(
            self,
            proj_key,
            **kwargs
        ):
            """List feature flags  # noqa: E501

            Get a list of all features in the given project. By default, each feature includes configurations for each environment. You can filter environments with the env query parameter. For example, setting `env=production` restricts the returned configurations to just your production environment. You can also filter feature flags by tag with the tag query parameter.  We support the following fields for filters:  - `query` is a string that matches against the flags' keys and names. It is not case sensitive. - `archived` is a boolean to filter the list to archived flags. When this is absent, only unarchived flags are returned. - `type` is a string allowing filtering to `temporary` or `permanent` flags. - `status` is a string allowing filtering to `new`, `inactive`, `active`, or `launched` flags in the specified environment. This filter also requires a `filterEnv` field to be set to a valid environment. For example: `filter=status:active,filterEnv:production`. - `tags` is a + separated list of tags. It filters the list to members who have all of the tags in the list. - `hasExperiment` is a boolean with values of true or false and returns any flags that have an attached metric. - `hasDataExport` is a boolean with values of true or false and returns any flags that are currently exporting data in the specified environment. This includes flags that are exporting data via Experimentation. This filter also requires a `filterEnv` field to be set to a valid environment key. e.g. `filter=hasExperiment:true,filterEnv:production` - `evaluated` is an object that contains a key of `after` and a value in Unix time in milliseconds. This returns all flags that have been evaluated since the time you specify in the environment provided. This filter also requires a `filterEnv` field to be set to a valid environment. For example: `filter=evaluated:{\"after\": 1590768455282},filterEnv:production`. - `filterEnv` is a string with the key of a valid environment. The filterEnv field is used for filters that are environment specific. If there are multiple environment specific filters you should only declare this parameter once. For example: `filter=evaluated:{\"after\": 1590768455282},filterEnv:production,status:active`.  An example filter is `query:abc,tags:foo+bar`. This matches flags with the string `abc` in their key or name, ignoring case, which also have the tags `foo` and `bar`.  By default, this returns all flags. You can page through the list with the `limit` parameter and by following the `first`, `prev`, `next`, and `last` links in the returned `_links` field. These links will not be present if the pages they refer to don't exist. For example, the `first` and `prev` links will be missing from the response on the first page.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_feature_flags(proj_key, async_req=True)
            >>> result = thread.get()

            Args:
                proj_key (str): The project key

            Keyword Args:
                env (str): Filter configurations by environment. [optional]
                tag (str): Filter feature flags by tag. [optional]
                limit (int): The number of feature flags to return. Defaults to -1, which returns all flags. [optional]
                offset (int): Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next limit items. [optional]
                query (str): A string that matches against the flags' keys and names. It is not case sensitive. [optional]
                archived (bool): A boolean to filter the list to archived flags. When this is absent, only unarchived flags will be returned. [optional]
                summary (bool): By default in API version >= 1, flags will _not_ include their list of prerequisites, targets or rules.  Set summary=0 to include these fields for each flag returned. [optional]
                filter (str): A comma-separated list of filters. Each filter is of the form field:value. [optional]
                sort (str): A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                FeatureFlags
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['proj_key'] = \
                proj_key
            return self.call_with_http_info(**kwargs)

        self.get_feature_flags = _Endpoint(
            settings={
                'response_type': (FeatureFlags,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projKey}',
                'operation_id': 'get_feature_flags',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'proj_key',
                    'env',
                    'tag',
                    'limit',
                    'offset',
                    'query',
                    'archived',
                    'summary',
                    'filter',
                    'sort',
                ],
                'required': [
                    'proj_key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'proj_key':
                        (str,),
                    'env':
                        (str,),
                    'tag':
                        (str,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                    'query':
                        (str,),
                    'archived':
                        (bool,),
                    'summary':
                        (bool,),
                    'filter':
                        (str,),
                    'sort':
                        (str,),
                },
                'attribute_map': {
                    'proj_key': 'projKey',
                    'env': 'env',
                    'tag': 'tag',
                    'limit': 'limit',
                    'offset': 'offset',
                    'query': 'query',
                    'archived': 'archived',
                    'summary': 'summary',
                    'filter': 'filter',
                    'sort': 'sort',
                },
                'location_map': {
                    'proj_key': 'path',
                    'env': 'query',
                    'tag': 'query',
                    'limit': 'query',
                    'offset': 'query',
                    'query': 'query',
                    'archived': 'query',
                    'summary': 'query',
                    'filter': 'query',
                    'sort': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_feature_flags
        )

        def __patch_expiring_user_targets(
            self,
            proj_key,
            env_key,
            flag_key,
            patch_with_comment,
            **kwargs
        ):
            """Update expiring user targets on feature flag  # noqa: E501

            Update the list of user targets on a feature flag that are scheduled for removal.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.patch_expiring_user_targets(proj_key, env_key, flag_key, patch_with_comment, async_req=True)
            >>> result = thread.get()

            Args:
                proj_key (str): The project key.
                env_key (str): The environment key.
                flag_key (str): The feature flag key.
                patch_with_comment (PatchWithComment):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ExpiringUserTargetPatchResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['proj_key'] = \
                proj_key
            kwargs['env_key'] = \
                env_key
            kwargs['flag_key'] = \
                flag_key
            kwargs['patch_with_comment'] = \
                patch_with_comment
            return self.call_with_http_info(**kwargs)

        self.patch_expiring_user_targets = _Endpoint(
            settings={
                'response_type': (ExpiringUserTargetPatchResponse,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projKey}/{flagKey}/expiring-user-targets/{envKey}',
                'operation_id': 'patch_expiring_user_targets',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'proj_key',
                    'env_key',
                    'flag_key',
                    'patch_with_comment',
                ],
                'required': [
                    'proj_key',
                    'env_key',
                    'flag_key',
                    'patch_with_comment',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'proj_key':
                        (str,),
                    'env_key':
                        (str,),
                    'flag_key':
                        (str,),
                    'patch_with_comment':
                        (PatchWithComment,),
                },
                'attribute_map': {
                    'proj_key': 'projKey',
                    'env_key': 'envKey',
                    'flag_key': 'flagKey',
                },
                'location_map': {
                    'proj_key': 'path',
                    'env_key': 'path',
                    'flag_key': 'path',
                    'patch_with_comment': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__patch_expiring_user_targets
        )

        def __patch_feature_flag(
            self,
            proj_key,
            key,
            patch_with_comment,
            **kwargs
        ):
            """Update feature flag  # noqa: E501

            Perform a partial update to a feature flag.  ## Using JSON Patches on a feature flag  When using the update feature flag endpoint to add individual users to a specific variation, there are two different patch documents, depending on whether users are already being individually targeted for the variation.  If a flag variation already has users individually targeted, the path for the JSON Patch operation is:  ```json {   \"op\": \"add\",   \"path\": \"/environments/devint/targets/0/values/-\",   \"value\": \"TestClient10\" } ```  If a flag variation does not already have users individually targeted, the path for the JSON Patch operation is:  ```json [   {     \"op\": \"add\",     \"path\": \"/environments/devint/targets/-\",     \"value\": { \"variation\": 0, \"values\": [\"TestClient10\"] }   } ] ```  ## Using semantic patches on a feature flag  To use a [semantic patch](/#section/Updates/Updates-via-semantic-patches) on a feature flag resource, you must include a header in the request. If you call a semantic patch resource without this header, you receive a `400` response as your semantic patch will be interpreted as a JSON patch.  Use this header:  ``` Content-Type: application/json; domain-model=launchdarkly.semanticpatch ```  The body of a semantic patch request takes the following three properties:  1. comment `string`: (Optional) A description of the update. 1. environmentKey `string`: (Required) The key of the LaunchDarkly environment. 1. instructions `array`: (Required) The action or list of actions to be performed by the update. Each update action in the list must be an object/hash table with a `kind` property, although depending on the action, other properties may be necessary. Read below for more information on the specific supported semantic patch instructions.  If any instruction in the patch encounters an error, the error will be returned and the flag will not be changed. In general, instructions will silently do nothing if the flag is already in the state requested by the patch instruction. For example, `removeUserTargets` does nothing when the targets have already been removed). They will generally error if a parameter refers to something that does not exist, like a variation ID that doesn't correspond to a variation on the flag or a rule ID that doesn't belong to a rule on the flag. Other specific error conditions are noted in the instruction descriptions.  ### Instructions  #### `turnFlagOn`  Sets the flag's targeting state to on.  #### `turnFlagOff`  Sets the flag's targeting state to off.  #### `addUserTargets`  Adds the user keys in `values` to the individual user targets for the variation specified by `variationId`. Returns an error if this causes the same user key to be targeted in multiple variations.  ##### Parameters  - `values`: list of user keys - `variationId`: ID of a variation on the flag  #### `removeUserTargets`  Removes the user keys in `values` to the individual user targets for the variation specified by `variationId`. Does nothing if the user keys are not targeted.  ##### Parameters  - `values`: list of user keys - `variationId`: ID of a variation on the flag  #### `replaceUserTargets`  Completely replaces the existing set of user targeting. All variations must be provided. Example:  ```json {   \"kind\": \"replaceUserTargets\",   \"targets\": [     {       \"variationId\": \"variation-1\",       \"values\": [\"blah\", \"foo\", \"bar\"]     },     {       \"variationId\": \"variation-2\",       \"values\": [\"abc\", \"def\"]     }   ] } ```  ##### Parameters  - `targets`: a list of user targeting  #### `clearUserTargets`  Removes all individual user targets from the variation specified by `variationId`  ##### Parameters  - `variationId`: ID of a variation on the flag  #### `addPrerequisite`  Adds the flag indicated by `key` with variation `variationId` as a prerequisite to the flag.  ##### Parameters  - `key`: flag key of another flag - `variationId`: ID of a variation of the flag with key `key`  #### `removePrerequisite`  Removes the prerequisite indicated by `key`. Does nothing if this prerequisite does not exist.  ##### Parameters  - `key`: flag key of an existing prerequisite  #### `updatePrerequisite`  Changes the prerequisite with flag key `key` to the variation indicated by `variationId`. Returns an error if this prerequisite does not exist.  ##### Parameters  - `key`: flag key of an existing prerequisite - `variationId`: ID of a variation of the flag with key `key`  #### `replacePrerequisites`  Completely replaces the existing set of prerequisites for a given flag. Example:  ```json {   \"kind\": \"replacePrerequisites\",   \"prerequisites\": [     {       \"key\": \"flag-key\",       \"variationId\": \"variation-1\"     },     {       \"key\": \"another-flag\",       \"variationId\": \"variation-2\"     }   ] } ```  ##### Parameters  - `prerequisites`: a list of prerequisites  #### `addRule`  Adds a new rule to the flag with the given `clauses` which serves the variation indicated by `variationId` or the percent rollout indicated by `rolloutWeights` and `rolloutBucketBy`. If `beforeRuleId` is set, the rule will be added in the list of rules before the indicated rule. Otherwise, the rule will be added to the end of the list.  ##### Parameters  - `clauses`: Array of clauses (see `addClauses`) - `beforeRuleId`: Optional ID of a rule in the flag - `variationId`: ID of a variation of the flag - `rolloutWeights`: Map of variationId to weight in thousandths of a percent (0-100000) - `rolloutBucketBy`: Optional user attribute  #### `removeRule`  Removes the targeting rule specified by `ruleId`. Does nothing if the rule does not exist.  ##### Parameters  - `ruleId`: ID of a rule in the flag  #### `replaceRules`  Completely replaces the existing rules for a given flag. Example:  ```json {   \"kind\": \"replaceRules\",   \"rules\": [     {       \"variationId\": \"variation-1\",       \"description\": \"myRule\",       \"clauses\": [         {           \"attribute\": \"segmentMatch\",           \"op\": \"segmentMatch\",           \"values\": [\"test\"]         }       ],       \"trackEvents\": true     }   ] } ```  ##### Parameters  - `rules`: a list of rules  #### `addClauses`  Adds the given clauses to the rule indicated by `ruleId`.  ##### Parameters  - `ruleId`: ID of a rule in the flag - `clauses`: Array of clause objects, with `attribute` (string), `op` (string), and `values` (array of strings, numbers, or dates) properties.  #### `removeClauses`  Removes the clauses specified by `clauseIds` from the rule indicated by `ruleId`.  #### Parameters  - `ruleId`: ID of a rule in the flag - `clauseIds`: Array of IDs of clauses in the rule  #### `updateClause`  Replaces the clause indicated by `ruleId` and `clauseId` with `clause`.  ##### Parameters  - `ruleId`: ID of a rule in the flag - `clauseId`: ID of a clause in that rule - `clause`: Clause object  #### `addValuesToClause`  Adds `values` to the values of the clause indicated by `ruleId` and `clauseId`.  ##### Parameters  - `ruleId`: ID of a rule in the flag - `clauseId`: ID of a clause in that rule - `values`: Array of strings  #### `removeValuesFromClause`  Removes `values` from the values of the clause indicated by `ruleId` and `clauseId`.  ##### Parameters  `ruleId`: ID of a rule in the flag `clauseId`: ID of a clause in that rule `values`: Array of strings  #### `reorderRules`  Rearranges the rules to match the order given in `ruleIds`. Will return an error if `ruleIds` does not match the current set of rules on the flag.  ##### Parameters  - `ruleIds`: Array of IDs of all rules in the flag  #### `updateRuleVariationOrRollout`  Updates what the rule indicated by `ruleId` serves if its clauses evaluate to true. Can either be a fixed variation indicated by `variationId` or a percent rollout indicated by `rolloutWeights` and `rolloutBucketBy`.  ##### Parameters  - `ruleId`: ID of a rule in the flag - `variationId`: ID of a variation of the flag   or - `rolloutWeights`: Map of variationId to weight in thousandths of a percent (0-100000) - `rolloutBucketBy`: Optional user attribute  #### `updateFallthroughVariationOrRollout`  Updates the flag's fallthrough, which is served if none of the targeting rules match. Can either be a fixed variation indicated by `variationId` or a percent rollout indicated by `rolloutWeights` and `rolloutBucketBy`.  ##### Parameters  `variationId`: ID of a variation of the flag or `rolloutWeights`: Map of variationId to weight in thousandths of a percent (0-100000) `rolloutBucketBy`: Optional user attribute  #### `updateOffVariation`  Updates the variation served when the flag's targeting is off to the variation indicated by `variationId`.  ##### Parameters  `variationId`: ID of a variation of the flag  ### Example  ```json {   \"environmentKey\": \"production\",   \"instructions\": [     {       \"kind\": \"turnFlagOn\"     },     {       \"kind\": \"turnFlagOff\"     },     {       \"kind\": \"addUserTargets\",       \"variationId\": \"8bfb304e-d516-47e5-8727-e7f798e8992d\",       \"values\": [\"userId\", \"userId2\"]     },     {       \"kind\": \"removeUserTargets\",       \"variationId\": \"8bfb304e-d516-47e5-8727-e7f798e8992d\",       \"values\": [\"userId3\", \"userId4\"]     },     {       \"kind\": \"updateFallthroughVariationOrRollout\",       \"rolloutWeights\": {         \"variationId\": 50000,         \"variationId2\": 50000       },       \"rolloutBucketBy\": null     },     {       \"kind\": \"addRule\",       \"clauses\": [         {           \"attribute\": \"segmentMatch\",           \"negate\": false,           \"values\": [\"test-segment\"]         }       ],       \"variationId\": null,       \"rolloutWeights\": {         \"variationId\": 50000,         \"variationId2\": 50000       },       \"rolloutBucketBy\": \"key\"     },     {       \"kind\": \"removeRule\",       \"ruleId\": \"99f12464-a429-40fc-86cc-b27612188955\"     },     {       \"kind\": \"reorderRules\",       \"ruleIds\": [\"2f72974e-de68-4243-8dd3-739582147a1f\", \"8bfb304e-d516-47e5-8727-e7f798e8992d\"]     },     {       \"kind\": \"addClauses\",       \"ruleId\": \"1134\",       \"clauses\": [         {           \"attribute\": \"email\",           \"op\": \"in\",           \"negate\": false,           \"values\": [\"test@test.com\"]         }       ]     },     {       \"kind\": \"removeClauses\",       \"ruleId\": \"1242529\",       \"clauseIds\": [\"8bfb304e-d516-47e5-8727-e7f798e8992d\"]     },     {       \"kind\": \"updateClause\",       \"ruleId\": \"2f72974e-de68-4243-8dd3-739582147a1f\",       \"clauseId\": \"309845\",       \"clause\": {         \"attribute\": \"segmentMatch\",         \"negate\": false,         \"values\": [\"test-segment\"]       }     },     {       \"kind\": \"updateRuleVariationOrRollout\",       \"ruleId\": \"2342\",       \"rolloutWeights\": null,       \"rolloutBucketBy\": null     },     {       \"kind\": \"updateOffVariation\",       \"variationId\": \"3242453\"     },     {       \"kind\": \"addPrerequisite\",       \"variationId\": \"234235\",       \"key\": \"flagKey2\"     },     {       \"kind\": \"updatePrerequisite\",       \"variationId\": \"234235\",       \"key\": \"flagKey2\"     },     {       \"kind\": \"removePrerequisite\",       \"key\": \"flagKey\"     }   ] } ```  ## Using JSON patches on a feature flag  If you do not include the header described above, you can use [JSON patch](/#section/Updates/Updates-via-JSON-Patch).   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.patch_feature_flag(proj_key, key, patch_with_comment, async_req=True)
            >>> result = thread.get()

            Args:
                proj_key (str): The project key.
                key (str): The feature flag's key. The key identifies the flag in your code.
                patch_with_comment (PatchWithComment):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                FeatureFlag
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['proj_key'] = \
                proj_key
            kwargs['key'] = \
                key
            kwargs['patch_with_comment'] = \
                patch_with_comment
            return self.call_with_http_info(**kwargs)

        self.patch_feature_flag = _Endpoint(
            settings={
                'response_type': (FeatureFlag,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projKey}/{key}',
                'operation_id': 'patch_feature_flag',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'proj_key',
                    'key',
                    'patch_with_comment',
                ],
                'required': [
                    'proj_key',
                    'key',
                    'patch_with_comment',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'proj_key':
                        (str,),
                    'key':
                        (str,),
                    'patch_with_comment':
                        (PatchWithComment,),
                },
                'attribute_map': {
                    'proj_key': 'projKey',
                    'key': 'key',
                },
                'location_map': {
                    'proj_key': 'path',
                    'key': 'path',
                    'patch_with_comment': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__patch_feature_flag
        )

        def __post_feature_flag(
            self,
            proj_key,
            feature_flag_body,
            **kwargs
        ):
            """Create a feature flag  # noqa: E501

            Create a feature flag with the given name, key, and variations  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_feature_flag(proj_key, feature_flag_body, async_req=True)
            >>> result = thread.get()

            Args:
                proj_key (str): The project key.
                feature_flag_body (FeatureFlagBody):

            Keyword Args:
                clone (str): The key of the feature flag to be cloned. The key identifies the flag in your code. For example, setting `clone=flagKey` copies the full targeting configuration for all environments, including `on/off` state, from the original flag to the new flag.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                FeatureFlag
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['proj_key'] = \
                proj_key
            kwargs['feature_flag_body'] = \
                feature_flag_body
            return self.call_with_http_info(**kwargs)

        self.post_feature_flag = _Endpoint(
            settings={
                'response_type': (FeatureFlag,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projKey}',
                'operation_id': 'post_feature_flag',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'proj_key',
                    'feature_flag_body',
                    'clone',
                ],
                'required': [
                    'proj_key',
                    'feature_flag_body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'proj_key':
                        (str,),
                    'feature_flag_body':
                        (FeatureFlagBody,),
                    'clone':
                        (str,),
                },
                'attribute_map': {
                    'proj_key': 'projKey',
                    'clone': 'clone',
                },
                'location_map': {
                    'proj_key': 'path',
                    'feature_flag_body': 'body',
                    'clone': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__post_feature_flag
        )
