# -*- coding: utf-8 -*-

"""
    LaunchDarkly REST API

    This documentation describes LaunchDarkly's REST API.  To access the complete OpenAPI spec directly, use [Get OpenAPI spec](https://launchdarkly.com/docs/api/other/get-openapi-spec).  ## Authentication  LaunchDarkly's REST API uses the HTTPS protocol with a minimum TLS version of 1.2.  All REST API resources are authenticated with either [personal or service access tokens](https://launchdarkly.com/docs/home/account/api), or session cookies. Other authentication mechanisms are not supported. You can manage personal access tokens on your [**Authorization**](https://app.launchdarkly.com/settings/authorization) page in the LaunchDarkly UI.  LaunchDarkly also has SDK keys, mobile keys, and client-side IDs that are used by our server-side SDKs, mobile SDKs, and JavaScript-based SDKs, respectively. **These keys cannot be used to access our REST API**. These keys are environment-specific, and can only perform read-only operations such as fetching feature flag settings.  | Auth mechanism                                                                                  | Allowed resources                                                                                     | Use cases                                          | | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------- | | [Personal or service access tokens](https://launchdarkly.com/docs/home/account/api) | Can be customized on a per-token basis                                                                | Building scripts, custom integrations, data export. | | SDK keys                                                                                        | Can only access read-only resources specific to server-side SDKs. Restricted to a single environment. | Server-side SDKs                     | | Mobile keys                                                                                     | Can only access read-only resources specific to mobile SDKs, and only for flags marked available to mobile keys. Restricted to a single environment.           | Mobile SDKs                                        | | Client-side ID                                                                                  | Can only access read-only resources specific to JavaScript-based client-side SDKs, and only for flags marked available to client-side. Restricted to a single environment.           | Client-side JavaScript                             |  > #### Keep your access tokens and SDK keys private > > Access tokens should _never_ be exposed in untrusted contexts. Never put an access token in client-side JavaScript, or embed it in a mobile application. LaunchDarkly has special mobile keys that you can embed in mobile apps. If you accidentally expose an access token or SDK key, you can reset it from your [**Authorization**](https://app.launchdarkly.com/settings/authorization) page. > > The client-side ID is safe to embed in untrusted contexts. It's designed for use in client-side JavaScript.  ### Authentication using request header  The preferred way to authenticate with the API is by adding an `Authorization` header containing your access token to your requests. The value of the `Authorization` header must be your access token.  Manage personal access tokens from the [**Authorization**](https://app.launchdarkly.com/settings/authorization) page.  ### Authentication using session cookie  For testing purposes, you can make API calls directly from your web browser. If you are logged in to the LaunchDarkly application, the API will use your existing session to authenticate calls.  If you have a [role](https://launchdarkly.com/docs/home/account/built-in-roles) other than Admin, or have a [custom role](https://launchdarkly.com/docs/home/account/custom-roles) defined, you may not have permission to perform some API calls. You will receive a `401` response code in that case.  > ### Modifying the Origin header causes an error > > LaunchDarkly validates that the Origin header for any API request authenticated by a session cookie matches the expected Origin header. The expected Origin header is `https://app.launchdarkly.com`. > > If the Origin header does not match what's expected, LaunchDarkly returns an error. This error can prevent the LaunchDarkly app from working correctly. > > Any browser extension that intentionally changes the Origin header can cause this problem. For example, the `Allow-Control-Allow-Origin: *` Chrome extension changes the Origin header to `http://evil.com` and causes the app to fail. > > To prevent this error, do not modify your Origin header. > > LaunchDarkly does not require origin matching when authenticating with an access token, so this issue does not affect normal API usage.  ## Representations  All resources expect and return JSON response bodies. Error responses also send a JSON body. To learn more about the error format of the API, read [Errors](https://launchdarkly.com/docs/api#errors).  In practice this means that you always get a response with a `Content-Type` header set to `application/json`.  In addition, request bodies for `PATCH`, `POST`, and `PUT` requests must be encoded as JSON with a `Content-Type` header set to `application/json`.  ### Summary and detailed representations  When you fetch a list of resources, the response includes only the most important attributes of each resource. This is a _summary representation_ of the resource. When you fetch an individual resource, such as a single feature flag, you receive a _detailed representation_ of the resource.  The best way to find a detailed representation is to follow links. Every summary representation includes a link to its detailed representation.  ### Expanding responses  Sometimes the detailed representation of a resource does not include all of the attributes of the resource by default. If this is the case, the request method will clearly document this and describe which attributes you can include in an expanded response.  To include the additional attributes, append the `expand` request parameter to your request and add a comma-separated list of the attributes to include. For example, when you append `?expand=members,maintainers` to the [Get team](https://launchdarkly.com/docs/api/teams/get-team) endpoint, the expanded response includes both of these attributes.  ### Links and addressability  The best way to navigate the API is by following links. These are attributes in representations that link to other resources. The API always uses the same format for links:  - Links to other resources within the API are encapsulated in a `_links` object - If the resource has a corresponding link to HTML content on the site, it is stored in a special `_site` link  Each link has two attributes:  - An `href`, which contains the URL - A `type`, which describes the content type  For example, a feature resource might return the following:  ```json {   \"_links\": {     \"parent\": {       \"href\": \"/api/features\",       \"type\": \"application/json\"     },     \"self\": {       \"href\": \"/api/features/sort.order\",       \"type\": \"application/json\"     }   },   \"_site\": {     \"href\": \"/features/sort.order\",     \"type\": \"text/html\"   } } ```  From this, you can navigate to the parent collection of features by following the `parent` link, or navigate to the site page for the feature by following the `_site` link.  Collections are always represented as a JSON object with an `items` attribute containing an array of representations. Like all other representations, collections have `_links` defined at the top level.  Paginated collections include `first`, `last`, `next`, and `prev` links containing a URL with the respective set of elements in the collection.  ## Updates  Resources that accept partial updates use the `PATCH` verb. Most resources support the [JSON patch](https://launchdarkly.com/docs/api#updates-using-json-patch) format. Some resources also support the [JSON merge patch](https://launchdarkly.com/docs/api#updates-using-json-merge-patch) format, and some resources support the [semantic patch](https://launchdarkly.com/docs/api#updates-using-semantic-patch) format, which is a way to specify the modifications to perform as a set of executable instructions. Each resource supports optional [comments](https://launchdarkly.com/docs/api#updates-with-comments) that you can submit with updates. Comments appear in outgoing webhooks, the audit log, and other integrations.  When a resource supports both JSON patch and semantic patch, we document both in the request method. However, the specific request body fields and descriptions included in our documentation only match one type of patch or the other.  ### Updates using JSON patch  [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) is a way to specify the modifications to perform on a resource. JSON patch uses paths and a limited set of operations to describe how to transform the current state of the resource into a new state. JSON patch documents are always arrays, where each element contains an operation, a path to the field to update, and the new value.  For example, in this feature flag representation:  ```json {     \"name\": \"New recommendations engine\",     \"key\": \"engine.enable\",     \"description\": \"This is the description\",     ... } ``` You can change the feature flag's description with the following patch document:  ```json [{ \"op\": \"replace\", \"path\": \"/description\", \"value\": \"This is the new description\" }] ```  You can specify multiple modifications to perform in a single request. You can also test that certain preconditions are met before applying the patch:  ```json [   { \"op\": \"test\", \"path\": \"/version\", \"value\": 10 },   { \"op\": \"replace\", \"path\": \"/description\", \"value\": \"The new description\" } ] ```  The above patch request tests whether the feature flag's `version` is `10`, and if so, changes the feature flag's description.  Attributes that are not editable, such as a resource's `_links`, have names that start with an underscore.  ### Updates using JSON merge patch  [JSON merge patch](https://datatracker.ietf.org/doc/html/rfc7386) is another format for specifying the modifications to perform on a resource. JSON merge patch is less expressive than JSON patch. However, in many cases it is simpler to construct a merge patch document. For example, you can change a feature flag's description with the following merge patch document:  ```json {   \"description\": \"New flag description\" } ```  ### Updates using semantic patch  Some resources support the semantic patch format. A semantic patch is a way to specify the modifications to perform on a resource as a set of executable instructions.  Semantic patch allows you to be explicit about intent using precise, custom instructions. In many cases, you can define semantic patch instructions independently of the current state of the resource. This can be useful when defining a change that may be applied at a future date.  To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header.  Here's how:  ``` Content-Type: application/json; domain-model=launchdarkly.semanticpatch ```  If you call a semantic patch resource without this header, you will receive a `400` response because your semantic patch will be interpreted as a JSON patch.  The body of a semantic patch request takes the following properties:  * `comment` (string): (Optional) A description of the update. * `environmentKey` (string): (Required for some resources only) The environment key. * `instructions` (array): (Required) A list of actions the update should perform. Each action in the list must be an object with a `kind` property that indicates the instruction. If the instruction requires parameters, you must include those parameters as additional fields in the object. The documentation for each resource that supports semantic patch includes the available instructions and any additional parameters.  For example:  ```json {   \"comment\": \"optional comment\",   \"instructions\": [ {\"kind\": \"turnFlagOn\"} ] } ```  Semantic patches are not applied partially; either all of the instructions are applied or none of them are. If **any** instruction is invalid, the endpoint returns an error and will not change the resource. If all instructions are valid, the request succeeds and the resources are updated if necessary, or left unchanged if they are already in the state you request.  ### Updates with comments  You can submit optional comments with `PATCH` changes.  To submit a comment along with a JSON patch document, use the following format:  ```json {   \"comment\": \"This is a comment string\",   \"patch\": [{ \"op\": \"replace\", \"path\": \"/description\", \"value\": \"The new description\" }] } ```  To submit a comment along with a JSON merge patch document, use the following format:  ```json {   \"comment\": \"This is a comment string\",   \"merge\": { \"description\": \"New flag description\" } } ```  To submit a comment along with a semantic patch, use the following format:  ```json {   \"comment\": \"This is a comment string\",   \"instructions\": [ {\"kind\": \"turnFlagOn\"} ] } ```  ## Errors  The API always returns errors in a common format. Here's an example:  ```json {   \"code\": \"invalid_request\",   \"message\": \"A feature with that key already exists\",   \"id\": \"30ce6058-87da-11e4-b116-123b93f75cba\" } ```  The `code` indicates the general class of error. The `message` is a human-readable explanation of what went wrong. The `id` is a unique identifier. Use it when you're working with LaunchDarkly Support to debug a problem with a specific API call.  ### HTTP status error response codes  | Code | Definition        | Description                                                                                       | Possible Solution                                                | | ---- | ----------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | | 400  | Invalid request       | The request cannot be understood.                                    | Ensure JSON syntax in request body is correct.                   | | 401  | Invalid access token      | Requestor is unauthorized or does not have permission for this API call.                                                | Ensure your API access token is valid and has the appropriate permissions.                                     | | 403  | Forbidden         | Requestor does not have access to this resource.                                                | Ensure that the account member or access token has proper permissions set. | | 404  | Invalid resource identifier | The requested resource is not valid. | Ensure that the resource is correctly identified by ID or key. | | 405  | Method not allowed | The request method is not allowed on this resource. | Ensure that the HTTP verb is correct. | | 409  | Conflict          | The API request can not be completed because it conflicts with a concurrent API request. | Retry your request.                                              | | 422  | Unprocessable entity | The API request can not be completed because the update description can not be understood. | Ensure that the request body is correct for the type of patch you are using, either JSON patch or semantic patch. | 429  | Too many requests | Read [Rate limiting](https://launchdarkly.com/docs/api#rate-limiting).                                               | Wait and try again later.                                        |  ## CORS  The LaunchDarkly API supports Cross Origin Resource Sharing (CORS) for AJAX requests from any origin. If an `Origin` header is given in a request, it will be echoed as an explicitly allowed origin. Otherwise the request returns a wildcard, `Access-Control-Allow-Origin: *`. For more information on CORS, read the [CORS W3C Recommendation](http://www.w3.org/TR/cors). Example CORS headers might look like:  ```http Access-Control-Allow-Headers: Accept, Content-Type, Content-Length, Accept-Encoding, Authorization Access-Control-Allow-Methods: OPTIONS, GET, DELETE, PATCH Access-Control-Allow-Origin: * Access-Control-Max-Age: 300 ```  You can make authenticated CORS calls just as you would make same-origin calls, using either [token or session-based authentication](https://launchdarkly.com/docs/api#authentication). If you are using session authentication, you should set the `withCredentials` property for your `xhr` request to `true`. You should never expose your access tokens to untrusted entities.  ## Rate limiting  We use several rate limiting strategies to ensure the availability of our APIs. Rate-limited calls to our APIs return a `429` status code. Calls to our APIs include headers indicating the current rate limit status. The specific headers returned depend on the API route being called. The limits differ based on the route, authentication mechanism, and other factors. Routes that are not rate limited may not contain any of the headers described below.  > ### Rate limiting and SDKs > > LaunchDarkly SDKs are never rate limited and do not use the API endpoints defined here. LaunchDarkly uses a different set of approaches, including streaming/server-sent events and a global CDN, to ensure availability to the routes used by LaunchDarkly SDKs.  ### Global rate limits  Authenticated requests are subject to a global limit. This is the maximum number of calls that your account can make to the API per ten seconds. All service and personal access tokens on the account share this limit, so exceeding the limit with one access token will impact other tokens. Calls that are subject to global rate limits may return the headers below:  | Header name                    | Description                                                                      | | ------------------------------ | -------------------------------------------------------------------------------- | | `X-Ratelimit-Global-Remaining` | The maximum number of requests the account is permitted to make per ten seconds. | | `X-Ratelimit-Reset`            | The time at which the current rate limit window resets in epoch milliseconds.    |  We do not publicly document the specific number of calls that can be made globally. This limit may change, and we encourage clients to program against the specification, relying on the two headers defined above, rather than hardcoding to the current limit.  ### Route-level rate limits  Some authenticated routes have custom rate limits. These also reset every ten seconds. Any service or personal access tokens hitting the same route share this limit, so exceeding the limit with one access token may impact other tokens. Calls that are subject to route-level rate limits return the headers below:  | Header name                   | Description                                                                                           | | ----------------------------- | ----------------------------------------------------------------------------------------------------- | | `X-Ratelimit-Route-Remaining` | The maximum number of requests to the current route the account is permitted to make per ten seconds. | | `X-Ratelimit-Reset`           | The time at which the current rate limit window resets in epoch milliseconds.                         |  A _route_ represents a specific URL pattern and verb. For example, the [Delete environment](https://launchdarkly.com/docs/api/environments/delete-environment) endpoint is considered a single route, and each call to delete an environment counts against your route-level rate limit for that route.  We do not publicly document the specific number of calls that an account can make to each endpoint per ten seconds. These limits may change, and we encourage clients to program against the specification, relying on the two headers defined above, rather than hardcoding to the current limits.  ### IP-based rate limiting  We also employ IP-based rate limiting on some API routes. If you hit an IP-based rate limit, your API response will include a `Retry-After` header indicating how long to wait before re-trying the call. Clients must wait at least `Retry-After` seconds before making additional calls to our API, and should employ jitter and backoff strategies to avoid triggering rate limits again.  ## OpenAPI (Swagger) and client libraries  We have a [complete OpenAPI (Swagger) specification](https://app.launchdarkly.com/api/v2/openapi.json) for our API.  We auto-generate multiple client libraries based on our OpenAPI specification. To learn more, visit the [collection of client libraries on GitHub](https://github.com/search?q=topic%3Alaunchdarkly-api+org%3Alaunchdarkly&type=Repositories). You can also use this specification to generate client libraries to interact with our REST API in your language of choice.  Our OpenAPI specification is supported by several API-based tools such as Postman and Insomnia. In many cases, you can directly import our specification to explore our APIs.  ## Method overriding  Some firewalls and HTTP clients restrict the use of verbs other than `GET` and `POST`. In those environments, our API endpoints that use `DELETE`, `PATCH`, and `PUT` verbs are inaccessible.  To avoid this issue, our API supports the `X-HTTP-Method-Override` header, allowing clients to \"tunnel\" `DELETE`, `PATCH`, and `PUT` requests using a `POST` request.  For example, to call a `PATCH` endpoint using a `POST` request, you can include `X-HTTP-Method-Override:PATCH` as a header.  ## Beta resources  We sometimes release new API resources in **beta** status before we release them with general availability.  Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.  We try to promote resources into general availability as quickly as possible. This happens after sufficient testing and when we're satisfied that we no longer need to make backwards-incompatible changes.  We mark beta resources with a \"Beta\" callout in our documentation, pictured below:  > ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](https://launchdarkly.com/docs/api#beta-resources). > > Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.  ### Using beta resources  To use a beta resource, you must include a header in the request. If you call a beta resource without this header, you receive a `403` response.  Use this header:  ``` LD-API-Version: beta ```  ## Federal environments  The version of LaunchDarkly that is available on domains controlled by the United States government is different from the version of LaunchDarkly available to the general public. If you are an employee or contractor for a United States federal agency and use LaunchDarkly in your work, you likely use the federal instance of LaunchDarkly.  If you are working in the federal instance of LaunchDarkly, the base URI for each request is `https://app.launchdarkly.us`.  To learn more, read [LaunchDarkly in federal environments](https://launchdarkly.com/docs/home/infrastructure/federal).  ## Versioning  We try hard to keep our REST API backwards compatible, but we occasionally have to make backwards-incompatible changes in the process of shipping new features. These breaking changes can cause unexpected behavior if you don't prepare for them accordingly.  Updates to our REST API include support for the latest features in LaunchDarkly. We also release a new version of our REST API every time we make a breaking change. We provide simultaneous support for multiple API versions so you can migrate from your current API version to a new version at your own pace.  ### Setting the API version per request  You can set the API version on a specific request by sending an `LD-API-Version` header, as shown in the example below:  ``` LD-API-Version: 20240415 ```  The header value is the version number of the API version you would like to request. The number for each version corresponds to the date the version was released in `yyyymmdd` format. In the example above the version `20240415` corresponds to April 15, 2024.  ### Setting the API version per access token  When you create an access token, you must specify a specific version of the API to use. This ensures that integrations using this token cannot be broken by version changes.  Tokens created before versioning was released have their version set to `20160426`, which is the version of the API that existed before the current versioning scheme, so that they continue working the same way they did before versioning.  If you would like to upgrade your integration to use a new API version, you can explicitly set the header described above.  > ### Best practice: Set the header for every client or integration > > We recommend that you set the API version header explicitly in any client or integration you build. > > Only rely on the access token API version during manual testing.  ### API version changelog  <table>   <tr>     <th>Version</th>     <th>Changes</th>     <th>End of life (EOL)</th>   </tr>   <tr>     <td>`20240415`</td>     <td>       <ul><li>Changed several endpoints from unpaginated to paginated. Use the `limit` and `offset` query parameters to page through the results.</li> <li>Changed the [list access tokens](https://launchdarkly.com/docs/api/access-tokens/get-tokens) endpoint: <ul><li>Response is now paginated with a default limit of `25`</li></ul></li> <li>Changed the [list account members](https://launchdarkly.com/docs/api/account-members/get-members) endpoint: <ul><li>The `accessCheck` filter is no longer available</li></ul></li> <li>Changed the [list custom roles](https://launchdarkly.com/docs/api/custom-roles/get-custom-roles) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li></ul></li> <li>Changed the [list feature flags](https://launchdarkly.com/docs/api/feature-flags/get-feature-flags) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li><li>The `environments` field is now only returned if the request is filtered by environment, using the `filterEnv` query parameter</li><li>The `followerId`, `hasDataExport`, `status`, `contextKindTargeted`, and `segmentTargeted` filters are no longer available</li><li>The `compare` query parameter is no longer available</li></ul></li> <li>Changed the [list segments](https://launchdarkly.com/docs/api/segments/get-segments) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li></ul></li> <li>Changed the [list teams](https://launchdarkly.com/docs/api/teams/get-teams) endpoint: <ul><li>The `expand` parameter no longer supports including `projects` or `roles`</li><li>In paginated results, the maximum page size is now 100</li></ul></li> <li>Changed the [get workflows](https://launchdarkly.com/docs/api/workflows/get-workflows) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li><li>The `_conflicts` field in the response is no longer available</li></ul></li> </ul>     </td>     <td>Current</td>   </tr>   <tr>     <td>`20220603`</td>     <td>       <ul><li>Changed the [list projects](https://launchdarkly.com/docs/api/projects/get-projects) return value:<ul><li>Response is now paginated with a default limit of `20`.</li><li>Added support for filter and sort.</li><li>The project `environments` field is now expandable. This field is omitted by default.</li></ul></li><li>Changed the [get project](https://launchdarkly.com/docs/api/projects/get-project) return value:<ul><li>The `environments` field is now expandable. This field is omitted by default.</li></ul></li></ul>     </td>     <td>2025-04-15</td>   </tr>   <tr>     <td>`20210729`</td>     <td>       <ul><li>Changed the [create approval request](https://launchdarkly.com/docs/api/approvals/post-approval-request) return value. It now returns HTTP Status Code `201` instead of `200`.</li><li> Changed the [get user](https://launchdarkly.com/docs/api/users/get-user) return value. It now returns a user record, not a user. </li><li>Added additional optional fields to environment, segments, flags, members, and segments, including the ability to create big segments. </li><li> Added default values for flag variations when new environments are created. </li><li>Added filtering and pagination for getting flags and members, including `limit`, `number`, `filter`, and `sort` query parameters. </li><li>Added endpoints for expiring user targets for flags and segments, scheduled changes, access tokens, Relay Proxy configuration, integrations and subscriptions, and approvals. </li></ul>     </td>     <td>2023-06-03</td>   </tr>   <tr>     <td>`20191212`</td>     <td>       <ul><li>[List feature flags](https://launchdarkly.com/docs/api/feature-flags/get-feature-flags) now defaults to sending summaries of feature flag configurations, equivalent to setting the query parameter `summary=true`. Summaries omit flag targeting rules and individual user targets from the payload. </li><li> Added endpoints for flags, flag status, projects, environments, audit logs, members, users, custom roles, segments, usage, streams, events, and data export. </li></ul>     </td>     <td>2022-07-29</td>   </tr>   <tr>     <td>`20160426`</td>     <td>       <ul><li>Initial versioning of API. Tokens created before versioning have their version set to this.</li></ul>     </td>     <td>2020-12-12</td>   </tr> </table>  To learn more about how EOL is determined, read LaunchDarkly's [End of Life (EOL) Policy](https://launchdarkly.com/policies/end-of-life-policy/).   # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@launchdarkly.com
    Generated by: https://openapi-generator.tech
"""


