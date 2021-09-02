This repository contains a client library for LaunchDarkly's REST API. This client was automatically
generated from our [OpenAPI specification](https://app.launchdarkly.com/api/v2/openapi.json) using a [code generation library](https://github.com/launchdarkly/ld-openapi). View our [sample code](#sample-code) for example usage.

This REST API is for custom integrations, data export, or automating your feature flag workflows. *DO NOT* use this client library to include feature flags in your web or mobile application. To integrate feature flags with your application, read the [SDK documentation](https://docs.launchdarkly.com/sdk).
# launchdarkly-api
# Authentication

All REST API resources are authenticated with either [personal or service access tokens](https://docs.launchdarkly.com/home/account-security/api-access-tokens), or session cookies. Other authentication mechanisms are not supported. You can manage personal access tokens on your [Account settings](https://app.launchdarkly.com/settings/tokens) page.

LaunchDarkly also has SDK keys, mobile keys, and client-side IDs that are used by our server-side SDKs, mobile SDKs, and client-side SDKs, respectively. **These keys cannot be used to access our REST API**. These keys are environment-specific, and can only perform read-only operations (fetching feature flag settings).

| Auth mechanism                                                                                  | Allowed resources                                                                                     | Use cases                                          |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| [Personal access tokens](https://docs.launchdarkly.com/home/account-security/api-access-tokens) | Can be customized on a per-token basis                                                                | Building scripts, custom integrations, data export |
| SDK keys                                                                                        | Can only access read-only SDK-specific resources and the firehose, restricted to a single environment | Server-side SDKs, Firehose API                     |
| Mobile keys                                                                                     | Can only access read-only mobile SDK-specific resources, restricted to a single environment           | Mobile SDKs                                        |
| Client-side ID                                                                                  | Single environment, only flags marked available to client-side                                        | Client-side JavaScript                             |

> ### Keep your access tokens and SDK keys private
>
> Access tokens should _never_ be exposed in untrusted contexts. Never put an access token in client-side JavaScript, or embed it in a mobile application. LaunchDarkly has special mobile keys that you can embed in mobile apps. If you accidentally expose an access token or SDK key, you can reset it from your [Account Settings](https://app.launchdarkly.com/settings#/tokens) page.
>
> The client-side ID is safe to embed in untrusted contexts. It's designed for use in client-side JavaScript.

## Via request header

The preferred way to authenticate with the API is by adding an `Authorization` header containing your access token to your requests. The value of the `Authorization` header must be your access token.

Manage personal access tokens from the [Account Settings](https://app.launchdarkly.com/settings/tokens) page.

## Via session cookie

For testing purposes, you can make API calls directly from your web browser. If you're logged in to the application, the API will use your existing session to authenticate calls.

If you have a [role](https://docs.launchdarkly.com/home/team/built-in-roles) other than Admin, or have a [custom role](https://docs.launchdarkly.com/home/team/custom-roles) defined, you may not have permission to perform some API calls. You will receive a `401` response code in that case.

> ### Modifying the Origin header causes an error
>
> LaunchDarkly validates that the Origin header for any API request authenticated by a session cookie matches the expected Origin header. The expected Origin header is `https://app.launchdarkly.com`.
>
> If the Origin header does not match what's expected, LaunchDarkly returns an error. This error can prevent the LaunchDarkly app from working correctly.
>
> Any browser extension that intentionally changes the Origin header can cause this problem. For example, the `Allow-Control-Allow-Origin: *` Chrome extension changes the Origin header to `http://evil.com` and causes the app to fail.
>
> To prevent this error, do not modify your Origin header.
>
> LaunchDarkly does not require origin matching when authenticating with an access token, so this issue does not affect normal API usage.

# Representations

All resources expect and return JSON response bodies. Error responses will also send a JSON body. Read [Errors](#section/Errors) for a more detailed description of the error format used by the API.

In practice this means that you always get a response with a `Content-Type` header set to `application/json`.

In addition, request bodies for `PUT`, `POST`, `REPORT` and `PATCH` requests must be encoded as JSON with a `Content-Type` header set to `application/json`.

## Summary and detailed representations

When you fetch a list of resources, the response includes only the most important attributes of each resource. This is a _summary representation_ of the resource. When you fetch an individual resource (for example, a single feature flag), you receive a _detailed representation_ containing all of the attributes of the resource.

The best way to find a detailed representation is to follow links. Every summary representation includes a link to its detailed representation.

## Links and addressability

The best way to navigate the API is by following links. These are attributes in representations that link to other resources. The API always uses the same format for links:

- Links to other resources within the API are encapsulated in a `_links` object.
- If the resource has a corresponding link to HTML content on the site, it is stored in a special `_site` link.

Each link has two attributes: an href (the URL) and a type (the content type). For example, a feature resource might return the following:

```json
{
  \"_links\": {
    \"parent\": {
      \"href\": \"/api/features\",
      \"type\": \"application/json\"
    },
    \"self\": {
      \"href\": \"/api/features/sort.order\",
      \"type\": \"application/json\"
    }
  },
  \"_site\": {
    \"href\": \"/features/sort.order\",
    \"type\": \"text/html\"
  }
}
```

From this, you can navigate to the parent collection of features by following the `parent` link, or navigate to the site page for the feature by following the `_site` link.

Collections are always represented as a JSON object with an `items` attribute containing an array of representations. Like all other representations, collections have `_links` defined at the top level.

Paginated collections include `first`, `last`, `next`, and `prev` links containing a URL with the respective set of elements in the collection.

# Updates

Resources that accept partial updates use the `PATCH` verb, and support the [JSON Patch](http://tools.ietf.org/html/rfc6902) format. Some resources also support the [JSON Merge Patch](https://tools.ietf.org/html/rfc7386) format. In addition, some resources support optional comments that can be submitted with updates. Comments appear in outgoing webhooks, the audit log, and other integrations.

## Updates via JSON Patch

[JSON Patch](http://tools.ietf.org/html/rfc6902) is a way to specify the modifications to perform on a resource. For example, in this feature flag representation:

```json
{
    \"name\": \"New recommendations engine\",
    \"key\": \"engine.enable\",
    \"description\": \"This is the description\",
    ...
}
```

You can change the feature flag's description with the following patch document:

```json
[{ \"op\": \"replace\", \"path\": \"/description\", \"value\": \"This is the new description\" }]
```

JSON Patch documents are always arrays. You can specify multiple modifications to perform in a single request. You can also test that certain preconditions are met before applying the patch:

```json
[
  { \"op\": \"test\", \"path\": \"/version\", \"value\": 10 },
  { \"op\": \"replace\", \"path\": \"/description\", \"value\": \"The new description\" }
]
```

The above patch request tests whether the feature flag's `version` is `10`, and if so, changes the feature flag's description.

Attributes that aren't editable, like a resource's `_links`, have names that start with an underscore.

## Updates via JSON Merge Patch

The API also supports the [JSON Merge Patch](https://tools.ietf.org/html/rfc7386) format, as well as the [Update feature flag](/tag/Feature-flags#operation/patchFeatureFlag) resource.

JSON Merge Patch is less expressive than JSON Patch but in many cases, it is simpler to construct a merge patch document. For example, you can change a feature flag's description with the following merge patch document:

```json
{
  \"description\": \"New flag description\"
}
```

## Updates with comments

You can submit optional comments with `PATCH` changes. The [Update feature flag](/tag/Feature-flags#operation/patchFeatureFlag) resource supports comments.

To submit a comment along with a JSON Patch document, use the following format:

```json
{
  \"comment\": \"This is a comment string\",
  \"patch\": [{ \"op\": \"replace\", \"path\": \"/description\", \"value\": \"The new description\" }]
}
```

To submit a comment along with a JSON Merge Patch document, use the following format:

```json
{
  \"comment\": \"This is a comment string\",
  \"merge\": { \"description\": \"New flag description\" }
}
```

## Updates via semantic patches

The API also supports the Semantic patch format. A semantic `PATCH` is a way to specify the modifications to perform on a resource as a set of executable instructions.

JSON Patch uses paths and a limited set of operations to describe how to transform the current state of the resource into a new state. Semantic patch allows you to be explicit about intent using precise, custom instructions. In many cases, semantic patch instructions can also be defined independently of the current state of the resource. This can be useful when defining a change that may be applied at a future date.

For example, in this feature flag configuration in environment Production:

```json
{
    \"name\": \"Alternate sort order\",
    \"kind\": \"boolean\",
    \"key\": \"sort.order\",
   ...
    \"environments\": {
        \"production\": {
            \"on\": true,
            \"archived\": false,
            \"salt\": \"c29ydC5vcmRlcg==\",
            \"sel\": \"8de1085cb7354b0ab41c0e778376dfd3\",
            \"lastModified\": 1469131558260,
            \"version\": 81,
            \"targets\": [
                {
                    \"values\": [
                        \"Gerhard.Little@yahoo.com\"
                    ],
                    \"variation\": 0
                },
                {
                    \"values\": [
                        \"1461797806429-33-861961230\",
                        \"438580d8-02ee-418d-9eec-0085cab2bdf0\"
                    ],
                    \"variation\": 1
                }
            ],
            \"rules\": [],
            \"fallthrough\": {
                \"variation\": 0
            },
            \"offVariation\": 1,
            \"prerequisites\": [],
            \"_site\": {
                \"href\": \"/default/production/features/sort.order\",
                \"type\": \"text/html\"
            }
       }
    }
}
```

You can add a date you want a user to be removed from the feature flag's user targets. For example, “remove user 1461797806429-33-861961230 from the user target for variation 0 on the Alternate sort order flag in the production environment on Wed Jul 08 2020 at 15:27:41 pm”. This is done using the following:

```json
{
  \"comment\": \"update expiring user targets\",
  \"instructions\": [
    {
      \"kind\": \"removeExpireUserTargetDate\",
      \"userKey\": \"userKey\",
      \"variationId\": \"978d53f9-7fe3-4a63-992d-97bcb4535dc8\"
    },
    {
      \"kind\": \"updateExpireUserTargetDate\",
      \"userKey\": \"userKey2\",
      \"variationId\": \"978d53f9-7fe3-4a63-992d-97bcb4535dc8\",
      \"value\": 1587582000000
    },
    {
      \"kind\": \"addExpireUserTargetDate\",
      \"userKey\": \"userKey3\",
      \"variationId\": \"978d53f9-7fe3-4a63-992d-97bcb4535dc8\",
      \"value\": 1594247266386
    }
  ]
}
```

Here is another example. In this feature flag configuration:

```json
{
  \"name\": \"New recommendations engine\",
  \"key\": \"engine.enable\",
  \"environments\": {
    \"test\": {
      \"on\": true
    }
  }
}
```

You can change the feature flag's description with the following patch document as a set of executable instructions. For example, “add user X to targets for variation Y and remove user A from targets for variation B for test flag”:

```json
{
  \"comment\": \"\",
  \"instructions\": [
    {
      \"kind\": \"removeUserTargets\",
      \"values\": [\"438580d8-02ee-418d-9eec-0085cab2bdf0\"],
      \"variationId\": \"852cb784-54ff-46b9-8c35-5498d2e4f270\"
    },
    {
      \"kind\": \"addUserTargets\",
      \"values\": [\"438580d8-02ee-418d-9eec-0085cab2bdf0\"],
      \"variationId\": \"1bb18465-33b6-49aa-a3bd-eeb6650b33ad\"
    }
  ]
}
```

> ### Supported semantic patch API endpoints
>
> - [Update feature flag](/tag/Feature-flags#operation/patchFeatureFlag)
> - [Update expiring user targets on feature flag](/tag/Feature-flags#operation/patchExpiringUserTargets)
> - [Update expiring user target for flags](/tag/User-Settings#operation/patchExpiringFlagsForUser)
> - [Update expiring user targets on segment](/tag/Segments#operation/patchExpiringUserTargetsOnSegment)

# Errors

The API always returns errors in a common format. Here's an example:

```json
{
  \"code\": \"invalid_request\",
  \"message\": \"A feature with that key already exists\",
  \"id\": \"30ce6058-87da-11e4-b116-123b93f75cba\"
}
```

The general class of error is indicated by the `code`. The `message` is a human-readable explanation of what went wrong. The `id` is a unique identifier. Use it when you're working with LaunchDarkly support to debug a problem with a specific API call.

## HTTP Status - Error Response Codes

| Code | Definition        | Desc.                                                                                       | Possible Solution                                                |
| ---- | ----------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| 400  | Bad Request       | A request that fails may return this HTTP response code.                                    | Ensure JSON syntax in request body is correct.                   |
| 401  | Unauthorized      | User doesn't have permission to an API call.                                                | Ensure your SDK key is good.                                     |
| 403  | Forbidden         | User does not have permission for operation.                                                | Ensure that the user or access token has proper permissions set. |
| 409  | Conflict          | The API request could not be completed because it conflicted with a concurrent API request. | Retry your request.                                              |
| 429  | Too many requests | See [Rate limiting](/#section/Rate-limiting).                                               | Wait and try again later.                                        |

# CORS

The LaunchDarkly API supports Cross Origin Resource Sharing (CORS) for AJAX requests from any origin. If an `Origin` header is given in a request, it will be echoed as an explicitly allowed origin. Otherwise, a wildcard is returned: `Access-Control-Allow-Origin: *`. For more information on CORS, see the [CORS W3C Recommendation](http://www.w3.org/TR/cors). Example CORS headers might look like:

```http
Access-Control-Allow-Headers: Accept, Content-Type, Content-Length, Accept-Encoding, Authorization
Access-Control-Allow-Methods: OPTIONS, GET, DELETE, PATCH
Access-Control-Allow-Origin: *
Access-Control-Max-Age: 300
```

You can make authenticated CORS calls just as you would make same-origin calls, using either [token or session-based authentication](#section/Authentication). If you’re using session auth, you should set the `withCredentials` property for your `xhr` request to `true`. You should never expose your access tokens to untrusted users.

# Rate limiting

We use several rate limiting strategies to ensure the availability of our APIs. Rate-limited calls to our APIs will return a `429` status code. Calls to our APIs will include headers indicating the current rate limit status. The specific headers returned depend on the API route being called. The limits differ based on the route, authentication mechanism, and other factors. Routes that are not rate limited may not contain any of the headers described below.

> ### Rate limiting and SDKs
>
> LaunchDarkly SDKs are never rate limited and do not use the API endpoints defined here. LaunchDarkly uses a different set of approaches, including streaming/server-sent events and a global CDN, to ensure availability to the routes used by LaunchDarkly SDKs.
>
> The client-side ID is safe to embed in untrusted contexts. It's designed for use in client-side JavaScript.

## Global rate limits

Authenticated requests are subject to a global limit. This is the maximum number of calls that can be made to the API per ten seconds. All personal access tokens on the account share this limit, so exceeding the limit with one access token will impact other tokens. Calls that are subject to global rate limits will return the headers below:

| Header name                    | Description                                                                      |
| ------------------------------ | -------------------------------------------------------------------------------- |
| `X-Ratelimit-Global-Remaining` | The maximum number of requests the account is permitted to make per ten seconds. |
| `X-Ratelimit-Reset`            | The time at which the current rate limit window resets in epoch milliseconds.    |

We do not publicly document the specific number of calls that can be made globally. This limit may change, and we encourage clients to program against the specification, relying on the two headers defined above, rather than hardcoding to the current limit.

## Route-level rate limits

Some authenticated routes have custom rate limits. These also reset every ten seconds. Any access tokens hitting the same route share this limit, so exceeding the limit with one access token may impact other tokens. Calls that are subject to route-level rate limits will return the headers below:

| Header name                   | Description                                                                                           |
| ----------------------------- | ----------------------------------------------------------------------------------------------------- |
| `X-Ratelimit-Route-Remaining` | The maximum number of requests to the current route the account is permitted to make per ten seconds. |
| `X-Ratelimit-Reset`           | The time at which the current rate limit window resets in epoch milliseconds.                         |

A _route_ represents a specific URL pattern and verb. For example, the [Delete environment](/tag/Environments#operation/deleteEnvironment) endpoint is considered a single route, and each call to delete an environment counts against your route-level rate limit for that route.

We do not publicly document the specific number of calls that can be made to each endpoint per ten seconds. These limits may change, and we encourage clients to program against the specification, relying on the two headers defined above, rather than hardcoding to the current limits.

## IP-based rate limiting

We also employ IP-based rate limiting on some API routes. If you hit an IP-based rate limit, your API response will include a `Retry-After` header indicating how long to wait before re-trying the call. Clients must wait at least `Retry-After` seconds before making additional calls to our API, and should employ jitter and backoff strategies to avoid triggering rate limits again.

# OpenAPI (Swagger)

We have a [complete OpenAPI (Swagger) specification](https://app.launchdarkly.com/api/v2/openapi.json) for our API.

You can use this specification to generate client libraries to interact with our REST API in your language of choice.

This specification is supported by several API-based tools such as Postman and Insomnia. In many cases, you can directly import our specification to ease use in navigating the APIs in the tooling.

# Client libraries

We auto-generate multiple client libraries based on our OpenAPI specification. To learn more, visit [GitHub](https://github.com/search?q=topic%3Alaunchdarkly-api+org%3Alaunchdarkly&type=Repositories).

# Method Overriding

Some firewalls and HTTP clients restrict the use of verbs other than `GET` and `POST`. In those environments, our API endpoints that use `PUT`, `PATCH`, and `DELETE` verbs will be inaccessible.

To avoid this issue, our API supports the `X-HTTP-Method-Override` header, allowing clients to \"tunnel\" `PUT`, `PATCH`, and `DELETE` requests via a `POST` request.

For example, if you wish to call one of our `PATCH` resources via a `POST` request, you can include `X-HTTP-Method-Override:PATCH` as a header.

# Beta resources

We sometimes release new API resources in **beta** status before we release them with general availability.

Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.

We try to promote resources into general availability as quickly as possible. This happens after sufficient testing and when we're satisfied that we no longer need to make backwards-incompatible changes.

We mark beta resources with a \"Beta\" callout in our documentation, pictured below:

> ### This feature is in beta
>
> To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](/#section/Beta-resources).

## Using beta resources

To use a beta resource, you must include a header in the request. If you call a beta resource without this header, you'll receive a `403` response.

Use this header:

```
LD-API-Version: beta
```

# Versioning

We try hard to keep our REST API backwards compatible, but we occasionally have to make backwards-incompatible changes in the process of shipping new features. These breaking changes can cause unexpected behavior if you don't prepare for them accordingly.

Updates to our REST API include support for the latest features in LaunchDarkly. We also release a new version of our REST API every time we make a breaking change. We provide simultaneous support for multiple API versions so you can migrate from your current API version to a new version at your own pace.

## Setting the API version per request

You can set the API version on a specific request by sending an `LD-API-Version` header, as shown in the example below:

```
LD-API-Version: 20191212
```

The header value is the version number of the API version you'd like to request. The number for each version corresponds to the date the version was released. In the example above the version `20191212` corresponds to December 12, 2019.

## Setting the API version per access token

When creating an access token, you must specify a specific version of the API to use. This ensures that integrations using this token cannot be broken by version changes.

Tokens created before versioning was released have their version set to `20160426` (the version of the API that existed before versioning) so that they continue working the same way they did before versioning.

If you would like to upgrade your integration to use a new API version, you can explicitly set the header described above.

> ### Best practice: Set the header for every client or integration
>
> We recommend that you set the API version header explicitly in any client or integration you build.
>
> Only rely on the access token API version during manual testing.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0
- Package version: 6.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://support.launchdarkly.com](https://support.launchdarkly.com)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/launchdarkly/api-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/launchdarkly/api-client-python.git`)

Then import the package:
```python
import launchdarkly_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import launchdarkly_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import launchdarkly_api
from pprint import pprint
from launchdarkly_api.api import access_tokens_api
from launchdarkly_api.model.access_token_post import AccessTokenPost
from launchdarkly_api.model.json_patch import JSONPatch
from launchdarkly_api.model.token import Token
from launchdarkly_api.model.tokens import Tokens
# Defining the host is optional and defaults to https://app.launchdarkly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = launchdarkly_api.Configuration(
    host = "https://app.launchdarkly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'


# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = access_tokens_api.AccessTokensApi(api_client)
    id = "id_example" # str | The ID of the access token to update

    try:
        # Delete access token
        api_instance.delete_token(id)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccessTokensApi->delete_token: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://app.launchdarkly.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccessTokensApi* | [**delete_token**](docs/AccessTokensApi.md#delete_token) | **DELETE** /api/v2/tokens/{id} | Delete access token
*AccessTokensApi* | [**get_token**](docs/AccessTokensApi.md#get_token) | **GET** /api/v2/tokens/{id} | Get access token
*AccessTokensApi* | [**get_tokens**](docs/AccessTokensApi.md#get_tokens) | **GET** /api/v2/tokens | List access tokens
*AccessTokensApi* | [**patch_token**](docs/AccessTokensApi.md#patch_token) | **PATCH** /api/v2/tokens/{id} | Patch access token
*AccessTokensApi* | [**post_token**](docs/AccessTokensApi.md#post_token) | **POST** /api/v2/tokens | Create access token
*AccessTokensApi* | [**reset_token**](docs/AccessTokensApi.md#reset_token) | **POST** /api/v2/tokens/{id}/reset | Reset access token
*AccountMembersApi* | [**delete_member**](docs/AccountMembersApi.md#delete_member) | **DELETE** /api/v2/members/{id} | Delete account member
*AccountMembersApi* | [**get_member**](docs/AccountMembersApi.md#get_member) | **GET** /api/v2/members/{id} | Get account member
*AccountMembersApi* | [**get_members**](docs/AccountMembersApi.md#get_members) | **GET** /api/v2/members | List account members
*AccountMembersApi* | [**patch_member**](docs/AccountMembersApi.md#patch_member) | **PATCH** /api/v2/members/{id} | Modify an account member
*AccountMembersApi* | [**post_members**](docs/AccountMembersApi.md#post_members) | **POST** /api/v2/members | Invite new members
*AccountUsageBetaApi* | [**get_evaluations_usage**](docs/AccountUsageBetaApi.md#get_evaluations_usage) | **GET** /api/v2/usage/evaluations/{projKey}/{envKey}/{flagKey} | Get evaluations usage
*AccountUsageBetaApi* | [**get_events_usage**](docs/AccountUsageBetaApi.md#get_events_usage) | **GET** /api/v2/usage/events/{type} | Get events usage
*AccountUsageBetaApi* | [**get_mau_sdks_by_type**](docs/AccountUsageBetaApi.md#get_mau_sdks_by_type) | **GET** /api/v2/usage/mau/sdks | Get MAU SDKs by type
*AccountUsageBetaApi* | [**get_mau_usage**](docs/AccountUsageBetaApi.md#get_mau_usage) | **GET** /api/v2/usage/mau | Get MAU usage
*AccountUsageBetaApi* | [**get_mau_usage_by_category**](docs/AccountUsageBetaApi.md#get_mau_usage_by_category) | **GET** /api/v2/usage/mau/bycategory | Get MAU usage by category
*AccountUsageBetaApi* | [**get_stream_usage**](docs/AccountUsageBetaApi.md#get_stream_usage) | **GET** /api/v2/usage/streams/{source} | Get stream usage
*AccountUsageBetaApi* | [**get_stream_usage_by_sdk_version**](docs/AccountUsageBetaApi.md#get_stream_usage_by_sdk_version) | **GET** /api/v2/usage/streams/{source}/bysdkversion | Get stream usage by SDK version
*AccountUsageBetaApi* | [**get_stream_usage_sdkversion**](docs/AccountUsageBetaApi.md#get_stream_usage_sdkversion) | **GET** /api/v2/usage/streams/{source}/sdkversions | Get stream usage SDK versions
*ApprovalsApi* | [**delete_approval_request**](docs/ApprovalsApi.md#delete_approval_request) | **DELETE** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id} | Delete approval request
*ApprovalsApi* | [**get_approval**](docs/ApprovalsApi.md#get_approval) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id} | Get approval request
*ApprovalsApi* | [**get_approvals**](docs/ApprovalsApi.md#get_approvals) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests | List all approval requests
*ApprovalsApi* | [**post_approval_request**](docs/ApprovalsApi.md#post_approval_request) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests | Create approval request
*ApprovalsApi* | [**post_approval_request_apply_request**](docs/ApprovalsApi.md#post_approval_request_apply_request) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id}/apply | Apply approval request
*ApprovalsApi* | [**post_approval_request_review**](docs/ApprovalsApi.md#post_approval_request_review) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id}/reviews | Review approval request
*ApprovalsApi* | [**post_flag_copy_config_approval_request**](docs/ApprovalsApi.md#post_flag_copy_config_approval_request) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/copy/environments/{environmentKey}/approval-requests-flag-copy | Create approval request to copy flag configurations across environments
*AuditLogApi* | [**get_audit_log_entries**](docs/AuditLogApi.md#get_audit_log_entries) | **GET** /api/v2/auditlog | List audit log feature flag entries
*AuditLogApi* | [**get_audit_log_entry**](docs/AuditLogApi.md#get_audit_log_entry) | **GET** /api/v2/auditlog/{id} | Get audit log entry
*CodeReferencesApi* | [**delete_branches**](docs/CodeReferencesApi.md#delete_branches) | **POST** /api/v2/code-refs/repositories/{repo}/branch-delete-tasks | Delete branches
*CodeReferencesApi* | [**delete_repository**](docs/CodeReferencesApi.md#delete_repository) | **DELETE** /api/v2/code-refs/repositories/{repo} | Delete repository
*CodeReferencesApi* | [**get_branch**](docs/CodeReferencesApi.md#get_branch) | **GET** /api/v2/code-refs/repositories/{repo}/branches/{branch} | Get branch
*CodeReferencesApi* | [**get_branches**](docs/CodeReferencesApi.md#get_branches) | **GET** /api/v2/code-refs/repositories/{repo}/branches | List branches
*CodeReferencesApi* | [**get_extinctions**](docs/CodeReferencesApi.md#get_extinctions) | **GET** /api/v2/code-refs/extinctions | List extinctions
*CodeReferencesApi* | [**get_repositories**](docs/CodeReferencesApi.md#get_repositories) | **GET** /api/v2/code-refs/repositories | List repositories
*CodeReferencesApi* | [**get_repository**](docs/CodeReferencesApi.md#get_repository) | **GET** /api/v2/code-refs/repositories/{repo} | Get repository
*CodeReferencesApi* | [**get_root_statistic**](docs/CodeReferencesApi.md#get_root_statistic) | **GET** /api/v2/code-refs/statistics | Get number of code references for flags
*CodeReferencesApi* | [**get_statistics**](docs/CodeReferencesApi.md#get_statistics) | **GET** /api/v2/code-refs/statistics/{projKey} | Get number of code references for flags
*CodeReferencesApi* | [**patch_repository**](docs/CodeReferencesApi.md#patch_repository) | **PATCH** /api/v2/code-refs/repositories/{repo} | Update repository
*CodeReferencesApi* | [**post_extinction**](docs/CodeReferencesApi.md#post_extinction) | **POST** /api/v2/code-refs/repositories/{repo}/branches/{branch} | Create extinction
*CodeReferencesApi* | [**post_repository**](docs/CodeReferencesApi.md#post_repository) | **POST** /api/v2/code-refs/repositories | Create repository
*CodeReferencesApi* | [**put_branch**](docs/CodeReferencesApi.md#put_branch) | **PUT** /api/v2/code-refs/repositories/{repo}/branches/{branch} | Upsert branch
*CustomRolesApi* | [**delete_custom_role**](docs/CustomRolesApi.md#delete_custom_role) | **DELETE** /api/v2/roles/{key} | Delete custom role
*CustomRolesApi* | [**get_custom_role**](docs/CustomRolesApi.md#get_custom_role) | **GET** /api/v2/roles/{key} | Get custom role
*CustomRolesApi* | [**get_custom_roles**](docs/CustomRolesApi.md#get_custom_roles) | **GET** /api/v2/roles | List custom roles
*CustomRolesApi* | [**patch_custom_role**](docs/CustomRolesApi.md#patch_custom_role) | **PATCH** /api/v2/roles/{key} | Update custom role
*CustomRolesApi* | [**post_custom_role**](docs/CustomRolesApi.md#post_custom_role) | **POST** /api/v2/roles | Create custom role
*DataExportDestinationsApi* | [**delete_destination**](docs/DataExportDestinationsApi.md#delete_destination) | **DELETE** /api/v2/destinations/{projKey}/{envKey}/{id} | Delete Data Export destination
*DataExportDestinationsApi* | [**get_destination**](docs/DataExportDestinationsApi.md#get_destination) | **GET** /api/v2/destinations/{projKey}/{envKey}/{id} | Get destination
*DataExportDestinationsApi* | [**get_destinations**](docs/DataExportDestinationsApi.md#get_destinations) | **GET** /api/v2/destinations | List destinations
*DataExportDestinationsApi* | [**patch_destination**](docs/DataExportDestinationsApi.md#patch_destination) | **PATCH** /api/v2/destinations/{projKey}/{envKey}/{id} | Update Data Export destination
*DataExportDestinationsApi* | [**post_destination**](docs/DataExportDestinationsApi.md#post_destination) | **POST** /api/v2/destinations/{projKey}/{envKey} | Create data export destination
*EnvironmentsApi* | [**delete_environment**](docs/EnvironmentsApi.md#delete_environment) | **DELETE** /api/v2/projects/{projectKey}/environments/{environmentKey} | Delete environment
*EnvironmentsApi* | [**get_environment**](docs/EnvironmentsApi.md#get_environment) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey} | Get environment
*EnvironmentsApi* | [**patch_environment**](docs/EnvironmentsApi.md#patch_environment) | **PATCH** /api/v2/projects/{projectKey}/environments/{environmentKey} | Update environment
*EnvironmentsApi* | [**post_environment**](docs/EnvironmentsApi.md#post_environment) | **POST** /api/v2/projects/{projectKey}/environments | Create environment
*EnvironmentsApi* | [**reset_environment_mobile_key**](docs/EnvironmentsApi.md#reset_environment_mobile_key) | **POST** /api/v2/projects/{projectKey}/environments/{envKey}/mobileKey | Reset environment mobile SDK key
*EnvironmentsApi* | [**reset_environment_sdk_key**](docs/EnvironmentsApi.md#reset_environment_sdk_key) | **POST** /api/v2/projects/{projectKey}/environments/{envKey}/apiKey | Reset environment SDK key
*ExperimentsBetaApi* | [**get_experiment**](docs/ExperimentsBetaApi.md#get_experiment) | **GET** /api/v2/flags/{projKey}/{flagKey}/experiments/{envKey}/{metricKey} | Get experiment results
*ExperimentsBetaApi* | [**reset_experiment**](docs/ExperimentsBetaApi.md#reset_experiment) | **DELETE** /api/v2/flags/{projKey}/{flagKey}/experiments/{envKey}/{metricKey}/results | Reset experiment results
*FeatureFlagsApi* | [**copy_feature_flag**](docs/FeatureFlagsApi.md#copy_feature_flag) | **POST** /api/v2/flags/{projKey}/{featureFlagKey}/copy | Copy feature flag
*FeatureFlagsApi* | [**delete_feature_flag**](docs/FeatureFlagsApi.md#delete_feature_flag) | **DELETE** /api/v2/flags/{projKey}/{key} | Delete feature flag
*FeatureFlagsApi* | [**get_expiring_user_targets**](docs/FeatureFlagsApi.md#get_expiring_user_targets) | **GET** /api/v2/flags/{projKey}/{flagKey}/expiring-user-targets/{envKey} | Get expiring user targets for feature flag
*FeatureFlagsApi* | [**get_feature_flag**](docs/FeatureFlagsApi.md#get_feature_flag) | **GET** /api/v2/flags/{projKey}/{key} | Get feature flag
*FeatureFlagsApi* | [**get_feature_flag_status**](docs/FeatureFlagsApi.md#get_feature_flag_status) | **GET** /api/v2/flag-statuses/{projKey}/{envKey}/{key} | Get feature flag status
*FeatureFlagsApi* | [**get_feature_flag_status_across_environments**](docs/FeatureFlagsApi.md#get_feature_flag_status_across_environments) | **GET** /api/v2/flag-status/{projKey}/{key} | Get flag status across environments
*FeatureFlagsApi* | [**get_feature_flag_statuses**](docs/FeatureFlagsApi.md#get_feature_flag_statuses) | **GET** /api/v2/flag-statuses/{projKey}/{envKey} | List feature flag statuses
*FeatureFlagsApi* | [**get_feature_flags**](docs/FeatureFlagsApi.md#get_feature_flags) | **GET** /api/v2/flags/{projKey} | List feature flags
*FeatureFlagsApi* | [**patch_expiring_user_targets**](docs/FeatureFlagsApi.md#patch_expiring_user_targets) | **PATCH** /api/v2/flags/{projKey}/{flagKey}/expiring-user-targets/{envKey} | Update expiring user targets on feature flag
*FeatureFlagsApi* | [**patch_feature_flag**](docs/FeatureFlagsApi.md#patch_feature_flag) | **PATCH** /api/v2/flags/{projKey}/{key} | Update feature flag
*FeatureFlagsApi* | [**post_feature_flag**](docs/FeatureFlagsApi.md#post_feature_flag) | **POST** /api/v2/flags/{projKey} | Create a feature flag
*FeatureFlagsBetaApi* | [**get_dependent_flags**](docs/FeatureFlagsBetaApi.md#get_dependent_flags) | **GET** /api/v2/flags/{projKey}/{flagKey}/dependent-flags | List dependent feature flags
*FeatureFlagsBetaApi* | [**get_dependent_flags_by_env**](docs/FeatureFlagsBetaApi.md#get_dependent_flags_by_env) | **GET** /api/v2/flags/{projKey}/{envKey}/{flagKey}/dependent-flags | List dependent feature flags by environment
*MetricsApi* | [**delete_metric**](docs/MetricsApi.md#delete_metric) | **DELETE** /api/v2/metrics/{projectKey}/{key} | Delete metric
*MetricsApi* | [**get_metric**](docs/MetricsApi.md#get_metric) | **GET** /api/v2/metrics/{projectKey}/{key} | Get metric
*MetricsApi* | [**get_metrics**](docs/MetricsApi.md#get_metrics) | **GET** /api/v2/metrics/{projectKey} | List metrics
*MetricsApi* | [**patch_metric**](docs/MetricsApi.md#patch_metric) | **PATCH** /api/v2/metrics/{projectKey}/{key} | Update metric
*MetricsApi* | [**post_metric**](docs/MetricsApi.md#post_metric) | **POST** /api/v2/metrics/{projectKey} | Create metric
*OtherApi* | [**get_ips**](docs/OtherApi.md#get_ips) | **GET** /api/v2/public-ip-list | Gets the public IP list
*OtherApi* | [**get_openapi_spec**](docs/OtherApi.md#get_openapi_spec) | **GET** /api/v2/openapi.json | Gets the OpenAPI spec in json
*OtherApi* | [**get_root**](docs/OtherApi.md#get_root) | **GET** /api/v2 | Root resource
*OtherApi* | [**get_versions**](docs/OtherApi.md#get_versions) | **GET** /api/v2/versions | Get version information
*ProjectsApi* | [**delete_project**](docs/ProjectsApi.md#delete_project) | **DELETE** /api/v2/projects/{projectKey} | Delete project
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /api/v2/projects/{projectKey} | Get project
*ProjectsApi* | [**get_projects**](docs/ProjectsApi.md#get_projects) | **GET** /api/v2/projects | List projects
*ProjectsApi* | [**patch_project**](docs/ProjectsApi.md#patch_project) | **PATCH** /api/v2/projects/{projectKey} | Update project
*ProjectsApi* | [**post_project**](docs/ProjectsApi.md#post_project) | **POST** /api/v2/projects | Create project
*RelayProxyConfigurationsApi* | [**delete_relay_auto_config**](docs/RelayProxyConfigurationsApi.md#delete_relay_auto_config) | **DELETE** /api/v2/account/relay-auto-configs/{id} | Delete Relay Proxy config by ID
*RelayProxyConfigurationsApi* | [**get_relay_proxy_config**](docs/RelayProxyConfigurationsApi.md#get_relay_proxy_config) | **GET** /api/v2/account/relay-auto-configs/{id} | Get Relay Proxy config
*RelayProxyConfigurationsApi* | [**get_relay_proxy_configs**](docs/RelayProxyConfigurationsApi.md#get_relay_proxy_configs) | **GET** /api/v2/account/relay-auto-configs | List Relay Proxy configs
*RelayProxyConfigurationsApi* | [**patch_relay_auto_config**](docs/RelayProxyConfigurationsApi.md#patch_relay_auto_config) | **PATCH** /api/v2/account/relay-auto-configs/{id} | Update a Relay Proxy config
*RelayProxyConfigurationsApi* | [**post_relay_auto_config**](docs/RelayProxyConfigurationsApi.md#post_relay_auto_config) | **POST** /api/v2/account/relay-auto-configs | Create a new Relay Proxy config
*RelayProxyConfigurationsApi* | [**reset_relay_auto_config**](docs/RelayProxyConfigurationsApi.md#reset_relay_auto_config) | **POST** /api/v2/account/relay-auto-configs/{id}/reset | Reset Relay Proxy configuration key
*ScheduledChangesApi* | [**delete_flag_config_scheduled_changes**](docs/ScheduledChangesApi.md#delete_flag_config_scheduled_changes) | **DELETE** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes/{id} | Delete scheduled changes workflow
*ScheduledChangesApi* | [**get_feature_flag_scheduled_change**](docs/ScheduledChangesApi.md#get_feature_flag_scheduled_change) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes/{id} | Get a scheduled change
*ScheduledChangesApi* | [**get_flag_config_scheduled_changes**](docs/ScheduledChangesApi.md#get_flag_config_scheduled_changes) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes | List scheduled changes
*ScheduledChangesApi* | [**patch_flag_config_scheduled_change**](docs/ScheduledChangesApi.md#patch_flag_config_scheduled_change) | **PATCH** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes/{id} | Update scheduled changes workflow
*ScheduledChangesApi* | [**post_flag_config_scheduled_changes**](docs/ScheduledChangesApi.md#post_flag_config_scheduled_changes) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes | Create scheduled changes workflow
*SegmentsApi* | [**delete_segment**](docs/SegmentsApi.md#delete_segment) | **DELETE** /api/v2/segments/{projKey}/{envKey}/{key} | Delete segment
*SegmentsApi* | [**get_expiring_user_targets_for_segment**](docs/SegmentsApi.md#get_expiring_user_targets_for_segment) | **GET** /api/v2/segments/{projKey}/{segmentKey}/expiring-user-targets/{envKey} | Get expiring user targets for segment
*SegmentsApi* | [**get_segment**](docs/SegmentsApi.md#get_segment) | **GET** /api/v2/segments/{projKey}/{envKey}/{key} | Get segment
*SegmentsApi* | [**get_segment_membership_for_user**](docs/SegmentsApi.md#get_segment_membership_for_user) | **GET** /api/v2/segments/{projKey}/{envKey}/{key}/users/{userKey} | Get Big Segment membership for user
*SegmentsApi* | [**get_segments**](docs/SegmentsApi.md#get_segments) | **GET** /api/v2/segments/{projKey}/{envKey} | List segments
*SegmentsApi* | [**patch_expiring_user_targets_for_segment**](docs/SegmentsApi.md#patch_expiring_user_targets_for_segment) | **PATCH** /api/v2/segments/{projKey}/{segmentKey}/expiring-user-targets/{envKey} | Update expiring user targets for segment
*SegmentsApi* | [**patch_segment**](docs/SegmentsApi.md#patch_segment) | **PATCH** /api/v2/segments/{projKey}/{envKey}/{key} | Patch segment
*SegmentsApi* | [**post_segment**](docs/SegmentsApi.md#post_segment) | **POST** /api/v2/segments/{projKey}/{envKey} | Create segment
*SegmentsApi* | [**update_big_segment_targets**](docs/SegmentsApi.md#update_big_segment_targets) | **POST** /api/v2/segments/{projKey}/{envKey}/{key}/users | Update targets on a Big Segment
*UserSettingsApi* | [**get_expiring_flags_for_user**](docs/UserSettingsApi.md#get_expiring_flags_for_user) | **GET** /api/v2/users/{projKey}/{userKey}/expiring-user-targets/{envKey} | Get expiring dates on flags for user
*UserSettingsApi* | [**get_user_flag_setting**](docs/UserSettingsApi.md#get_user_flag_setting) | **GET** /api/v2/users/{projKey}/{envKey}/{key}/flags/{featureKey} | Get flag setting for user
*UserSettingsApi* | [**get_user_flag_settings**](docs/UserSettingsApi.md#get_user_flag_settings) | **GET** /api/v2/users/{projKey}/{envKey}/{key}/flags | List flag settings for user
*UserSettingsApi* | [**patch_expiring_flags_for_user**](docs/UserSettingsApi.md#patch_expiring_flags_for_user) | **PATCH** /api/v2/users/{projKey}/{userKey}/expiring-user-targets/{envKey} | Update expiring user target for flags
*UserSettingsApi* | [**put_flag_setting**](docs/UserSettingsApi.md#put_flag_setting) | **PUT** /api/v2/users/{projKey}/{envKey}/{key}/flags/{featureKey} | Update flag settings for user
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /api/v2/users/{projKey}/{envKey}/{key} | Delete user
*UsersApi* | [**get_search_users**](docs/UsersApi.md#get_search_users) | **GET** /api/v2/user-search/{projKey}/{envKey} | Find users
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /api/v2/users/{projKey}/{envKey}/{key} | Get user
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /api/v2/users/{projKey}/{envKey} | List users
*UsersBetaApi* | [**get_user_attribute_names**](docs/UsersBetaApi.md#get_user_attribute_names) | **GET** /api/v2/user-attributes/{projectKey}/{environmentKey} | Get user attribute names
*WebhooksApi* | [**delete_webhook**](docs/WebhooksApi.md#delete_webhook) | **DELETE** /api/v2/webhooks/{id} | Delete webhook
*WebhooksApi* | [**get_all_webhooks**](docs/WebhooksApi.md#get_all_webhooks) | **GET** /api/v2/webhooks | List webhooks
*WebhooksApi* | [**get_webhook**](docs/WebhooksApi.md#get_webhook) | **GET** /api/v2/webhooks/{id} | Get webhook
*WebhooksApi* | [**patch_webhook**](docs/WebhooksApi.md#patch_webhook) | **PATCH** /api/v2/webhooks/{id} | Update webhook
*WebhooksApi* | [**post_webhook**](docs/WebhooksApi.md#post_webhook) | **POST** /api/v2/webhooks | Creates a webhook


## Documentation For Models

 - [AccessDeniedReasonRep](docs/AccessDeniedReasonRep.md)
 - [AccessDeniedRep](docs/AccessDeniedRep.md)
 - [AccessRep](docs/AccessRep.md)
 - [AccessTokenPost](docs/AccessTokenPost.md)
 - [AllVariationsSummary](docs/AllVariationsSummary.md)
 - [ApprovalSettings](docs/ApprovalSettings.md)
 - [AuditLogEntryListingRep](docs/AuditLogEntryListingRep.md)
 - [AuditLogEntryListingRepCollection](docs/AuditLogEntryListingRepCollection.md)
 - [AuditLogEntryRep](docs/AuditLogEntryRep.md)
 - [AuthorizedAppDataRep](docs/AuthorizedAppDataRep.md)
 - [BigSegmentTarget](docs/BigSegmentTarget.md)
 - [BranchCollectionRep](docs/BranchCollectionRep.md)
 - [BranchRep](docs/BranchRep.md)
 - [Clause](docs/Clause.md)
 - [ClientSideAvailability](docs/ClientSideAvailability.md)
 - [ClientSideAvailabilityPost](docs/ClientSideAvailabilityPost.md)
 - [ConfidenceIntervalRep](docs/ConfidenceIntervalRep.md)
 - [Conflict](docs/Conflict.md)
 - [CopiedFromEnv](docs/CopiedFromEnv.md)
 - [CreateCopyFlagConfigApprovalRequestRequest](docs/CreateCopyFlagConfigApprovalRequestRequest.md)
 - [CreateFlagConfigApprovalRequestRequest](docs/CreateFlagConfigApprovalRequestRequest.md)
 - [CustomProperties](docs/CustomProperties.md)
 - [CustomProperty](docs/CustomProperty.md)
 - [CustomRole](docs/CustomRole.md)
 - [CustomRolePost](docs/CustomRolePost.md)
 - [CustomRolePostData](docs/CustomRolePostData.md)
 - [CustomRoles](docs/CustomRoles.md)
 - [DefaultClientSideAvailabilityPost](docs/DefaultClientSideAvailabilityPost.md)
 - [Defaults](docs/Defaults.md)
 - [DependentFlag](docs/DependentFlag.md)
 - [DependentFlagEnvironment](docs/DependentFlagEnvironment.md)
 - [DependentFlagsByEnvironment](docs/DependentFlagsByEnvironment.md)
 - [Destination](docs/Destination.md)
 - [DestinationPost](docs/DestinationPost.md)
 - [Destinations](docs/Destinations.md)
 - [Environment](docs/Environment.md)
 - [EnvironmentPost](docs/EnvironmentPost.md)
 - [ExperimentAllocationRep](docs/ExperimentAllocationRep.md)
 - [ExperimentEnabledPeriodRep](docs/ExperimentEnabledPeriodRep.md)
 - [ExperimentEnvironmentSettingRep](docs/ExperimentEnvironmentSettingRep.md)
 - [ExperimentInfoRep](docs/ExperimentInfoRep.md)
 - [ExperimentMetadataRep](docs/ExperimentMetadataRep.md)
 - [ExperimentRep](docs/ExperimentRep.md)
 - [ExperimentResultsRep](docs/ExperimentResultsRep.md)
 - [ExperimentStatsRep](docs/ExperimentStatsRep.md)
 - [ExperimentTimeSeriesSlice](docs/ExperimentTimeSeriesSlice.md)
 - [ExperimentTimeSeriesVariationSlice](docs/ExperimentTimeSeriesVariationSlice.md)
 - [ExperimentTimeSeriesVariationSlices](docs/ExperimentTimeSeriesVariationSlices.md)
 - [ExperimentTotalsRep](docs/ExperimentTotalsRep.md)
 - [ExpiringUserTargetError](docs/ExpiringUserTargetError.md)
 - [ExpiringUserTargetGetResponse](docs/ExpiringUserTargetGetResponse.md)
 - [ExpiringUserTargetItem](docs/ExpiringUserTargetItem.md)
 - [ExpiringUserTargetPatchResponse](docs/ExpiringUserTargetPatchResponse.md)
 - [Extinction](docs/Extinction.md)
 - [ExtinctionCollectionRep](docs/ExtinctionCollectionRep.md)
 - [ExtinctionRep](docs/ExtinctionRep.md)
 - [FeatureFlag](docs/FeatureFlag.md)
 - [FeatureFlagBody](docs/FeatureFlagBody.md)
 - [FeatureFlagConfig](docs/FeatureFlagConfig.md)
 - [FeatureFlagScheduledChange](docs/FeatureFlagScheduledChange.md)
 - [FeatureFlagScheduledChanges](docs/FeatureFlagScheduledChanges.md)
 - [FeatureFlagStatus](docs/FeatureFlagStatus.md)
 - [FeatureFlagStatusAcrossEnvironments](docs/FeatureFlagStatusAcrossEnvironments.md)
 - [FeatureFlagStatuses](docs/FeatureFlagStatuses.md)
 - [FeatureFlags](docs/FeatureFlags.md)
 - [FlagConfigApprovalRequestResponse](docs/FlagConfigApprovalRequestResponse.md)
 - [FlagConfigApprovalRequestsResponse](docs/FlagConfigApprovalRequestsResponse.md)
 - [FlagCopyConfigEnvironment](docs/FlagCopyConfigEnvironment.md)
 - [FlagCopyConfigPost](docs/FlagCopyConfigPost.md)
 - [FlagGlobalAttributesRep](docs/FlagGlobalAttributesRep.md)
 - [FlagListingRep](docs/FlagListingRep.md)
 - [FlagScheduledChangesInput](docs/FlagScheduledChangesInput.md)
 - [FlagStatusRep](docs/FlagStatusRep.md)
 - [FlagSummary](docs/FlagSummary.md)
 - [FormVariableConfig](docs/FormVariableConfig.md)
 - [HunkRep](docs/HunkRep.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [Instruction](docs/Instruction.md)
 - [Instructions](docs/Instructions.md)
 - [IntegrationMetadata](docs/IntegrationMetadata.md)
 - [IntegrationStatus](docs/IntegrationStatus.md)
 - [IpList](docs/IpList.md)
 - [JSONPatch](docs/JSONPatch.md)
 - [LastSeenMetadata](docs/LastSeenMetadata.md)
 - [Link](docs/Link.md)
 - [Member](docs/Member.md)
 - [MemberDataRep](docs/MemberDataRep.md)
 - [MemberPermissionGrantSummaryRep](docs/MemberPermissionGrantSummaryRep.md)
 - [MemberSummaryRep](docs/MemberSummaryRep.md)
 - [MemberTeamSummaryRep](docs/MemberTeamSummaryRep.md)
 - [Members](docs/Members.md)
 - [MetricCollectionRep](docs/MetricCollectionRep.md)
 - [MetricListingRep](docs/MetricListingRep.md)
 - [MetricPost](docs/MetricPost.md)
 - [MetricRep](docs/MetricRep.md)
 - [Modification](docs/Modification.md)
 - [MultiEnvironmentDependentFlag](docs/MultiEnvironmentDependentFlag.md)
 - [MultiEnvironmentDependentFlags](docs/MultiEnvironmentDependentFlags.md)
 - [NewMemberForm](docs/NewMemberForm.md)
 - [ParentResourceRep](docs/ParentResourceRep.md)
 - [PatchOperation](docs/PatchOperation.md)
 - [PatchSegmentInstruction](docs/PatchSegmentInstruction.md)
 - [PatchSegmentRequest](docs/PatchSegmentRequest.md)
 - [PatchWithComment](docs/PatchWithComment.md)
 - [PostApprovalRequestApplyRequest](docs/PostApprovalRequestApplyRequest.md)
 - [PostApprovalRequestReviewRequest](docs/PostApprovalRequestReviewRequest.md)
 - [PostFlagScheduledChangesInput](docs/PostFlagScheduledChangesInput.md)
 - [Prerequisite](docs/Prerequisite.md)
 - [Project](docs/Project.md)
 - [ProjectListingRep](docs/ProjectListingRep.md)
 - [ProjectPost](docs/ProjectPost.md)
 - [Projects](docs/Projects.md)
 - [PubNubDetailRep](docs/PubNubDetailRep.md)
 - [ReferenceRep](docs/ReferenceRep.md)
 - [RelayAutoConfigCollectionRep](docs/RelayAutoConfigCollectionRep.md)
 - [RelayAutoConfigPost](docs/RelayAutoConfigPost.md)
 - [RelayAutoConfigRep](docs/RelayAutoConfigRep.md)
 - [RepositoryCollectionRep](docs/RepositoryCollectionRep.md)
 - [RepositoryPost](docs/RepositoryPost.md)
 - [RepositoryRep](docs/RepositoryRep.md)
 - [ResourceAccess](docs/ResourceAccess.md)
 - [ResourceIDResponse](docs/ResourceIDResponse.md)
 - [ReviewResponse](docs/ReviewResponse.md)
 - [Rollout](docs/Rollout.md)
 - [Rule](docs/Rule.md)
 - [SdkListRep](docs/SdkListRep.md)
 - [SdkVersionListRep](docs/SdkVersionListRep.md)
 - [SdkVersionRep](docs/SdkVersionRep.md)
 - [SegmentBody](docs/SegmentBody.md)
 - [SegmentMetadata](docs/SegmentMetadata.md)
 - [SegmentUserList](docs/SegmentUserList.md)
 - [SegmentUserState](docs/SegmentUserState.md)
 - [SeriesListRep](docs/SeriesListRep.md)
 - [SeriesMetadataRep](docs/SeriesMetadataRep.md)
 - [SeriesTimeSliceRep](docs/SeriesTimeSliceRep.md)
 - [SourceFlag](docs/SourceFlag.md)
 - [Statement](docs/Statement.md)
 - [StatementPost](docs/StatementPost.md)
 - [StatementPostData](docs/StatementPostData.md)
 - [StatementPostList](docs/StatementPostList.md)
 - [StatementRep](docs/StatementRep.md)
 - [StatisticCollectionRep](docs/StatisticCollectionRep.md)
 - [StatisticRep](docs/StatisticRep.md)
 - [StatisticsRoot](docs/StatisticsRoot.md)
 - [SubjectDataRep](docs/SubjectDataRep.md)
 - [Target](docs/Target.md)
 - [TargetResourceRep](docs/TargetResourceRep.md)
 - [TitleRep](docs/TitleRep.md)
 - [Token](docs/Token.md)
 - [TokenDataRep](docs/TokenDataRep.md)
 - [Tokens](docs/Tokens.md)
 - [UrlMatchers](docs/UrlMatchers.md)
 - [UrlPost](docs/UrlPost.md)
 - [User](docs/User.md)
 - [UserAttributeNamesRep](docs/UserAttributeNamesRep.md)
 - [UserFlagSetting](docs/UserFlagSetting.md)
 - [UserFlagSettings](docs/UserFlagSettings.md)
 - [UserRecord](docs/UserRecord.md)
 - [UserSegment](docs/UserSegment.md)
 - [UserSegmentRule](docs/UserSegmentRule.md)
 - [UserSegments](docs/UserSegments.md)
 - [Users](docs/Users.md)
 - [ValuePut](docs/ValuePut.md)
 - [Variate](docs/Variate.md)
 - [Variation](docs/Variation.md)
 - [VariationOrRolloutRep](docs/VariationOrRolloutRep.md)
 - [VariationSummary](docs/VariationSummary.md)
 - [VersionsRep](docs/VersionsRep.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookPost](docs/WebhookPost.md)
 - [Webhooks](docs/Webhooks.md)
 - [WeightedVariation](docs/WeightedVariation.md)


## Documentation For Authorization


## ApiKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

support@launchdarkly.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in launchdarkly_api.apis and launchdarkly_api.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from launchdarkly_api.api.default_api import DefaultApi`
- `from launchdarkly_api.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import launchdarkly_api
from launchdarkly_api.apis import *
from launchdarkly_api.models import *
```

## Sample Code

```python
from __future__ import print_function
import os
from pprint import pprint

import launchdarkly_api
from launchdarkly_api.model.variate import Variate
from launchdarkly_api.model.feature_flag_body import FeatureFlagBody
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.rest import ApiException

configuration = launchdarkly_api.Configuration()
configuration.api_key['ApiKey'] = os.getenv("LD_API_KEY")

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'


# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = feature_flags_api.FeatureFlagsApi(api_client)

    project_key = "openapi"
    flag_key = "test-python"

    # Create a flag with json variations
    flag_post = FeatureFlagBody(
        name=flag_key,
        key=flag_key,
        variations=[
            Variate(value=[1, 2]),
            Variate(value=[3, 4]),
            Variate(value=[5]),
        ])

    try:
        api_response = api_instance.post_feature_flag(project_key, flag_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception creating flag: %s\n" % e)

    # Clean up the flag
    try:
        api_response = api_instance.delete_feature_flag(project_key, flag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception deleting flag: %s\n" % e)
```
