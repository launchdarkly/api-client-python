This repository contains a client library for LaunchDarkly's REST API. This client was automatically
generated from our [OpenAPI specification](https://app.launchdarkly.com/api/v2/openapi.json) using a [code generation library](https://github.com/launchdarkly/ld-openapi).

This REST API is for custom integrations, data export, or automating your feature flag workflows. *DO NOT* use this client library to include feature flags in your web or mobile application. To integrate feature flags with your application, read the [SDK documentation](https://docs.launchdarkly.com/sdk).

This client library is only compatible with the latest version of our REST API, version `20220603`. Previous versions of this client library, prior to version 10.0.0, are only compatible with earlier versions of our REST API. When you create an access token, you can set the REST API version associated with the token. By default, API requests you send using the token will use the specified API version. To learn more, read [Versioning](https://apidocs.launchdarkly.com/#section/Overview/Versioning).
View our [sample code](#sample-code) for example usage.

# launchdarkly-api
# Overview

## Authentication

LaunchDarkly's REST API uses the HTTPS protocol with a minimum TLS version of 1.2.

All REST API resources are authenticated with either [personal or service access tokens](https://docs.launchdarkly.com/home/account/api), or session cookies. Other authentication mechanisms are not supported. You can manage personal access tokens on your [**Authorization**](https://app.launchdarkly.com/settings/authorization) page in the LaunchDarkly UI.

LaunchDarkly also has SDK keys, mobile keys, and client-side IDs that are used by our server-side SDKs, mobile SDKs, and JavaScript-based SDKs, respectively. **These keys cannot be used to access our REST API**. These keys are environment-specific, and can only perform read-only operations such as fetching feature flag settings.

| Auth mechanism                                                                                  | Allowed resources                                                                                     | Use cases                                          |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| [Personal or service access tokens](https://docs.launchdarkly.com/home/account/api) | Can be customized on a per-token basis                                                                | Building scripts, custom integrations, data export. |
| SDK keys                                                                                        | Can only access read-only resources specific to server-side SDKs. Restricted to a single environment. | Server-side SDKs                     |
| Mobile keys                                                                                     | Can only access read-only resources specific to mobile SDKs, and only for flags marked available to mobile keys. Restricted to a single environment.           | Mobile SDKs                                        |
| Client-side ID                                                                                  | Can only access read-only resources specific to JavaScript-based client-side SDKs, and only for flags marked available to client-side. Restricted to a single environment.           | Client-side JavaScript                             |

> #### Keep your access tokens and SDK keys private
>
> Access tokens should _never_ be exposed in untrusted contexts. Never put an access token in client-side JavaScript, or embed it in a mobile application. LaunchDarkly has special mobile keys that you can embed in mobile apps. If you accidentally expose an access token or SDK key, you can reset it from your [**Authorization**](https://app.launchdarkly.com/settings/authorization) page.
>
> The client-side ID is safe to embed in untrusted contexts. It's designed for use in client-side JavaScript.

### Authentication using request header

The preferred way to authenticate with the API is by adding an `Authorization` header containing your access token to your requests. The value of the `Authorization` header must be your access token.

Manage personal access tokens from the [**Authorization**](https://app.launchdarkly.com/settings/authorization) page.

### Authentication using session cookie

For testing purposes, you can make API calls directly from your web browser. If you are logged in to the LaunchDarkly application, the API will use your existing session to authenticate calls.

If you have a [role](https://docs.launchdarkly.com/home/account/built-in-roles) other than Admin, or have a [custom role](https://docs.launchdarkly.com/home/account/custom-roles) defined, you may not have permission to perform some API calls. You will receive a `401` response code in that case.

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

## Representations

All resources expect and return JSON response bodies. Error responses also send a JSON body. To learn more about the error format of the API, read [Errors](/#section/Overview/Errors).

In practice this means that you always get a response with a `Content-Type` header set to `application/json`.

In addition, request bodies for `PATCH`, `POST`, and `PUT` requests must be encoded as JSON with a `Content-Type` header set to `application/json`.

### Summary and detailed representations

When you fetch a list of resources, the response includes only the most important attributes of each resource. This is a _summary representation_ of the resource. When you fetch an individual resource, such as a single feature flag, you receive a _detailed representation_ of the resource.

The best way to find a detailed representation is to follow links. Every summary representation includes a link to its detailed representation.

### Expanding responses

Sometimes the detailed representation of a resource does not include all of the attributes of the resource by default. If this is the case, the request method will clearly document this and describe which attributes you can include in an expanded response.

To include the additional attributes, append the `expand` request parameter to your request and add a comma-separated list of the attributes to include. For example, when you append `?expand=members,maintainers` to the [Get team](/tag/Teams#operation/getTeam) endpoint, the expanded response includes both of these attributes.

### Links and addressability

The best way to navigate the API is by following links. These are attributes in representations that link to other resources. The API always uses the same format for links:

- Links to other resources within the API are encapsulated in a `_links` object
- If the resource has a corresponding link to HTML content on the site, it is stored in a special `_site` link

Each link has two attributes:

- An `href`, which contains the URL
- A `type`, which describes the content type

For example, a feature resource might return the following:

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

## Updates

Resources that accept partial updates use the `PATCH` verb. Most resources support the [JSON patch](/reference#updates-using-json-patch) format. Some resources also support the [JSON merge patch](/reference#updates-using-json-merge-patch) format, and some resources support the [semantic patch](/reference#updates-using-semantic-patch) format, which is a way to specify the modifications to perform as a set of executable instructions. Each resource supports optional [comments](/reference#updates-with-comments) that you can submit with updates. Comments appear in outgoing webhooks, the audit log, and other integrations.

When a resource supports both JSON patch and semantic patch, we document both in the request method. However, the specific request body fields and descriptions included in our documentation only match one type of patch or the other.

### Updates using JSON patch

[JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) is a way to specify the modifications to perform on a resource. JSON patch uses paths and a limited set of operations to describe how to transform the current state of the resource into a new state. JSON patch documents are always arrays, where each element contains an operation, a path to the field to update, and the new value.

For example, in this feature flag representation:

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

You can specify multiple modifications to perform in a single request. You can also test that certain preconditions are met before applying the patch:

```json
[
  { \"op\": \"test\", \"path\": \"/version\", \"value\": 10 },
  { \"op\": \"replace\", \"path\": \"/description\", \"value\": \"The new description\" }
]
```

The above patch request tests whether the feature flag's `version` is `10`, and if so, changes the feature flag's description.

Attributes that are not editable, such as a resource's `_links`, have names that start with an underscore.

### Updates using JSON merge patch

[JSON merge patch](https://datatracker.ietf.org/doc/html/rfc7386) is another format for specifying the modifications to perform on a resource. JSON merge patch is less expressive than JSON patch. However, in many cases it is simpler to construct a merge patch document. For example, you can change a feature flag's description with the following merge patch document:

```json
{
  \"description\": \"New flag description\"
}
```

### Updates using semantic patch

Some resources support the semantic patch format. A semantic patch is a way to specify the modifications to perform on a resource as a set of executable instructions.

Semantic patch allows you to be explicit about intent using precise, custom instructions. In many cases, you can define semantic patch instructions independently of the current state of the resource. This can be useful when defining a change that may be applied at a future date.

To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header.

Here's how:

```
Content-Type: application/json; domain-model=launchdarkly.semanticpatch
```

If you call a semantic patch resource without this header, you will receive a `400` response because your semantic patch will be interpreted as a JSON patch.

The body of a semantic patch request takes the following properties:

* `comment` (string): (Optional) A description of the update.
* `environmentKey` (string): (Required for some resources only) The environment key.
* `instructions` (array): (Required) A list of actions the update should perform. Each action in the list must be an object with a `kind` property that indicates the instruction. If the instruction requires parameters, you must include those parameters as additional fields in the object. The documentation for each resource that supports semantic patch includes the available instructions and any additional parameters.

For example:

```json
{
  \"comment\": \"optional comment\",
  \"instructions\": [ {\"kind\": \"turnFlagOn\"} ]
}
```

Semantic patches are not applied partially; either all of the instructions are applied or none of them are. If **any** instruction is invalid, the endpoint returns an error and will not change the resource. If all instructions are valid, the request succeeds and the resources are updated if necessary, or left unchanged if they are already in the state you request.

### Updates with comments

You can submit optional comments with `PATCH` changes.

To submit a comment along with a JSON patch document, use the following format:

```json
{
  \"comment\": \"This is a comment string\",
  \"patch\": [{ \"op\": \"replace\", \"path\": \"/description\", \"value\": \"The new description\" }]
}
```

To submit a comment along with a JSON merge patch document, use the following format:

```json
{
  \"comment\": \"This is a comment string\",
  \"merge\": { \"description\": \"New flag description\" }
}
```

To submit a comment along with a semantic patch, use the following format:

```json
{
  \"comment\": \"This is a comment string\",
  \"instructions\": [ {\"kind\": \"turnFlagOn\"} ]
}
```

## Errors

The API always returns errors in a common format. Here's an example:

```json
{
  \"code\": \"invalid_request\",
  \"message\": \"A feature with that key already exists\",
  \"id\": \"30ce6058-87da-11e4-b116-123b93f75cba\"
}
```

The `code` indicates the general class of error. The `message` is a human-readable explanation of what went wrong. The `id` is a unique identifier. Use it when you're working with LaunchDarkly Support to debug a problem with a specific API call.

### HTTP status error response codes

| Code | Definition        | Description                                                                                       | Possible Solution                                                |
| ---- | ----------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| 400  | Invalid request       | The request cannot be understood.                                    | Ensure JSON syntax in request body is correct.                   |
| 401  | Invalid access token      | Requestor is unauthorized or does not have permission for this API call.                                                | Ensure your API access token is valid and has the appropriate permissions.                                     |
| 403  | Forbidden         | Requestor does not have access to this resource.                                                | Ensure that the account member or access token has proper permissions set. |
| 404  | Invalid resource identifier | The requested resource is not valid. | Ensure that the resource is correctly identified by ID or key. |
| 405  | Method not allowed | The request method is not allowed on this resource. | Ensure that the HTTP verb is correct. |
| 409  | Conflict          | The API request can not be completed because it conflicts with a concurrent API request. | Retry your request.                                              |
| 422  | Unprocessable entity | The API request can not be completed because the update description can not be understood. | Ensure that the request body is correct for the type of patch you are using, either JSON patch or semantic patch.
| 429  | Too many requests | Read [Rate limiting](/#section/Overview/Rate-limiting).                                               | Wait and try again later.                                        |

## CORS

The LaunchDarkly API supports Cross Origin Resource Sharing (CORS) for AJAX requests from any origin. If an `Origin` header is given in a request, it will be echoed as an explicitly allowed origin. Otherwise the request returns a wildcard, `Access-Control-Allow-Origin: *`. For more information on CORS, read the [CORS W3C Recommendation](http://www.w3.org/TR/cors). Example CORS headers might look like:

```http
Access-Control-Allow-Headers: Accept, Content-Type, Content-Length, Accept-Encoding, Authorization
Access-Control-Allow-Methods: OPTIONS, GET, DELETE, PATCH
Access-Control-Allow-Origin: *
Access-Control-Max-Age: 300
```

You can make authenticated CORS calls just as you would make same-origin calls, using either [token or session-based authentication](/#section/Overview/Authentication). If you are using session authentication, you should set the `withCredentials` property for your `xhr` request to `true`. You should never expose your access tokens to untrusted entities.

## Rate limiting

We use several rate limiting strategies to ensure the availability of our APIs. Rate-limited calls to our APIs return a `429` status code. Calls to our APIs include headers indicating the current rate limit status. The specific headers returned depend on the API route being called. The limits differ based on the route, authentication mechanism, and other factors. Routes that are not rate limited may not contain any of the headers described below.

> ### Rate limiting and SDKs
>
> LaunchDarkly SDKs are never rate limited and do not use the API endpoints defined here. LaunchDarkly uses a different set of approaches, including streaming/server-sent events and a global CDN, to ensure availability to the routes used by LaunchDarkly SDKs.

### Global rate limits

Authenticated requests are subject to a global limit. This is the maximum number of calls that your account can make to the API per ten seconds. All service and personal access tokens on the account share this limit, so exceeding the limit with one access token will impact other tokens. Calls that are subject to global rate limits may return the headers below:

| Header name                    | Description                                                                      |
| ------------------------------ | -------------------------------------------------------------------------------- |
| `X-Ratelimit-Global-Remaining` | The maximum number of requests the account is permitted to make per ten seconds. |
| `X-Ratelimit-Reset`            | The time at which the current rate limit window resets in epoch milliseconds.    |

We do not publicly document the specific number of calls that can be made globally. This limit may change, and we encourage clients to program against the specification, relying on the two headers defined above, rather than hardcoding to the current limit.

### Route-level rate limits

Some authenticated routes have custom rate limits. These also reset every ten seconds. Any service or personal access tokens hitting the same route share this limit, so exceeding the limit with one access token may impact other tokens. Calls that are subject to route-level rate limits return the headers below:

| Header name                   | Description                                                                                           |
| ----------------------------- | ----------------------------------------------------------------------------------------------------- |
| `X-Ratelimit-Route-Remaining` | The maximum number of requests to the current route the account is permitted to make per ten seconds. |
| `X-Ratelimit-Reset`           | The time at which the current rate limit window resets in epoch milliseconds.                         |

A _route_ represents a specific URL pattern and verb. For example, the [Delete environment](/tag/Environments#operation/deleteEnvironment) endpoint is considered a single route, and each call to delete an environment counts against your route-level rate limit for that route.

We do not publicly document the specific number of calls that an account can make to each endpoint per ten seconds. These limits may change, and we encourage clients to program against the specification, relying on the two headers defined above, rather than hardcoding to the current limits.

### IP-based rate limiting

We also employ IP-based rate limiting on some API routes. If you hit an IP-based rate limit, your API response will include a `Retry-After` header indicating how long to wait before re-trying the call. Clients must wait at least `Retry-After` seconds before making additional calls to our API, and should employ jitter and backoff strategies to avoid triggering rate limits again.

## OpenAPI (Swagger) and client libraries

We have a [complete OpenAPI (Swagger) specification](https://app.launchdarkly.com/api/v2/openapi.json) for our API.

We auto-generate multiple client libraries based on our OpenAPI specification. To learn more, visit the [collection of client libraries on GitHub](https://github.com/search?q=topic%3Alaunchdarkly-api+org%3Alaunchdarkly&type=Repositories). You can also use this specification to generate client libraries to interact with our REST API in your language of choice.

Our OpenAPI specification is supported by several API-based tools such as Postman and Insomnia. In many cases, you can directly import our specification to explore our APIs.

## Method overriding

Some firewalls and HTTP clients restrict the use of verbs other than `GET` and `POST`. In those environments, our API endpoints that use `DELETE`, `PATCH`, and `PUT` verbs are inaccessible.

To avoid this issue, our API supports the `X-HTTP-Method-Override` header, allowing clients to \"tunnel\" `DELETE`, `PATCH`, and `PUT` requests using a `POST` request.

For example, to call a `PATCH` endpoint using a `POST` request, you can include `X-HTTP-Method-Override:PATCH` as a header.

## Beta resources

We sometimes release new API resources in **beta** status before we release them with general availability.

Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.

We try to promote resources into general availability as quickly as possible. This happens after sufficient testing and when we're satisfied that we no longer need to make backwards-incompatible changes.

We mark beta resources with a \"Beta\" callout in our documentation, pictured below:

> ### This feature is in beta
>
> To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](/#section/Overview/Beta-resources).
>
> Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.

### Using beta resources

To use a beta resource, you must include a header in the request. If you call a beta resource without this header, you receive a `403` response.

Use this header:

```
LD-API-Version: beta
```

## Federal environments

The version of LaunchDarkly that is available on domains controlled by the United States government is different from the version of LaunchDarkly available to the general public. If you are an employee or contractor for a United States federal agency and use LaunchDarkly in your work, you likely use the federal instance of LaunchDarkly.

If you are working in the federal instance of LaunchDarkly, the base URI for each request is `https://app.launchdarkly.us`. In the \"Try it\" sandbox for each request, click the request path to view the complete resource path for the federal environment.

To learn more, read [LaunchDarkly in federal environments](https://docs.launchdarkly.com/home/infrastructure/federal).

## Versioning

We try hard to keep our REST API backwards compatible, but we occasionally have to make backwards-incompatible changes in the process of shipping new features. These breaking changes can cause unexpected behavior if you don't prepare for them accordingly.

Updates to our REST API include support for the latest features in LaunchDarkly. We also release a new version of our REST API every time we make a breaking change. We provide simultaneous support for multiple API versions so you can migrate from your current API version to a new version at your own pace.

### Setting the API version per request

You can set the API version on a specific request by sending an `LD-API-Version` header, as shown in the example below:

```
LD-API-Version: 20240415
```

The header value is the version number of the API version you would like to request. The number for each version corresponds to the date the version was released in `yyyymmdd` format. In the example above the version `20240415` corresponds to April 15, 2024.

### Setting the API version per access token

When you create an access token, you must specify a specific version of the API to use. This ensures that integrations using this token cannot be broken by version changes.

Tokens created before versioning was released have their version set to `20160426`, which is the version of the API that existed before the current versioning scheme, so that they continue working the same way they did before versioning.

If you would like to upgrade your integration to use a new API version, you can explicitly set the header described above.

> ### Best practice: Set the header for every client or integration
>
> We recommend that you set the API version header explicitly in any client or integration you build.
>
> Only rely on the access token API version during manual testing.

### API version changelog

|<div style=\"width:75px\">Version</div> | Changes | End of life (EOL)
|---|---|---|
| `20240415` | <ul><li>Changed several endpoints from unpaginated to paginated. Use the `limit` and `offset` query parameters to page through the results.</li> <li>Changed the [list access tokens](/tag/Access-tokens#operation/getTokens) endpoint: <ul><li>Response is now paginated with a default limit of `25`</li></ul></li> <li>Changed the [list account members](/tag/Account-members#operation/getMembers) endpoint: <ul><li>The `accessCheck` filter is no longer available</li></ul></li> <li>Changed the [list custom roles](/tag/Custom-roles#operation/getCustomRoles) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li></ul></li> <li>Changed the [list feature flags](/tag/Feature-flags#operation/getFeatureFlags) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li><li>The `environments` field is now only returned if the request is filtered by environment, using the `filterEnv` query parameter</li><li>The `filterEnv` query parameter supports a maximum of three environments</li><li>The `followerId`, `hasDataExport`, `status`, `contextKindTargeted`, and `segmentTargeted` filters are no longer available</li></ul></li> <li>Changed the [list segments](/tag/Segments#operation/getSegments) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li></ul></li> <li>Changed the [list teams](/tag/Teams#operation/getTeams) endpoint: <ul><li>The `expand` parameter no longer supports including `projects` or `roles`</li><li>In paginated results, the maximum page size is now 100</li></ul></li> <li>Changed the [get workflows](/tag/Workflows#operation/getWorkflows) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li><li>The `_conflicts` field in the response is no longer available</li></ul></li> </ul>  | Current |
| `20220603` | <ul><li>Changed the [list projects](/tag/Projects#operation/getProjects) return value:<ul><li>Response is now paginated with a default limit of `20`.</li><li>Added support for filter and sort.</li><li>The project `environments` field is now expandable. This field is omitted by default.</li></ul></li><li>Changed the [get project](/tag/Projects#operation/getProject) return value:<ul><li>The `environments` field is now expandable. This field is omitted by default.</li></ul></li></ul> | 2025-04-15 |
| `20210729` | <ul><li>Changed the [create approval request](/tag/Approvals#operation/postApprovalRequest) return value. It now returns HTTP Status Code `201` instead of `200`.</li><li> Changed the [get users](/tag/Users#operation/getUser) return value. It now returns a user record, not a user. </li><li>Added additional optional fields to environment, segments, flags, members, and segments, including the ability to create big segments. </li><li> Added default values for flag variations when new environments are created. </li><li>Added filtering and pagination for getting flags and members, including `limit`, `number`, `filter`, and `sort` query parameters. </li><li>Added endpoints for expiring user targets for flags and segments, scheduled changes, access tokens, Relay Proxy configuration, integrations and subscriptions, and approvals. </li></ul> | 2023-06-03 |
| `20191212` | <ul><li>[List feature flags](/tag/Feature-flags#operation/getFeatureFlags) now defaults to sending summaries of feature flag configurations, equivalent to setting the query parameter `summary=true`. Summaries omit flag targeting rules and individual user targets from the payload. </li><li> Added endpoints for flags, flag status, projects, environments, audit logs, members, users, custom roles, segments, usage, streams, events, and data export. </li></ul> | 2022-07-29 |
| `20160426` | <ul><li>Initial versioning of API. Tokens created before versioning have their version set to this.</li></ul> | 2020-12-12 |

To learn more about how EOL is determined, read LaunchDarkly's [End of Life (EOL) Policy](https://launchdarkly.com/policies/end-of-life-policy/).


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0
- Package version: 17.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://support.launchdarkly.com](https://support.launchdarkly.com)

## Requirements.

Python >=3.6

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
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.json_patch import JSONPatch
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.patch_failed_error_rep import PatchFailedErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.status_conflict_error_rep import StatusConflictErrorRep
from launchdarkly_api.model.token import Token
from launchdarkly_api.model.tokens import Tokens
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
*AccountMembersApi* | [**post_member_teams**](docs/AccountMembersApi.md#post_member_teams) | **POST** /api/v2/members/{id}/teams | Add a member to teams
*AccountMembersApi* | [**post_members**](docs/AccountMembersApi.md#post_members) | **POST** /api/v2/members | Invite new members
*AccountMembersBetaApi* | [**patch_members**](docs/AccountMembersBetaApi.md#patch_members) | **PATCH** /api/v2/members | Modify account members
*AccountUsageBetaApi* | [**get_data_export_events_usage**](docs/AccountUsageBetaApi.md#get_data_export_events_usage) | **GET** /api/v2/usage/data-export-events | Get data export events usage
*AccountUsageBetaApi* | [**get_evaluations_usage**](docs/AccountUsageBetaApi.md#get_evaluations_usage) | **GET** /api/v2/usage/evaluations/{projectKey}/{environmentKey}/{featureFlagKey} | Get evaluations usage
*AccountUsageBetaApi* | [**get_events_usage**](docs/AccountUsageBetaApi.md#get_events_usage) | **GET** /api/v2/usage/events/{type} | Get events usage
*AccountUsageBetaApi* | [**get_experimentation_keys_usage**](docs/AccountUsageBetaApi.md#get_experimentation_keys_usage) | **GET** /api/v2/usage/experimentation-keys | Get experimentation keys usage
*AccountUsageBetaApi* | [**get_experimentation_units_usage**](docs/AccountUsageBetaApi.md#get_experimentation_units_usage) | **GET** /api/v2/usage/experimentation-units | Get experimentation units usage
*AccountUsageBetaApi* | [**get_mau_sdks_by_type**](docs/AccountUsageBetaApi.md#get_mau_sdks_by_type) | **GET** /api/v2/usage/mau/sdks | Get MAU SDKs by type
*AccountUsageBetaApi* | [**get_mau_usage**](docs/AccountUsageBetaApi.md#get_mau_usage) | **GET** /api/v2/usage/mau | Get MAU usage
*AccountUsageBetaApi* | [**get_mau_usage_by_category**](docs/AccountUsageBetaApi.md#get_mau_usage_by_category) | **GET** /api/v2/usage/mau/bycategory | Get MAU usage by category
*AccountUsageBetaApi* | [**get_service_connection_usage**](docs/AccountUsageBetaApi.md#get_service_connection_usage) | **GET** /api/v2/usage/service-connections | Get service connection usage
*AccountUsageBetaApi* | [**get_stream_usage**](docs/AccountUsageBetaApi.md#get_stream_usage) | **GET** /api/v2/usage/streams/{source} | Get stream usage
*AccountUsageBetaApi* | [**get_stream_usage_by_sdk_version**](docs/AccountUsageBetaApi.md#get_stream_usage_by_sdk_version) | **GET** /api/v2/usage/streams/{source}/bysdkversion | Get stream usage by SDK version
*AccountUsageBetaApi* | [**get_stream_usage_sdkversion**](docs/AccountUsageBetaApi.md#get_stream_usage_sdkversion) | **GET** /api/v2/usage/streams/{source}/sdkversions | Get stream usage SDK versions
*ApplicationsBetaApi* | [**delete_application**](docs/ApplicationsBetaApi.md#delete_application) | **DELETE** /api/v2/applications/{applicationKey} | Delete application
*ApplicationsBetaApi* | [**delete_application_version**](docs/ApplicationsBetaApi.md#delete_application_version) | **DELETE** /api/v2/applications/{applicationKey}/versions/{versionKey} | Delete application version
*ApplicationsBetaApi* | [**get_application**](docs/ApplicationsBetaApi.md#get_application) | **GET** /api/v2/applications/{applicationKey} | Get application by key
*ApplicationsBetaApi* | [**get_application_versions**](docs/ApplicationsBetaApi.md#get_application_versions) | **GET** /api/v2/applications/{applicationKey}/versions | Get application versions by application key
*ApplicationsBetaApi* | [**get_applications**](docs/ApplicationsBetaApi.md#get_applications) | **GET** /api/v2/applications | Get applications
*ApplicationsBetaApi* | [**patch_application**](docs/ApplicationsBetaApi.md#patch_application) | **PATCH** /api/v2/applications/{applicationKey} | Update application
*ApplicationsBetaApi* | [**patch_application_version**](docs/ApplicationsBetaApi.md#patch_application_version) | **PATCH** /api/v2/applications/{applicationKey}/versions/{versionKey} | Update application version
*ApprovalsApi* | [**delete_approval_request**](docs/ApprovalsApi.md#delete_approval_request) | **DELETE** /api/v2/approval-requests/{id} | Delete approval request
*ApprovalsApi* | [**delete_approval_request_for_flag**](docs/ApprovalsApi.md#delete_approval_request_for_flag) | **DELETE** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id} | Delete approval request for a flag
*ApprovalsApi* | [**get_approval_for_flag**](docs/ApprovalsApi.md#get_approval_for_flag) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id} | Get approval request for a flag
*ApprovalsApi* | [**get_approval_request**](docs/ApprovalsApi.md#get_approval_request) | **GET** /api/v2/approval-requests/{id} | Get approval request
*ApprovalsApi* | [**get_approval_requests**](docs/ApprovalsApi.md#get_approval_requests) | **GET** /api/v2/approval-requests | List approval requests
*ApprovalsApi* | [**get_approvals_for_flag**](docs/ApprovalsApi.md#get_approvals_for_flag) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests | List approval requests for a flag
*ApprovalsApi* | [**post_approval_request**](docs/ApprovalsApi.md#post_approval_request) | **POST** /api/v2/approval-requests | Create approval request
*ApprovalsApi* | [**post_approval_request_apply**](docs/ApprovalsApi.md#post_approval_request_apply) | **POST** /api/v2/approval-requests/{id}/apply | Apply approval request
*ApprovalsApi* | [**post_approval_request_apply_for_flag**](docs/ApprovalsApi.md#post_approval_request_apply_for_flag) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id}/apply | Apply approval request for a flag
*ApprovalsApi* | [**post_approval_request_for_flag**](docs/ApprovalsApi.md#post_approval_request_for_flag) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests | Create approval request for a flag
*ApprovalsApi* | [**post_approval_request_review**](docs/ApprovalsApi.md#post_approval_request_review) | **POST** /api/v2/approval-requests/{id}/reviews | Review approval request
*ApprovalsApi* | [**post_approval_request_review_for_flag**](docs/ApprovalsApi.md#post_approval_request_review_for_flag) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id}/reviews | Review approval request for a flag
*ApprovalsApi* | [**post_flag_copy_config_approval_request**](docs/ApprovalsApi.md#post_flag_copy_config_approval_request) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests-flag-copy | Create approval request to copy flag configurations across environments
*ApprovalsBetaApi* | [**patch_approval_request**](docs/ApprovalsBetaApi.md#patch_approval_request) | **PATCH** /api/v2/approval-requests/{id} | Update approval request
*ApprovalsBetaApi* | [**patch_flag_config_approval_request**](docs/ApprovalsBetaApi.md#patch_flag_config_approval_request) | **PATCH** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id} | Update flag approval request
*AuditLogApi* | [**get_audit_log_entries**](docs/AuditLogApi.md#get_audit_log_entries) | **GET** /api/v2/auditlog | List audit log entries
*AuditLogApi* | [**get_audit_log_entry**](docs/AuditLogApi.md#get_audit_log_entry) | **GET** /api/v2/auditlog/{id} | Get audit log entry
*AuditLogApi* | [**post_audit_log_entries**](docs/AuditLogApi.md#post_audit_log_entries) | **POST** /api/v2/auditlog | Search audit log entries
*CodeReferencesApi* | [**delete_branches**](docs/CodeReferencesApi.md#delete_branches) | **POST** /api/v2/code-refs/repositories/{repo}/branch-delete-tasks | Delete branches
*CodeReferencesApi* | [**delete_repository**](docs/CodeReferencesApi.md#delete_repository) | **DELETE** /api/v2/code-refs/repositories/{repo} | Delete repository
*CodeReferencesApi* | [**get_branch**](docs/CodeReferencesApi.md#get_branch) | **GET** /api/v2/code-refs/repositories/{repo}/branches/{branch} | Get branch
*CodeReferencesApi* | [**get_branches**](docs/CodeReferencesApi.md#get_branches) | **GET** /api/v2/code-refs/repositories/{repo}/branches | List branches
*CodeReferencesApi* | [**get_extinctions**](docs/CodeReferencesApi.md#get_extinctions) | **GET** /api/v2/code-refs/extinctions | List extinctions
*CodeReferencesApi* | [**get_repositories**](docs/CodeReferencesApi.md#get_repositories) | **GET** /api/v2/code-refs/repositories | List repositories
*CodeReferencesApi* | [**get_repository**](docs/CodeReferencesApi.md#get_repository) | **GET** /api/v2/code-refs/repositories/{repo} | Get repository
*CodeReferencesApi* | [**get_root_statistic**](docs/CodeReferencesApi.md#get_root_statistic) | **GET** /api/v2/code-refs/statistics | Get links to code reference repositories for each project
*CodeReferencesApi* | [**get_statistics**](docs/CodeReferencesApi.md#get_statistics) | **GET** /api/v2/code-refs/statistics/{projectKey} | Get code references statistics for flags
*CodeReferencesApi* | [**patch_repository**](docs/CodeReferencesApi.md#patch_repository) | **PATCH** /api/v2/code-refs/repositories/{repo} | Update repository
*CodeReferencesApi* | [**post_extinction**](docs/CodeReferencesApi.md#post_extinction) | **POST** /api/v2/code-refs/repositories/{repo}/branches/{branch}/extinction-events | Create extinction
*CodeReferencesApi* | [**post_repository**](docs/CodeReferencesApi.md#post_repository) | **POST** /api/v2/code-refs/repositories | Create repository
*CodeReferencesApi* | [**put_branch**](docs/CodeReferencesApi.md#put_branch) | **PUT** /api/v2/code-refs/repositories/{repo}/branches/{branch} | Upsert branch
*ContextSettingsApi* | [**put_context_flag_setting**](docs/ContextSettingsApi.md#put_context_flag_setting) | **PUT** /api/v2/projects/{projectKey}/environments/{environmentKey}/contexts/{contextKind}/{contextKey}/flags/{featureFlagKey} | Update flag settings for context
*ContextsApi* | [**delete_context_instances**](docs/ContextsApi.md#delete_context_instances) | **DELETE** /api/v2/projects/{projectKey}/environments/{environmentKey}/context-instances/{id} | Delete context instances
*ContextsApi* | [**evaluate_context_instance**](docs/ContextsApi.md#evaluate_context_instance) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/flags/evaluate | Evaluate flags for context instance
*ContextsApi* | [**get_context_attribute_names**](docs/ContextsApi.md#get_context_attribute_names) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/context-attributes | Get context attribute names
*ContextsApi* | [**get_context_attribute_values**](docs/ContextsApi.md#get_context_attribute_values) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/context-attributes/{attributeName} | Get context attribute values
*ContextsApi* | [**get_context_instances**](docs/ContextsApi.md#get_context_instances) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/context-instances/{id} | Get context instances
*ContextsApi* | [**get_context_kinds_by_project_key**](docs/ContextsApi.md#get_context_kinds_by_project_key) | **GET** /api/v2/projects/{projectKey}/context-kinds | Get context kinds
*ContextsApi* | [**get_contexts**](docs/ContextsApi.md#get_contexts) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/contexts/{kind}/{key} | Get contexts
*ContextsApi* | [**put_context_kind**](docs/ContextsApi.md#put_context_kind) | **PUT** /api/v2/projects/{projectKey}/context-kinds/{key} | Create or update context kind
*ContextsApi* | [**search_context_instances**](docs/ContextsApi.md#search_context_instances) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/context-instances/search | Search for context instances
*ContextsApi* | [**search_contexts**](docs/ContextsApi.md#search_contexts) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/contexts/search | Search for contexts
*CustomRolesApi* | [**delete_custom_role**](docs/CustomRolesApi.md#delete_custom_role) | **DELETE** /api/v2/roles/{customRoleKey} | Delete custom role
*CustomRolesApi* | [**get_custom_role**](docs/CustomRolesApi.md#get_custom_role) | **GET** /api/v2/roles/{customRoleKey} | Get custom role
*CustomRolesApi* | [**get_custom_roles**](docs/CustomRolesApi.md#get_custom_roles) | **GET** /api/v2/roles | List custom roles
*CustomRolesApi* | [**patch_custom_role**](docs/CustomRolesApi.md#patch_custom_role) | **PATCH** /api/v2/roles/{customRoleKey} | Update custom role
*CustomRolesApi* | [**post_custom_role**](docs/CustomRolesApi.md#post_custom_role) | **POST** /api/v2/roles | Create custom role
*DataExportDestinationsApi* | [**delete_destination**](docs/DataExportDestinationsApi.md#delete_destination) | **DELETE** /api/v2/destinations/{projectKey}/{environmentKey}/{id} | Delete Data Export destination
*DataExportDestinationsApi* | [**get_destination**](docs/DataExportDestinationsApi.md#get_destination) | **GET** /api/v2/destinations/{projectKey}/{environmentKey}/{id} | Get destination
*DataExportDestinationsApi* | [**get_destinations**](docs/DataExportDestinationsApi.md#get_destinations) | **GET** /api/v2/destinations | List destinations
*DataExportDestinationsApi* | [**patch_destination**](docs/DataExportDestinationsApi.md#patch_destination) | **PATCH** /api/v2/destinations/{projectKey}/{environmentKey}/{id} | Update Data Export destination
*DataExportDestinationsApi* | [**post_destination**](docs/DataExportDestinationsApi.md#post_destination) | **POST** /api/v2/destinations/{projectKey}/{environmentKey} | Create Data Export destination
*EnvironmentsApi* | [**delete_environment**](docs/EnvironmentsApi.md#delete_environment) | **DELETE** /api/v2/projects/{projectKey}/environments/{environmentKey} | Delete environment
*EnvironmentsApi* | [**get_environment**](docs/EnvironmentsApi.md#get_environment) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey} | Get environment
*EnvironmentsApi* | [**get_environments_by_project**](docs/EnvironmentsApi.md#get_environments_by_project) | **GET** /api/v2/projects/{projectKey}/environments | List environments
*EnvironmentsApi* | [**patch_environment**](docs/EnvironmentsApi.md#patch_environment) | **PATCH** /api/v2/projects/{projectKey}/environments/{environmentKey} | Update environment
*EnvironmentsApi* | [**post_environment**](docs/EnvironmentsApi.md#post_environment) | **POST** /api/v2/projects/{projectKey}/environments | Create environment
*EnvironmentsApi* | [**reset_environment_mobile_key**](docs/EnvironmentsApi.md#reset_environment_mobile_key) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/mobileKey | Reset environment mobile SDK key
*EnvironmentsApi* | [**reset_environment_sdk_key**](docs/EnvironmentsApi.md#reset_environment_sdk_key) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/apiKey | Reset environment SDK key
*ExperimentsApi* | [**create_experiment**](docs/ExperimentsApi.md#create_experiment) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments | Create experiment
*ExperimentsApi* | [**create_iteration**](docs/ExperimentsApi.md#create_iteration) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey}/iterations | Create iteration
*ExperimentsApi* | [**get_experiment**](docs/ExperimentsApi.md#get_experiment) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey} | Get experiment
*ExperimentsApi* | [**get_experiment_results**](docs/ExperimentsApi.md#get_experiment_results) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey}/metrics/{metricKey}/results | Get experiment results
*ExperimentsApi* | [**get_experiment_results_for_metric_group**](docs/ExperimentsApi.md#get_experiment_results_for_metric_group) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey}/metric-groups/{metricGroupKey}/results | Get experiment results for metric group
*ExperimentsApi* | [**get_experimentation_settings**](docs/ExperimentsApi.md#get_experimentation_settings) | **GET** /api/v2/projects/{projectKey}/experimentation-settings | Get experimentation settings
*ExperimentsApi* | [**get_experiments**](docs/ExperimentsApi.md#get_experiments) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments | Get experiments
*ExperimentsApi* | [**get_legacy_experiment_results**](docs/ExperimentsApi.md#get_legacy_experiment_results) | **GET** /api/v2/flags/{projectKey}/{featureFlagKey}/experiments/{environmentKey}/{metricKey} | Get legacy experiment results (deprecated)
*ExperimentsApi* | [**patch_experiment**](docs/ExperimentsApi.md#patch_experiment) | **PATCH** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey} | Patch experiment
*ExperimentsApi* | [**put_experimentation_settings**](docs/ExperimentsApi.md#put_experimentation_settings) | **PUT** /api/v2/projects/{projectKey}/experimentation-settings | Update experimentation settings
*FeatureFlagsApi* | [**copy_feature_flag**](docs/FeatureFlagsApi.md#copy_feature_flag) | **POST** /api/v2/flags/{projectKey}/{featureFlagKey}/copy | Copy feature flag
*FeatureFlagsApi* | [**delete_feature_flag**](docs/FeatureFlagsApi.md#delete_feature_flag) | **DELETE** /api/v2/flags/{projectKey}/{featureFlagKey} | Delete feature flag
*FeatureFlagsApi* | [**get_expiring_context_targets**](docs/FeatureFlagsApi.md#get_expiring_context_targets) | **GET** /api/v2/flags/{projectKey}/{featureFlagKey}/expiring-targets/{environmentKey} | Get expiring context targets for feature flag
*FeatureFlagsApi* | [**get_expiring_user_targets**](docs/FeatureFlagsApi.md#get_expiring_user_targets) | **GET** /api/v2/flags/{projectKey}/{featureFlagKey}/expiring-user-targets/{environmentKey} | Get expiring user targets for feature flag
*FeatureFlagsApi* | [**get_feature_flag**](docs/FeatureFlagsApi.md#get_feature_flag) | **GET** /api/v2/flags/{projectKey}/{featureFlagKey} | Get feature flag
*FeatureFlagsApi* | [**get_feature_flag_status**](docs/FeatureFlagsApi.md#get_feature_flag_status) | **GET** /api/v2/flag-statuses/{projectKey}/{environmentKey}/{featureFlagKey} | Get feature flag status
*FeatureFlagsApi* | [**get_feature_flag_status_across_environments**](docs/FeatureFlagsApi.md#get_feature_flag_status_across_environments) | **GET** /api/v2/flag-status/{projectKey}/{featureFlagKey} | Get flag status across environments
*FeatureFlagsApi* | [**get_feature_flag_statuses**](docs/FeatureFlagsApi.md#get_feature_flag_statuses) | **GET** /api/v2/flag-statuses/{projectKey}/{environmentKey} | List feature flag statuses
*FeatureFlagsApi* | [**get_feature_flags**](docs/FeatureFlagsApi.md#get_feature_flags) | **GET** /api/v2/flags/{projectKey} | List feature flags
*FeatureFlagsApi* | [**patch_expiring_targets**](docs/FeatureFlagsApi.md#patch_expiring_targets) | **PATCH** /api/v2/flags/{projectKey}/{featureFlagKey}/expiring-targets/{environmentKey} | Update expiring context targets on feature flag
*FeatureFlagsApi* | [**patch_expiring_user_targets**](docs/FeatureFlagsApi.md#patch_expiring_user_targets) | **PATCH** /api/v2/flags/{projectKey}/{featureFlagKey}/expiring-user-targets/{environmentKey} | Update expiring user targets on feature flag
*FeatureFlagsApi* | [**patch_feature_flag**](docs/FeatureFlagsApi.md#patch_feature_flag) | **PATCH** /api/v2/flags/{projectKey}/{featureFlagKey} | Update feature flag
*FeatureFlagsApi* | [**post_feature_flag**](docs/FeatureFlagsApi.md#post_feature_flag) | **POST** /api/v2/flags/{projectKey} | Create a feature flag
*FeatureFlagsApi* | [**post_migration_safety_issues**](docs/FeatureFlagsApi.md#post_migration_safety_issues) | **POST** /api/v2/projects/{projectKey}/flags/{flagKey}/environments/{environmentKey}/migration-safety-issues | Get migration safety issues
*FeatureFlagsBetaApi* | [**get_dependent_flags**](docs/FeatureFlagsBetaApi.md#get_dependent_flags) | **GET** /api/v2/flags/{projectKey}/{featureFlagKey}/dependent-flags | List dependent feature flags
*FeatureFlagsBetaApi* | [**get_dependent_flags_by_env**](docs/FeatureFlagsBetaApi.md#get_dependent_flags_by_env) | **GET** /api/v2/flags/{projectKey}/{environmentKey}/{featureFlagKey}/dependent-flags | List dependent feature flags by environment
*FlagImportConfigurationsBetaApi* | [**create_flag_import_configuration**](docs/FlagImportConfigurationsBetaApi.md#create_flag_import_configuration) | **POST** /api/v2/integration-capabilities/flag-import/{projectKey}/{integrationKey} | Create a flag import configuration
*FlagImportConfigurationsBetaApi* | [**delete_flag_import_configuration**](docs/FlagImportConfigurationsBetaApi.md#delete_flag_import_configuration) | **DELETE** /api/v2/integration-capabilities/flag-import/{projectKey}/{integrationKey}/{integrationId} | Delete a flag import configuration
*FlagImportConfigurationsBetaApi* | [**get_flag_import_configuration**](docs/FlagImportConfigurationsBetaApi.md#get_flag_import_configuration) | **GET** /api/v2/integration-capabilities/flag-import/{projectKey}/{integrationKey}/{integrationId} | Get a single flag import configuration
*FlagImportConfigurationsBetaApi* | [**get_flag_import_configurations**](docs/FlagImportConfigurationsBetaApi.md#get_flag_import_configurations) | **GET** /api/v2/integration-capabilities/flag-import | List all flag import configurations
*FlagImportConfigurationsBetaApi* | [**patch_flag_import_configuration**](docs/FlagImportConfigurationsBetaApi.md#patch_flag_import_configuration) | **PATCH** /api/v2/integration-capabilities/flag-import/{projectKey}/{integrationKey}/{integrationId} | Update a flag import configuration
*FlagImportConfigurationsBetaApi* | [**trigger_flag_import_job**](docs/FlagImportConfigurationsBetaApi.md#trigger_flag_import_job) | **POST** /api/v2/integration-capabilities/flag-import/{projectKey}/{integrationKey}/{integrationId}/trigger | Trigger a single flag import run
*FlagLinksBetaApi* | [**create_flag_link**](docs/FlagLinksBetaApi.md#create_flag_link) | **POST** /api/v2/flag-links/projects/{projectKey}/flags/{featureFlagKey} | Create flag link
*FlagLinksBetaApi* | [**delete_flag_link**](docs/FlagLinksBetaApi.md#delete_flag_link) | **DELETE** /api/v2/flag-links/projects/{projectKey}/flags/{featureFlagKey}/{id} | Delete flag link
*FlagLinksBetaApi* | [**get_flag_links**](docs/FlagLinksBetaApi.md#get_flag_links) | **GET** /api/v2/flag-links/projects/{projectKey}/flags/{featureFlagKey} | List flag links
*FlagLinksBetaApi* | [**update_flag_link**](docs/FlagLinksBetaApi.md#update_flag_link) | **PATCH** /api/v2/flag-links/projects/{projectKey}/flags/{featureFlagKey}/{id} | Update flag link
*FlagTriggersApi* | [**create_trigger_workflow**](docs/FlagTriggersApi.md#create_trigger_workflow) | **POST** /api/v2/flags/{projectKey}/{featureFlagKey}/triggers/{environmentKey} | Create flag trigger
*FlagTriggersApi* | [**delete_trigger_workflow**](docs/FlagTriggersApi.md#delete_trigger_workflow) | **DELETE** /api/v2/flags/{projectKey}/{featureFlagKey}/triggers/{environmentKey}/{id} | Delete flag trigger
*FlagTriggersApi* | [**get_trigger_workflow_by_id**](docs/FlagTriggersApi.md#get_trigger_workflow_by_id) | **GET** /api/v2/flags/{projectKey}/{featureFlagKey}/triggers/{environmentKey}/{id} | Get flag trigger by ID
*FlagTriggersApi* | [**get_trigger_workflows**](docs/FlagTriggersApi.md#get_trigger_workflows) | **GET** /api/v2/flags/{projectKey}/{featureFlagKey}/triggers/{environmentKey} | List flag triggers
*FlagTriggersApi* | [**patch_trigger_workflow**](docs/FlagTriggersApi.md#patch_trigger_workflow) | **PATCH** /api/v2/flags/{projectKey}/{featureFlagKey}/triggers/{environmentKey}/{id} | Update flag trigger
*FollowFlagsApi* | [**delete_flag_follower**](docs/FollowFlagsApi.md#delete_flag_follower) | **DELETE** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/followers/{memberId} | Remove a member as a follower of a flag in a project and environment
*FollowFlagsApi* | [**get_flag_followers**](docs/FollowFlagsApi.md#get_flag_followers) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/followers | Get followers of a flag in a project and environment
*FollowFlagsApi* | [**get_followers_by_proj_env**](docs/FollowFlagsApi.md#get_followers_by_proj_env) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/followers | Get followers of all flags in a given project and environment
*FollowFlagsApi* | [**put_flag_follower**](docs/FollowFlagsApi.md#put_flag_follower) | **PUT** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/followers/{memberId} | Add a member as a follower of a flag in a project and environment
*HoldoutsBetaApi* | [**get_all_holdouts**](docs/HoldoutsBetaApi.md#get_all_holdouts) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/holdouts | Get all holdouts
*HoldoutsBetaApi* | [**get_holdout**](docs/HoldoutsBetaApi.md#get_holdout) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/holdouts/{holdoutKey} | Get holdout
*HoldoutsBetaApi* | [**get_holdout_by_id**](docs/HoldoutsBetaApi.md#get_holdout_by_id) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/holdouts/id/{holdoutId} | Get Holdout by Id
*HoldoutsBetaApi* | [**patch_holdout**](docs/HoldoutsBetaApi.md#patch_holdout) | **PATCH** /api/v2/projects/{projectKey}/environments/{environmentKey}/holdouts/{holdoutKey} | Patch holdout
*HoldoutsBetaApi* | [**post_holdout**](docs/HoldoutsBetaApi.md#post_holdout) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/holdouts | Create holdout
*InsightsChartsBetaApi* | [**get_deployment_frequency_chart**](docs/InsightsChartsBetaApi.md#get_deployment_frequency_chart) | **GET** /api/v2/engineering-insights/charts/deployments/frequency | Get deployment frequency chart data
*InsightsChartsBetaApi* | [**get_flag_status_chart**](docs/InsightsChartsBetaApi.md#get_flag_status_chart) | **GET** /api/v2/engineering-insights/charts/flags/status | Get flag status chart data
*InsightsChartsBetaApi* | [**get_lead_time_chart**](docs/InsightsChartsBetaApi.md#get_lead_time_chart) | **GET** /api/v2/engineering-insights/charts/lead-time | Get lead time chart data
*InsightsChartsBetaApi* | [**get_release_frequency_chart**](docs/InsightsChartsBetaApi.md#get_release_frequency_chart) | **GET** /api/v2/engineering-insights/charts/releases/frequency | Get release frequency chart data
*InsightsChartsBetaApi* | [**get_stale_flags_chart**](docs/InsightsChartsBetaApi.md#get_stale_flags_chart) | **GET** /api/v2/engineering-insights/charts/flags/stale | Get stale flags chart data
*InsightsDeploymentsBetaApi* | [**create_deployment_event**](docs/InsightsDeploymentsBetaApi.md#create_deployment_event) | **POST** /api/v2/engineering-insights/deployment-events | Create deployment event
*InsightsDeploymentsBetaApi* | [**get_deployment**](docs/InsightsDeploymentsBetaApi.md#get_deployment) | **GET** /api/v2/engineering-insights/deployments/{deploymentID} | Get deployment
*InsightsDeploymentsBetaApi* | [**get_deployments**](docs/InsightsDeploymentsBetaApi.md#get_deployments) | **GET** /api/v2/engineering-insights/deployments | List deployments
*InsightsDeploymentsBetaApi* | [**update_deployment**](docs/InsightsDeploymentsBetaApi.md#update_deployment) | **PATCH** /api/v2/engineering-insights/deployments/{deploymentID} | Update deployment
*InsightsFlagEventsBetaApi* | [**get_flag_events**](docs/InsightsFlagEventsBetaApi.md#get_flag_events) | **GET** /api/v2/engineering-insights/flag-events | List flag events
*InsightsPullRequestsBetaApi* | [**get_pull_requests**](docs/InsightsPullRequestsBetaApi.md#get_pull_requests) | **GET** /api/v2/engineering-insights/pull-requests | List pull requests
*InsightsRepositoriesBetaApi* | [**associate_repositories_and_projects**](docs/InsightsRepositoriesBetaApi.md#associate_repositories_and_projects) | **PUT** /api/v2/engineering-insights/repositories/projects | Associate repositories with projects
*InsightsRepositoriesBetaApi* | [**delete_repository_project**](docs/InsightsRepositoriesBetaApi.md#delete_repository_project) | **DELETE** /api/v2/engineering-insights/repositories/{repositoryKey}/projects/{projectKey} | Remove repository project association
*InsightsRepositoriesBetaApi* | [**get_insights_repositories**](docs/InsightsRepositoriesBetaApi.md#get_insights_repositories) | **GET** /api/v2/engineering-insights/repositories | List repositories
*InsightsScoresBetaApi* | [**create_insight_group**](docs/InsightsScoresBetaApi.md#create_insight_group) | **POST** /api/v2/engineering-insights/insights/group | Create insight group
*InsightsScoresBetaApi* | [**delete_insight_group**](docs/InsightsScoresBetaApi.md#delete_insight_group) | **DELETE** /api/v2/engineering-insights/insights/groups/{insightGroupKey} | Delete insight group
*InsightsScoresBetaApi* | [**get_insight_group**](docs/InsightsScoresBetaApi.md#get_insight_group) | **GET** /api/v2/engineering-insights/insights/groups/{insightGroupKey} | Get insight group
*InsightsScoresBetaApi* | [**get_insight_groups**](docs/InsightsScoresBetaApi.md#get_insight_groups) | **GET** /api/v2/engineering-insights/insights/groups | List insight groups
*InsightsScoresBetaApi* | [**get_insights_scores**](docs/InsightsScoresBetaApi.md#get_insights_scores) | **GET** /api/v2/engineering-insights/insights/scores | Get insight scores
*InsightsScoresBetaApi* | [**patch_insight_group**](docs/InsightsScoresBetaApi.md#patch_insight_group) | **PATCH** /api/v2/engineering-insights/insights/groups/{insightGroupKey} | Patch insight group
*IntegrationAuditLogSubscriptionsApi* | [**create_subscription**](docs/IntegrationAuditLogSubscriptionsApi.md#create_subscription) | **POST** /api/v2/integrations/{integrationKey} | Create audit log subscription
*IntegrationAuditLogSubscriptionsApi* | [**delete_subscription**](docs/IntegrationAuditLogSubscriptionsApi.md#delete_subscription) | **DELETE** /api/v2/integrations/{integrationKey}/{id} | Delete audit log subscription
*IntegrationAuditLogSubscriptionsApi* | [**get_subscription_by_id**](docs/IntegrationAuditLogSubscriptionsApi.md#get_subscription_by_id) | **GET** /api/v2/integrations/{integrationKey}/{id} | Get audit log subscription by ID
*IntegrationAuditLogSubscriptionsApi* | [**get_subscriptions**](docs/IntegrationAuditLogSubscriptionsApi.md#get_subscriptions) | **GET** /api/v2/integrations/{integrationKey} | Get audit log subscriptions by integration
*IntegrationAuditLogSubscriptionsApi* | [**update_subscription**](docs/IntegrationAuditLogSubscriptionsApi.md#update_subscription) | **PATCH** /api/v2/integrations/{integrationKey}/{id} | Update audit log subscription
*IntegrationDeliveryConfigurationsBetaApi* | [**create_integration_delivery_configuration**](docs/IntegrationDeliveryConfigurationsBetaApi.md#create_integration_delivery_configuration) | **POST** /api/v2/integration-capabilities/featureStore/{projectKey}/{environmentKey}/{integrationKey} | Create delivery configuration
*IntegrationDeliveryConfigurationsBetaApi* | [**delete_integration_delivery_configuration**](docs/IntegrationDeliveryConfigurationsBetaApi.md#delete_integration_delivery_configuration) | **DELETE** /api/v2/integration-capabilities/featureStore/{projectKey}/{environmentKey}/{integrationKey}/{id} | Delete delivery configuration
*IntegrationDeliveryConfigurationsBetaApi* | [**get_integration_delivery_configuration_by_environment**](docs/IntegrationDeliveryConfigurationsBetaApi.md#get_integration_delivery_configuration_by_environment) | **GET** /api/v2/integration-capabilities/featureStore/{projectKey}/{environmentKey} | Get delivery configurations by environment
*IntegrationDeliveryConfigurationsBetaApi* | [**get_integration_delivery_configuration_by_id**](docs/IntegrationDeliveryConfigurationsBetaApi.md#get_integration_delivery_configuration_by_id) | **GET** /api/v2/integration-capabilities/featureStore/{projectKey}/{environmentKey}/{integrationKey}/{id} | Get delivery configuration by ID
*IntegrationDeliveryConfigurationsBetaApi* | [**get_integration_delivery_configurations**](docs/IntegrationDeliveryConfigurationsBetaApi.md#get_integration_delivery_configurations) | **GET** /api/v2/integration-capabilities/featureStore | List all delivery configurations
*IntegrationDeliveryConfigurationsBetaApi* | [**patch_integration_delivery_configuration**](docs/IntegrationDeliveryConfigurationsBetaApi.md#patch_integration_delivery_configuration) | **PATCH** /api/v2/integration-capabilities/featureStore/{projectKey}/{environmentKey}/{integrationKey}/{id} | Update delivery configuration
*IntegrationDeliveryConfigurationsBetaApi* | [**validate_integration_delivery_configuration**](docs/IntegrationDeliveryConfigurationsBetaApi.md#validate_integration_delivery_configuration) | **POST** /api/v2/integration-capabilities/featureStore/{projectKey}/{environmentKey}/{integrationKey}/{id}/validate | Validate delivery configuration
*IntegrationsBetaApi* | [**create_integration_configuration**](docs/IntegrationsBetaApi.md#create_integration_configuration) | **POST** /api/v2/integration-configurations/keys/{integrationKey} | Create integration configuration
*IntegrationsBetaApi* | [**delete_integration_configuration**](docs/IntegrationsBetaApi.md#delete_integration_configuration) | **DELETE** /api/v2/integration-configurations/{integrationConfigurationId} | Delete integration configuration
*IntegrationsBetaApi* | [**get_all_integration_configurations**](docs/IntegrationsBetaApi.md#get_all_integration_configurations) | **GET** /api/v2/integration-configurations/keys/{integrationKey} | Get all configurations for the integration
*IntegrationsBetaApi* | [**get_integration_configuration**](docs/IntegrationsBetaApi.md#get_integration_configuration) | **GET** /api/v2/integration-configurations/{integrationConfigurationId} | Get an integration configuration
*IntegrationsBetaApi* | [**update_integration_configuration**](docs/IntegrationsBetaApi.md#update_integration_configuration) | **PATCH** /api/v2/integration-configurations/{integrationConfigurationId} | Update integration configuration
*LayersApi* | [**create_layer**](docs/LayersApi.md#create_layer) | **POST** /api/v2/projects/{projectKey}/layers | Create layer
*LayersApi* | [**get_layers**](docs/LayersApi.md#get_layers) | **GET** /api/v2/projects/{projectKey}/layers | Get layers
*LayersApi* | [**update_layer**](docs/LayersApi.md#update_layer) | **PATCH** /api/v2/projects/{projectKey}/layers/{layerKey} | Update layer
*MetricsApi* | [**delete_metric**](docs/MetricsApi.md#delete_metric) | **DELETE** /api/v2/metrics/{projectKey}/{metricKey} | Delete metric
*MetricsApi* | [**get_metric**](docs/MetricsApi.md#get_metric) | **GET** /api/v2/metrics/{projectKey}/{metricKey} | Get metric
*MetricsApi* | [**get_metrics**](docs/MetricsApi.md#get_metrics) | **GET** /api/v2/metrics/{projectKey} | List metrics
*MetricsApi* | [**patch_metric**](docs/MetricsApi.md#patch_metric) | **PATCH** /api/v2/metrics/{projectKey}/{metricKey} | Update metric
*MetricsApi* | [**post_metric**](docs/MetricsApi.md#post_metric) | **POST** /api/v2/metrics/{projectKey} | Create metric
*MetricsBetaApi* | [**create_metric_group**](docs/MetricsBetaApi.md#create_metric_group) | **POST** /api/v2/projects/{projectKey}/metric-groups | Create metric group
*MetricsBetaApi* | [**delete_metric_group**](docs/MetricsBetaApi.md#delete_metric_group) | **DELETE** /api/v2/projects/{projectKey}/metric-groups/{metricGroupKey} | Delete metric group
*MetricsBetaApi* | [**get_metric_group**](docs/MetricsBetaApi.md#get_metric_group) | **GET** /api/v2/projects/{projectKey}/metric-groups/{metricGroupKey} | Get metric group
*MetricsBetaApi* | [**get_metric_groups**](docs/MetricsBetaApi.md#get_metric_groups) | **GET** /api/v2/projects/{projectKey}/metric-groups | List metric groups
*MetricsBetaApi* | [**patch_metric_group**](docs/MetricsBetaApi.md#patch_metric_group) | **PATCH** /api/v2/projects/{projectKey}/metric-groups/{metricGroupKey} | Patch metric group
*OAuth2ClientsApi* | [**create_o_auth2_client**](docs/OAuth2ClientsApi.md#create_o_auth2_client) | **POST** /api/v2/oauth/clients | Create a LaunchDarkly OAuth 2.0 client
*OAuth2ClientsApi* | [**delete_o_auth_client**](docs/OAuth2ClientsApi.md#delete_o_auth_client) | **DELETE** /api/v2/oauth/clients/{clientId} | Delete OAuth 2.0 client
*OAuth2ClientsApi* | [**get_o_auth_client_by_id**](docs/OAuth2ClientsApi.md#get_o_auth_client_by_id) | **GET** /api/v2/oauth/clients/{clientId} | Get client by ID
*OAuth2ClientsApi* | [**get_o_auth_clients**](docs/OAuth2ClientsApi.md#get_o_auth_clients) | **GET** /api/v2/oauth/clients | Get clients
*OAuth2ClientsApi* | [**patch_o_auth_client**](docs/OAuth2ClientsApi.md#patch_o_auth_client) | **PATCH** /api/v2/oauth/clients/{clientId} | Patch client by ID
*OtherApi* | [**get_caller_identity**](docs/OtherApi.md#get_caller_identity) | **GET** /api/v2/caller-identity | Identify the caller
*OtherApi* | [**get_ips**](docs/OtherApi.md#get_ips) | **GET** /api/v2/public-ip-list | Gets the public IP list
*OtherApi* | [**get_openapi_spec**](docs/OtherApi.md#get_openapi_spec) | **GET** /api/v2/openapi.json | Gets the OpenAPI spec in json
*OtherApi* | [**get_root**](docs/OtherApi.md#get_root) | **GET** /api/v2 | Root resource
*OtherApi* | [**get_versions**](docs/OtherApi.md#get_versions) | **GET** /api/v2/versions | Get version information
*PersistentStoreIntegrationsBetaApi* | [**create_big_segment_store_integration**](docs/PersistentStoreIntegrationsBetaApi.md#create_big_segment_store_integration) | **POST** /api/v2/integration-capabilities/big-segment-store/{projectKey}/{environmentKey}/{integrationKey} | Create big segment store integration
*PersistentStoreIntegrationsBetaApi* | [**delete_big_segment_store_integration**](docs/PersistentStoreIntegrationsBetaApi.md#delete_big_segment_store_integration) | **DELETE** /api/v2/integration-capabilities/big-segment-store/{projectKey}/{environmentKey}/{integrationKey}/{integrationId} | Delete big segment store integration
*PersistentStoreIntegrationsBetaApi* | [**get_big_segment_store_integration**](docs/PersistentStoreIntegrationsBetaApi.md#get_big_segment_store_integration) | **GET** /api/v2/integration-capabilities/big-segment-store/{projectKey}/{environmentKey}/{integrationKey}/{integrationId} | Get big segment store integration by ID
*PersistentStoreIntegrationsBetaApi* | [**get_big_segment_store_integrations**](docs/PersistentStoreIntegrationsBetaApi.md#get_big_segment_store_integrations) | **GET** /api/v2/integration-capabilities/big-segment-store | List all big segment store integrations
*PersistentStoreIntegrationsBetaApi* | [**patch_big_segment_store_integration**](docs/PersistentStoreIntegrationsBetaApi.md#patch_big_segment_store_integration) | **PATCH** /api/v2/integration-capabilities/big-segment-store/{projectKey}/{environmentKey}/{integrationKey}/{integrationId} | Update big segment store integration
*ProjectsApi* | [**delete_project**](docs/ProjectsApi.md#delete_project) | **DELETE** /api/v2/projects/{projectKey} | Delete project
*ProjectsApi* | [**get_flag_defaults_by_project**](docs/ProjectsApi.md#get_flag_defaults_by_project) | **GET** /api/v2/projects/{projectKey}/flag-defaults | Get flag defaults for project
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /api/v2/projects/{projectKey} | Get project
*ProjectsApi* | [**get_projects**](docs/ProjectsApi.md#get_projects) | **GET** /api/v2/projects | List projects
*ProjectsApi* | [**patch_flag_defaults_by_project**](docs/ProjectsApi.md#patch_flag_defaults_by_project) | **PATCH** /api/v2/projects/{projectKey}/flag-defaults | Update flag default for project
*ProjectsApi* | [**patch_project**](docs/ProjectsApi.md#patch_project) | **PATCH** /api/v2/projects/{projectKey} | Update project
*ProjectsApi* | [**post_project**](docs/ProjectsApi.md#post_project) | **POST** /api/v2/projects | Create project
*ProjectsApi* | [**put_flag_defaults_by_project**](docs/ProjectsApi.md#put_flag_defaults_by_project) | **PUT** /api/v2/projects/{projectKey}/flag-defaults | Create or update flag defaults for project
*RelayProxyConfigurationsApi* | [**delete_relay_auto_config**](docs/RelayProxyConfigurationsApi.md#delete_relay_auto_config) | **DELETE** /api/v2/account/relay-auto-configs/{id} | Delete Relay Proxy config by ID
*RelayProxyConfigurationsApi* | [**get_relay_proxy_config**](docs/RelayProxyConfigurationsApi.md#get_relay_proxy_config) | **GET** /api/v2/account/relay-auto-configs/{id} | Get Relay Proxy config
*RelayProxyConfigurationsApi* | [**get_relay_proxy_configs**](docs/RelayProxyConfigurationsApi.md#get_relay_proxy_configs) | **GET** /api/v2/account/relay-auto-configs | List Relay Proxy configs
*RelayProxyConfigurationsApi* | [**patch_relay_auto_config**](docs/RelayProxyConfigurationsApi.md#patch_relay_auto_config) | **PATCH** /api/v2/account/relay-auto-configs/{id} | Update a Relay Proxy config
*RelayProxyConfigurationsApi* | [**post_relay_auto_config**](docs/RelayProxyConfigurationsApi.md#post_relay_auto_config) | **POST** /api/v2/account/relay-auto-configs | Create a new Relay Proxy config
*RelayProxyConfigurationsApi* | [**reset_relay_auto_config**](docs/RelayProxyConfigurationsApi.md#reset_relay_auto_config) | **POST** /api/v2/account/relay-auto-configs/{id}/reset | Reset Relay Proxy configuration key
*ReleasePipelinesBetaApi* | [**delete_release_pipeline**](docs/ReleasePipelinesBetaApi.md#delete_release_pipeline) | **DELETE** /api/v2/projects/{projectKey}/release-pipelines/{pipelineKey} | Delete release pipeline
*ReleasePipelinesBetaApi* | [**get_all_release_pipelines**](docs/ReleasePipelinesBetaApi.md#get_all_release_pipelines) | **GET** /api/v2/projects/{projectKey}/release-pipelines | Get all release pipelines
*ReleasePipelinesBetaApi* | [**get_all_release_progressions_for_release_pipeline**](docs/ReleasePipelinesBetaApi.md#get_all_release_progressions_for_release_pipeline) | **GET** /api/v2/projects/{projectKey}/release-pipelines/{pipelineKey}/releases | Get release progressions for release pipeline
*ReleasePipelinesBetaApi* | [**get_release_pipeline_by_key**](docs/ReleasePipelinesBetaApi.md#get_release_pipeline_by_key) | **GET** /api/v2/projects/{projectKey}/release-pipelines/{pipelineKey} | Get release pipeline by key
*ReleasePipelinesBetaApi* | [**post_release_pipeline**](docs/ReleasePipelinesBetaApi.md#post_release_pipeline) | **POST** /api/v2/projects/{projectKey}/release-pipelines | Create a release pipeline
*ReleasePipelinesBetaApi* | [**put_release_pipeline**](docs/ReleasePipelinesBetaApi.md#put_release_pipeline) | **PUT** /api/v2/projects/{projectKey}/release-pipelines/{pipelineKey} | Update a release pipeline
*ReleasesBetaApi* | [**create_release_for_flag**](docs/ReleasesBetaApi.md#create_release_for_flag) | **PUT** /api/v2/projects/{projectKey}/flags/{flagKey}/release | Create a new release for flag
*ReleasesBetaApi* | [**delete_release_by_flag_key**](docs/ReleasesBetaApi.md#delete_release_by_flag_key) | **DELETE** /api/v2/flags/{projectKey}/{flagKey}/release | Delete a release for flag
*ReleasesBetaApi* | [**get_release_by_flag_key**](docs/ReleasesBetaApi.md#get_release_by_flag_key) | **GET** /api/v2/flags/{projectKey}/{flagKey}/release | Get release for flag
*ReleasesBetaApi* | [**patch_release_by_flag_key**](docs/ReleasesBetaApi.md#patch_release_by_flag_key) | **PATCH** /api/v2/flags/{projectKey}/{flagKey}/release | Patch release for flag
*ReleasesBetaApi* | [**update_phase_status**](docs/ReleasesBetaApi.md#update_phase_status) | **PUT** /api/v2/projects/{projectKey}/flags/{flagKey}/release/phases/{phaseId} | Update phase status for release
*ScheduledChangesApi* | [**delete_flag_config_scheduled_changes**](docs/ScheduledChangesApi.md#delete_flag_config_scheduled_changes) | **DELETE** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes/{id} | Delete scheduled changes workflow
*ScheduledChangesApi* | [**get_feature_flag_scheduled_change**](docs/ScheduledChangesApi.md#get_feature_flag_scheduled_change) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes/{id} | Get a scheduled change
*ScheduledChangesApi* | [**get_flag_config_scheduled_changes**](docs/ScheduledChangesApi.md#get_flag_config_scheduled_changes) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes | List scheduled changes
*ScheduledChangesApi* | [**patch_flag_config_scheduled_change**](docs/ScheduledChangesApi.md#patch_flag_config_scheduled_change) | **PATCH** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes/{id} | Update scheduled changes workflow
*ScheduledChangesApi* | [**post_flag_config_scheduled_changes**](docs/ScheduledChangesApi.md#post_flag_config_scheduled_changes) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes | Create scheduled changes workflow
*SegmentsApi* | [**delete_segment**](docs/SegmentsApi.md#delete_segment) | **DELETE** /api/v2/segments/{projectKey}/{environmentKey}/{segmentKey} | Delete segment
*SegmentsApi* | [**get_context_instance_segments_membership_by_env**](docs/SegmentsApi.md#get_context_instance_segments_membership_by_env) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/segments/evaluate | List segment memberships for context instance
*SegmentsApi* | [**get_expiring_targets_for_segment**](docs/SegmentsApi.md#get_expiring_targets_for_segment) | **GET** /api/v2/segments/{projectKey}/{segmentKey}/expiring-targets/{environmentKey} | Get expiring targets for segment
*SegmentsApi* | [**get_expiring_user_targets_for_segment**](docs/SegmentsApi.md#get_expiring_user_targets_for_segment) | **GET** /api/v2/segments/{projectKey}/{segmentKey}/expiring-user-targets/{environmentKey} | Get expiring user targets for segment
*SegmentsApi* | [**get_segment**](docs/SegmentsApi.md#get_segment) | **GET** /api/v2/segments/{projectKey}/{environmentKey}/{segmentKey} | Get segment
*SegmentsApi* | [**get_segment_membership_for_context**](docs/SegmentsApi.md#get_segment_membership_for_context) | **GET** /api/v2/segments/{projectKey}/{environmentKey}/{segmentKey}/contexts/{contextKey} | Get big segment membership for context
*SegmentsApi* | [**get_segment_membership_for_user**](docs/SegmentsApi.md#get_segment_membership_for_user) | **GET** /api/v2/segments/{projectKey}/{environmentKey}/{segmentKey}/users/{userKey} | Get big segment membership for user
*SegmentsApi* | [**get_segments**](docs/SegmentsApi.md#get_segments) | **GET** /api/v2/segments/{projectKey}/{environmentKey} | List segments
*SegmentsApi* | [**patch_expiring_targets_for_segment**](docs/SegmentsApi.md#patch_expiring_targets_for_segment) | **PATCH** /api/v2/segments/{projectKey}/{segmentKey}/expiring-targets/{environmentKey} | Update expiring targets for segment
*SegmentsApi* | [**patch_expiring_user_targets_for_segment**](docs/SegmentsApi.md#patch_expiring_user_targets_for_segment) | **PATCH** /api/v2/segments/{projectKey}/{segmentKey}/expiring-user-targets/{environmentKey} | Update expiring user targets for segment
*SegmentsApi* | [**patch_segment**](docs/SegmentsApi.md#patch_segment) | **PATCH** /api/v2/segments/{projectKey}/{environmentKey}/{segmentKey} | Patch segment
*SegmentsApi* | [**post_segment**](docs/SegmentsApi.md#post_segment) | **POST** /api/v2/segments/{projectKey}/{environmentKey} | Create segment
*SegmentsApi* | [**update_big_segment_context_targets**](docs/SegmentsApi.md#update_big_segment_context_targets) | **POST** /api/v2/segments/{projectKey}/{environmentKey}/{segmentKey}/contexts | Update context targets on a big segment
*SegmentsApi* | [**update_big_segment_targets**](docs/SegmentsApi.md#update_big_segment_targets) | **POST** /api/v2/segments/{projectKey}/{environmentKey}/{segmentKey}/users | Update user context targets on a big segment
*SegmentsBetaApi* | [**create_big_segment_export**](docs/SegmentsBetaApi.md#create_big_segment_export) | **POST** /api/v2/segments/{projectKey}/{environmentKey}/{segmentKey}/exports | Create big segment export
*SegmentsBetaApi* | [**create_big_segment_import**](docs/SegmentsBetaApi.md#create_big_segment_import) | **POST** /api/v2/segments/{projectKey}/{environmentKey}/{segmentKey}/imports | Create big segment import
*SegmentsBetaApi* | [**get_big_segment_export**](docs/SegmentsBetaApi.md#get_big_segment_export) | **GET** /api/v2/segments/{projectKey}/{environmentKey}/{segmentKey}/exports/{exportID} | Get big segment export
*SegmentsBetaApi* | [**get_big_segment_import**](docs/SegmentsBetaApi.md#get_big_segment_import) | **GET** /api/v2/segments/{projectKey}/{environmentKey}/{segmentKey}/imports/{importID} | Get big segment import
*TagsApi* | [**get_tags**](docs/TagsApi.md#get_tags) | **GET** /api/v2/tags | List tags
*TeamsApi* | [**delete_team**](docs/TeamsApi.md#delete_team) | **DELETE** /api/v2/teams/{teamKey} | Delete team
*TeamsApi* | [**get_team**](docs/TeamsApi.md#get_team) | **GET** /api/v2/teams/{teamKey} | Get team
*TeamsApi* | [**get_team_maintainers**](docs/TeamsApi.md#get_team_maintainers) | **GET** /api/v2/teams/{teamKey}/maintainers | Get team maintainers
*TeamsApi* | [**get_team_roles**](docs/TeamsApi.md#get_team_roles) | **GET** /api/v2/teams/{teamKey}/roles | Get team custom roles
*TeamsApi* | [**get_teams**](docs/TeamsApi.md#get_teams) | **GET** /api/v2/teams | List teams
*TeamsApi* | [**patch_team**](docs/TeamsApi.md#patch_team) | **PATCH** /api/v2/teams/{teamKey} | Update team
*TeamsApi* | [**post_team**](docs/TeamsApi.md#post_team) | **POST** /api/v2/teams | Create team
*TeamsApi* | [**post_team_members**](docs/TeamsApi.md#post_team_members) | **POST** /api/v2/teams/{teamKey}/members | Add multiple members to team
*TeamsBetaApi* | [**patch_teams**](docs/TeamsBetaApi.md#patch_teams) | **PATCH** /api/v2/teams | Update teams
*UserSettingsApi* | [**get_expiring_flags_for_user**](docs/UserSettingsApi.md#get_expiring_flags_for_user) | **GET** /api/v2/users/{projectKey}/{userKey}/expiring-user-targets/{environmentKey} | Get expiring dates on flags for user
*UserSettingsApi* | [**get_user_flag_setting**](docs/UserSettingsApi.md#get_user_flag_setting) | **GET** /api/v2/users/{projectKey}/{environmentKey}/{userKey}/flags/{featureFlagKey} | Get flag setting for user
*UserSettingsApi* | [**get_user_flag_settings**](docs/UserSettingsApi.md#get_user_flag_settings) | **GET** /api/v2/users/{projectKey}/{environmentKey}/{userKey}/flags | List flag settings for user
*UserSettingsApi* | [**patch_expiring_flags_for_user**](docs/UserSettingsApi.md#patch_expiring_flags_for_user) | **PATCH** /api/v2/users/{projectKey}/{userKey}/expiring-user-targets/{environmentKey} | Update expiring user target for flags
*UserSettingsApi* | [**put_flag_setting**](docs/UserSettingsApi.md#put_flag_setting) | **PUT** /api/v2/users/{projectKey}/{environmentKey}/{userKey}/flags/{featureFlagKey} | Update flag settings for user
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /api/v2/users/{projectKey}/{environmentKey}/{userKey} | Delete user
*UsersApi* | [**get_search_users**](docs/UsersApi.md#get_search_users) | **GET** /api/v2/user-search/{projectKey}/{environmentKey} | Find users
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /api/v2/users/{projectKey}/{environmentKey}/{userKey} | Get user
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /api/v2/users/{projectKey}/{environmentKey} | List users
*UsersBetaApi* | [**get_user_attribute_names**](docs/UsersBetaApi.md#get_user_attribute_names) | **GET** /api/v2/user-attributes/{projectKey}/{environmentKey} | Get user attribute names
*WebhooksApi* | [**delete_webhook**](docs/WebhooksApi.md#delete_webhook) | **DELETE** /api/v2/webhooks/{id} | Delete webhook
*WebhooksApi* | [**get_all_webhooks**](docs/WebhooksApi.md#get_all_webhooks) | **GET** /api/v2/webhooks | List webhooks
*WebhooksApi* | [**get_webhook**](docs/WebhooksApi.md#get_webhook) | **GET** /api/v2/webhooks/{id} | Get webhook
*WebhooksApi* | [**patch_webhook**](docs/WebhooksApi.md#patch_webhook) | **PATCH** /api/v2/webhooks/{id} | Update webhook
*WebhooksApi* | [**post_webhook**](docs/WebhooksApi.md#post_webhook) | **POST** /api/v2/webhooks | Creates a webhook
*WorkflowTemplatesApi* | [**create_workflow_template**](docs/WorkflowTemplatesApi.md#create_workflow_template) | **POST** /api/v2/templates | Create workflow template
*WorkflowTemplatesApi* | [**delete_workflow_template**](docs/WorkflowTemplatesApi.md#delete_workflow_template) | **DELETE** /api/v2/templates/{templateKey} | Delete workflow template
*WorkflowTemplatesApi* | [**get_workflow_templates**](docs/WorkflowTemplatesApi.md#get_workflow_templates) | **GET** /api/v2/templates | Get workflow templates
*WorkflowsApi* | [**delete_workflow**](docs/WorkflowsApi.md#delete_workflow) | **DELETE** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/workflows/{workflowId} | Delete workflow
*WorkflowsApi* | [**get_custom_workflow**](docs/WorkflowsApi.md#get_custom_workflow) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/workflows/{workflowId} | Get custom workflow
*WorkflowsApi* | [**get_workflows**](docs/WorkflowsApi.md#get_workflows) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/workflows | Get workflows
*WorkflowsApi* | [**post_workflow**](docs/WorkflowsApi.md#post_workflow) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/workflows | Create workflow


## Documentation For Models

 - [Access](docs/Access.md)
 - [AccessAllowedReason](docs/AccessAllowedReason.md)
 - [AccessAllowedRep](docs/AccessAllowedRep.md)
 - [AccessDenied](docs/AccessDenied.md)
 - [AccessDeniedReason](docs/AccessDeniedReason.md)
 - [AccessTokenPost](docs/AccessTokenPost.md)
 - [ActionInput](docs/ActionInput.md)
 - [ActionOutput](docs/ActionOutput.md)
 - [AllVariationsSummary](docs/AllVariationsSummary.md)
 - [ApplicationCollectionRep](docs/ApplicationCollectionRep.md)
 - [ApplicationFlagCollectionRep](docs/ApplicationFlagCollectionRep.md)
 - [ApplicationRep](docs/ApplicationRep.md)
 - [ApplicationVersionRep](docs/ApplicationVersionRep.md)
 - [ApplicationVersionsCollectionRep](docs/ApplicationVersionsCollectionRep.md)
 - [ApprovalRequestResponse](docs/ApprovalRequestResponse.md)
 - [ApprovalSettings](docs/ApprovalSettings.md)
 - [ApprovalsCapabilityConfig](docs/ApprovalsCapabilityConfig.md)
 - [Audience](docs/Audience.md)
 - [AudienceConfiguration](docs/AudienceConfiguration.md)
 - [AudiencePost](docs/AudiencePost.md)
 - [Audiences](docs/Audiences.md)
 - [AuditLogEntryListingRep](docs/AuditLogEntryListingRep.md)
 - [AuditLogEntryListingRepCollection](docs/AuditLogEntryListingRepCollection.md)
 - [AuditLogEntryRep](docs/AuditLogEntryRep.md)
 - [AuditLogEventsHookCapabilityConfigPost](docs/AuditLogEventsHookCapabilityConfigPost.md)
 - [AuditLogEventsHookCapabilityConfigRep](docs/AuditLogEventsHookCapabilityConfigRep.md)
 - [AuthorizedAppDataRep](docs/AuthorizedAppDataRep.md)
 - [BayesianBetaBinomialStatsRep](docs/BayesianBetaBinomialStatsRep.md)
 - [BayesianNormalStatsRep](docs/BayesianNormalStatsRep.md)
 - [BigSegmentStoreIntegration](docs/BigSegmentStoreIntegration.md)
 - [BigSegmentStoreIntegrationCollection](docs/BigSegmentStoreIntegrationCollection.md)
 - [BigSegmentStoreIntegrationCollectionLinks](docs/BigSegmentStoreIntegrationCollectionLinks.md)
 - [BigSegmentStoreIntegrationLinks](docs/BigSegmentStoreIntegrationLinks.md)
 - [BigSegmentStoreStatus](docs/BigSegmentStoreStatus.md)
 - [BigSegmentTarget](docs/BigSegmentTarget.md)
 - [BooleanDefaults](docs/BooleanDefaults.md)
 - [BooleanFlagDefaults](docs/BooleanFlagDefaults.md)
 - [BranchCollectionRep](docs/BranchCollectionRep.md)
 - [BranchRep](docs/BranchRep.md)
 - [BulkEditMembersRep](docs/BulkEditMembersRep.md)
 - [BulkEditTeamsRep](docs/BulkEditTeamsRep.md)
 - [CallerIdentityRep](docs/CallerIdentityRep.md)
 - [CapabilityConfigPost](docs/CapabilityConfigPost.md)
 - [CapabilityConfigRep](docs/CapabilityConfigRep.md)
 - [Clause](docs/Clause.md)
 - [Client](docs/Client.md)
 - [ClientCollection](docs/ClientCollection.md)
 - [ClientSideAvailability](docs/ClientSideAvailability.md)
 - [ClientSideAvailabilityPost](docs/ClientSideAvailabilityPost.md)
 - [CompletedBy](docs/CompletedBy.md)
 - [ConditionInput](docs/ConditionInput.md)
 - [ConditionOutput](docs/ConditionOutput.md)
 - [ConfidenceIntervalRep](docs/ConfidenceIntervalRep.md)
 - [Conflict](docs/Conflict.md)
 - [ConflictOutput](docs/ConflictOutput.md)
 - [ContextAttributeName](docs/ContextAttributeName.md)
 - [ContextAttributeNames](docs/ContextAttributeNames.md)
 - [ContextAttributeNamesCollection](docs/ContextAttributeNamesCollection.md)
 - [ContextAttributeValue](docs/ContextAttributeValue.md)
 - [ContextAttributeValues](docs/ContextAttributeValues.md)
 - [ContextAttributeValuesCollection](docs/ContextAttributeValuesCollection.md)
 - [ContextInstance](docs/ContextInstance.md)
 - [ContextInstanceEvaluation](docs/ContextInstanceEvaluation.md)
 - [ContextInstanceEvaluationReason](docs/ContextInstanceEvaluationReason.md)
 - [ContextInstanceEvaluations](docs/ContextInstanceEvaluations.md)
 - [ContextInstanceRecord](docs/ContextInstanceRecord.md)
 - [ContextInstanceSearch](docs/ContextInstanceSearch.md)
 - [ContextInstanceSegmentMembership](docs/ContextInstanceSegmentMembership.md)
 - [ContextInstanceSegmentMemberships](docs/ContextInstanceSegmentMemberships.md)
 - [ContextInstances](docs/ContextInstances.md)
 - [ContextKindRep](docs/ContextKindRep.md)
 - [ContextKindsCollectionRep](docs/ContextKindsCollectionRep.md)
 - [ContextRecord](docs/ContextRecord.md)
 - [ContextSearch](docs/ContextSearch.md)
 - [Contexts](docs/Contexts.md)
 - [CopiedFromEnv](docs/CopiedFromEnv.md)
 - [CreateApprovalRequestRequest](docs/CreateApprovalRequestRequest.md)
 - [CreateCopyFlagConfigApprovalRequestRequest](docs/CreateCopyFlagConfigApprovalRequestRequest.md)
 - [CreateFlagConfigApprovalRequestRequest](docs/CreateFlagConfigApprovalRequestRequest.md)
 - [CreatePhaseInput](docs/CreatePhaseInput.md)
 - [CreateReleaseInput](docs/CreateReleaseInput.md)
 - [CreateReleasePipelineInput](docs/CreateReleasePipelineInput.md)
 - [CreateWorkflowTemplateInput](docs/CreateWorkflowTemplateInput.md)
 - [CredibleIntervalRep](docs/CredibleIntervalRep.md)
 - [CustomProperties](docs/CustomProperties.md)
 - [CustomProperty](docs/CustomProperty.md)
 - [CustomRole](docs/CustomRole.md)
 - [CustomRolePost](docs/CustomRolePost.md)
 - [CustomRoles](docs/CustomRoles.md)
 - [CustomWorkflowInput](docs/CustomWorkflowInput.md)
 - [CustomWorkflowMeta](docs/CustomWorkflowMeta.md)
 - [CustomWorkflowOutput](docs/CustomWorkflowOutput.md)
 - [CustomWorkflowStageMeta](docs/CustomWorkflowStageMeta.md)
 - [CustomWorkflowsListingOutput](docs/CustomWorkflowsListingOutput.md)
 - [DefaultClientSideAvailability](docs/DefaultClientSideAvailability.md)
 - [DefaultClientSideAvailabilityPost](docs/DefaultClientSideAvailabilityPost.md)
 - [Defaults](docs/Defaults.md)
 - [DependentExperimentListRep](docs/DependentExperimentListRep.md)
 - [DependentExperimentRep](docs/DependentExperimentRep.md)
 - [DependentFlag](docs/DependentFlag.md)
 - [DependentFlagEnvironment](docs/DependentFlagEnvironment.md)
 - [DependentFlagsByEnvironment](docs/DependentFlagsByEnvironment.md)
 - [DependentMetricGroupRep](docs/DependentMetricGroupRep.md)
 - [DependentMetricGroupRepWithMetrics](docs/DependentMetricGroupRepWithMetrics.md)
 - [DependentMetricOrMetricGroupRep](docs/DependentMetricOrMetricGroupRep.md)
 - [DeploymentCollectionRep](docs/DeploymentCollectionRep.md)
 - [DeploymentRep](docs/DeploymentRep.md)
 - [Destination](docs/Destination.md)
 - [DestinationPost](docs/DestinationPost.md)
 - [Destinations](docs/Destinations.md)
 - [Distribution](docs/Distribution.md)
 - [DynamicOptions](docs/DynamicOptions.md)
 - [DynamicOptionsParser](docs/DynamicOptionsParser.md)
 - [Endpoint](docs/Endpoint.md)
 - [Environment](docs/Environment.md)
 - [EnvironmentPost](docs/EnvironmentPost.md)
 - [EnvironmentSummary](docs/EnvironmentSummary.md)
 - [Environments](docs/Environments.md)
 - [Error](docs/Error.md)
 - [EvaluationReason](docs/EvaluationReason.md)
 - [EvaluationsSummary](docs/EvaluationsSummary.md)
 - [ExecutionOutput](docs/ExecutionOutput.md)
 - [ExpandableApprovalRequestResponse](docs/ExpandableApprovalRequestResponse.md)
 - [ExpandableApprovalRequestsResponse](docs/ExpandableApprovalRequestsResponse.md)
 - [ExpandedFlagRep](docs/ExpandedFlagRep.md)
 - [ExpandedResourceRep](docs/ExpandedResourceRep.md)
 - [Experiment](docs/Experiment.md)
 - [ExperimentAllocationRep](docs/ExperimentAllocationRep.md)
 - [ExperimentBayesianResultsRep](docs/ExperimentBayesianResultsRep.md)
 - [ExperimentCollectionRep](docs/ExperimentCollectionRep.md)
 - [ExperimentEnabledPeriodRep](docs/ExperimentEnabledPeriodRep.md)
 - [ExperimentEnvironmentSettingRep](docs/ExperimentEnvironmentSettingRep.md)
 - [ExperimentInfoRep](docs/ExperimentInfoRep.md)
 - [ExperimentMetadataRep](docs/ExperimentMetadataRep.md)
 - [ExperimentPatchInput](docs/ExperimentPatchInput.md)
 - [ExperimentPost](docs/ExperimentPost.md)
 - [ExperimentResults](docs/ExperimentResults.md)
 - [ExperimentStatsRep](docs/ExperimentStatsRep.md)
 - [ExperimentTimeSeriesSlice](docs/ExperimentTimeSeriesSlice.md)
 - [ExperimentTimeSeriesVariationSlice](docs/ExperimentTimeSeriesVariationSlice.md)
 - [ExperimentTimeSeriesVariationSlices](docs/ExperimentTimeSeriesVariationSlices.md)
 - [ExperimentTotalsRep](docs/ExperimentTotalsRep.md)
 - [ExpiringTarget](docs/ExpiringTarget.md)
 - [ExpiringTargetError](docs/ExpiringTargetError.md)
 - [ExpiringTargetGetResponse](docs/ExpiringTargetGetResponse.md)
 - [ExpiringTargetPatchResponse](docs/ExpiringTargetPatchResponse.md)
 - [ExpiringUserTargetGetResponse](docs/ExpiringUserTargetGetResponse.md)
 - [ExpiringUserTargetItem](docs/ExpiringUserTargetItem.md)
 - [ExpiringUserTargetPatchResponse](docs/ExpiringUserTargetPatchResponse.md)
 - [Export](docs/Export.md)
 - [Extinction](docs/Extinction.md)
 - [ExtinctionCollectionRep](docs/ExtinctionCollectionRep.md)
 - [ExtinctionListPost](docs/ExtinctionListPost.md)
 - [FailureReasonRep](docs/FailureReasonRep.md)
 - [FeatureFlag](docs/FeatureFlag.md)
 - [FeatureFlagBody](docs/FeatureFlagBody.md)
 - [FeatureFlagConfig](docs/FeatureFlagConfig.md)
 - [FeatureFlagScheduledChange](docs/FeatureFlagScheduledChange.md)
 - [FeatureFlagScheduledChanges](docs/FeatureFlagScheduledChanges.md)
 - [FeatureFlagStatus](docs/FeatureFlagStatus.md)
 - [FeatureFlagStatusAcrossEnvironments](docs/FeatureFlagStatusAcrossEnvironments.md)
 - [FeatureFlagStatuses](docs/FeatureFlagStatuses.md)
 - [FeatureFlags](docs/FeatureFlags.md)
 - [FileRep](docs/FileRep.md)
 - [FlagConfigApprovalRequestResponse](docs/FlagConfigApprovalRequestResponse.md)
 - [FlagConfigApprovalRequestsResponse](docs/FlagConfigApprovalRequestsResponse.md)
 - [FlagConfigEvaluation](docs/FlagConfigEvaluation.md)
 - [FlagConfigMigrationSettingsRep](docs/FlagConfigMigrationSettingsRep.md)
 - [FlagCopyConfigEnvironment](docs/FlagCopyConfigEnvironment.md)
 - [FlagCopyConfigPost](docs/FlagCopyConfigPost.md)
 - [FlagDefaultsRep](docs/FlagDefaultsRep.md)
 - [FlagEventCollectionRep](docs/FlagEventCollectionRep.md)
 - [FlagEventExperiment](docs/FlagEventExperiment.md)
 - [FlagEventExperimentCollection](docs/FlagEventExperimentCollection.md)
 - [FlagEventExperimentIteration](docs/FlagEventExperimentIteration.md)
 - [FlagEventImpactRep](docs/FlagEventImpactRep.md)
 - [FlagEventMemberRep](docs/FlagEventMemberRep.md)
 - [FlagEventRep](docs/FlagEventRep.md)
 - [FlagFollowersByProjEnvGetRep](docs/FlagFollowersByProjEnvGetRep.md)
 - [FlagFollowersGetRep](docs/FlagFollowersGetRep.md)
 - [FlagImportConfigurationPost](docs/FlagImportConfigurationPost.md)
 - [FlagImportIntegration](docs/FlagImportIntegration.md)
 - [FlagImportIntegrationCollection](docs/FlagImportIntegrationCollection.md)
 - [FlagImportIntegrationCollectionLinks](docs/FlagImportIntegrationCollectionLinks.md)
 - [FlagImportIntegrationLinks](docs/FlagImportIntegrationLinks.md)
 - [FlagImportStatus](docs/FlagImportStatus.md)
 - [FlagInput](docs/FlagInput.md)
 - [FlagLinkCollectionRep](docs/FlagLinkCollectionRep.md)
 - [FlagLinkMember](docs/FlagLinkMember.md)
 - [FlagLinkPost](docs/FlagLinkPost.md)
 - [FlagLinkRep](docs/FlagLinkRep.md)
 - [FlagListingRep](docs/FlagListingRep.md)
 - [FlagMigrationSettingsRep](docs/FlagMigrationSettingsRep.md)
 - [FlagPrerequisitePost](docs/FlagPrerequisitePost.md)
 - [FlagReferenceCollectionRep](docs/FlagReferenceCollectionRep.md)
 - [FlagReferenceRep](docs/FlagReferenceRep.md)
 - [FlagRep](docs/FlagRep.md)
 - [FlagScheduledChangesInput](docs/FlagScheduledChangesInput.md)
 - [FlagSempatch](docs/FlagSempatch.md)
 - [FlagStatusRep](docs/FlagStatusRep.md)
 - [FlagSummary](docs/FlagSummary.md)
 - [FlagTriggerInput](docs/FlagTriggerInput.md)
 - [FlagsInput](docs/FlagsInput.md)
 - [FollowFlagMember](docs/FollowFlagMember.md)
 - [FollowersPerFlag](docs/FollowersPerFlag.md)
 - [ForbiddenErrorRep](docs/ForbiddenErrorRep.md)
 - [FormVariable](docs/FormVariable.md)
 - [FormVariableConfig](docs/FormVariableConfig.md)
 - [HMACSignature](docs/HMACSignature.md)
 - [HeaderItems](docs/HeaderItems.md)
 - [HoldoutDetailRep](docs/HoldoutDetailRep.md)
 - [HoldoutPatchInput](docs/HoldoutPatchInput.md)
 - [HoldoutPostRequest](docs/HoldoutPostRequest.md)
 - [HoldoutRep](docs/HoldoutRep.md)
 - [HoldoutsCollectionRep](docs/HoldoutsCollectionRep.md)
 - [HunkRep](docs/HunkRep.md)
 - [InitiatorRep](docs/InitiatorRep.md)
 - [InsightGroup](docs/InsightGroup.md)
 - [InsightGroupCollection](docs/InsightGroupCollection.md)
 - [InsightGroupCollectionMetadata](docs/InsightGroupCollectionMetadata.md)
 - [InsightGroupCollectionScoreMetadata](docs/InsightGroupCollectionScoreMetadata.md)
 - [InsightGroupScores](docs/InsightGroupScores.md)
 - [InsightGroupsCountByIndicator](docs/InsightGroupsCountByIndicator.md)
 - [InsightPeriod](docs/InsightPeriod.md)
 - [InsightScores](docs/InsightScores.md)
 - [InsightsChart](docs/InsightsChart.md)
 - [InsightsChartBounds](docs/InsightsChartBounds.md)
 - [InsightsChartMetadata](docs/InsightsChartMetadata.md)
 - [InsightsChartMetadataCustomValues](docs/InsightsChartMetadataCustomValues.md)
 - [InsightsChartMetric](docs/InsightsChartMetric.md)
 - [InsightsChartMetrics](docs/InsightsChartMetrics.md)
 - [InsightsChartSeries](docs/InsightsChartSeries.md)
 - [InsightsChartSeriesDataPoint](docs/InsightsChartSeriesDataPoint.md)
 - [InsightsChartSeriesMetadata](docs/InsightsChartSeriesMetadata.md)
 - [InsightsChartSeriesMetadataAxis](docs/InsightsChartSeriesMetadataAxis.md)
 - [InsightsMetricIndicatorRange](docs/InsightsMetricIndicatorRange.md)
 - [InsightsMetricScore](docs/InsightsMetricScore.md)
 - [InsightsMetricTierDefinition](docs/InsightsMetricTierDefinition.md)
 - [InsightsRepository](docs/InsightsRepository.md)
 - [InsightsRepositoryCollection](docs/InsightsRepositoryCollection.md)
 - [InsightsRepositoryProject](docs/InsightsRepositoryProject.md)
 - [InsightsRepositoryProjectCollection](docs/InsightsRepositoryProjectCollection.md)
 - [InsightsRepositoryProjectMappings](docs/InsightsRepositoryProjectMappings.md)
 - [Instruction](docs/Instruction.md)
 - [InstructionUserRequest](docs/InstructionUserRequest.md)
 - [Instructions](docs/Instructions.md)
 - [Integration](docs/Integration.md)
 - [IntegrationConfigurationCollectionRep](docs/IntegrationConfigurationCollectionRep.md)
 - [IntegrationConfigurationPost](docs/IntegrationConfigurationPost.md)
 - [IntegrationConfigurationsRep](docs/IntegrationConfigurationsRep.md)
 - [IntegrationDeliveryConfiguration](docs/IntegrationDeliveryConfiguration.md)
 - [IntegrationDeliveryConfigurationCollection](docs/IntegrationDeliveryConfigurationCollection.md)
 - [IntegrationDeliveryConfigurationCollectionLinks](docs/IntegrationDeliveryConfigurationCollectionLinks.md)
 - [IntegrationDeliveryConfigurationLinks](docs/IntegrationDeliveryConfigurationLinks.md)
 - [IntegrationDeliveryConfigurationPost](docs/IntegrationDeliveryConfigurationPost.md)
 - [IntegrationDeliveryConfigurationResponse](docs/IntegrationDeliveryConfigurationResponse.md)
 - [IntegrationMetadata](docs/IntegrationMetadata.md)
 - [IntegrationStatus](docs/IntegrationStatus.md)
 - [IntegrationStatusRep](docs/IntegrationStatusRep.md)
 - [IntegrationSubscriptionStatusRep](docs/IntegrationSubscriptionStatusRep.md)
 - [Integrations](docs/Integrations.md)
 - [InvalidRequestErrorRep](docs/InvalidRequestErrorRep.md)
 - [IpList](docs/IpList.md)
 - [IterationInput](docs/IterationInput.md)
 - [IterationRep](docs/IterationRep.md)
 - [JSONPatch](docs/JSONPatch.md)
 - [LastSeenMetadata](docs/LastSeenMetadata.md)
 - [LayerCollectionRep](docs/LayerCollectionRep.md)
 - [LayerConfigurationRep](docs/LayerConfigurationRep.md)
 - [LayerPatchInput](docs/LayerPatchInput.md)
 - [LayerPost](docs/LayerPost.md)
 - [LayerRep](docs/LayerRep.md)
 - [LayerReservationRep](docs/LayerReservationRep.md)
 - [LayerSnapshotRep](docs/LayerSnapshotRep.md)
 - [LeadTimeStagesRep](docs/LeadTimeStagesRep.md)
 - [LegacyExperimentRep](docs/LegacyExperimentRep.md)
 - [Link](docs/Link.md)
 - [MaintainerRep](docs/MaintainerRep.md)
 - [MaintainerTeam](docs/MaintainerTeam.md)
 - [Member](docs/Member.md)
 - [MemberDataRep](docs/MemberDataRep.md)
 - [MemberImportItem](docs/MemberImportItem.md)
 - [MemberPermissionGrantSummaryRep](docs/MemberPermissionGrantSummaryRep.md)
 - [MemberSummary](docs/MemberSummary.md)
 - [MemberTeamSummaryRep](docs/MemberTeamSummaryRep.md)
 - [MemberTeamsPostInput](docs/MemberTeamsPostInput.md)
 - [Members](docs/Members.md)
 - [MembersPatchInput](docs/MembersPatchInput.md)
 - [MethodNotAllowedErrorRep](docs/MethodNotAllowedErrorRep.md)
 - [MetricCollectionRep](docs/MetricCollectionRep.md)
 - [MetricEventDefaultRep](docs/MetricEventDefaultRep.md)
 - [MetricGroupCollectionRep](docs/MetricGroupCollectionRep.md)
 - [MetricGroupPost](docs/MetricGroupPost.md)
 - [MetricGroupRep](docs/MetricGroupRep.md)
 - [MetricGroupResultsRep](docs/MetricGroupResultsRep.md)
 - [MetricInGroupRep](docs/MetricInGroupRep.md)
 - [MetricInGroupResultsRep](docs/MetricInGroupResultsRep.md)
 - [MetricInMetricGroupInput](docs/MetricInMetricGroupInput.md)
 - [MetricInput](docs/MetricInput.md)
 - [MetricListingRep](docs/MetricListingRep.md)
 - [MetricPost](docs/MetricPost.md)
 - [MetricRep](docs/MetricRep.md)
 - [MetricSeen](docs/MetricSeen.md)
 - [MetricV2Rep](docs/MetricV2Rep.md)
 - [MetricsInput](docs/MetricsInput.md)
 - [MigrationSafetyIssueRep](docs/MigrationSafetyIssueRep.md)
 - [MigrationSettingsPost](docs/MigrationSettingsPost.md)
 - [ModelImport](docs/ModelImport.md)
 - [Modification](docs/Modification.md)
 - [MultiEnvironmentDependentFlag](docs/MultiEnvironmentDependentFlag.md)
 - [MultiEnvironmentDependentFlags](docs/MultiEnvironmentDependentFlags.md)
 - [NamingConvention](docs/NamingConvention.md)
 - [NewMemberForm](docs/NewMemberForm.md)
 - [NewMemberFormListPost](docs/NewMemberFormListPost.md)
 - [NotFoundErrorRep](docs/NotFoundErrorRep.md)
 - [OauthClientPost](docs/OauthClientPost.md)
 - [Object](docs/Object.md)
 - [OptionsArray](docs/OptionsArray.md)
 - [ParameterDefault](docs/ParameterDefault.md)
 - [ParameterRep](docs/ParameterRep.md)
 - [ParentResourceRep](docs/ParentResourceRep.md)
 - [PatchFailedErrorRep](docs/PatchFailedErrorRep.md)
 - [PatchFlagsRequest](docs/PatchFlagsRequest.md)
 - [PatchOperation](docs/PatchOperation.md)
 - [PatchSegmentExpiringTargetInputRep](docs/PatchSegmentExpiringTargetInputRep.md)
 - [PatchSegmentExpiringTargetInstruction](docs/PatchSegmentExpiringTargetInstruction.md)
 - [PatchSegmentInstruction](docs/PatchSegmentInstruction.md)
 - [PatchSegmentRequest](docs/PatchSegmentRequest.md)
 - [PatchUsersRequest](docs/PatchUsersRequest.md)
 - [PatchWithComment](docs/PatchWithComment.md)
 - [PermissionGrantInput](docs/PermissionGrantInput.md)
 - [Phase](docs/Phase.md)
 - [PhaseInfo](docs/PhaseInfo.md)
 - [PostApprovalRequestApplyRequest](docs/PostApprovalRequestApplyRequest.md)
 - [PostApprovalRequestReviewRequest](docs/PostApprovalRequestReviewRequest.md)
 - [PostDeploymentEventInput](docs/PostDeploymentEventInput.md)
 - [PostFlagScheduledChangesInput](docs/PostFlagScheduledChangesInput.md)
 - [PostInsightGroupParams](docs/PostInsightGroupParams.md)
 - [Prerequisite](docs/Prerequisite.md)
 - [Project](docs/Project.md)
 - [ProjectPost](docs/ProjectPost.md)
 - [ProjectRep](docs/ProjectRep.md)
 - [ProjectSummary](docs/ProjectSummary.md)
 - [ProjectSummaryCollection](docs/ProjectSummaryCollection.md)
 - [Projects](docs/Projects.md)
 - [PullRequestCollectionRep](docs/PullRequestCollectionRep.md)
 - [PullRequestLeadTimeRep](docs/PullRequestLeadTimeRep.md)
 - [PullRequestRep](docs/PullRequestRep.md)
 - [PutBranch](docs/PutBranch.md)
 - [RandomizationSettingsPut](docs/RandomizationSettingsPut.md)
 - [RandomizationSettingsRep](docs/RandomizationSettingsRep.md)
 - [RandomizationUnitInput](docs/RandomizationUnitInput.md)
 - [RandomizationUnitRep](docs/RandomizationUnitRep.md)
 - [RateLimitedErrorRep](docs/RateLimitedErrorRep.md)
 - [RecentTriggerBody](docs/RecentTriggerBody.md)
 - [ReferenceRep](docs/ReferenceRep.md)
 - [RelatedExperimentRep](docs/RelatedExperimentRep.md)
 - [RelativeDifferenceRep](docs/RelativeDifferenceRep.md)
 - [RelayAutoConfigCollectionRep](docs/RelayAutoConfigCollectionRep.md)
 - [RelayAutoConfigPost](docs/RelayAutoConfigPost.md)
 - [RelayAutoConfigRep](docs/RelayAutoConfigRep.md)
 - [Release](docs/Release.md)
 - [ReleaseAudience](docs/ReleaseAudience.md)
 - [ReleaseGuardianConfiguration](docs/ReleaseGuardianConfiguration.md)
 - [ReleaseGuardianConfigurationInput](docs/ReleaseGuardianConfigurationInput.md)
 - [ReleasePhase](docs/ReleasePhase.md)
 - [ReleasePipeline](docs/ReleasePipeline.md)
 - [ReleasePipelineCollection](docs/ReleasePipelineCollection.md)
 - [ReleaseProgression](docs/ReleaseProgression.md)
 - [ReleaseProgressionCollection](docs/ReleaseProgressionCollection.md)
 - [ReleaserAudienceConfigInput](docs/ReleaserAudienceConfigInput.md)
 - [RepositoryCollectionRep](docs/RepositoryCollectionRep.md)
 - [RepositoryPost](docs/RepositoryPost.md)
 - [RepositoryRep](docs/RepositoryRep.md)
 - [ResourceAccess](docs/ResourceAccess.md)
 - [ResourceIDResponse](docs/ResourceIDResponse.md)
 - [ResourceId](docs/ResourceId.md)
 - [ReviewOutput](docs/ReviewOutput.md)
 - [ReviewResponse](docs/ReviewResponse.md)
 - [RoleAttributeMap](docs/RoleAttributeMap.md)
 - [RoleAttributeValues](docs/RoleAttributeValues.md)
 - [Rollout](docs/Rollout.md)
 - [RootResponse](docs/RootResponse.md)
 - [Rule](docs/Rule.md)
 - [RuleClause](docs/RuleClause.md)
 - [SdkListRep](docs/SdkListRep.md)
 - [SdkVersionListRep](docs/SdkVersionListRep.md)
 - [SdkVersionRep](docs/SdkVersionRep.md)
 - [SegmentBody](docs/SegmentBody.md)
 - [SegmentMetadata](docs/SegmentMetadata.md)
 - [SegmentTarget](docs/SegmentTarget.md)
 - [SegmentUserList](docs/SegmentUserList.md)
 - [SegmentUserState](docs/SegmentUserState.md)
 - [Series](docs/Series.md)
 - [SeriesIntervalsRep](docs/SeriesIntervalsRep.md)
 - [SeriesListRep](docs/SeriesListRep.md)
 - [SeriesMetadataRep](docs/SeriesMetadataRep.md)
 - [SeriesTimeSliceRep](docs/SeriesTimeSliceRep.md)
 - [SimpleHoldoutRep](docs/SimpleHoldoutRep.md)
 - [SlicedResultsRep](docs/SlicedResultsRep.md)
 - [SourceEnv](docs/SourceEnv.md)
 - [SourceFlag](docs/SourceFlag.md)
 - [StageInput](docs/StageInput.md)
 - [StageOutput](docs/StageOutput.md)
 - [Statement](docs/Statement.md)
 - [StatementPost](docs/StatementPost.md)
 - [StatementPostList](docs/StatementPostList.md)
 - [StatisticCollectionRep](docs/StatisticCollectionRep.md)
 - [StatisticRep](docs/StatisticRep.md)
 - [StatisticsRoot](docs/StatisticsRoot.md)
 - [StatusConflictErrorRep](docs/StatusConflictErrorRep.md)
 - [StatusResponse](docs/StatusResponse.md)
 - [StatusServiceUnavailable](docs/StatusServiceUnavailable.md)
 - [StoreIntegrationError](docs/StoreIntegrationError.md)
 - [SubjectDataRep](docs/SubjectDataRep.md)
 - [SubscriptionPost](docs/SubscriptionPost.md)
 - [TagsCollection](docs/TagsCollection.md)
 - [TagsLink](docs/TagsLink.md)
 - [Target](docs/Target.md)
 - [TargetResourceRep](docs/TargetResourceRep.md)
 - [Team](docs/Team.md)
 - [TeamCustomRole](docs/TeamCustomRole.md)
 - [TeamCustomRoles](docs/TeamCustomRoles.md)
 - [TeamImportsRep](docs/TeamImportsRep.md)
 - [TeamMaintainers](docs/TeamMaintainers.md)
 - [TeamMembers](docs/TeamMembers.md)
 - [TeamPatchInput](docs/TeamPatchInput.md)
 - [TeamPostInput](docs/TeamPostInput.md)
 - [TeamProjects](docs/TeamProjects.md)
 - [Teams](docs/Teams.md)
 - [TeamsPatchInput](docs/TeamsPatchInput.md)
 - [TimestampRep](docs/TimestampRep.md)
 - [Token](docs/Token.md)
 - [TokenSummary](docs/TokenSummary.md)
 - [Tokens](docs/Tokens.md)
 - [TreatmentInput](docs/TreatmentInput.md)
 - [TreatmentParameterInput](docs/TreatmentParameterInput.md)
 - [TreatmentRep](docs/TreatmentRep.md)
 - [TreatmentResultRep](docs/TreatmentResultRep.md)
 - [TreatmentsInput](docs/TreatmentsInput.md)
 - [TriggerPost](docs/TriggerPost.md)
 - [TriggerWorkflowCollectionRep](docs/TriggerWorkflowCollectionRep.md)
 - [TriggerWorkflowRep](docs/TriggerWorkflowRep.md)
 - [UnauthorizedErrorRep](docs/UnauthorizedErrorRep.md)
 - [UpdatePhaseStatusInput](docs/UpdatePhaseStatusInput.md)
 - [UpdateReleasePipelineInput](docs/UpdateReleasePipelineInput.md)
 - [UpsertContextKindPayload](docs/UpsertContextKindPayload.md)
 - [UpsertFlagDefaultsPayload](docs/UpsertFlagDefaultsPayload.md)
 - [UpsertPayloadRep](docs/UpsertPayloadRep.md)
 - [UpsertResponseRep](docs/UpsertResponseRep.md)
 - [UrlMatcher](docs/UrlMatcher.md)
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
 - [UsersRep](docs/UsersRep.md)
 - [ValidationFailedErrorRep](docs/ValidationFailedErrorRep.md)
 - [ValuePut](docs/ValuePut.md)
 - [Variation](docs/Variation.md)
 - [VariationEvalSummary](docs/VariationEvalSummary.md)
 - [VariationOrRolloutRep](docs/VariationOrRolloutRep.md)
 - [VariationSummary](docs/VariationSummary.md)
 - [VersionsRep](docs/VersionsRep.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookPost](docs/WebhookPost.md)
 - [Webhooks](docs/Webhooks.md)
 - [WeightedVariation](docs/WeightedVariation.md)
 - [WorkflowTemplateMetadata](docs/WorkflowTemplateMetadata.md)
 - [WorkflowTemplateOutput](docs/WorkflowTemplateOutput.md)
 - [WorkflowTemplateParameter](docs/WorkflowTemplateParameter.md)
 - [WorkflowTemplatesListingOutputRep](docs/WorkflowTemplatesListingOutputRep.md)


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
from launchdarkly_api.model.variation import Variation
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
            Variation(value=[1, 2]),
            Variation(value=[3, 4]),
            Variation(value=[5]),
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