from datetime import date, datetime  # noqa: F401
from copy import deepcopy
import inspect
import io
import os
import pprint
import re
import tempfile
import uuid

from dateutil.parser import parse

from launchdarkly_api.exceptions import (
    ApiKeyError,
    ApiAttributeError,
    ApiTypeError,
    ApiValueError,
)

none_type = type(None)
file_type = io.IOBase


def convert_js_args_to_python_args(fn):
    from functools import wraps
    @wraps(fn)
    def wrapped_init(_self, *args, **kwargs):
        """
        An attribute named `self` received from the api will conflicts with the reserved `self`
        parameter of a class method. During generation, `self` attributes are mapped
        to `_self` in models. Here, we name `_self` instead of `self` to avoid conflicts.
        """
        spec_property_naming = kwargs.get('_spec_property_naming', False)
        if spec_property_naming:
            kwargs = change_keys_js_to_python(
                kwargs, _self if isinstance(
                    _self, type) else _self.__class__)
        return fn(_self, *args, **kwargs)
    return wrapped_init


class cached_property(object):
    # this caches the result of the function call for fn with no inputs
    # use this as a decorator on function methods that you want converted
    # into cached properties
    result_key = '_results'

    def __init__(self, fn):
        self._fn = fn

    def __get__(self, instance, cls=None):
        if self.result_key in vars(self):
            return vars(self)[self.result_key]
        else:
            result = self._fn()
            setattr(self, self.result_key, result)
            return result


