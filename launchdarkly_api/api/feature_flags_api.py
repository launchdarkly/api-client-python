# -*- coding: utf-8 -*-

"""
    LaunchDarkly REST API

    # Overview  ## Authentication  All REST API resources are authenticated with either [personal or service access tokens](https://docs.launchdarkly.com/home/account-security/api-access-tokens), or session cookies. Other authentication mechanisms are not supported. You can manage personal access tokens on your [**Account settings**](https://app.launchdarkly.com/settings/tokens) page.  LaunchDarkly also has SDK keys, mobile keys, and client-side IDs that are used by our server-side SDKs, mobile SDKs, and JavaScript-based SDKs, respectively. **These keys cannot be used to access our REST API**. These keys are environment-specific, and can only perform read-only operations such as fetching feature flag settings.  | Auth mechanism                                                                                  | Allowed resources                                                                                     | Use cases                                          | | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------- | | [Personal or service access tokens](https://docs.launchdarkly.com/home/account-security/api-access-tokens) | Can be customized on a per-token basis                                                                | Building scripts, custom integrations, data export. | | SDK keys                                                                                        | Can only access read-only resources specific to server-side SDKs. Restricted to a single environment. | Server-side SDKs                     | | Mobile keys                                                                                     | Can only access read-only resources specific to mobile SDKs, and only for flags marked available to mobile keys. Restricted to a single environment.           | Mobile SDKs                                        | | Client-side ID                                                                                  | Can only access read-only resources specific to JavaScript-based client-side SDKs, and only for flags marked available to client-side. Restricted to a single environment.           | Client-side JavaScript                             |  > #### Keep your access tokens and SDK keys private > > Access tokens should _never_ be exposed in untrusted contexts. Never put an access token in client-side JavaScript, or embed it in a mobile application. LaunchDarkly has special mobile keys that you can embed in mobile apps. If you accidentally expose an access token or SDK key, you can reset it from your [**Account settings**](https://app.launchdarkly.com/settings/tokens) page. > > The client-side ID is safe to embed in untrusted contexts. It's designed for use in client-side JavaScript.  ### Authentication using request header  The preferred way to authenticate with the API is by adding an `Authorization` header containing your access token to your requests. The value of the `Authorization` header must be your access token.  Manage personal access tokens from the [**Account settings**](https://app.launchdarkly.com/settings/tokens) page.  ### Authentication using session cookie  For testing purposes, you can make API calls directly from your web browser. If you are logged in to the LaunchDarkly application, the API will use your existing session to authenticate calls.  If you have a [role](https://docs.launchdarkly.com/home/team/built-in-roles) other than Admin, or have a [custom role](https://docs.launchdarkly.com/home/team/custom-roles) defined, you may not have permission to perform some API calls. You will receive a `401` response code in that case.  > ### Modifying the Origin header causes an error > > LaunchDarkly validates that the Origin header for any API request authenticated by a session cookie matches the expected Origin header. The expected Origin header is `https://app.launchdarkly.com`. > > If the Origin header does not match what's expected, LaunchDarkly returns an error. This error can prevent the LaunchDarkly app from working correctly. > > Any browser extension that intentionally changes the Origin header can cause this problem. For example, the `Allow-Control-Allow-Origin: *` Chrome extension changes the Origin header to `http://evil.com` and causes the app to fail. > > To prevent this error, do not modify your Origin header. > > LaunchDarkly does not require origin matching when authenticating with an access token, so this issue does not affect normal API usage.  ## Representations  All resources expect and return JSON response bodies. Error responses also send a JSON body. To learn more about the error format of the API, read [Errors](/#section/Overview/Errors).  In practice this means that you always get a response with a `Content-Type` header set to `application/json`.  In addition, request bodies for `PATCH`, `POST`, `PUT`, and `REPORT` requests must be encoded as JSON with a `Content-Type` header set to `application/json`.  ### Summary and detailed representations  When you fetch a list of resources, the response includes only the most important attributes of each resource. This is a _summary representation_ of the resource. When you fetch an individual resource, such as a single feature flag, you receive a _detailed representation_ of the resource.  The best way to find a detailed representation is to follow links. Every summary representation includes a link to its detailed representation.  ### Expanding responses  Sometimes the detailed representation of a resource does not include all of the attributes of the resource by default. If this is the case, the request method will clearly document this and describe which attributes you can include in an expanded response.  To include the additional attributes, append the `expand` request parameter to your request and add a comma-separated list of the attributes to include. For example, when you append `?expand=members,roles` to the [Get team](/tag/Teams#operation/getTeam) endpoint, the expanded response includes both of these attributes.  ### Links and addressability  The best way to navigate the API is by following links. These are attributes in representations that link to other resources. The API always uses the same format for links:  - Links to other resources within the API are encapsulated in a `_links` object - If the resource has a corresponding link to HTML content on the site, it is stored in a special `_site` link  Each link has two attributes:  - An `href`, which contains the URL - A `type`, which describes the content type  For example, a feature resource might return the following:  ```json {   \"_links\": {     \"parent\": {       \"href\": \"/api/features\",       \"type\": \"application/json\"     },     \"self\": {       \"href\": \"/api/features/sort.order\",       \"type\": \"application/json\"     }   },   \"_site\": {     \"href\": \"/features/sort.order\",     \"type\": \"text/html\"   } } ```  From this, you can navigate to the parent collection of features by following the `parent` link, or navigate to the site page for the feature by following the `_site` link.  Collections are always represented as a JSON object with an `items` attribute containing an array of representations. Like all other representations, collections have `_links` defined at the top level.  Paginated collections include `first`, `last`, `next`, and `prev` links containing a URL with the respective set of elements in the collection.  ## Updates  Resources that accept partial updates use the `PATCH` verb. Most resources support the [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) format. Some resources also support the [JSON merge patch](https://datatracker.ietf.org/doc/html/rfc7386) format, and some resources support the [semantic patch](/reference#updates-using-semantic-patch) format, which is a way to specify the modifications to perform as a set of executable instructions. Each resource supports optional [comments](/reference#updates-with-comments) that you can submit with updates. Comments appear in outgoing webhooks, the audit log, and other integrations.  When a resource supports both JSON patch and semantic patch, we document both in the request method. However, the specific request body fields and descriptions included in our documentation only match one type of patch or the other.  ### Updates using JSON patch  [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) is a way to specify the modifications to perform on a resource. JSON patch uses paths and a limited set of operations to describe how to transform the current state of the resource into a new state. JSON patch documents are always arrays, where each element contains an operation, a path to the field to update, and the new value.  For example, in this feature flag representation:  ```json {     \"name\": \"New recommendations engine\",     \"key\": \"engine.enable\",     \"description\": \"This is the description\",     ... } ``` You can change the feature flag's description with the following patch document:  ```json [{ \"op\": \"replace\", \"path\": \"/description\", \"value\": \"This is the new description\" }] ```  You can specify multiple modifications to perform in a single request. You can also test that certain preconditions are met before applying the patch:  ```json [   { \"op\": \"test\", \"path\": \"/version\", \"value\": 10 },   { \"op\": \"replace\", \"path\": \"/description\", \"value\": \"The new description\" } ] ```  The above patch request tests whether the feature flag's `version` is `10`, and if so, changes the feature flag's description.  Attributes that are not editable, such as a resource's `_links`, have names that start with an underscore.  ### Updates using JSON merge patch  [JSON merge patch](https://datatracker.ietf.org/doc/html/rfc7386) is another format for specifying the modifications to perform on a resource. JSON merge patch is less expressive than JSON patch. However, in many cases it is simpler to construct a merge patch document. For example, you can change a feature flag's description with the following merge patch document:  ```json {   \"description\": \"New flag description\" } ```  ### Updates using semantic patch  The API also supports the semantic patch format. A semantic patch is a way to specify the modifications to perform on a resource as a set of executable instructions.  Semantic patch allows you to be explicit about intent using precise, custom instructions. In many cases, you can define semantic patch instructions independently of the current state of the resource. This can be useful when defining a change that may be applied at a future date.  To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header.  Here's how:  ``` Content-Type: application/json; domain-model=launchdarkly.semanticpatch ```  If you call a semantic patch resource without this header, you will receive a `400` response because your semantic patch will be interpreted as a JSON patch.  The body of a semantic patch request takes the following properties:  * `comment` (string): (Optional) A description of the update. * `environmentKey` (string): (Required for some resources only) The environment key. * `instructions` (array): (Required) A list of actions the update should perform. Each action in the list must be an object with a `kind` property that indicates the instruction. If the instruction requires parameters, you must include those parameters as additional fields in the object. The documentation for each resource that supports semantic patch includes the available instructions and any additional parameters.  For example:  ```json {   \"comment\": \"optional comment\",   \"instructions\": [ {\"kind\": \"turnFlagOn\"} ] } ```  If any instruction in the patch encounters an error, the endpoint returns an error and will not change the resource. In general, each instruction silently does nothing if the resource is already in the state you request.  ### Updates with comments  You can submit optional comments with `PATCH` changes.  To submit a comment along with a JSON patch document, use the following format:  ```json {   \"comment\": \"This is a comment string\",   \"patch\": [{ \"op\": \"replace\", \"path\": \"/description\", \"value\": \"The new description\" }] } ```  To submit a comment along with a JSON merge patch document, use the following format:  ```json {   \"comment\": \"This is a comment string\",   \"merge\": { \"description\": \"New flag description\" } } ```  To submit a comment along with a semantic patch, use the following format:  ```json {   \"comment\": \"This is a comment string\",   \"instructions\": [ {\"kind\": \"turnFlagOn\"} ] } ```  ## Errors  The API always returns errors in a common format. Here's an example:  ```json {   \"code\": \"invalid_request\",   \"message\": \"A feature with that key already exists\",   \"id\": \"30ce6058-87da-11e4-b116-123b93f75cba\" } ```  The `code` indicates the general class of error. The `message` is a human-readable explanation of what went wrong. The `id` is a unique identifier. Use it when you're working with LaunchDarkly Support to debug a problem with a specific API call.  ### HTTP status error response codes  | Code | Definition        | Description                                                                                       | Possible Solution                                                | | ---- | ----------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | | 400  | Invalid request       | The request cannot be understood.                                    | Ensure JSON syntax in request body is correct.                   | | 401  | Invalid access token      | Requestor is unauthorized or does not have permission for this API call.                                                | Ensure your API access token is valid and has the appropriate permissions.                                     | | 403  | Forbidden         | Requestor does not have access to this resource.                                                | Ensure that the account member or access token has proper permissions set. | | 404  | Invalid resource identifier | The requested resource is not valid. | Ensure that the resource is correctly identified by id or key. | | 405  | Method not allowed | The request method is not allowed on this resource. | Ensure that the HTTP verb is correct. | | 409  | Conflict          | The API request can not be completed because it conflicts with a concurrent API request. | Retry your request.                                              | | 422  | Unprocessable entity | The API request can not be completed because the update description can not be understood. | Ensure that the request body is correct for the type of patch you are using, either JSON patch or semantic patch. | 429  | Too many requests | Read [Rate limiting](/#section/Overview/Rate-limiting).                                               | Wait and try again later.                                        |  ## CORS  The LaunchDarkly API supports Cross Origin Resource Sharing (CORS) for AJAX requests from any origin. If an `Origin` header is given in a request, it will be echoed as an explicitly allowed origin. Otherwise the request returns a wildcard, `Access-Control-Allow-Origin: *`. For more information on CORS, read the [CORS W3C Recommendation](http://www.w3.org/TR/cors). Example CORS headers might look like:  ```http Access-Control-Allow-Headers: Accept, Content-Type, Content-Length, Accept-Encoding, Authorization Access-Control-Allow-Methods: OPTIONS, GET, DELETE, PATCH Access-Control-Allow-Origin: * Access-Control-Max-Age: 300 ```  You can make authenticated CORS calls just as you would make same-origin calls, using either [token or session-based authentication](/#section/Overview/Authentication). If you are using session authentication, you should set the `withCredentials` property for your `xhr` request to `true`. You should never expose your access tokens to untrusted users.  ## Rate limiting  We use several rate limiting strategies to ensure the availability of our APIs. Rate-limited calls to our APIs return a `429` status code. Calls to our APIs include headers indicating the current rate limit status. The specific headers returned depend on the API route being called. The limits differ based on the route, authentication mechanism, and other factors. Routes that are not rate limited may not contain any of the headers described below.  > ### Rate limiting and SDKs > > LaunchDarkly SDKs are never rate limited and do not use the API endpoints defined here. LaunchDarkly uses a different set of approaches, including streaming/server-sent events and a global CDN, to ensure availability to the routes used by LaunchDarkly SDKs.  ### Global rate limits  Authenticated requests are subject to a global limit. This is the maximum number of calls that your account can make to the API per ten seconds. All personal access tokens on the account share this limit, so exceeding the limit with one access token will impact other tokens. Calls that are subject to global rate limits return the headers below:  | Header name                    | Description                                                                      | | ------------------------------ | -------------------------------------------------------------------------------- | | `X-Ratelimit-Global-Remaining` | The maximum number of requests the account is permitted to make per ten seconds. | | `X-Ratelimit-Reset`            | The time at which the current rate limit window resets in epoch milliseconds.    |  We do not publicly document the specific number of calls that can be made globally. This limit may change, and we encourage clients to program against the specification, relying on the two headers defined above, rather than hardcoding to the current limit.  ### Route-level rate limits  Some authenticated routes have custom rate limits. These also reset every ten seconds. Any access tokens hitting the same route share this limit, so exceeding the limit with one access token may impact other tokens. Calls that are subject to route-level rate limits return the headers below:  | Header name                   | Description                                                                                           | | ----------------------------- | ----------------------------------------------------------------------------------------------------- | | `X-Ratelimit-Route-Remaining` | The maximum number of requests to the current route the account is permitted to make per ten seconds. | | `X-Ratelimit-Reset`           | The time at which the current rate limit window resets in epoch milliseconds.                         |  A _route_ represents a specific URL pattern and verb. For example, the [Delete environment](/tag/Environments#operation/deleteEnvironment) endpoint is considered a single route, and each call to delete an environment counts against your route-level rate limit for that route.  We do not publicly document the specific number of calls that an account can make to each endpoint per ten seconds. These limits may change, and we encourage clients to program against the specification, relying on the two headers defined above, rather than hardcoding to the current limits.  ### IP-based rate limiting  We also employ IP-based rate limiting on some API routes. If you hit an IP-based rate limit, your API response will include a `Retry-After` header indicating how long to wait before re-trying the call. Clients must wait at least `Retry-After` seconds before making additional calls to our API, and should employ jitter and backoff strategies to avoid triggering rate limits again.  ## OpenAPI (Swagger) and client libraries  We have a [complete OpenAPI (Swagger) specification](https://app.launchdarkly.com/api/v2/openapi.json) for our API.  We auto-generate multiple client libraries based on our OpenAPI specification. To learn more, visit the [collection of client libraries on GitHub](https://github.com/search?q=topic%3Alaunchdarkly-api+org%3Alaunchdarkly&type=Repositories). You can also use this specification to generate client libraries to interact with our REST API in your language of choice.  Our OpenAPI specification is supported by several API-based tools such as Postman and Insomnia. In many cases, you can directly import our specification to explore our APIs.  ## Method overriding  Some firewalls and HTTP clients restrict the use of verbs other than `GET` and `POST`. In those environments, our API endpoints that use `DELETE`, `PATCH`, and `PUT` verbs are inaccessible.  To avoid this issue, our API supports the `X-HTTP-Method-Override` header, allowing clients to \"tunnel\" `DELETE`, `PATCH`, and `PUT` requests using a `POST` request.  For example, to call a `PATCH` endpoint using a `POST` request, you can include `X-HTTP-Method-Override:PATCH` as a header.  ## Beta resources  We sometimes release new API resources in **beta** status before we release them with general availability.  Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.  We try to promote resources into general availability as quickly as possible. This happens after sufficient testing and when we're satisfied that we no longer need to make backwards-incompatible changes.  We mark beta resources with a \"Beta\" callout in our documentation, pictured below:  > ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](/#section/Overview/Beta-resources). > > Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.  ### Using beta resources  To use a beta resource, you must include a header in the request. If you call a beta resource without this header, you receive a `403` response.  Use this header:  ``` LD-API-Version: beta ```  ## Versioning  We try hard to keep our REST API backwards compatible, but we occasionally have to make backwards-incompatible changes in the process of shipping new features. These breaking changes can cause unexpected behavior if you don't prepare for them accordingly.  Updates to our REST API include support for the latest features in LaunchDarkly. We also release a new version of our REST API every time we make a breaking change. We provide simultaneous support for multiple API versions so you can migrate from your current API version to a new version at your own pace.  ### Setting the API version per request  You can set the API version on a specific request by sending an `LD-API-Version` header, as shown in the example below:  ``` LD-API-Version: 20220603 ```  The header value is the version number of the API version you would like to request. The number for each version corresponds to the date the version was released in `yyyymmdd` format. In the example above the version `20220603` corresponds to June 03, 2022.  ### Setting the API version per access token  When you create an access token, you must specify a specific version of the API to use. This ensures that integrations using this token cannot be broken by version changes.  Tokens created before versioning was released have their version set to `20160426`, which is the version of the API that existed before the current versioning scheme, so that they continue working the same way they did before versioning.  If you would like to upgrade your integration to use a new API version, you can explicitly set the header described above.  > ### Best practice: Set the header for every client or integration > > We recommend that you set the API version header explicitly in any client or integration you build. > > Only rely on the access token API version during manual testing.  ### API version changelog  |<div style=\"width:75px\">Version</div> | Changes | End of life (EOL) |---|---|---| | `20220603` | <ul><li>Changed the [list projects](/tag/Projects#operation/getProjects) return value:<ul><li>Response is now paginated with a default limit of `20`.</li><li>Added support for filter and sort.</li><li>The project `environments` field is now expandable. This field is omitted by default.</li></ul></li><li>Changed the [get project](/tag/Projects#operation/getProject) return value:<ul><li>The `environments` field is now expandable. This field is omitted by default.</li></ul></li></ul> | Current | | `20210729` | <ul><li>Changed the [create approval request](/tag/Approvals#operation/postApprovalRequest) return value. It now returns HTTP Status Code `201` instead of `200`.</li><li> Changed the [get users](/tag/Users#operation/getUser) return value. It now returns a user record, not a user. </li><li>Added additional optional fields to environment, segments, flags, members, and segments, including the ability to create Big Segments. </li><li> Added default values for flag variations when new environments are created. </li><li>Added filtering and pagination for getting flags and members, including `limit`, `number`, `filter`, and `sort` query parameters. </li><li>Added endpoints for expiring user targets for flags and segments, scheduled changes, access tokens, Relay Proxy configuration, integrations and subscriptions, and approvals. </li></ul> | 2023-06-03 | | `20191212` | <ul><li>[List feature flags](/tag/Feature-flags#operation/getFeatureFlags) now defaults to sending summaries of feature flag configurations, equivalent to setting the query parameter `summary=true`. Summaries omit flag targeting rules and individual user targets from the payload. </li><li> Added endpoints for flags, flag status, projects, environments, users, audit logs, members, users, custom roles, segments, usage, streams, events, and data export. </li></ul> | 2022-07-29 | | `20160426` | <ul><li>Initial versioning of API. Tokens created before versioning have their version set to this.</li></ul> | 2020-12-12 |   # noqa: E501

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
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.patch_flags_request import PatchFlagsRequest
from launchdarkly_api.model.patch_with_comment import PatchWithComment
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.status_conflict_error_rep import StatusConflictErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep


class FeatureFlagsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.copy_feature_flag_endpoint = _Endpoint(
            settings={
                'response_type': (FeatureFlag,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projectKey}/{featureFlagKey}/copy',
                'operation_id': 'copy_feature_flag',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_key',
                    'feature_flag_key',
                    'flag_copy_config_post',
                ],
                'required': [
                    'project_key',
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
                    'project_key':
                        (str,),
                    'feature_flag_key':
                        (str,),
                    'flag_copy_config_post':
                        (FlagCopyConfigPost,),
                },
                'attribute_map': {
                    'project_key': 'projectKey',
                    'feature_flag_key': 'featureFlagKey',
                },
                'location_map': {
                    'project_key': 'path',
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
            api_client=api_client
        )
        self.delete_feature_flag_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projectKey}/{featureFlagKey}',
                'operation_id': 'delete_feature_flag',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_key',
                    'feature_flag_key',
                ],
                'required': [
                    'project_key',
                    'feature_flag_key',
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
                    'project_key':
                        (str,),
                    'feature_flag_key':
                        (str,),
                },
                'attribute_map': {
                    'project_key': 'projectKey',
                    'feature_flag_key': 'featureFlagKey',
                },
                'location_map': {
                    'project_key': 'path',
                    'feature_flag_key': 'path',
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
            api_client=api_client
        )
        self.get_expiring_user_targets_endpoint = _Endpoint(
            settings={
                'response_type': (ExpiringUserTargetGetResponse,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projectKey}/{featureFlagKey}/expiring-user-targets/{environmentKey}',
                'operation_id': 'get_expiring_user_targets',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_key',
                    'environment_key',
                    'feature_flag_key',
                ],
                'required': [
                    'project_key',
                    'environment_key',
                    'feature_flag_key',
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
                    'project_key':
                        (str,),
                    'environment_key':
                        (str,),
                    'feature_flag_key':
                        (str,),
                },
                'attribute_map': {
                    'project_key': 'projectKey',
                    'environment_key': 'environmentKey',
                    'feature_flag_key': 'featureFlagKey',
                },
                'location_map': {
                    'project_key': 'path',
                    'environment_key': 'path',
                    'feature_flag_key': 'path',
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
            api_client=api_client
        )
        self.get_feature_flag_endpoint = _Endpoint(
            settings={
                'response_type': (FeatureFlag,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projectKey}/{featureFlagKey}',
                'operation_id': 'get_feature_flag',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_key',
                    'feature_flag_key',
                    'env',
                ],
                'required': [
                    'project_key',
                    'feature_flag_key',
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
                    'project_key':
                        (str,),
                    'feature_flag_key':
                        (str,),
                    'env':
                        (str,),
                },
                'attribute_map': {
                    'project_key': 'projectKey',
                    'feature_flag_key': 'featureFlagKey',
                    'env': 'env',
                },
                'location_map': {
                    'project_key': 'path',
                    'feature_flag_key': 'path',
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
            api_client=api_client
        )
        self.get_feature_flag_status_endpoint = _Endpoint(
            settings={
                'response_type': (FlagStatusRep,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flag-statuses/{projectKey}/{environmentKey}/{featureFlagKey}',
                'operation_id': 'get_feature_flag_status',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_key',
                    'environment_key',
                    'feature_flag_key',
                ],
                'required': [
                    'project_key',
                    'environment_key',
                    'feature_flag_key',
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
                    'project_key':
                        (str,),
                    'environment_key':
                        (str,),
                    'feature_flag_key':
                        (str,),
                },
                'attribute_map': {
                    'project_key': 'projectKey',
                    'environment_key': 'environmentKey',
                    'feature_flag_key': 'featureFlagKey',
                },
                'location_map': {
                    'project_key': 'path',
                    'environment_key': 'path',
                    'feature_flag_key': 'path',
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
            api_client=api_client
        )
        self.get_feature_flag_status_across_environments_endpoint = _Endpoint(
            settings={
                'response_type': (FeatureFlagStatusAcrossEnvironments,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flag-status/{projectKey}/{featureFlagKey}',
                'operation_id': 'get_feature_flag_status_across_environments',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_key',
                    'feature_flag_key',
                    'env',
                ],
                'required': [
                    'project_key',
                    'feature_flag_key',
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
                    'project_key':
                        (str,),
                    'feature_flag_key':
                        (str,),
                    'env':
                        (str,),
                },
                'attribute_map': {
                    'project_key': 'projectKey',
                    'feature_flag_key': 'featureFlagKey',
                    'env': 'env',
                },
                'location_map': {
                    'project_key': 'path',
                    'feature_flag_key': 'path',
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
            api_client=api_client
        )
        self.get_feature_flag_statuses_endpoint = _Endpoint(
            settings={
                'response_type': (FeatureFlagStatuses,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flag-statuses/{projectKey}/{environmentKey}',
                'operation_id': 'get_feature_flag_statuses',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_key',
                    'environment_key',
                ],
                'required': [
                    'project_key',
                    'environment_key',
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
                    'project_key':
                        (str,),
                    'environment_key':
                        (str,),
                },
                'attribute_map': {
                    'project_key': 'projectKey',
                    'environment_key': 'environmentKey',
                },
                'location_map': {
                    'project_key': 'path',
                    'environment_key': 'path',
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
            api_client=api_client
        )
        self.get_feature_flags_endpoint = _Endpoint(
            settings={
                'response_type': (FeatureFlags,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projectKey}',
                'operation_id': 'get_feature_flags',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_key',
                    'env',
                    'tag',
                    'limit',
                    'offset',
                    'archived',
                    'summary',
                    'filter',
                    'sort',
                    'compare',
                ],
                'required': [
                    'project_key',
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
                    'project_key':
                        (str,),
                    'env':
                        (str,),
                    'tag':
                        (str,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                    'archived':
                        (bool,),
                    'summary':
                        (bool,),
                    'filter':
                        (str,),
                    'sort':
                        (str,),
                    'compare':
                        (bool,),
                },
                'attribute_map': {
                    'project_key': 'projectKey',
                    'env': 'env',
                    'tag': 'tag',
                    'limit': 'limit',
                    'offset': 'offset',
                    'archived': 'archived',
                    'summary': 'summary',
                    'filter': 'filter',
                    'sort': 'sort',
                    'compare': 'compare',
                },
                'location_map': {
                    'project_key': 'path',
                    'env': 'query',
                    'tag': 'query',
                    'limit': 'query',
                    'offset': 'query',
                    'archived': 'query',
                    'summary': 'query',
                    'filter': 'query',
                    'sort': 'query',
                    'compare': 'query',
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
            api_client=api_client
        )
        self.patch_expiring_user_targets_endpoint = _Endpoint(
            settings={
                'response_type': (ExpiringUserTargetPatchResponse,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projectKey}/{featureFlagKey}/expiring-user-targets/{environmentKey}',
                'operation_id': 'patch_expiring_user_targets',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_key',
                    'environment_key',
                    'feature_flag_key',
                    'patch_flags_request',
                ],
                'required': [
                    'project_key',
                    'environment_key',
                    'feature_flag_key',
                    'patch_flags_request',
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
                    'project_key':
                        (str,),
                    'environment_key':
                        (str,),
                    'feature_flag_key':
                        (str,),
                    'patch_flags_request':
                        (PatchFlagsRequest,),
                },
                'attribute_map': {
                    'project_key': 'projectKey',
                    'environment_key': 'environmentKey',
                    'feature_flag_key': 'featureFlagKey',
                },
                'location_map': {
                    'project_key': 'path',
                    'environment_key': 'path',
                    'feature_flag_key': 'path',
                    'patch_flags_request': 'body',
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
            api_client=api_client
        )
        self.patch_feature_flag_endpoint = _Endpoint(
            settings={
                'response_type': (FeatureFlag,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projectKey}/{featureFlagKey}',
                'operation_id': 'patch_feature_flag',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_key',
                    'feature_flag_key',
                    'patch_with_comment',
                ],
                'required': [
                    'project_key',
                    'feature_flag_key',
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
                    'project_key':
                        (str,),
                    'feature_flag_key':
                        (str,),
                    'patch_with_comment':
                        (PatchWithComment,),
                },
                'attribute_map': {
                    'project_key': 'projectKey',
                    'feature_flag_key': 'featureFlagKey',
                },
                'location_map': {
                    'project_key': 'path',
                    'feature_flag_key': 'path',
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
            api_client=api_client
        )
        self.post_feature_flag_endpoint = _Endpoint(
            settings={
                'response_type': (FeatureFlag,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/api/v2/flags/{projectKey}',
                'operation_id': 'post_feature_flag',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_key',
                    'feature_flag_body',
                    'clone',
                ],
                'required': [
                    'project_key',
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
                    'project_key':
                        (str,),
                    'feature_flag_body':
                        (FeatureFlagBody,),
                    'clone':
                        (str,),
                },
                'attribute_map': {
                    'project_key': 'projectKey',
                    'clone': 'clone',
                },
                'location_map': {
                    'project_key': 'path',
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
            api_client=api_client
        )

    def copy_feature_flag(
        self,
        project_key,
        feature_flag_key,
        flag_copy_config_post,
        **kwargs
    ):
        """Copy feature flag  # noqa: E501

         > ### Copying flag settings is an Enterprise feature > > Copying flag settings is available to customers on an Enterprise plan. To learn more, [read about our pricing](https://launchdarkly.com/pricing/). To upgrade your plan, [contact Sales](https://launchdarkly.com/contact-sales/).  Copy flag settings from a source environment to a target environment.  By default, this operation copies the entire flag configuration. You can use the `includedActions` or `excludedActions` to specify that only part of the flag configuration is copied.  If you provide the optional `currentVersion` of a flag, this operation tests to ensure that the current flag version in the environment matches the version you've specified. The operation rejects attempts to copy flag settings if the environment's current version  of the flag does not match the version you've specified. You can use this to enforce optimistic locking on copy attempts.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.copy_feature_flag(project_key, feature_flag_key, flag_copy_config_post, async_req=True)
        >>> result = thread.get()

        Args:
            project_key (str): The project key
            feature_flag_key (str): The feature flag key. The key identifies the flag in your code.
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_key'] = \
            project_key
        kwargs['feature_flag_key'] = \
            feature_flag_key
        kwargs['flag_copy_config_post'] = \
            flag_copy_config_post
        return self.copy_feature_flag_endpoint.call_with_http_info(**kwargs)

    def delete_feature_flag(
        self,
        project_key,
        feature_flag_key,
        **kwargs
    ):
        """Delete feature flag  # noqa: E501

        Delete a feature flag in all environments. Use with caution: only delete feature flags your application no longer uses.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_feature_flag(project_key, feature_flag_key, async_req=True)
        >>> result = thread.get()

        Args:
            project_key (str): The project key
            feature_flag_key (str): The feature flag key. The key identifies the flag in your code.

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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_key'] = \
            project_key
        kwargs['feature_flag_key'] = \
            feature_flag_key
        return self.delete_feature_flag_endpoint.call_with_http_info(**kwargs)

    def get_expiring_user_targets(
        self,
        project_key,
        environment_key,
        feature_flag_key,
        **kwargs
    ):
        """Get expiring user targets for feature flag  # noqa: E501

        Get a list of user targets on a feature flag that are scheduled for removal.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_expiring_user_targets(project_key, environment_key, feature_flag_key, async_req=True)
        >>> result = thread.get()

        Args:
            project_key (str): The project key
            environment_key (str): The environment key
            feature_flag_key (str): The feature flag key

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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_key'] = \
            project_key
        kwargs['environment_key'] = \
            environment_key
        kwargs['feature_flag_key'] = \
            feature_flag_key
        return self.get_expiring_user_targets_endpoint.call_with_http_info(**kwargs)

    def get_feature_flag(
        self,
        project_key,
        feature_flag_key,
        **kwargs
    ):
        """Get feature flag  # noqa: E501

        Get a single feature flag by key. By default, this returns the configurations for all environments. You can filter environments with the `env` query parameter. For example, setting `env=production` restricts the returned configurations to just the `production` environment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_feature_flag(project_key, feature_flag_key, async_req=True)
        >>> result = thread.get()

        Args:
            project_key (str): The project key
            feature_flag_key (str): The feature flag key

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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_key'] = \
            project_key
        kwargs['feature_flag_key'] = \
            feature_flag_key
        return self.get_feature_flag_endpoint.call_with_http_info(**kwargs)

    def get_feature_flag_status(
        self,
        project_key,
        environment_key,
        feature_flag_key,
        **kwargs
    ):
        """Get feature flag status  # noqa: E501

        Get the status for a particular feature flag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_feature_flag_status(project_key, environment_key, feature_flag_key, async_req=True)
        >>> result = thread.get()

        Args:
            project_key (str): The project key
            environment_key (str): The environment key
            feature_flag_key (str): The feature flag key

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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_key'] = \
            project_key
        kwargs['environment_key'] = \
            environment_key
        kwargs['feature_flag_key'] = \
            feature_flag_key
        return self.get_feature_flag_status_endpoint.call_with_http_info(**kwargs)

    def get_feature_flag_status_across_environments(
        self,
        project_key,
        feature_flag_key,
        **kwargs
    ):
        """Get flag status across environments  # noqa: E501

        Get the status for a particular feature flag across environments.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_feature_flag_status_across_environments(project_key, feature_flag_key, async_req=True)
        >>> result = thread.get()

        Args:
            project_key (str): The project key
            feature_flag_key (str): The feature flag key

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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_key'] = \
            project_key
        kwargs['feature_flag_key'] = \
            feature_flag_key
        return self.get_feature_flag_status_across_environments_endpoint.call_with_http_info(**kwargs)

    def get_feature_flag_statuses(
        self,
        project_key,
        environment_key,
        **kwargs
    ):
        """List feature flag statuses  # noqa: E501

        Get a list of statuses for all feature flags. The status includes the last time the feature flag was requested, as well as a state, which is one of the following:  - `new`: the feature flag was created within the last seven days, and has not been requested yet - `active`: the feature flag was requested by your servers or clients within the last seven days - `inactive`: the feature flag was created more than seven days ago, and hasn't been requested by your servers or clients within the past seven days - `launched`: one variation of the feature flag has been rolled out to all your users for at least 7 days   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_feature_flag_statuses(project_key, environment_key, async_req=True)
        >>> result = thread.get()

        Args:
            project_key (str): The project key
            environment_key (str): The environment key

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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_key'] = \
            project_key
        kwargs['environment_key'] = \
            environment_key
        return self.get_feature_flag_statuses_endpoint.call_with_http_info(**kwargs)

    def get_feature_flags(
        self,
        project_key,
        **kwargs
    ):
        """List feature flags  # noqa: E501

        Get a list of all features in the given project. By default, each feature includes configurations for each environment. You can filter environments with the `env` query parameter. For example, setting `env=production` restricts the returned configurations to just your production environment. You can also filter feature flags by tag with the tag query parameter.  ### Filtering flags  You can filter on certain fields using the `filter` query parameter. For example, setting `filter=query:dark-mode,tags:beta+test` matches flags with the string `dark-mode` in their key or name, ignoring case, which also have the tags `beta` and `test`.  The `filter` query parameter supports the following arguments:  - `query` is a string that matches against the flags' keys and names. It is not case sensitive. - `archived` is a boolean with values of `true` or `false` that filters the list to archived flags. Setting the value to `true` returns only archived flags. When this is absent, only unarchived flags are returned. - `type` is a string allowing filtering to `temporary` or `permanent` flags. - `status` is a string allowing filtering to `new`, `inactive`, `active`, or `launched` flags in the specified environment. This filter also requires a `filterEnv` field to be set to a valid environment. For example: `filter=status:active,filterEnv:production`. - `tags` is a `+` separated list of tags. It filters the list to members who have all of the tags in the list. For example: `filter=tags:beta+test`. - `hasExperiment` is a boolean with values of `true` or `false` that returns any flags that are used in an experiment. - `hasDataExport` is a boolean with values of `true` or `false` that returns any flags that are exporting data in the specified environment. This includes flags that are exporting data from Experimentation. This filter also requires that you set a `filterEnv` field to a valid environment key. For example: `filter=hasDataExport:true,filterEnv:production` - `evaluated` is an object that contains a key of `after` and a value in Unix time in milliseconds. This returns all flags that have been evaluated since the time you specify in the environment provided. This filter also requires you to set a `filterEnv` field to a valid environment. For example: `filter=evaluated:{\"after\": 1590768455282},filterEnv:production`. - `filterEnv` is a string with the key of a valid environment. You can use the `filterEnv` field for filters that are environment-specific. If there are multiple environment-specific filters, you should only declare this parameter once. For example: `filter=evaluated:{\"after\": 1590768455282},filterEnv:production,status:active`.  By default, this returns all flags. You can page through the list with the `limit` parameter and by following the `first`, `prev`, `next`, and `last` links in the returned `_links` field. These links will not be present if the pages they refer to don't exist. For example, the `first` and `prev` links will be missing from the response on the first page.  ### Sorting flags  You can sort flags based on the following fields:  - `creationDate` sorts by the creation date of the flag. - `key` sorts by the key of the flag. - `maintainerId` sorts by the flag maintainer. - `name` sorts by flag name. - `tags` sorts by tags. - `targetingModifiedDate` sorts by the date that the flag's targeting rules were last modified in a given environment. It must be used with `env` parameter and it can not be combined with any other sort. If multiple `env` values are provided, it will perform sort using the first one. For example, `sort=-targetingModifiedDate&env=production&env=staging` returns results sorted by `targetingModifiedDate` for the `production` environment. - `type` sorts by flag type  All fields are sorted in ascending order by default. To sort in descending order, prefix the field with a dash ( - ). For example, `sort=-name` sorts the response by flag name in descending order.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_feature_flags(project_key, async_req=True)
        >>> result = thread.get()

        Args:
            project_key (str): The project key

        Keyword Args:
            env (str): Filter configurations by environment. [optional]
            tag (str): Filter feature flags by tag. [optional]
            limit (int): The number of feature flags to return. Defaults to -1, which returns all flags. [optional]
            offset (int): Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`.. [optional]
            archived (bool): A boolean to filter the list to archived flags. When this is absent, only unarchived flags will be returned. [optional]
            summary (bool): By default in API version >= 1, flags will _not_ include their list of prerequisites, targets or rules.  Set summary=0 to include these fields for each flag returned. [optional]
            filter (str): A comma-separated list of filters. Each filter is of the form field:value. Read the endpoint description for a full list of available filter fields.. [optional]
            sort (str): A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order. Read the endpoint description for a full list of available sort fields.. [optional]
            compare (bool): A boolean to filter results by only flags that have differences between environments. [optional]
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_key'] = \
            project_key
        return self.get_feature_flags_endpoint.call_with_http_info(**kwargs)

    def patch_expiring_user_targets(
        self,
        project_key,
        environment_key,
        feature_flag_key,
        patch_flags_request,
        **kwargs
    ):
        """Update expiring user targets on feature flag  # noqa: E501

        Schedule a user for removal from individual targeting on a feature flag. The flag must already individually target the user.  You can add, update, or remove a scheduled removal date. You can only schedule a user for removal on a single variation per flag.  This request only supports semantic patches. To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](/reference#updates-using-semantic-patch).  ### Instructions  #### addExpireUserTargetDate  Adds a date and time that LaunchDarkly will remove the user from the flag's individual targeting.  ##### Parameters  * `value`: The time, in Unix milliseconds, when LaunchDarkly should remove the user from individual targeting for this flag * `variationId`: The version of the flag variation to update. You can retrieve this by making a GET request for the flag. * `userKey`: The user key for the user to remove from individual targeting  #### updateExpireUserTargetDate  Updates the date and time that LaunchDarkly will remove the user from the flag's individual targeting.  ##### Parameters  * `value`: The time, in Unix milliseconds, when LaunchDarkly should remove the user from individual targeting for this flag * `variationId`: The version of the flag variation to update. You can retrieve this by making a GET request for the flag. * `userKey`: The user key for the user to remove from individual targeting  #### removeExpireUserTargetDate  Removes the scheduled removal of the user from the flag's individual targeting. The user will remain part of the flag's individual targeting until you explicitly remove them, or until you schedule another removal.  ##### Parameters  * `variationId`: The version of the flag variation to update. You can retrieve this by making a GET request for the flag. * `userKey`: The user key for the user to remove from individual targeting   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_expiring_user_targets(project_key, environment_key, feature_flag_key, patch_flags_request, async_req=True)
        >>> result = thread.get()

        Args:
            project_key (str): The project key
            environment_key (str): The environment key
            feature_flag_key (str): The feature flag key
            patch_flags_request (PatchFlagsRequest):

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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_key'] = \
            project_key
        kwargs['environment_key'] = \
            environment_key
        kwargs['feature_flag_key'] = \
            feature_flag_key
        kwargs['patch_flags_request'] = \
            patch_flags_request
        return self.patch_expiring_user_targets_endpoint.call_with_http_info(**kwargs)

    def patch_feature_flag(
        self,
        project_key,
        feature_flag_key,
        patch_with_comment,
        **kwargs
    ):
        """Update feature flag  # noqa: E501

        Perform a partial update to a feature flag. The request body must be a valid semantic patch or JSON patch.  ### Using semantic patches on a feature flag  To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](/reference#updates-using-semantic-patch).  The body of a semantic patch request for updating feature flags requires an `environmentKey` in addition to `instructions` and an optional `comment`. The body of the request takes the following properties:  * `comment` (string): (Optional) A description of the update. * `environmentKey` (string): (Required) The key of the LaunchDarkly environment. * `instructions` (array): (Required) A list of actions the update should perform. Each action in the list must be an object with a `kind` property that indicates the instruction. If the action requires parameters, you must include those parameters as additional fields in the object.  ### Instructions  Semantic patch requests support the following `kind` instructions for updating feature flags.  <details> <summary>Click to expand instructions for turning flags on and off</summary>  #### turnFlagOff  Sets the flag's targeting state to **Off**.  For example, to turn a flag off, use this request body:  ```json {   \"environmentKey\": \"example-environment-key\",   \"instructions\": [ { \"kind\": \"turnFlagOff\" } ] } ```  #### turnFlagOn  Sets the flag's targeting state to **On**.  For example, to turn a flag on, use this request body:  ```json {   \"environmentKey\": \"example-environment-key\",   \"instructions\": [ { \"kind\": \"turnFlagOn\" } ] } ```  </details><br />  <details> <summary>Click to expand instructions for working with targeting and variations</summary>  #### addClauses  Adds the given clauses to the rule indicated by `ruleId`.  ##### Parameters  - `ruleId`: ID of a rule in the flag. - `clauses`: Array of clause objects, with `attribute` (string), `op` (string), `negate` (boolean), and `values` (array of strings, numbers, or dates) properties.  #### addPrerequisite  Adds the flag indicated by `key` with variation `variationId` as a prerequisite to the flag in the path parameter.  ##### Parameters  - `key`: Flag key of the prerequisite flag. - `variationId`: ID of a variation of the prerequisite flag.  #### addRule  Adds a new targeting rule to the flag. The rule may contain `clauses` and serve the variation that `variationId` indicates, or serve a percentage rollout that `rolloutWeights` and `rolloutBucketBy` indicate.  If you set `beforeRuleId`, this adds the new rule before the indicated rule. Otherwise, adds the new rule to the end of the list.  ##### Parameters  - `clauses`: Array of clause objects, with `attribute` (string), `op` (string), `negate` (boolean), and `values` (array of strings, numbers, or dates) properties. - `beforeRuleId`: (Optional) ID of a flag rule. - `variationId`: ID of a variation of the flag. - `rolloutWeights`: Map of `variationId` to weight, in thousandths of a percent (0-100000). - `rolloutBucketBy`: (Optional) User attribute.  #### addUserTargets  Adds user keys to the individual user targets for the variation that `variationId` specifies. Returns an error if this causes the flag to target the same user key in multiple variations.  ##### Parameters  - `values`: List of user keys. - `variationId`: ID of a variation on the flag.  #### addValuesToClause  Adds `values` to the values of the clause that `ruleId` and `clauseId` indicate.  ##### Parameters  - `ruleId`: ID of a rule in the flag. - `clauseId`: ID of a clause in that rule. - `values`: Array of strings.  #### clearUserTargets  Removes all individual user targets from the variation that `variationId` specifies.  ##### Parameters  - `variationId`: ID of a variation on the flag.  #### removeClauses  Removes the clauses specified by `clauseIds` from the rule indicated by `ruleId`.  ##### Parameters  - `ruleId`: ID of a rule in the flag. - `clauseIds`: Array of IDs of clauses in the rule.  #### removePrerequisite  Removes the prerequisite flag indicated by `key`. Does nothing if this prerequisite does not exist.  ##### Parameters  - `key`: Flag key of an existing prerequisite flag.  #### removeRule  Removes the targeting rule specified by `ruleId`. Does nothing if the rule does not exist.  ##### Parameters  - `ruleId`: ID of a rule in the flag.  #### removeUserTargets  Removes user keys from the individual user targets for the variation that `variationId` specifies. Does nothing if the flag does not target the user keys.  ##### Parameters  - `values`: List of user keys. - `variationId`: ID of a flag variation.  #### removeValuesFromClause  Removes `values` from the values of the clause indicated by `ruleId` and `clauseId`.  ##### Parameters  - `ruleId`: ID of a rule in the flag. - `clauseId`: ID of a clause in that rule. - `values`: Array of strings.  #### reorderRules  Rearranges the rules to match the order given in `ruleIds`. Returns an error if `ruleIds` does not match the current set of rules on the flag.  ##### Parameters  - `ruleIds`: Array of IDs of all rules in the flag.  #### replacePrerequisites  Removes all existing prerequisites and replaces them with the list you provide.  ##### Parameters  - `prerequisites`: A list of prerequisites. Each item in the list must include a flag `key` and `variationId`.  For example, to replace prerequisites, use this request body:  ```json {   \"environmentKey\": \"example-environment-key\",   \"instructions\": [     {       \"kind\": \"replacePrerequisites\",       \"prerequisites\": [         {           \"key\": \"prereq-flag-key\",           \"variationId\": \"variation-1\"         },         {           \"key\": \"another-prereq-flag-key\",           \"variationId\": \"variation-2\"         }       ]     }   ] } ```  #### replaceRules  Removes all targeting rules for the flag and replaces them with the list you provide.  ##### Parameters  - `rules`: A list of rules.  For example, to replace rules, use this request body:  ```json {   \"environmentKey\": \"example-environment-key\",   \"instructions\": [     {       \"kind\": \"replaceRules\",       \"rules\": [         {           \"variationId\": \"variation-1\",           \"description\": \"myRule\",           \"clauses\": [             {               \"attribute\": \"segmentMatch\",               \"op\": \"segmentMatch\",               \"values\": [\"test\"]             }           ],           \"trackEvents\": true         }       ]     }   ] } ```  #### replaceUserTargets  Removes all existing user targeting and replaces it with the list of targets you provide.  ##### Parameters  - `targets`: A list of user targeting. Each item in the list must include a `variationId` and a list of `values`.  For example, to replace user targets, use this request body:  ```json {   \"environmentKey\": \"example-environment-key\",   \"instructions\": [     {       \"kind\": \"replaceUserTargets\",       \"targets\": [         {           \"variationId\": \"variation-1\",           \"values\": [\"blah\", \"foo\", \"bar\"]         },         {           \"variationId\": \"variation-2\",           \"values\": [\"abc\", \"def\"]         }       ]     }       ] } ```  #### updateClause  Replaces the clause indicated by `ruleId` and `clauseId` with `clause`.  ##### Parameters  - `ruleId`: ID of a rule in the flag. - `clauseId`: ID of a clause in that rule. - `clause`: New `clause` object, with `attribute` (string), `op` (string), `negate` (boolean), and `values` (array of strings, numbers, or dates) properties.  #### updateFallthroughVariationOrRollout  Updates the default or \"fallthrough\" rule for the flag, which the flag serves when a user matches none of the targeting rules. The rule can serve either the variation that `variationId` indicates, or a percent rollout that `rolloutWeights` and `rolloutBucketBy` indicate.  ##### Parameters  - `variationId`: ID of a variation of the flag. or - `rolloutWeights`: Map of `variationId` to weight, in thousandths of a percent (0-100000). - `rolloutBucketBy`: Optional user attribute.  #### updateOffVariation  Updates the default off variation to `variationId`. The flag serves the default off variation when the flag's targeting is **Off**.  ##### Parameters  - `variationId`: ID of a variation of the flag.  #### updatePrerequisite  Changes the prerequisite flag that `key` indicates to use the variation that `variationId` indicates. Returns an error if this prerequisite does not exist.  ##### Parameters  - `key`: Flag key of an existing prerequisite flag. - `variationId`: ID of a variation of the prerequisite flag.  #### updateRuleDescription  Updates the description of the feature flag rule.  ##### Parameters  - `description`: The new human-readable description for this rule. - `ruleId`: The ID of the rule. You can retrieve this by making a GET request for the flag.  #### updateRuleTrackEvents  Updates whether or not LaunchDarkly tracks events for the feature flag associated with this rule.  ##### Parameters  - `ruleId`: The ID of the rule. You can retrieve this by making a GET request for the flag. - `trackEvents`: Whether or not events are tracked.  #### updateRuleVariationOrRollout  Updates what `ruleId` serves when its clauses evaluate to true. The rule can serve either the variation that `variationId` indicates, or a percent rollout that `rolloutWeights` and `rolloutBucketBy` indicate.  ##### Parameters  - `ruleId`: ID of a rule in the flag. - `variationId`: ID of a variation of the flag.    or  - `rolloutWeights`: Map of `variationId` to weight, in thousandths of a percent (0-100000). - `rolloutBucketBy`: Optional user attribute.  #### updateTrackEvents  Updates whether or not LaunchDarkly tracks events for the feature flag, for all rules.  ##### Parameters  - `trackEvents`: Whether or not events are tracked.  #### updateTrackEventsFallthrough  Updates whether or not LaunchDarkly tracks events for the feature flag, for the default rule.  ##### Parameters  - `trackEvents`: Whether or not events are tracked.  </details><br />  <details> <summary>Click to expand instructions for updating flag settings</summary>  #### addTags  Adds tags to the feature flag.  ##### Parameters  - `values`: A list of tags to add.  #### makeFlagPermanent  Marks the feature flag as permanent. LaunchDarkly does not prompt you to remove permanent flags, even if one variation is rolled out to all your users.  #### makeFlagTemporary  Marks the feature flag as temporary.  #### removeMaintainer  Removes the flag's maintainer. To set a new maintainer, use the flag's **Settings** tab in the LaunchDarkly user interface.  #### removeTags  Removes tags from the feature flag.  ##### Parameters  - `values`: A list of tags to remove.  #### turnOffClientSideAvailability  Turns off client-side SDK availability for the flag. This is equivalent to unchecking the **SDKs using Mobile Key** and/or **SDKs using client-side ID** boxes for the flag. If you're using a client-side or mobile SDK, you must expose your feature flags in order for the client-side or mobile SDKs to evaluate them.  ##### Parameters  - `value`: Use \"usingMobileKey\" to turn on availability for mobile SDKs. Use \"usingEnvironmentId\" to turn on availability for client-side SDKs.  #### turnOnClientSideAvailability  Turns on client-side SDK availability for the flag. This is equivalent to unchecking the **SDKs using Mobile Key** and/or **SDKs using client-side ID** boxes for the flag. If you're using a client-side or mobile SDK, you must expose your feature flags in order for the client-side or mobile SDKs to evaluate them.  ##### Parameters  - `value`: Use \"usingMobileKey\" to turn on availability for mobile SDKs. Use \"usingEnvironmentId\" to turn on availability for client-side SDKs.  #### updateDescription  Updates the feature flag description.  ##### Parameters  - `value`: The new description.  #### updateName  Updates the feature flag name.  ##### Parameters  - `value`: The new name.  </details><br />  <details> <summary>Click to expand instructions for updating the flag lifecycle</summary>  #### archiveFlag  Archives the feature flag. This retires it from LaunchDarkly without deleting it. You cannot archive a flag that is a prerequisite of other flags.  #### deleteFlag  Deletes the feature flag and its rules. You cannot restore a deleted flag. If this flag is requested again, the flag value defined in code will be returned for all users.  #### restoreFlag  Restores the feature flag if it was previously archived.  </details>  ### Example  The body of a single semantic patch can contain many different instructions.  <details> <summary>Click to expand example semantic patch request body</summary>  ```json {   \"environmentKey\": \"production\",   \"instructions\": [     {       \"kind\": \"turnFlagOn\"     },     {       \"kind\": \"turnFlagOff\"     },     {       \"kind\": \"addUserTargets\",       \"variationId\": \"8bfb304e-d516-47e5-8727-e7f798e8992d\",       \"values\": [\"userId\", \"userId2\"]     },     {       \"kind\": \"removeUserTargets\",       \"variationId\": \"8bfb304e-d516-47e5-8727-e7f798e8992d\",       \"values\": [\"userId3\", \"userId4\"]     },     {       \"kind\": \"updateFallthroughVariationOrRollout\",       \"rolloutWeights\": {         \"variationId\": 50000,         \"variationId2\": 50000       },       \"rolloutBucketBy\": null     },     {       \"kind\": \"addRule\",       \"clauses\": [         {           \"attribute\": \"segmentMatch\",           \"negate\": false,           \"values\": [\"test-segment\"]         }       ],       \"variationId\": null,       \"rolloutWeights\": {         \"variationId\": 50000,         \"variationId2\": 50000       },       \"rolloutBucketBy\": \"key\"     },     {       \"kind\": \"removeRule\",       \"ruleId\": \"99f12464-a429-40fc-86cc-b27612188955\"     },     {       \"kind\": \"reorderRules\",       \"ruleIds\": [\"2f72974e-de68-4243-8dd3-739582147a1f\", \"8bfb304e-d516-47e5-8727-e7f798e8992d\"]     },     {       \"kind\": \"addClauses\",       \"ruleId\": \"1134\",       \"clauses\": [         {           \"attribute\": \"email\",           \"op\": \"in\",           \"negate\": false,           \"values\": [\"test@test.com\"]         }       ]     },     {       \"kind\": \"removeClauses\",       \"ruleId\": \"1242529\",       \"clauseIds\": [\"8bfb304e-d516-47e5-8727-e7f798e8992d\"]     },     {       \"kind\": \"updateClause\",       \"ruleId\": \"2f72974e-de68-4243-8dd3-739582147a1f\",       \"clauseId\": \"309845\",       \"clause\": {         \"attribute\": \"segmentMatch\",         \"negate\": false,         \"values\": [\"test-segment\"]       }     },     {       \"kind\": \"updateRuleVariationOrRollout\",       \"ruleId\": \"2342\",       \"rolloutWeights\": null,       \"rolloutBucketBy\": null     },     {       \"kind\": \"updateOffVariation\",       \"variationId\": \"3242453\"     },     {       \"kind\": \"addPrerequisite\",       \"variationId\": \"234235\",       \"key\": \"flagKey2\"     },     {       \"kind\": \"updatePrerequisite\",       \"variationId\": \"234235\",       \"key\": \"flagKey2\"     },     {       \"kind\": \"removePrerequisite\",       \"key\": \"flagKey\"     }   ] } ``` </details>  ### Using JSON Patches on a feature flag If you do not include the header described above, you can use [JSON patch](/reference#updates-using-json-patch).  When using the update feature flag endpoint to add individual users to a specific variation, there are two different patch documents, depending on whether users are already being individually targeted for the variation.  If a flag variation already has users individually targeted, the path for the JSON Patch operation is:  ```json {   \"op\": \"add\",   \"path\": \"/environments/devint/targets/0/values/-\",   \"value\": \"TestClient10\" } ```  If a flag variation does not already have users individually targeted, the path for the JSON Patch operation is:  ```json [   {     \"op\": \"add\",     \"path\": \"/environments/devint/targets/-\",     \"value\": { \"variation\": 0, \"values\": [\"TestClient10\"] }   } ] ```   ### Required approvals If a request attempts to alter a flag configuration in an environment where approvals are required for the flag, the request will fail with a 405. Changes to the flag configuration in that environment will require creating an [approval request](/tag/Approvals) or a [workflow](/tag/Workflows-(beta)).  ### Conflicts If a flag configuration change made through this endpoint would cause a pending scheduled change or approval request to fail, this endpoint will return a 400. You can ignore this check by adding an `ignoreConflicts` query parameter set to `true`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_feature_flag(project_key, feature_flag_key, patch_with_comment, async_req=True)
        >>> result = thread.get()

        Args:
            project_key (str): The project key
            feature_flag_key (str): The feature flag key. The key identifies the flag in your code.
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_key'] = \
            project_key
        kwargs['feature_flag_key'] = \
            feature_flag_key
        kwargs['patch_with_comment'] = \
            patch_with_comment
        return self.patch_feature_flag_endpoint.call_with_http_info(**kwargs)

    def post_feature_flag(
        self,
        project_key,
        feature_flag_body,
        **kwargs
    ):
        """Create a feature flag  # noqa: E501

        Create a feature flag with the given name, key, and variations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_feature_flag(project_key, feature_flag_body, async_req=True)
        >>> result = thread.get()

        Args:
            project_key (str): The project key
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_key'] = \
            project_key
        kwargs['feature_flag_body'] = \
            feature_flag_body
        return self.post_feature_flag_endpoint.call_with_http_info(**kwargs)