PRIMITIVE_TYPES = (list, float, int, bool, datetime, date, str, file_type)


def allows_single_value_input(cls):
    """
    This function returns True if the input composed schema model or any
    descendant model allows a value only input
    This is true for cases where oneOf contains items like:
    oneOf:
      - float
      - NumberWithValidation
      - StringEnum
      - ArrayModel
      - null
    TODO: lru_cache this
    """
    if (
        issubclass(cls, ModelSimple) or
        cls in PRIMITIVE_TYPES
    ):
        return True
    elif issubclass(cls, ModelComposed):
        if not cls._composed_schemas['oneOf']:
            return False
        return any(allows_single_value_input(c) for c in cls._composed_schemas['oneOf'])
    return False


def composed_model_input_classes(cls):
    """
    This function returns a list of the possible models that can be accepted as
    inputs.
    TODO: lru_cache this
    """
    if issubclass(cls, ModelSimple) or cls in PRIMITIVE_TYPES:
        return [cls]
    elif issubclass(cls, ModelNormal):
        if cls.discriminator is None:
            return [cls]
        else:
            return get_discriminated_classes(cls)
    elif issubclass(cls, ModelComposed):
        if not cls._composed_schemas['oneOf']:
            return []
        if cls.discriminator is None:
            input_classes = []
            for c in cls._composed_schemas['oneOf']:
                input_classes.extend(composed_model_input_classes(c))
            return input_classes
        else:
            return get_discriminated_classes(cls)
    return []


class OpenApiModel(object):
    """The base class for all OpenAPIModels"""

    def set_attribute(self, name, value):
        # this is only used to set properties on self

        path_to_item = []
        if self._path_to_item:
            path_to_item.extend(self._path_to_item)
        path_to_item.append(name)

        if name in self.openapi_types:
            required_types_mixed = self.openapi_types[name]
        elif self.additional_properties_type is None:
            raise ApiAttributeError(
                "{0} has no attribute '{1}'".format(
                    type(self).__name__, name),
                path_to_item
            )
        elif self.additional_properties_type is not None:
            required_types_mixed = self.additional_properties_type

        if get_simple_class(name) != str:
            error_msg = type_error_message(
                var_name=name,
                var_value=name,
                valid_classes=(str,),
                key_type=True
            )
            raise ApiTypeError(
                error_msg,
                path_to_item=path_to_item,
                valid_classes=(str,),
                key_type=True
            )

        if self._check_type:
            value = validate_and_convert_types(
                value, required_types_mixed, path_to_item, self._spec_property_naming,
                self._check_type, configuration=self._configuration)
        if (name,) in self.allowed_values:
            check_allowed_values(
                self.allowed_values,
                (name,),
                value
            )
        if (name,) in self.validations:
            check_validations(
                self.validations,
                (name,),
                value,
                self._configuration
            )
        self.__dict__['_data_store'][name] = value

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    def __setattr__(self, attr, value):
        """set the value of an attribute using dot notation: `instance.attr = val`"""
        self[attr] = value

    def __getattr__(self, attr):
        """get the value of an attribute using dot notation: `instance.attr`"""
        return self.__getitem__(attr)

    def __copy__(self):
        cls = self.__class__
        if self.get("_spec_property_naming", False):
            return cls._new_from_openapi_data(**self.__dict__)
        else:
            return cls.__new__(cls, **self.__dict__)

    def __deepcopy__(self, memo):
        cls = self.__class__

        if self.get("_spec_property_naming", False):
            new_inst = cls._new_from_openapi_data()
        else:
            new_inst = cls.__new__(cls)

        for k, v in self.__dict__.items():
            setattr(new_inst, k, deepcopy(v, memo))
        return new_inst


    def __new__(cls, *args, **kwargs):
        # this function uses the discriminator to
        # pick a new schema/class to instantiate because a discriminator
        # propertyName value was passed in

        if len(args) == 1:
            arg = args[0]
            if arg is None and is_type_nullable(cls):
                # The input data is the 'null' value and the type is nullable.
                return None

            if issubclass(cls, ModelComposed) and allows_single_value_input(cls):
                model_kwargs = {}
                oneof_instance = get_oneof_instance(cls, model_kwargs, kwargs, model_arg=arg)
                return oneof_instance

        visited_composed_classes = kwargs.get('_visited_composed_classes', ())
        if (
            cls.discriminator is None or
            cls in visited_composed_classes
        ):
            # Use case 1: this openapi schema (cls) does not have a discriminator
            # Use case 2: we have already visited this class before and are sure that we
            # want to instantiate it this time. We have visited this class deserializing
            # a payload with a discriminator. During that process we traveled through
            # this class but did not make an instance of it. Now we are making an
            # instance of a composed class which contains cls in it, so this time make an instance of cls.
            #
            # Here's an example of use case 2: If Animal has a discriminator
            # petType and we pass in "Dog", and the class Dog
            # allOf includes Animal, we move through Animal
            # once using the discriminator, and pick Dog.
            # Then in the composed schema dog Dog, we will make an instance of the
            # Animal class (because Dal has allOf: Animal) but this time we won't travel
            # through Animal's discriminator because we passed in
            # _visited_composed_classes = (Animal,)

            return super(OpenApiModel, cls).__new__(cls)

        # Get the name and value of the discriminator property.
        # The discriminator name is obtained from the discriminator meta-data
        # and the discriminator value is obtained from the input data.
        discr_propertyname_py = list(cls.discriminator.keys())[0]
        discr_propertyname_js = cls.attribute_map[discr_propertyname_py]
        if discr_propertyname_js in kwargs:
            discr_value = kwargs[discr_propertyname_js]
        elif discr_propertyname_py in kwargs:
            discr_value = kwargs[discr_propertyname_py]
        else:
            # The input data does not contain the discriminator property.
            path_to_item = kwargs.get('_path_to_item', ())
            raise ApiValueError(
                "Cannot deserialize input data due to missing discriminator. "
                "The discriminator property '%s' is missing at path: %s" %
                (discr_propertyname_js, path_to_item)
            )

        # Implementation note: the last argument to get_discriminator_class
        # is a list of visited classes. get_discriminator_class may recursively
        # call itself and update the list of visited classes, and the initial
        # value must be an empty list. Hence not using 'visited_composed_classes'
        new_cls = get_discriminator_class(
            cls, discr_propertyname_py, discr_value, [])
        if new_cls is None:
            path_to_item = kwargs.get('_path_to_item', ())
            disc_prop_value = kwargs.get(
                discr_propertyname_js, kwargs.get(discr_propertyname_py))
            raise ApiValueError(
                "Cannot deserialize input data due to invalid discriminator "
                "value. The OpenAPI document has no mapping for discriminator "
                "property '%s'='%s' at path: %s" %
                (discr_propertyname_js, disc_prop_value, path_to_item)
            )

        if new_cls in visited_composed_classes:
            # if we are making an instance of a composed schema Descendent
            # which allOf includes Ancestor, then Ancestor contains
            # a discriminator that includes Descendent.
            # So if we make an instance of Descendent, we have to make an
            # instance of Ancestor to hold the allOf properties.
            # This code detects that use case and makes the instance of Ancestor
            # For example:
            # When making an instance of Dog, _visited_composed_classes = (Dog,)
            # then we make an instance of Animal to include in dog._composed_instances
            # so when we are here, cls is Animal
            # cls.discriminator != None
            # cls not in _visited_composed_classes
            # new_cls = Dog
            # but we know we know that we already have Dog
            # because it is in visited_composed_classes
            # so make Animal here
            return super(OpenApiModel, cls).__new__(cls)

        # Build a list containing all oneOf and anyOf descendants.
        oneof_anyof_classes = None
        if cls._composed_schemas is not None:
            oneof_anyof_classes = (
                cls._composed_schemas.get('oneOf', ()) +
                cls._composed_schemas.get('anyOf', ()))
        oneof_anyof_child = new_cls in oneof_anyof_classes
        kwargs['_visited_composed_classes'] = visited_composed_classes + (cls,)

        if cls._composed_schemas.get('allOf') and oneof_anyof_child:
            # Validate that we can make self because when we make the
            # new_cls it will not include the allOf validations in self
            self_inst = super(OpenApiModel, cls).__new__(cls)
            self_inst.__init__(*args, **kwargs)

        if kwargs.get("_spec_property_naming", False):
            # when true, implies new is from deserialization
            new_inst = new_cls._new_from_openapi_data(*args, **kwargs)
        else:
            new_inst = new_cls.__new__(new_cls, *args, **kwargs)
            new_inst.__init__(*args, **kwargs)

        return new_inst

    @classmethod
    @convert_js_args_to_python_args
    def _new_from_openapi_data(cls, *args, **kwargs):
        # this function uses the discriminator to
        # pick a new schema/class to instantiate because a discriminator
        # propertyName value was passed in

        if len(args) == 1:
            arg = args[0]
            if arg is None and is_type_nullable(cls):
                # The input data is the 'null' value and the type is nullable.
                return None

            if issubclass(cls, ModelComposed) and allows_single_value_input(cls):
                model_kwargs = {}
                oneof_instance = get_oneof_instance(cls, model_kwargs, kwargs, model_arg=arg)
                return oneof_instance

        visited_composed_classes = kwargs.get('_visited_composed_classes', ())
        if (
            cls.discriminator is None or
            cls in visited_composed_classes
        ):
            # Use case 1: this openapi schema (cls) does not have a discriminator
            # Use case 2: we have already visited this class before and are sure that we
            # want to instantiate it this time. We have visited this class deserializing
            # a payload with a discriminator. During that process we traveled through
            # this class but did not make an instance of it. Now we are making an
            # instance of a composed class which contains cls in it, so this time make an instance of cls.
            #
            # Here's an example of use case 2: If Animal has a discriminator
            # petType and we pass in "Dog", and the class Dog
            # allOf includes Animal, we move through Animal
            # once using the discriminator, and pick Dog.
            # Then in the composed schema dog Dog, we will make an instance of the
            # Animal class (because Dal has allOf: Animal) but this time we won't travel
            # through Animal's discriminator because we passed in
            # _visited_composed_classes = (Animal,)

            return cls._from_openapi_data(*args, **kwargs)

        # Get the name and value of the discriminator property.
        # The discriminator name is obtained from the discriminator meta-data
        # and the discriminator value is obtained from the input data.
        discr_propertyname_py = list(cls.discriminator.keys())[0]
        discr_propertyname_js = cls.attribute_map[discr_propertyname_py]
        if discr_propertyname_js in kwargs:
            discr_value = kwargs[discr_propertyname_js]
        elif discr_propertyname_py in kwargs:
            discr_value = kwargs[discr_propertyname_py]
        else:
            # The input data does not contain the discriminator property.
            path_to_item = kwargs.get('_path_to_item', ())
            raise ApiValueError(
                "Cannot deserialize input data due to missing discriminator. "
                "The discriminator property '%s' is missing at path: %s" %
                (discr_propertyname_js, path_to_item)
            )

        # Implementation note: the last argument to get_discriminator_class
        # is a list of visited classes. get_discriminator_class may recursively
        # call itself and update the list of visited classes, and the initial
        # value must be an empty list. Hence not using 'visited_composed_classes'
        new_cls = get_discriminator_class(
            cls, discr_propertyname_py, discr_value, [])
        if new_cls is None:
            path_to_item = kwargs.get('_path_to_item', ())
            disc_prop_value = kwargs.get(
                discr_propertyname_js, kwargs.get(discr_propertyname_py))
            raise ApiValueError(
                "Cannot deserialize input data due to invalid discriminator "
                "value. The OpenAPI document has no mapping for discriminator "
                "property '%s'='%s' at path: %s" %
                (discr_propertyname_js, disc_prop_value, path_to_item)
            )

        if new_cls in visited_composed_classes:
            # if we are making an instance of a composed schema Descendent
            # which allOf includes Ancestor, then Ancestor contains
            # a discriminator that includes Descendent.
            # So if we make an instance of Descendent, we have to make an
            # instance of Ancestor to hold the allOf properties.
            # This code detects that use case and makes the instance of Ancestor
            # For example:
            # When making an instance of Dog, _visited_composed_classes = (Dog,)
            # then we make an instance of Animal to include in dog._composed_instances
            # so when we are here, cls is Animal
            # cls.discriminator != None
            # cls not in _visited_composed_classes
            # new_cls = Dog
            # but we know we know that we already have Dog
            # because it is in visited_composed_classes
            # so make Animal here
            return cls._from_openapi_data(*args, **kwargs)

        # Build a list containing all oneOf and anyOf descendants.
        oneof_anyof_classes = None
        if cls._composed_schemas is not None:
            oneof_anyof_classes = (
                cls._composed_schemas.get('oneOf', ()) +
                cls._composed_schemas.get('anyOf', ()))
        oneof_anyof_child = new_cls in oneof_anyof_classes
        kwargs['_visited_composed_classes'] = visited_composed_classes + (cls,)

        if cls._composed_schemas.get('allOf') and oneof_anyof_child:
            # Validate that we can make self because when we make the
            # new_cls it will not include the allOf validations in self
            self_inst = cls._from_openapi_data(*args, **kwargs)

        new_inst = new_cls._new_from_openapi_data(*args, **kwargs)
        return new_inst


class ModelSimple(OpenApiModel):
    """the parent class of models whose type != object in their
    swagger/openapi"""

    def __setitem__(self, name, value):
        """set the value of an attribute using square-bracket notation: `instance[attr] = val`"""
        if name in self.required_properties:
            self.__dict__[name] = value
            return

        self.set_attribute(name, value)

    def get(self, name, default=None):
        """returns the value of an attribute or some default value if the attribute was not set"""
        if name in self.required_properties:
            return self.__dict__[name]

        return self.__dict__['_data_store'].get(name, default)

    def __getitem__(self, name):
        """get the value of an attribute using square-bracket notation: `instance[attr]`"""
        if name in self:
            return self.get(name)

        raise ApiAttributeError(
            "{0} has no attribute '{1}'".format(
                type(self).__name__, name),
            [e for e in [self._path_to_item, name] if e]
        )

    def __contains__(self, name):
        """used by `in` operator to check if an attribute value was set in an instance: `'attr' in instance`"""
        if name in self.required_properties:
            return name in self.__dict__

        return name in self.__dict__['_data_store']

    def to_str(self):
        """Returns the string representation of the model"""
        return str(self.value)

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, self.__class__):
            return False

        this_val = self._data_store['value']
        that_val = other._data_store['value']
        types = set()
        types.add(this_val.__class__)
        types.add(that_val.__class__)
        vals_equal = this_val == that_val
        return vals_equal


class ModelNormal(OpenApiModel):
    """the parent class of models whose type == object in their
    swagger/openapi"""

    def __setitem__(self, name, value):
        """set the value of an attribute using square-bracket notation: `instance[attr] = val`"""
        if name in self.required_properties:
            self.__dict__[name] = value
            return

        self.set_attribute(name, value)

    def get(self, name, default=None):
        """returns the value of an attribute or some default value if the attribute was not set"""
        if name in self.required_properties:
            return self.__dict__[name]

        return self.__dict__['_data_store'].get(name, default)

    def __getitem__(self, name):
        """get the value of an attribute using square-bracket notation: `instance[attr]`"""
        if name in self:
            return self.get(name)

        raise ApiAttributeError(
            "{0} has no attribute '{1}'".format(
                type(self).__name__, name),
            [e for e in [self._path_to_item, name] if e]
        )

    def __contains__(self, name):
        """used by `in` operator to check if an attribute value was set in an instance: `'attr' in instance`"""
        if name in self.required_properties:
            return name in self.__dict__

        return name in self.__dict__['_data_store']

    def to_dict(self):
        """Returns the model properties as a dict"""
        return model_to_dict(self, serialize=False)

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, self.__class__):
            return False

        if not set(self._data_store.keys()) == set(other._data_store.keys()):
            return False
        for _var_name, this_val in self._data_store.items():
            that_val = other._data_store[_var_name]
            types = set()
            types.add(this_val.__class__)
            types.add(that_val.__class__)
            vals_equal = this_val == that_val
            if not vals_equal:
                return False
        return True


class ModelComposed(OpenApiModel):
    """the parent class of models whose type == object in their
    swagger/openapi and have oneOf/allOf/anyOf

    When one sets a property we use var_name_to_model_instances to store the value in
    the correct class instances + run any type checking + validation code.
    When one gets a property we use var_name_to_model_instances to get the value
    from the correct class instances.
    This allows multiple composed schemas to contain the same property with additive
    constraints on the value.

    _composed_schemas (dict) stores the anyOf/allOf/oneOf classes
    key (str): allOf/oneOf/anyOf
    value (list): the classes in the XOf definition.
        Note: none_type can be included when the openapi document version >= 3.1.0
    _composed_instances (list): stores a list of instances of the composed schemas
    defined in _composed_schemas. When properties are accessed in the self instance,
    they are returned from the self._data_store or the data stores in the instances
    in self._composed_schemas
    _var_name_to_model_instances (dict): maps between a variable name on self and
    the composed instances (self included) which contain that data
    key (str): property name
    value (list): list of class instances, self or instances in _composed_instances
    which contain the value that the key is referring to.
    """

    def __setitem__(self, name, value):
        """set the value of an attribute using square-bracket notation: `instance[attr] = val`"""
        if name in self.required_properties:
            self.__dict__[name] = value
            return

        """
        Use cases:
        1. additional_properties_type is None (additionalProperties == False in spec)
            Check for property presence in self.openapi_types
            if not present then throw an error
            if present set in self, set attribute
            always set on composed schemas
        2.  additional_properties_type exists
            set attribute on self
            always set on composed schemas
        """
        if self.additional_properties_type is None:
            """
            For an attribute to exist on a composed schema it must:
            - fulfill schema_requirements in the self composed schema not considering oneOf/anyOf/allOf schemas AND
            - fulfill schema_requirements in each oneOf/anyOf/allOf schemas

            schema_requirements:
            For an attribute to exist on a schema it must:
            - be present in properties at the schema OR
            - have additionalProperties unset (defaults additionalProperties = any type) OR
            - have additionalProperties set
            """
            if name not in self.openapi_types:
                raise ApiAttributeError(
                    "{0} has no attribute '{1}'".format(
                        type(self).__name__, name),
                    [e for e in [self._path_to_item, name] if e]
                )
        # attribute must be set on self and composed instances
        self.set_attribute(name, value)
        for model_instance in self._composed_instances:
            setattr(model_instance, name, value)
        if name not in self._var_name_to_model_instances:
            # we assigned an additional property
            self.__dict__['_var_name_to_model_instances'][name] = self._composed_instances + [self]
        return None

    __unset_attribute_value__ = object()

    def get(self, name, default=None):
        """returns the value of an attribute or some default value if the attribute was not set"""
        if name in self.required_properties:
            return self.__dict__[name]

        # get the attribute from the correct instance
        model_instances = self._var_name_to_model_instances.get(name)
        values = []
        # A composed model stores self and child (oneof/anyOf/allOf) models under
        # self._var_name_to_model_instances.
        # Any property must exist in self and all model instances
        # The value stored in all model instances must be the same
        if model_instances:
            for model_instance in model_instances:
                if name in model_instance._data_store:
                    v = model_instance._data_store[name]
                    if v not in values:
                        values.append(v)
        len_values = len(values)
        if len_values == 0:
            return default
        elif len_values == 1:
            return values[0]
        elif len_values > 1:
            raise ApiValueError(
                "Values stored for property {0} in {1} differ when looking "
                "at self and self's composed instances. All values must be "
                "the same".format(name, type(self).__name__),
                [e for e in [self._path_to_item, name] if e]
            )

    def __getitem__(self, name):
        """get the value of an attribute using square-bracket notation: `instance[attr]`"""
        value = self.get(name, self.__unset_attribute_value__)
        if value is self.__unset_attribute_value__:
            raise ApiAttributeError(
                "{0} has no attribute '{1}'".format(
                    type(self).__name__, name),
                    [e for e in [self._path_to_item, name] if e]
            )
        return value

    def __contains__(self, name):
        """used by `in` operator to check if an attribute value was set in an instance: `'attr' in instance`"""

        if name in self.required_properties:
            return name in self.__dict__

        model_instances = self._var_name_to_model_instances.get(
            name, self._additional_properties_model_instances)

        if model_instances:
            for model_instance in model_instances:
                if name in model_instance._data_store:
                    return True

        return False

    def to_dict(self):
        """Returns the model properties as a dict"""
        return model_to_dict(self, serialize=False)

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, self.__class__):
            return False

        if not set(self._data_store.keys()) == set(other._data_store.keys()):
            return False
        for _var_name, this_val in self._data_store.items():
            that_val = other._data_store[_var_name]
            types = set()
            types.add(this_val.__class__)
            types.add(that_val.__class__)
            vals_equal = this_val == that_val
            if not vals_equal:
                return False
        return True


COERCION_INDEX_BY_TYPE = {
    ModelComposed: 0,
    ModelNormal: 1,
    ModelSimple: 2,
    none_type: 3,    # The type of 'None'.
    list: 4,
    dict: 5,
    float: 6,
    int: 7,
    bool: 8,
    datetime: 9,
    date: 10,
    str: 11,
    file_type: 12,   # 'file_type' is an alias for the built-in 'file' or 'io.IOBase' type.
}

# these are used to limit what type conversions we try to do
# when we have a valid type already and we want to try converting
# to another type
UPCONVERSION_TYPE_PAIRS = (
    (str, datetime),
    (str, date),
    # A float may be serialized as an integer, e.g. '3' is a valid serialized float.
    (int, float),
    (list, ModelComposed),
    (dict, ModelComposed),
    (str, ModelComposed),
    (int, ModelComposed),
    (float, ModelComposed),
    (list, ModelComposed),
    (list, ModelNormal),
    (dict, ModelNormal),
    (str, ModelSimple),
    (int, ModelSimple),
    (float, ModelSimple),
    (list, ModelSimple),
)

COERCIBLE_TYPE_PAIRS = {
    False: (  # client instantiation of a model with client data
        # (dict, ModelComposed),
        # (list, ModelComposed),
        # (dict, ModelNormal),
        # (list, ModelNormal),
        # (str, ModelSimple),
        # (int, ModelSimple),
        # (float, ModelSimple),
        # (list, ModelSimple),
        # (str, int),
        # (str, float),
        # (str, datetime),
        # (str, date),
        # (int, str),
        # (float, str),
    ),
    True: (  # server -> client data
        (dict, ModelComposed),
        (list, ModelComposed),
        (dict, ModelNormal),
        (list, ModelNormal),
        (str, ModelSimple),
        (int, ModelSimple),
        (float, ModelSimple),
        (list, ModelSimple),
        # (str, int),
        # (str, float),
        (str, datetime),
        (str, date),
        # (int, str),
        # (float, str),
        (str, file_type)
    ),
}


def get_simple_class(input_value):
    """Returns an input_value's simple class that we will use for type checking
    Python2:
    float and int will return int, where int is the python3 int backport
    str and unicode will return str, where str is the python3 str backport
    Note: float and int ARE both instances of int backport
    Note: str_py2 and unicode_py2 are NOT both instances of str backport

    Args:
        input_value (class/class_instance): the item for which we will return
                                            the simple class
    """
    if isinstance(input_value, type):
        # input_value is a class
        return input_value
    elif isinstance(input_value, tuple):
        return tuple
    elif isinstance(input_value, list):
        return list
    elif isinstance(input_value, dict):
        return dict
    elif isinstance(input_value, none_type):
        return none_type
    elif isinstance(input_value, file_type):
        return file_type
    elif isinstance(input_value, bool):
        # this must be higher than the int check because
        # isinstance(True, int) == True
        return bool
    elif isinstance(input_value, int):
        return int
    elif isinstance(input_value, datetime):
        # this must be higher than the date check because
        # isinstance(datetime_instance, date) == True
        return datetime
    elif isinstance(input_value, date):
        return date
    elif isinstance(input_value, str):
        return str
    return type(input_value)


def check_allowed_values(allowed_values, input_variable_path, input_values):
    """Raises an exception if the input_values are not allowed

    Args:
        allowed_values (dict): the allowed_values dict
        input_variable_path (tuple): the path to the input variable
        input_values (list/str/int/float/date/datetime): the values that we
            are checking to see if they are in allowed_values
    """
    these_allowed_values = list(allowed_values[input_variable_path].values())
    if (isinstance(input_values, list)
            and not set(input_values).issubset(
                set(these_allowed_values))):
        invalid_values = ", ".join(
            map(str, set(input_values) - set(these_allowed_values))),
        raise ApiValueError(
            "Invalid values for `%s` [%s], must be a subset of [%s]" %
            (
                input_variable_path[0],
                invalid_values,
                ", ".join(map(str, these_allowed_values))
            )
        )
    elif (isinstance(input_values, dict)
            and not set(
                input_values.keys()).issubset(set(these_allowed_values))):
        invalid_values = ", ".join(
            map(str, set(input_values.keys()) - set(these_allowed_values)))
        raise ApiValueError(
            "Invalid keys in `%s` [%s], must be a subset of [%s]" %
            (
                input_variable_path[0],
                invalid_values,
                ", ".join(map(str, these_allowed_values))
            )
        )
    elif (not isinstance(input_values, (list, dict))
            and input_values not in these_allowed_values):
        raise ApiValueError(
            "Invalid value for `%s` (%s), must be one of %s" %
            (
                input_variable_path[0],
                input_values,
                these_allowed_values
            )
        )


def is_json_validation_enabled(schema_keyword, configuration=None):
    """Returns true if JSON schema validation is enabled for the specified
    validation keyword. This can be used to skip JSON schema structural validation
    as requested in the configuration.

    Args:
        schema_keyword (string): the name of a JSON schema validation keyword.
        configuration (Configuration): the configuration class.
    """

    return (configuration is None or
            not hasattr(configuration, '_disabled_client_side_validations') or
            schema_keyword not in configuration._disabled_client_side_validations)


def check_validations(
        validations, input_variable_path, input_values,
        configuration=None):
    """Raises an exception if the input_values are invalid

    Args:
        validations (dict): the validation dictionary.
        input_variable_path (tuple): the path to the input variable.
        input_values (list/str/int/float/date/datetime): the values that we
            are checking.
        configuration (Configuration): the configuration class.
    """

    if input_values is None:
        return

    current_validations = validations[input_variable_path]
    if (is_json_validation_enabled('multipleOf', configuration) and
            'multiple_of' in current_validations and
            isinstance(input_values, (int, float)) and
            not (float(input_values) / current_validations['multiple_of']).is_integer()):
        # Note 'multipleOf' will be as good as the floating point arithmetic.
        raise ApiValueError(
            "Invalid value for `%s`, value must be a multiple of "
            "`%s`" % (
                input_variable_path[0],
                current_validations['multiple_of']
            )
        )

    if (is_json_validation_enabled('maxLength', configuration) and
            'max_length' in current_validations and
            len(input_values) > current_validations['max_length']):
        raise ApiValueError(
            "Invalid value for `%s`, length must be less than or equal to "
            "`%s`" % (
                input_variable_path[0],
                current_validations['max_length']
            )
        )

    if (is_json_validation_enabled('minLength', configuration) and
            'min_length' in current_validations and
            len(input_values) < current_validations['min_length']):
        raise ApiValueError(
            "Invalid value for `%s`, length must be greater than or equal to "
            "`%s`" % (
                input_variable_path[0],
                current_validations['min_length']
            )
        )

    if (is_json_validation_enabled('maxItems', configuration) and
            'max_items' in current_validations and
            len(input_values) > current_validations['max_items']):
        raise ApiValueError(
            "Invalid value for `%s`, number of items must be less than or "
            "equal to `%s`" % (
                input_variable_path[0],
                current_validations['max_items']
            )
        )

    if (is_json_validation_enabled('minItems', configuration) and
            'min_items' in current_validations and
            len(input_values) < current_validations['min_items']):
        raise ValueError(
            "Invalid value for `%s`, number of items must be greater than or "
            "equal to `%s`" % (
                input_variable_path[0],
                current_validations['min_items']
            )
        )

    items = ('exclusive_maximum', 'inclusive_maximum', 'exclusive_minimum',
             'inclusive_minimum')
    if (any(item in current_validations for item in items)):
        if isinstance(input_values, list):
            max_val = max(input_values)
            min_val = min(input_values)
        elif isinstance(input_values, dict):
            max_val = max(input_values.values())
            min_val = min(input_values.values())
        else:
            max_val = input_values
            min_val = input_values

    if (is_json_validation_enabled('exclusiveMaximum', configuration) and
            'exclusive_maximum' in current_validations and
            max_val >= current_validations['exclusive_maximum']):
        raise ApiValueError(
            "Invalid value for `%s`, must be a value less than `%s`" % (
                input_variable_path[0],
                current_validations['exclusive_maximum']
            )
        )

    if (is_json_validation_enabled('maximum', configuration) and
            'inclusive_maximum' in current_validations and
            max_val > current_validations['inclusive_maximum']):
        raise ApiValueError(
            "Invalid value for `%s`, must be a value less than or equal to "
            "`%s`" % (
                input_variable_path[0],
                current_validations['inclusive_maximum']
            )
        )

    if (is_json_validation_enabled('exclusiveMinimum', configuration) and
            'exclusive_minimum' in current_validations and
            min_val <= current_validations['exclusive_minimum']):
        raise ApiValueError(
            "Invalid value for `%s`, must be a value greater than `%s`" %
            (
                input_variable_path[0],
                current_validations['exclusive_maximum']
            )
        )

    if (is_json_validation_enabled('minimum', configuration) and
            'inclusive_minimum' in current_validations and
            min_val < current_validations['inclusive_minimum']):
        raise ApiValueError(
            "Invalid value for `%s`, must be a value greater than or equal "
            "to `%s`" % (
                input_variable_path[0],
                current_validations['inclusive_minimum']
            )
        )
    flags = current_validations.get('regex', {}).get('flags', 0)
    if (is_json_validation_enabled('pattern', configuration) and
            'regex' in current_validations and
            not re.search(current_validations['regex']['pattern'],
                          input_values, flags=flags)):
        err_msg = r"Invalid value for `%s`, must match regular expression `%s`" % (
            input_variable_path[0],
            current_validations['regex']['pattern']
        )
        if flags != 0:
            # Don't print the regex flags if the flags are not
            # specified in the OAS document.
            err_msg = r"%s with flags=`%s`" % (err_msg, flags)
        raise ApiValueError(err_msg)


def order_response_types(required_types):
    """Returns the required types sorted in coercion order

    Args:
        required_types (list/tuple): collection of classes or instance of
            list or dict with class information inside it.

    Returns:
        (list): coercion order sorted collection of classes or instance
            of list or dict with class information inside it.
    """

    def index_getter(class_or_instance):
        if isinstance(class_or_instance, list):
            return COERCION_INDEX_BY_TYPE[list]
        elif isinstance(class_or_instance, dict):
            return COERCION_INDEX_BY_TYPE[dict]
        elif (inspect.isclass(class_or_instance)
                and issubclass(class_or_instance, ModelComposed)):
            return COERCION_INDEX_BY_TYPE[ModelComposed]
        elif (inspect.isclass(class_or_instance)
                and issubclass(class_or_instance, ModelNormal)):
            return COERCION_INDEX_BY_TYPE[ModelNormal]
        elif (inspect.isclass(class_or_instance)
                and issubclass(class_or_instance, ModelSimple)):
            return COERCION_INDEX_BY_TYPE[ModelSimple]
        elif class_or_instance in COERCION_INDEX_BY_TYPE:
            return COERCION_INDEX_BY_TYPE[class_or_instance]
        raise ApiValueError("Unsupported type: %s" % class_or_instance)

    sorted_types = sorted(
        required_types,
        key=lambda class_or_instance: index_getter(class_or_instance)
    )
    return sorted_types


def remove_uncoercible(required_types_classes, current_item, spec_property_naming,
                       must_convert=True):
    """Only keeps the type conversions that are possible

    Args:
        required_types_classes (tuple): tuple of classes that are required
                          these should be ordered by COERCION_INDEX_BY_TYPE
        spec_property_naming (bool): True if the variable names in the input
            data are serialized names as specified in the OpenAPI document.
            False if the variables names in the input data are python
            variable names in PEP-8 snake case.
        current_item (any): the current item (input data) to be converted

    Keyword Args:
        must_convert (bool): if True the item to convert is of the wrong
                          type and we want a big list of coercibles
                          if False, we want a limited list of coercibles

    Returns:
        (list): the remaining coercible required types, classes only
    """
    current_type_simple = get_simple_class(current_item)

    results_classes = []
    for required_type_class in required_types_classes:
        # convert our models to OpenApiModel
        required_type_class_simplified = required_type_class
        if isinstance(required_type_class_simplified, type):
            if issubclass(required_type_class_simplified, ModelComposed):
                required_type_class_simplified = ModelComposed
            elif issubclass(required_type_class_simplified, ModelNormal):
                required_type_class_simplified = ModelNormal
            elif issubclass(required_type_class_simplified, ModelSimple):
                required_type_class_simplified = ModelSimple

        if required_type_class_simplified == current_type_simple:
            # don't consider converting to one's own class
            continue

        class_pair = (current_type_simple, required_type_class_simplified)
        if must_convert and class_pair in COERCIBLE_TYPE_PAIRS[spec_property_naming]:
            results_classes.append(required_type_class)
        elif class_pair in UPCONVERSION_TYPE_PAIRS:
            results_classes.append(required_type_class)
    return results_classes


def get_discriminated_classes(cls):
    """
    Returns all the classes that a discriminator converts to
    TODO: lru_cache this
    """
    possible_classes = []
    key = list(cls.discriminator.keys())[0]
    if is_type_nullable(cls):
        possible_classes.append(cls)
    for discr_cls in cls.discriminator[key].values():
        if hasattr(discr_cls, 'discriminator') and discr_cls.discriminator is not None:
            possible_classes.extend(get_discriminated_classes(discr_cls))
        else:
            possible_classes.append(discr_cls)
    return possible_classes


def get_possible_classes(cls, from_server_context):
    # TODO: lru_cache this
    possible_classes = [cls]
    if from_server_context:
        return possible_classes
    if hasattr(cls, 'discriminator') and cls.discriminator is not None:
        possible_classes = []
        possible_classes.extend(get_discriminated_classes(cls))
    elif issubclass(cls, ModelComposed):
        possible_classes.extend(composed_model_input_classes(cls))
    return possible_classes


def get_required_type_classes(required_types_mixed, spec_property_naming):
    """Converts the tuple required_types into a tuple and a dict described
    below

    Args:
        required_types_mixed (tuple/list): will contain either classes or
            instance of list or dict
        spec_property_naming (bool): if True these values came from the
            server, and we use the data types in our endpoints.
            If False, we are client side and we need to include
            oneOf and discriminator classes inside the data types in our endpoints

    Returns:
        (valid_classes, dict_valid_class_to_child_types_mixed):
            valid_classes (tuple): the valid classes that the current item
                                   should be
            dict_valid_class_to_child_types_mixed (dict):
                valid_class (class): this is the key
                child_types_mixed (list/dict/tuple): describes the valid child
                    types
    """
    valid_classes = []
    child_req_types_by_current_type = {}
    for required_type in required_types_mixed:
        if isinstance(required_type, list):
            valid_classes.append(list)
            child_req_types_by_current_type[list] = required_type
        elif isinstance(required_type, tuple):
            valid_classes.append(tuple)
            child_req_types_by_current_type[tuple] = required_type
        elif isinstance(required_type, dict):
            valid_classes.append(dict)
            child_req_types_by_current_type[dict] = required_type[str]
        else:
            valid_classes.extend(get_possible_classes(required_type, spec_property_naming))
    return tuple(valid_classes), child_req_types_by_current_type


def change_keys_js_to_python(input_dict, model_class):
    """
    Converts from javascript_key keys in the input_dict to python_keys in
    the output dict using the mapping in model_class.
    If the input_dict contains a key which does not declared in the model_class,
    the key is added to the output dict as is. The assumption is the model_class
    may have undeclared properties (additionalProperties attribute in the OAS
    document).
    """

    if getattr(model_class, 'attribute_map', None) is None:
        return input_dict
    output_dict = {}
    reversed_attr_map = {value: key for key, value in
                         model_class.attribute_map.items()}
    for javascript_key, value in input_dict.items():
        python_key = reversed_attr_map.get(javascript_key)
        if python_key is None:
            # if the key is unknown, it is in error or it is an
            # additionalProperties variable
            python_key = javascript_key
        output_dict[python_key] = value
    return output_dict


def get_type_error(var_value, path_to_item, valid_classes, key_type=False):
    error_msg = type_error_message(
        var_name=path_to_item[-1],
        var_value=var_value,
        valid_classes=valid_classes,
        key_type=key_type
    )
    return ApiTypeError(
        error_msg,
        path_to_item=path_to_item,
        valid_classes=valid_classes,
        key_type=key_type
    )


def deserialize_primitive(data, klass, path_to_item):
    """Deserializes string to primitive type.

    :param data: str/int/float
    :param klass: str/class the class to convert to

    :return: int, float, str, bool, date, datetime
    """
    additional_message = ""
    try:
        if klass in {datetime, date}:
            additional_message = (
                "If you need your parameter to have a fallback "
                "string value, please set its type as `type: {}` in your "
                "spec. That allows the value to be any type. "
            )
            if klass == datetime:
                if len(data) < 8:
                    raise ValueError("This is not a datetime")
                # The string should be in iso8601 datetime format.
                parsed_datetime = parse(data)
                date_only = (
                    parsed_datetime.hour == 0 and
                    parsed_datetime.minute == 0 and
                    parsed_datetime.second == 0 and
                    parsed_datetime.tzinfo is None and
                    8 <= len(data) <= 10
                )
                if date_only:
                    raise ValueError("This is a date, not a datetime")
                return parsed_datetime
            elif klass == date:
                if len(data) < 8:
                    raise ValueError("This is not a date")
                return parse(data).date()
        else:
            converted_value = klass(data)
            if isinstance(data, str) and klass == float:
                if str(converted_value) != data:
                    # '7' -> 7.0 -> '7.0' != '7'
                    raise ValueError('This is not a float')
            return converted_value
    except (OverflowError, ValueError) as ex:
        # parse can raise OverflowError
        raise ApiValueError(
            "{0}Failed to parse {1} as {2}".format(
                additional_message, repr(data), klass.__name__
            ),
            path_to_item=path_to_item
        ) from ex


def get_discriminator_class(model_class,
                            discr_name,
                            discr_value, cls_visited):
    """Returns the child class specified by the discriminator.

    Args:
        model_class (OpenApiModel): the model class.
        discr_name (string): the name of the discriminator property.
        discr_value (any): the discriminator value.
        cls_visited (list): list of model classes that have been visited.
            Used to determine the discriminator class without
            visiting circular references indefinitely.

    Returns:
        used_model_class (class/None): the chosen child class that will be used
            to deserialize the data, for example dog.Dog.
            If a class is not found, None is returned.
    """

    if model_class in cls_visited:
        # The class has already been visited and no suitable class was found.
        return None
    cls_visited.append(model_class)
    used_model_class = None
    if discr_name in model_class.discriminator:
        class_name_to_discr_class = model_class.discriminator[discr_name]
        used_model_class = class_name_to_discr_class.get(discr_value)
    if used_model_class is None:
        # We didn't find a discriminated class in class_name_to_discr_class.
        # So look in the ancestor or descendant discriminators
        # The discriminator mapping may exist in a descendant (anyOf, oneOf)
        # or ancestor (allOf).
        # Ancestor example: in the GrandparentAnimal -> ParentPet -> ChildCat
        #   hierarchy, the discriminator mappings may be defined at any level
        #   in the hierarchy.
        # Descendant example:  mammal -> whale/zebra/Pig -> BasquePig/DanishPig
        #   if we try to make BasquePig from mammal, we need to travel through
        #   the oneOf descendant discriminators to find BasquePig
        descendant_classes = model_class._composed_schemas.get('oneOf', ()) + \
            model_class._composed_schemas.get('anyOf', ())
        ancestor_classes = model_class._composed_schemas.get('allOf', ())
        possible_classes = descendant_classes + ancestor_classes
        for cls in possible_classes:
            # Check if the schema has inherited discriminators.
            if hasattr(cls, 'discriminator') and cls.discriminator is not None:
                used_model_class = get_discriminator_class(
                    cls, discr_name, discr_value, cls_visited)
                if used_model_class is not None:
                    return used_model_class
    return used_model_class


def deserialize_model(model_data, model_class, path_to_item, check_type,
                      configuration, spec_property_naming):
    """Deserializes model_data to model instance.

    Args:
        model_data (int/str/float/bool/none_type/list/dict): data to instantiate the model
        model_class (OpenApiModel): the model class
        path_to_item (list): path to the model in the received data
        check_type (bool): whether to check the data tupe for the values in
            the model
        configuration (Configuration): the instance to use to convert files
        spec_property_naming (bool): True if the variable names in the input
            data are serialized names as specified in the OpenAPI document.
            False if the variables names in the input data are python
            variable names in PEP-8 snake case.

    Returns:
        model instance

    Raise:
        ApiTypeError
        ApiValueError
        ApiKeyError
    """

    kw_args = dict(_check_type=check_type,
                   _path_to_item=path_to_item,
                   _configuration=configuration,
                   _spec_property_naming=spec_property_naming)

    if issubclass(model_class, ModelSimple):
        return model_class._new_from_openapi_data(model_data, **kw_args)
    elif isinstance(model_data, list):
        return model_class._new_from_openapi_data(*model_data, **kw_args)
    if isinstance(model_data, dict):
        kw_args.update(model_data)
        return model_class._new_from_openapi_data(**kw_args)
    elif isinstance(model_data, PRIMITIVE_TYPES):
        return model_class._new_from_openapi_data(model_data, **kw_args)


def deserialize_file(response_data, configuration, content_disposition=None):
    """Deserializes body to file

    Saves response body into a file in a temporary folder,
    using the filename from the `Content-Disposition` header if provided.

    Args:
        param response_data (str):  the file data to write
        configuration (Configuration): the instance to use to convert files

    Keyword Args:
        content_disposition (str):  the value of the Content-Disposition
            header

    Returns:
        (file_type): the deserialized file which is open
            The user is responsible for closing and reading the file
    """
    fd, path = tempfile.mkstemp(dir=configuration.temp_folder_path)
    os.close(fd)
    os.remove(path)

    if content_disposition:
        filename = re.search(r'filename=[\'"]?([^\'"\s]+)[\'"]?',
                             content_disposition,
                             flags=re.I)
        if filename is not None:
            filename = filename.group(1)
        else:
            filename = "default_" + str(uuid.uuid4())

        path = os.path.join(os.path.dirname(path), filename)

    with open(path, "wb") as f:
        if isinstance(response_data, str):
            # change str to bytes so we can write it
            response_data = response_data.encode('utf-8')
        f.write(response_data)

    f = open(path, "rb")
    return f


def attempt_convert_item(input_value, valid_classes, path_to_item,
                         configuration, spec_property_naming, key_type=False,
                         must_convert=False, check_type=True):
    """
    Args:
        input_value (any): the data to convert
        valid_classes (any): the classes that are valid
        path_to_item (list): the path to the item to convert
        configuration (Configuration): the instance to use to convert files
        spec_property_naming (bool): True if the variable names in the input
            data are serialized names as specified in the OpenAPI document.
            False if the variables names in the input data are python
            variable names in PEP-8 snake case.
        key_type (bool): if True we need to convert a key type (not supported)
        must_convert (bool): if True we must convert
        check_type (bool): if True we check the type or the returned data in
            ModelComposed/ModelNormal/ModelSimple instances

    Returns:
        instance (any) the fixed item

    Raises:
        ApiTypeError
        ApiValueError
        ApiKeyError
    """
    valid_classes_ordered = order_response_types(valid_classes)
    valid_classes_coercible = remove_uncoercible(
        valid_classes_ordered, input_value, spec_property_naming)
    if not valid_classes_coercible or key_type:
        # we do not handle keytype errors, json will take care
        # of this for us
        if configuration is None or not configuration.discard_unknown_keys:
            raise get_type_error(input_value, path_to_item, valid_classes,
                                 key_type=key_type)
    for valid_class in valid_classes_coercible:
        try:
            if issubclass(valid_class, OpenApiModel):
                return deserialize_model(input_value, valid_class,
                                         path_to_item, check_type,
                                         configuration, spec_property_naming)
            elif valid_class == file_type:
                return deserialize_file(input_value, configuration)
            return deserialize_primitive(input_value, valid_class,
                                         path_to_item)
        except (ApiTypeError, ApiValueError, ApiKeyError) as conversion_exc:
            if must_convert:
                raise conversion_exc
            # if we have conversion errors when must_convert == False
            # we ignore the exception and move on to the next class
            continue
    # we were unable to convert, must_convert == False
    return input_value


def is_type_nullable(input_type):
    """
    Returns true if None is an allowed value for the specified input_type.

    A type is nullable if at least one of the following conditions is true:
    1. The OAS 'nullable' attribute has been specified,
    1. The type is the 'null' type,
    1. The type is a anyOf/oneOf composed schema, and a child schema is
       the 'null' type.
    Args:
        input_type (type): the class of the input_value that we are
            checking
    Returns:
        bool
    """
    if input_type is none_type:
        return True
    if issubclass(input_type, OpenApiModel) and input_type._nullable:
        return True
    if issubclass(input_type, ModelComposed):
        # If oneOf/anyOf, check if the 'null' type is one of the allowed types.
        for t in input_type._composed_schemas.get('oneOf', ()):
            if is_type_nullable(t):
                return True
        for t in input_type._composed_schemas.get('anyOf', ()):
            if is_type_nullable(t):
                return True
    return False


def is_valid_type(input_class_simple, valid_classes):
    """
    Args:
        input_class_simple (class): the class of the input_value that we are
            checking
        valid_classes (tuple): the valid classes that the current item
            should be
    Returns:
        bool
    """
    if issubclass(input_class_simple, OpenApiModel) and \
            valid_classes == (bool, date, datetime, dict, float, int, list, str, none_type,):
        return True
    valid_type = input_class_simple in valid_classes
    if not valid_type and (
            issubclass(input_class_simple, OpenApiModel) or
            input_class_simple is none_type):
        for valid_class in valid_classes:
            if input_class_simple is none_type and is_type_nullable(valid_class):
                # Schema is oneOf/anyOf and the 'null' type is one of the allowed types.
                return True
            if not (issubclass(valid_class, OpenApiModel) and valid_class.discriminator):
                continue
            discr_propertyname_py = list(valid_class.discriminator.keys())[0]
            discriminator_classes = (
                valid_class.discriminator[discr_propertyname_py].values()
            )
            valid_type = is_valid_type(input_class_simple, discriminator_classes)
            if valid_type:
                return True
    return valid_type


def validate_and_convert_types(input_value, required_types_mixed, path_to_item,
                               spec_property_naming, _check_type, configuration=None):
    """Raises a TypeError is there is a problem, otherwise returns value

    Args:
        input_value (any): the data to validate/convert
        required_types_mixed (list/dict/tuple): A list of
            valid classes, or a list tuples of valid classes, or a dict where
            the value is a tuple of value classes
        path_to_item: (list) the path to the data being validated
            this stores a list of keys or indices to get to the data being
            validated
        spec_property_naming (bool): True if the variable names in the input
            data are serialized names as specified in the OpenAPI document.
            False if the variables names in the input data are python
            variable names in PEP-8 snake case.
        _check_type: (boolean) if true, type will be checked and conversion
            will be attempted.
        configuration: (Configuration): the configuration class to use
            when converting file_type items.
            If passed, conversion will be attempted when possible
            If not passed, no conversions will be attempted and
            exceptions will be raised

    Returns:
        the correctly typed value

    Raises:
        ApiTypeError
    """
    results = get_required_type_classes(required_types_mixed, spec_property_naming)
    valid_classes, child_req_types_by_current_type = results

    input_class_simple = get_simple_class(input_value)
    valid_type = is_valid_type(input_class_simple, valid_classes)
    if not valid_type:
        if (configuration
                or (input_class_simple == dict
                    and dict not in valid_classes)):
            # if input_value is not valid_type try to convert it
            converted_instance = attempt_convert_item(
                input_value,
                valid_classes,
                path_to_item,
                configuration,
                spec_property_naming,
                key_type=False,
                must_convert=True,
                check_type=_check_type
            )
            return converted_instance
        else:
            raise get_type_error(input_value, path_to_item, valid_classes,
                                 key_type=False)

    # input_value's type is in valid_classes
    if len(valid_classes) > 1 and configuration:
        # there are valid classes which are not the current class
        valid_classes_coercible = remove_uncoercible(
            valid_classes, input_value, spec_property_naming, must_convert=False)
        if valid_classes_coercible:
            converted_instance = attempt_convert_item(
                input_value,
                valid_classes_coercible,
                path_to_item,
                configuration,
                spec_property_naming,
                key_type=False,
                must_convert=False,
                check_type=_check_type
            )
            return converted_instance

    if child_req_types_by_current_type == {}:
        # all types are of the required types and there are no more inner
        # variables left to look at
        return input_value
    inner_required_types = child_req_types_by_current_type.get(
        type(input_value)
    )
    if inner_required_types is None:
        # for this type, there are not more inner variables left to look at
        return input_value
    if isinstance(input_value, list):
        if input_value == []:
            # allow an empty list
            return input_value
        for index, inner_value in enumerate(input_value):
            inner_path = list(path_to_item)
            inner_path.append(index)
            input_value[index] = validate_and_convert_types(
                inner_value,
                inner_required_types,
                inner_path,
                spec_property_naming,
                _check_type,
                configuration=configuration
            )
    elif isinstance(input_value, dict):
        if input_value == {}:
            # allow an empty dict
            return input_value
        for inner_key, inner_val in input_value.items():
            inner_path = list(path_to_item)
            inner_path.append(inner_key)
            if get_simple_class(inner_key) != str:
                raise get_type_error(inner_key, inner_path, valid_classes,
                                     key_type=True)
            input_value[inner_key] = validate_and_convert_types(
                inner_val,
                inner_required_types,
                inner_path,
                spec_property_naming,
                _check_type,
                configuration=configuration
            )
    return input_value


def model_to_dict(model_instance, serialize=True):
    """Returns the model properties as a dict

    Args:
        model_instance (one of your model instances): the model instance that
            will be converted to a dict.

    Keyword Args:
        serialize (bool): if True, the keys in the dict will be values from
            attribute_map
    """
    result = {}

    def extract_item(item): return (
        item[0], model_to_dict(
            item[1], serialize=serialize)) if hasattr(
        item[1], '_data_store') else item

    model_instances = [model_instance]
    if model_instance._composed_schemas:
        model_instances.extend(model_instance._composed_instances)
    seen_json_attribute_names = set()
    used_fallback_python_attribute_names = set()
    py_to_json_map = {}
    for model_instance in model_instances:
        for attr, value in model_instance._data_store.items():
            if serialize:
                # we use get here because additional property key names do not
                # exist in attribute_map
                try:
                    attr = model_instance.attribute_map[attr]
                    py_to_json_map.update(model_instance.attribute_map)
                    seen_json_attribute_names.add(attr)
                except KeyError:
                    used_fallback_python_attribute_names.add(attr)
            if isinstance(value, list):
                if not value:
                    # empty list or None
                    result[attr] = value
                else:
                    res = []
                    for v in value:
                        if isinstance(v, PRIMITIVE_TYPES) or v is None:
                            res.append(v)
                        elif isinstance(v, ModelSimple):
                            res.append(v.value)
                        elif isinstance(v, dict):
                            res.append(dict(map(
                                extract_item,
                                v.items()
                            )))
                        else:
                            res.append(model_to_dict(v, serialize=serialize))
                    result[attr] = res
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    extract_item,
                    value.items()
                ))
            elif isinstance(value, ModelSimple):
                result[attr] = value.value
            elif hasattr(value, '_data_store'):
                result[attr] = model_to_dict(value, serialize=serialize)
            else:
                result[attr] = value
    if serialize:
        for python_key in used_fallback_python_attribute_names:
            json_key = py_to_json_map.get(python_key)
            if json_key is None:
                continue
            if python_key == json_key:
                continue
            json_key_assigned_no_need_for_python_key = json_key in seen_json_attribute_names
            if json_key_assigned_no_need_for_python_key:
                del result[python_key]

    return result


def type_error_message(var_value=None, var_name=None, valid_classes=None,
                       key_type=None):
    """
    Keyword Args:
        var_value (any): the variable which has the type_error
        var_name (str): the name of the variable which has the typ error
        valid_classes (tuple): the accepted classes for current_item's
                                  value
        key_type (bool): False if our value is a value in a dict
                         True if it is a key in a dict
                         False if our item is an item in a list
    """
    key_or_value = 'value'
    if key_type:
        key_or_value = 'key'
    valid_classes_phrase = get_valid_classes_phrase(valid_classes)
    msg = (
        "Invalid type for variable '{0}'. Required {1} type {2} and "
        "passed type was {3}".format(
            var_name,
            key_or_value,
            valid_classes_phrase,
            type(var_value).__name__,
        )
    )
    return msg


def get_valid_classes_phrase(input_classes):
    """Returns a string phrase describing what types are allowed
    """
    all_classes = list(input_classes)
    all_classes = sorted(all_classes, key=lambda cls: cls.__name__)
    all_class_names = [cls.__name__ for cls in all_classes]
    if len(all_class_names) == 1:
        return 'is {0}'.format(all_class_names[0])
    return "is one of [{0}]".format(", ".join(all_class_names))


def get_allof_instances(self, model_args, constant_args):
    """
    Args:
        self: the class we are handling
        model_args (dict): var_name to var_value
            used to make instances
        constant_args (dict):
            metadata arguments:
            _check_type
            _path_to_item
            _spec_property_naming
            _configuration
            _visited_composed_classes

    Returns
        composed_instances (list)
    """
    composed_instances = []
    for allof_class in self._composed_schemas['allOf']:

        try:
            if constant_args.get('_spec_property_naming'):
                allof_instance = allof_class._from_openapi_data(**model_args, **constant_args)
            else:
                allof_instance = allof_class(**model_args, **constant_args)
            composed_instances.append(allof_instance)
        except Exception as ex:
            raise ApiValueError(
                "Invalid inputs given to generate an instance of '%s'. The "
                "input data was invalid for the allOf schema '%s' in the composed "
                "schema '%s'. Error=%s" % (
                    allof_class.__name__,
                    allof_class.__name__,
                    self.__class__.__name__,
                    str(ex)
                )
            ) from ex
    return composed_instances


def get_oneof_instance(cls, model_kwargs, constant_kwargs, model_arg=None):
    """
    Find the oneOf schema that matches the input data (e.g. payload).
    If exactly one schema matches the input data, an instance of that schema
    is returned.
    If zero or more than one schema match the input data, an exception is raised.
    In OAS 3.x, the payload MUST, by validation, match exactly one of the
    schemas described by oneOf.

    Args:
        cls: the class we are handling
        model_kwargs (dict): var_name to var_value
            The input data, e.g. the payload that must match a oneOf schema
            in the OpenAPI document.
        constant_kwargs (dict): var_name to var_value
            args that every model requires, including configuration, server
            and path to item.

    Kwargs:
        model_arg: (int, float, bool, str, date, datetime, ModelSimple, None):
            the value to assign to a primitive class or ModelSimple class
            Notes:
            - this is only passed in when oneOf includes types which are not object
            - None is used to suppress handling of model_arg, nullable models are handled in __new__

    Returns
        oneof_instance (instance)
    """
    if len(cls._composed_schemas['oneOf']) == 0:
        return None

    oneof_instances = []
    # Iterate over each oneOf schema and determine if the input data
    # matches the oneOf schemas.
    for oneof_class in cls._composed_schemas['oneOf']:
        # The composed oneOf schema allows the 'null' type and the input data
        # is the null value. This is a OAS >= 3.1 feature.
        if oneof_class is none_type:
            # skip none_types because we are deserializing dict data.
            # none_type deserialization is handled in the __new__ method
            continue

        single_value_input = allows_single_value_input(oneof_class)

        try:
            if not single_value_input:
                if constant_kwargs.get('_spec_property_naming'):
                    oneof_instance = oneof_class._from_openapi_data(
                        **model_kwargs, **constant_kwargs)
                else:
                    oneof_instance = oneof_class(**model_kwargs, **constant_kwargs)
            else:
                if issubclass(oneof_class, ModelSimple):
                    if constant_kwargs.get('_spec_property_naming'):
                        oneof_instance = oneof_class._from_openapi_data(
                            model_arg, **constant_kwargs)
                    else:
                        oneof_instance = oneof_class(model_arg, **constant_kwargs)
                elif oneof_class in PRIMITIVE_TYPES:
                    oneof_instance = validate_and_convert_types(
                        model_arg,
                        (oneof_class,),
                        constant_kwargs['_path_to_item'],
                        constant_kwargs['_spec_property_naming'],
                        constant_kwargs['_check_type'],
                        configuration=constant_kwargs['_configuration']
                    )
            oneof_instances.append(oneof_instance)
        except Exception:
            pass
    if len(oneof_instances) == 0:
        raise ApiValueError(
            "Invalid inputs given to generate an instance of %s. None "
            "of the oneOf schemas matched the input data." %
            cls.__name__
        )
    elif len(oneof_instances) > 1:
        raise ApiValueError(
            "Invalid inputs given to generate an instance of %s. Multiple "
            "oneOf schemas matched the inputs, but a max of one is allowed." %
            cls.__name__
        )
    return oneof_instances[0]


def get_anyof_instances(self, model_args, constant_args):
    """
    Args:
        self: the class we are handling
        model_args (dict): var_name to var_value
            The input data, e.g. the payload that must match at least one
            anyOf child schema in the OpenAPI document.
        constant_args (dict): var_name to var_value
            args that every model requires, including configuration, server
            and path to item.

    Returns
        anyof_instances (list)
    """
    anyof_instances = []
    if len(self._composed_schemas['anyOf']) == 0:
        return anyof_instances

    for anyof_class in self._composed_schemas['anyOf']:
        # The composed oneOf schema allows the 'null' type and the input data
        # is the null value. This is a OAS >= 3.1 feature.
        if anyof_class is none_type:
            # skip none_types because we are deserializing dict data.
            # none_type deserialization is handled in the __new__ method
            continue

        try:
            if constant_args.get('_spec_property_naming'):
                anyof_instance = anyof_class._from_openapi_data(**model_args, **constant_args)
            else:
                anyof_instance = anyof_class(**model_args, **constant_args)
            anyof_instances.append(anyof_instance)
        except Exception:
            pass
    if len(anyof_instances) == 0:
        raise ApiValueError(
            "Invalid inputs given to generate an instance of %s. None of the "
            "anyOf schemas matched the inputs." %
            self.__class__.__name__
        )
    return anyof_instances


def get_discarded_args(self, composed_instances, model_args):
    """
    Gathers the args that were discarded by configuration.discard_unknown_keys
    """
    model_arg_keys = model_args.keys()
    discarded_args = set()
    # arguments passed to self were already converted to python names
    # before __init__ was called
    for instance in composed_instances:
        if instance.__class__ in self._composed_schemas['allOf']:
            try:
                keys = instance.to_dict().keys()
                discarded_keys = model_args - keys
                discarded_args.update(discarded_keys)
            except Exception:
                # allOf integer schema will throw exception
                pass
        else:
            try:
                all_keys = set(model_to_dict(instance, serialize=False).keys())
                js_keys = model_to_dict(instance, serialize=True).keys()
                all_keys.update(js_keys)
                discarded_keys = model_arg_keys - all_keys
                discarded_args.update(discarded_keys)
            except Exception:
                # allOf integer schema will throw exception
                pass
    return discarded_args


def validate_get_composed_info(constant_args, model_args, self):
    """
    For composed schemas, generate schema instances for
    all schemas in the oneOf/anyOf/allOf definition. If additional
    properties are allowed, also assign those properties on
    all matched schemas that contain additionalProperties.
    Openapi schemas are python classes.

    Exceptions are raised if:
    - 0 or > 1 oneOf schema matches the model_args input data
    - no anyOf schema matches the model_args input data
    - any of the allOf schemas do not match the model_args input data

    Args:
        constant_args (dict): these are the args that every model requires
        model_args (dict): these are the required and optional spec args that
            were passed in to make this model
        self (class): the class that we are instantiating
            This class contains self._composed_schemas

    Returns:
        composed_info (list): length three
            composed_instances (list): the composed instances which are not
                self
            var_name_to_model_instances (dict): a dict going from var_name
                to the model_instance which holds that var_name
                the model_instance may be self or an instance of one of the
                classes in self.composed_instances()
            additional_properties_model_instances (list): a list of the
                model instances which have the property
                additional_properties_type. This list can include self
    """
    # create composed_instances
    composed_instances = []
    allof_instances = get_allof_instances(self, model_args, constant_args)
    composed_instances.extend(allof_instances)
    oneof_instance = get_oneof_instance(self.__class__, model_args, constant_args)
    if oneof_instance is not None:
        composed_instances.append(oneof_instance)
    anyof_instances = get_anyof_instances(self, model_args, constant_args)
    composed_instances.extend(anyof_instances)
    """
    set additional_properties_model_instances
    additional properties must be evaluated at the schema level
    so self's additional properties are most important
    If self is a composed schema with:
    - no properties defined in self
    - additionalProperties: False
    Then for object payloads every property is an additional property
    and they are not allowed, so only empty dict is allowed

    Properties must be set on all matching schemas
    so when a property is assigned toa composed instance, it must be set on all
    composed instances regardless of additionalProperties presence
    keeping it to prevent breaking changes in v5.0.1
    TODO remove cls._additional_properties_model_instances in 6.0.0
    """
    additional_properties_model_instances = []
    if self.additional_properties_type is not None:
        additional_properties_model_instances = [self]

    """
    no need to set properties on self in here, they will be set in __init__
    By here all composed schema oneOf/anyOf/allOf instances have their properties set using
    model_args
    """
    discarded_args = get_discarded_args(self, composed_instances, model_args)

    # map variable names to composed_instances
    var_name_to_model_instances = {}
    for prop_name in model_args:
        if prop_name not in discarded_args:
            var_name_to_model_instances[prop_name] = [self] + composed_instances

    return [
        composed_instances,
        var_name_to_model_instances,
        additional_properties_model_instances,
        discarded_args
    ]
