# coding: utf-8

"""
    LaunchDarkly REST API

    This documentation describes LaunchDarkly's REST API. To access the complete OpenAPI spec directly, use [Get OpenAPI spec](https://launchdarkly.com/docs/api/other/get-openapi-spec).  To learn how to use LaunchDarkly using the user interface (UI) instead, read our [product documentation](https://launchdarkly.com/docs/home).  ## Authentication  LaunchDarkly's REST API uses the HTTPS protocol with a minimum TLS version of 1.2.  All REST API resources are authenticated with either [personal or service access tokens](https://launchdarkly.com/docs/home/account/api), or session cookies. Other authentication mechanisms are not supported. You can manage personal access tokens on your [**Authorization**](https://app.launchdarkly.com/settings/authorization) page in the LaunchDarkly UI.  LaunchDarkly also has SDK keys, mobile keys, and client-side IDs that are used by our server-side SDKs, mobile SDKs, and JavaScript-based SDKs, respectively. **These keys cannot be used to access our REST API**. These keys are environment-specific, and can only perform read-only operations such as fetching feature flag settings.  | Auth mechanism                                                                                  | Allowed resources                                                                                     | Use cases                                          | | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------- | | [Personal or service access tokens](https://launchdarkly.com/docs/home/account/api) | Can be customized on a per-token basis                                                                | Building scripts, custom integrations, data export. | | SDK keys                                                                                        | Can only access read-only resources specific to server-side SDKs. Restricted to a single environment. | Server-side SDKs                     | | Mobile keys                                                                                     | Can only access read-only resources specific to mobile SDKs, and only for flags marked available to mobile keys. Restricted to a single environment.           | Mobile SDKs                                        | | Client-side ID                                                                                  | Can only access read-only resources specific to JavaScript-based client-side SDKs, and only for flags marked available to client-side. Restricted to a single environment.           | Client-side JavaScript                             |  > #### Keep your access tokens and SDK keys private > > Access tokens should _never_ be exposed in untrusted contexts. Never put an access token in client-side JavaScript, or embed it in a mobile application. LaunchDarkly has special mobile keys that you can embed in mobile apps. If you accidentally expose an access token or SDK key, you can reset it from your [**Authorization**](https://app.launchdarkly.com/settings/authorization) page. > > The client-side ID is safe to embed in untrusted contexts. It's designed for use in client-side JavaScript.  ### Authentication using request header  The preferred way to authenticate with the API is by adding an `Authorization` header containing your access token to your requests. The value of the `Authorization` header must be your access token.  Manage personal access tokens from the [**Authorization**](https://app.launchdarkly.com/settings/authorization) page.  ### Authentication using session cookie  For testing purposes, you can make API calls directly from your web browser. If you are logged in to the LaunchDarkly application, the API will use your existing session to authenticate calls.  Depending on the permissions granted as part of your [role](https://launchdarkly.com/docs/home/account/roles), you may not have permission to perform some API calls. You will receive a `401` response code in that case.  > ### Modifying the Origin header causes an error > > LaunchDarkly validates that the Origin header for any API request authenticated by a session cookie matches the expected Origin header. The expected Origin header is `https://app.launchdarkly.com`. > > If the Origin header does not match what's expected, LaunchDarkly returns an error. This error can prevent the LaunchDarkly app from working correctly. > > Any browser extension that intentionally changes the Origin header can cause this problem. For example, the `Allow-Control-Allow-Origin: *` Chrome extension changes the Origin header to `http://evil.com` and causes the app to fail. > > To prevent this error, do not modify your Origin header. > > LaunchDarkly does not require origin matching when authenticating with an access token, so this issue does not affect normal API usage.  ## Representations  All resources expect and return JSON response bodies. Error responses also send a JSON body. To learn more about the error format of the API, read [Errors](https://launchdarkly.com/docs/api#errors).  In practice this means that you always get a response with a `Content-Type` header set to `application/json`.  In addition, request bodies for `PATCH`, `POST`, and `PUT` requests must be encoded as JSON with a `Content-Type` header set to `application/json`.  ### Summary and detailed representations  When you fetch a list of resources, the response includes only the most important attributes of each resource. This is a _summary representation_ of the resource. When you fetch an individual resource, such as a single feature flag, you receive a _detailed representation_ of the resource.  The best way to find a detailed representation is to follow links. Every summary representation includes a link to its detailed representation.  ### Expanding responses  Sometimes the detailed representation of a resource does not include all of the attributes of the resource by default. If this is the case, the request method will clearly document this and describe which attributes you can include in an expanded response.  To include the additional attributes, append the `expand` request parameter to your request and add a comma-separated list of the attributes to include. For example, when you append `?expand=members,maintainers` to the [Get team](https://launchdarkly.com/docs/api/teams/get-team) endpoint, the expanded response includes both of these attributes.  ### Links and addressability  The best way to navigate the API is by following links. These are attributes in representations that link to other resources. The API always uses the same format for links:  - Links to other resources within the API are encapsulated in a `_links` object - If the resource has a corresponding link to HTML content on the site, it is stored in a special `_site` link  Each link has two attributes:  - An `href`, which contains the URL - A `type`, which describes the content type  For example, a feature resource might return the following:  ```json {   \"_links\": {     \"parent\": {       \"href\": \"/api/features\",       \"type\": \"application/json\"     },     \"self\": {       \"href\": \"/api/features/sort.order\",       \"type\": \"application/json\"     }   },   \"_site\": {     \"href\": \"/features/sort.order\",     \"type\": \"text/html\"   } } ```  From this, you can navigate to the parent collection of features by following the `parent` link, or navigate to the site page for the feature by following the `_site` link.  Collections are always represented as a JSON object with an `items` attribute containing an array of representations. Like all other representations, collections have `_links` defined at the top level.  Paginated collections include `first`, `last`, `next`, and `prev` links containing a URL with the respective set of elements in the collection.  ## Updates  Resources that accept partial updates use the `PATCH` verb. Most resources support the [JSON patch](https://launchdarkly.com/docs/api#updates-using-json-patch) format. Some resources also support the [JSON merge patch](https://launchdarkly.com/docs/api#updates-using-json-merge-patch) format, and some resources support the [semantic patch](https://launchdarkly.com/docs/api#updates-using-semantic-patch) format, which is a way to specify the modifications to perform as a set of executable instructions. Each resource supports optional [comments](https://launchdarkly.com/docs/api#updates-with-comments) that you can submit with updates. Comments appear in outgoing webhooks, the audit log, and other integrations.  When a resource supports both JSON patch and semantic patch, we document both in the request method. However, the specific request body fields and descriptions included in our documentation only match one type of patch or the other.  ### Updates using JSON patch  [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) is a way to specify the modifications to perform on a resource. JSON patch uses paths and a limited set of operations to describe how to transform the current state of the resource into a new state. JSON patch documents are always arrays, where each element contains an operation, a path to the field to update, and the new value.  For example, in this feature flag representation:  ```json {     \"name\": \"New recommendations engine\",     \"key\": \"engine.enable\",     \"description\": \"This is the description\",     ... } ``` You can change the feature flag's description with the following patch document:  ```json [{ \"op\": \"replace\", \"path\": \"/description\", \"value\": \"This is the new description\" }] ```  You can specify multiple modifications to perform in a single request. You can also test that certain preconditions are met before applying the patch:  ```json [   { \"op\": \"test\", \"path\": \"/version\", \"value\": 10 },   { \"op\": \"replace\", \"path\": \"/description\", \"value\": \"The new description\" } ] ```  The above patch request tests whether the feature flag's `version` is `10`, and if so, changes the feature flag's description.  Attributes that are not editable, such as a resource's `_links`, have names that start with an underscore.  ### Updates using JSON merge patch  [JSON merge patch](https://datatracker.ietf.org/doc/html/rfc7386) is another format for specifying the modifications to perform on a resource. JSON merge patch is less expressive than JSON patch. However, in many cases it is simpler to construct a merge patch document. For example, you can change a feature flag's description with the following merge patch document:  ```json {   \"description\": \"New flag description\" } ```  ### Updates using semantic patch  Some resources support the semantic patch format. A semantic patch is a way to specify the modifications to perform on a resource as a set of executable instructions.  Semantic patch allows you to be explicit about intent using precise, custom instructions. In many cases, you can define semantic patch instructions independently of the current state of the resource. This can be useful when defining a change that may be applied at a future date.  To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header.  Here's how:  ``` Content-Type: application/json; domain-model=launchdarkly.semanticpatch ```  If you call a semantic patch resource without this header, you will receive a `400` response because your semantic patch will be interpreted as a JSON patch.  The body of a semantic patch request takes the following properties:  * `comment` (string): (Optional) A description of the update. * `environmentKey` (string): (Required for some resources only) The environment key. * `instructions` (array): (Required) A list of actions the update should perform. Each action in the list must be an object with a `kind` property that indicates the instruction. If the instruction requires parameters, you must include those parameters as additional fields in the object. The documentation for each resource that supports semantic patch includes the available instructions and any additional parameters.  For example:  ```json {   \"comment\": \"optional comment\",   \"instructions\": [ {\"kind\": \"turnFlagOn\"} ] } ```  Semantic patches are not applied partially; either all of the instructions are applied or none of them are. If **any** instruction is invalid, the endpoint returns an error and will not change the resource. If all instructions are valid, the request succeeds and the resources are updated if necessary, or left unchanged if they are already in the state you request.  ### Updates with comments  You can submit optional comments with `PATCH` changes.  To submit a comment along with a JSON patch document, use the following format:  ```json {   \"comment\": \"This is a comment string\",   \"patch\": [{ \"op\": \"replace\", \"path\": \"/description\", \"value\": \"The new description\" }] } ```  To submit a comment along with a JSON merge patch document, use the following format:  ```json {   \"comment\": \"This is a comment string\",   \"merge\": { \"description\": \"New flag description\" } } ```  To submit a comment along with a semantic patch, use the following format:  ```json {   \"comment\": \"This is a comment string\",   \"instructions\": [ {\"kind\": \"turnFlagOn\"} ] } ```  ## Errors  The API always returns errors in a common format. Here's an example:  ```json {   \"code\": \"invalid_request\",   \"message\": \"A feature with that key already exists\",   \"id\": \"30ce6058-87da-11e4-b116-123b93f75cba\" } ```  The `code` indicates the general class of error. The `message` is a human-readable explanation of what went wrong. The `id` is a unique identifier. Use it when you're working with LaunchDarkly Support to debug a problem with a specific API call.  ### HTTP status error response codes  | Code | Definition        | Description                                                                                       | Possible Solution                                                | | ---- | ----------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | | 400  | Invalid request       | The request cannot be understood.                                    | Ensure JSON syntax in request body is correct.                   | | 401  | Invalid access token      | Requestor is unauthorized or does not have permission for this API call.                                                | Ensure your API access token is valid and has the appropriate permissions.                                     | | 403  | Forbidden         | Requestor does not have access to this resource.                                                | Ensure that the account member or access token has proper permissions set. | | 404  | Invalid resource identifier | The requested resource is not valid. | Ensure that the resource is correctly identified by ID or key. | | 405  | Method not allowed | The request method is not allowed on this resource. | Ensure that the HTTP verb is correct. | | 409  | Conflict          | The API request can not be completed because it conflicts with a concurrent API request. | Retry your request.                                              | | 422  | Unprocessable entity | The API request can not be completed because the update description can not be understood. | Ensure that the request body is correct for the type of patch you are using, either JSON patch or semantic patch. | 429  | Too many requests | Read [Rate limiting](https://launchdarkly.com/docs/api#rate-limiting).                                               | Wait and try again later.                                        |  ## CORS  The LaunchDarkly API supports Cross Origin Resource Sharing (CORS) for AJAX requests from any origin. If an `Origin` header is given in a request, it will be echoed as an explicitly allowed origin. Otherwise the request returns a wildcard, `Access-Control-Allow-Origin: *`. For more information on CORS, read the [CORS W3C Recommendation](http://www.w3.org/TR/cors). Example CORS headers might look like:  ```http Access-Control-Allow-Headers: Accept, Content-Type, Content-Length, Accept-Encoding, Authorization Access-Control-Allow-Methods: OPTIONS, GET, DELETE, PATCH Access-Control-Allow-Origin: * Access-Control-Max-Age: 300 ```  You can make authenticated CORS calls just as you would make same-origin calls, using either [token or session-based authentication](https://launchdarkly.com/docs/api#authentication). If you are using session authentication, you should set the `withCredentials` property for your `xhr` request to `true`. You should never expose your access tokens to untrusted entities.  ## Rate limiting  We use several rate limiting strategies to ensure the availability of our APIs. Rate-limited calls to our APIs return a `429` status code. Calls to our APIs include headers indicating the current rate limit status. The specific headers returned depend on the API route being called. The limits differ based on the route, authentication mechanism, and other factors. Routes that are not rate limited may not contain any of the headers described below.  > ### Rate limiting and SDKs > > LaunchDarkly SDKs are never rate limited and do not use the API endpoints defined here. LaunchDarkly uses a different set of approaches, including streaming/server-sent events and a global CDN, to ensure availability to the routes used by LaunchDarkly SDKs.  ### Global rate limits  Authenticated requests are subject to a global limit. This is the maximum number of calls that your account can make to the API per ten seconds. All service and personal access tokens on the account share this limit, so exceeding the limit with one access token will impact other tokens. Calls that are subject to global rate limits may return the headers below:  | Header name                    | Description                                                                      | | ------------------------------ | -------------------------------------------------------------------------------- | | `X-Ratelimit-Global-Remaining` | The maximum number of requests the account is permitted to make per ten seconds. | | `X-Ratelimit-Reset`            | The time at which the current rate limit window resets in epoch milliseconds.    |  We do not publicly document the specific number of calls that can be made globally. This limit may change, and we encourage clients to program against the specification, relying on the two headers defined above, rather than hardcoding to the current limit.  ### Route-level rate limits  Some authenticated routes have custom rate limits. These also reset every ten seconds. Any service or personal access tokens hitting the same route share this limit, so exceeding the limit with one access token may impact other tokens. Calls that are subject to route-level rate limits return the headers below:  | Header name                   | Description                                                                                           | | ----------------------------- | ----------------------------------------------------------------------------------------------------- | | `X-Ratelimit-Route-Remaining` | The maximum number of requests to the current route the account is permitted to make per ten seconds. | | `X-Ratelimit-Reset`           | The time at which the current rate limit window resets in epoch milliseconds.                         |  A _route_ represents a specific URL pattern and verb. For example, the [Delete environment](https://launchdarkly.com/docs/api/environments/delete-environment) endpoint is considered a single route, and each call to delete an environment counts against your route-level rate limit for that route.  We do not publicly document the specific number of calls that an account can make to each endpoint per ten seconds. These limits may change, and we encourage clients to program against the specification, relying on the two headers defined above, rather than hardcoding to the current limits.  ### IP-based rate limiting  We also employ IP-based rate limiting on some API routes. If you hit an IP-based rate limit, your API response will include a `Retry-After` header indicating how long to wait before re-trying the call. Clients must wait at least `Retry-After` seconds before making additional calls to our API, and should employ jitter and backoff strategies to avoid triggering rate limits again.  ## OpenAPI (Swagger) and client libraries  We have a [complete OpenAPI (Swagger) specification](https://app.launchdarkly.com/api/v2/openapi.json) for our API.  We auto-generate multiple client libraries based on our OpenAPI specification. To learn more, visit the [collection of client libraries on GitHub](https://github.com/search?q=topic%3Alaunchdarkly-api+org%3Alaunchdarkly&type=Repositories). You can also use this specification to generate client libraries to interact with our REST API in your language of choice.  Our OpenAPI specification is supported by several API-based tools such as Postman and Insomnia. In many cases, you can directly import our specification to explore our APIs.  ## Method overriding  Some firewalls and HTTP clients restrict the use of verbs other than `GET` and `POST`. In those environments, our API endpoints that use `DELETE`, `PATCH`, and `PUT` verbs are inaccessible.  To avoid this issue, our API supports the `X-HTTP-Method-Override` header, allowing clients to \"tunnel\" `DELETE`, `PATCH`, and `PUT` requests using a `POST` request.  For example, to call a `PATCH` endpoint using a `POST` request, you can include `X-HTTP-Method-Override:PATCH` as a header.  ## Beta resources  We sometimes release new API resources in **beta** status before we release them with general availability.  Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.  We try to promote resources into general availability as quickly as possible. This happens after sufficient testing and when we're satisfied that we no longer need to make backwards-incompatible changes.  We mark beta resources with a \"Beta\" callout in our documentation, pictured below:  > ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](https://launchdarkly.com/docs/api#beta-resources). > > Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.  ### Using beta resources  To use a beta resource, you must include a header in the request. If you call a beta resource without this header, you receive a `403` response.  Use this header:  ``` LD-API-Version: beta ```  ## Federal and EU environments  In addition to the commercial versions, LaunchDarkly offers instances for federal agencies and those based in the European Union (EU).  ### Federal environments  The version of LaunchDarkly that is available on domains controlled by the United States government is different from the version of LaunchDarkly available to the general public. If you are an employee or contractor for a United States federal agency and use LaunchDarkly in your work, you likely use the federal instance of LaunchDarkly.  If you are working in the federal instance of LaunchDarkly, the base URI for each request is `https://app.launchdarkly.us`.  To learn more, read [LaunchDarkly in federal environments](https://launchdarkly.com/docs/home/infrastructure/federal).  ### EU environments  The version of LaunchDarkly that is available in the EU is different from the version of LaunchDarkly available to other regions. If you are based in the EU, you likely use the EU instance of LaunchDarkly. The LaunchDarkly EU instance complies with EU data residency principles, including the protection and confidentiality of EU customer information.  If you are working in the EU instance of LaunchDarkly, the base URI for each request is `https://app.eu.launchdarkly.com`.  To learn more, read [LaunchDarkly in the European Union (EU)](https://launchdarkly.com/docs/home/infrastructure/eu).  ## Versioning  We try hard to keep our REST API backwards compatible, but we occasionally have to make backwards-incompatible changes in the process of shipping new features. These breaking changes can cause unexpected behavior if you don't prepare for them accordingly.  Updates to our REST API include support for the latest features in LaunchDarkly. We also release a new version of our REST API every time we make a breaking change. We provide simultaneous support for multiple API versions so you can migrate from your current API version to a new version at your own pace.  ### Setting the API version per request  You can set the API version on a specific request by sending an `LD-API-Version` header, as shown in the example below:  ``` LD-API-Version: 20240415 ```  The header value is the version number of the API version you would like to request. The number for each version corresponds to the date the version was released in `yyyymmdd` format. In the example above the version `20240415` corresponds to April 15, 2024.  ### Setting the API version per access token  When you create an access token, you must specify a specific version of the API to use. This ensures that integrations using this token cannot be broken by version changes.  Tokens created before versioning was released have their version set to `20160426`, which is the version of the API that existed before the current versioning scheme, so that they continue working the same way they did before versioning.  If you would like to upgrade your integration to use a new API version, you can explicitly set the header described above.  > ### Best practice: Set the header for every client or integration > > We recommend that you set the API version header explicitly in any client or integration you build. > > Only rely on the access token API version during manual testing.  ### API version changelog  <table>   <tr>     <th>Version</th>     <th>Changes</th>     <th>End of life (EOL)</th>   </tr>   <tr>     <td>`20240415`</td>     <td>       <ul><li>Changed several endpoints from unpaginated to paginated. Use the `limit` and `offset` query parameters to page through the results.</li> <li>Changed the [list access tokens](https://launchdarkly.com/docs/api/access-tokens/get-tokens) endpoint: <ul><li>Response is now paginated with a default limit of `25`</li></ul></li> <li>Changed the [list account members](https://launchdarkly.com/docs/api/account-members/get-members) endpoint: <ul><li>The `accessCheck` filter is no longer available</li></ul></li> <li>Changed the [list custom roles](https://launchdarkly.com/docs/api/custom-roles/get-custom-roles) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li></ul></li> <li>Changed the [list feature flags](https://launchdarkly.com/docs/api/feature-flags/get-feature-flags) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li><li>The `environments` field is now only returned if the request is filtered by environment, using the `filterEnv` query parameter</li><li>The `followerId`, `hasDataExport`, `status`, `contextKindTargeted`, and `segmentTargeted` filters are no longer available</li><li>The `compare` query parameter is no longer available</li></ul></li> <li>Changed the [list segments](https://launchdarkly.com/docs/api/segments/get-segments) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li></ul></li> <li>Changed the [list teams](https://launchdarkly.com/docs/api/teams/get-teams) endpoint: <ul><li>The `expand` parameter no longer supports including `projects` or `roles`</li><li>In paginated results, the maximum page size is now 100</li></ul></li> <li>Changed the [get workflows](https://launchdarkly.com/docs/api/workflows/get-workflows) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li><li>The `_conflicts` field in the response is no longer available</li></ul></li> </ul>     </td>     <td>Current</td>   </tr>   <tr>     <td>`20220603`</td>     <td>       <ul><li>Changed the [list projects](https://launchdarkly.com/docs/api/projects/get-projects) return value:<ul><li>Response is now paginated with a default limit of `20`.</li><li>Added support for filter and sort.</li><li>The project `environments` field is now expandable. This field is omitted by default.</li></ul></li><li>Changed the [get project](https://launchdarkly.com/docs/api/projects/get-project) return value:<ul><li>The `environments` field is now expandable. This field is omitted by default.</li></ul></li></ul>     </td>     <td>2025-04-15</td>   </tr>   <tr>     <td>`20210729`</td>     <td>       <ul><li>Changed the [create approval request](https://launchdarkly.com/docs/api/approvals/post-approval-request) return value. It now returns HTTP Status Code `201` instead of `200`.</li><li> Changed the [get user](https://launchdarkly.com/docs/api/users/get-user) return value. It now returns a user record, not a user. </li><li>Added additional optional fields to environment, segments, flags, members, and segments, including the ability to create big segments. </li><li> Added default values for flag variations when new environments are created. </li><li>Added filtering and pagination for getting flags and members, including `limit`, `number`, `filter`, and `sort` query parameters. </li><li>Added endpoints for expiring user targets for flags and segments, scheduled changes, access tokens, Relay Proxy configuration, integrations and subscriptions, and approvals. </li></ul>     </td>     <td>2023-06-03</td>   </tr>   <tr>     <td>`20191212`</td>     <td>       <ul><li>[List feature flags](https://launchdarkly.com/docs/api/feature-flags/get-feature-flags) now defaults to sending summaries of feature flag configurations, equivalent to setting the query parameter `summary=true`. Summaries omit flag targeting rules and individual user targets from the payload. </li><li> Added endpoints for flags, flag status, projects, environments, audit logs, members, users, custom roles, segments, usage, streams, events, and data export. </li></ul>     </td>     <td>2022-07-29</td>   </tr>   <tr>     <td>`20160426`</td>     <td>       <ul><li>Initial versioning of API. Tokens created before versioning have their version set to this.</li></ul>     </td>     <td>2020-12-12</td>   </tr> </table>  To learn more about how EOL is determined, read LaunchDarkly's [End of Life (EOL) Policy](https://launchdarkly.com/policies/end-of-life-policy/). 

    The version of the OpenAPI document: 2.0
    Contact: support@launchdarkly.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, Dict, Optional
from typing_extensions import Annotated
from launchdarkly_api.models.context_attribute_names_collection import ContextAttributeNamesCollection
from launchdarkly_api.models.context_attribute_values_collection import ContextAttributeValuesCollection
from launchdarkly_api.models.context_instance_evaluations import ContextInstanceEvaluations
from launchdarkly_api.models.context_instance_search import ContextInstanceSearch
from launchdarkly_api.models.context_instances import ContextInstances
from launchdarkly_api.models.context_kinds_collection_rep import ContextKindsCollectionRep
from launchdarkly_api.models.context_search import ContextSearch
from launchdarkly_api.models.contexts import Contexts
from launchdarkly_api.models.upsert_context_kind_payload import UpsertContextKindPayload
from launchdarkly_api.models.upsert_response_rep import UpsertResponseRep

from launchdarkly_api.api_client import ApiClient, RequestSerialized
from launchdarkly_api.api_response import ApiResponse
from launchdarkly_api.rest import RESTResponseType


class ContextsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def delete_context_instances(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        id: Annotated[StrictStr, Field(description="The context instance ID")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Delete context instances

        Delete context instances by ID.

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param id: The context instance ID (required)
        :type id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_context_instances_serialize(
            project_key=project_key,
            environment_key=environment_key,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '404': "NotFoundErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def delete_context_instances_with_http_info(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        id: Annotated[StrictStr, Field(description="The context instance ID")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Delete context instances

        Delete context instances by ID.

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param id: The context instance ID (required)
        :type id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_context_instances_serialize(
            project_key=project_key,
            environment_key=environment_key,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '404': "NotFoundErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def delete_context_instances_without_preload_content(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        id: Annotated[StrictStr, Field(description="The context instance ID")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Delete context instances

        Delete context instances by ID.

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param id: The context instance ID (required)
        :type id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_context_instances_serialize(
            project_key=project_key,
            environment_key=environment_key,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '404': "NotFoundErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_context_instances_serialize(
        self,
        project_key,
        environment_key,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if project_key is not None:
            _path_params['projectKey'] = project_key
        if environment_key is not None:
            _path_params['environmentKey'] = environment_key
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKey'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v2/projects/{projectKey}/environments/{environmentKey}/context-instances/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def evaluate_context_instance(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        request_body: Dict[str, Any],
        limit: Annotated[Optional[StrictInt], Field(description="The number of feature flags to return. Defaults to -1, which returns all flags")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of filters. Each filter is of the form `field operator value`. Supported fields are explained above.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ContextInstanceEvaluations:
        """Evaluate flags for context instance

        Evaluate flags for a context instance, for example, to determine the expected flag variation. **Do not use this API instead of an SDK.** The LaunchDarkly SDKs are specialized for the tasks of evaluating feature flags in your application at scale and generating analytics events based on those evaluations. This API is not designed for that use case. Any evaluations you perform with this API will not be reflected in features such as flag statuses and flag insights. Context instances evaluated by this API will not appear in the Contexts list. To learn more, read [Comparing LaunchDarkly's SDKs and REST API](https://launchdarkly.com/docs/guides/api/comparing-sdk-rest-api).  ### Filtering  LaunchDarkly supports the `filter` query param for filtering, with the following fields:  - `query` filters for a string that matches against the flags' keys and names. It is not case sensitive. For example: `filter=query equals dark-mode`. - `tags` filters the list to flags that have all of the tags in the list. For example: `filter=tags contains [\"beta\",\"q1\"]`.  You can also apply multiple filters at once. For example, setting `filter=query equals dark-mode, tags contains [\"beta\",\"q1\"]` matches flags which match the key or name `dark-mode` and are tagged `beta` and `q1`. 

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param request_body: (required)
        :type request_body: Dict[str, object]
        :param limit: The number of feature flags to return. Defaults to -1, which returns all flags
        :type limit: int
        :param offset: Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`.
        :type offset: int
        :param sort: A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order
        :type sort: str
        :param filter: A comma-separated list of filters. Each filter is of the form `field operator value`. Supported fields are explained above.
        :type filter: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._evaluate_context_instance_serialize(
            project_key=project_key,
            environment_key=environment_key,
            request_body=request_body,
            limit=limit,
            offset=offset,
            sort=sort,
            filter=filter,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextInstanceEvaluations",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '404': "NotFoundErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def evaluate_context_instance_with_http_info(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        request_body: Dict[str, Any],
        limit: Annotated[Optional[StrictInt], Field(description="The number of feature flags to return. Defaults to -1, which returns all flags")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of filters. Each filter is of the form `field operator value`. Supported fields are explained above.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ContextInstanceEvaluations]:
        """Evaluate flags for context instance

        Evaluate flags for a context instance, for example, to determine the expected flag variation. **Do not use this API instead of an SDK.** The LaunchDarkly SDKs are specialized for the tasks of evaluating feature flags in your application at scale and generating analytics events based on those evaluations. This API is not designed for that use case. Any evaluations you perform with this API will not be reflected in features such as flag statuses and flag insights. Context instances evaluated by this API will not appear in the Contexts list. To learn more, read [Comparing LaunchDarkly's SDKs and REST API](https://launchdarkly.com/docs/guides/api/comparing-sdk-rest-api).  ### Filtering  LaunchDarkly supports the `filter` query param for filtering, with the following fields:  - `query` filters for a string that matches against the flags' keys and names. It is not case sensitive. For example: `filter=query equals dark-mode`. - `tags` filters the list to flags that have all of the tags in the list. For example: `filter=tags contains [\"beta\",\"q1\"]`.  You can also apply multiple filters at once. For example, setting `filter=query equals dark-mode, tags contains [\"beta\",\"q1\"]` matches flags which match the key or name `dark-mode` and are tagged `beta` and `q1`. 

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param request_body: (required)
        :type request_body: Dict[str, object]
        :param limit: The number of feature flags to return. Defaults to -1, which returns all flags
        :type limit: int
        :param offset: Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`.
        :type offset: int
        :param sort: A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order
        :type sort: str
        :param filter: A comma-separated list of filters. Each filter is of the form `field operator value`. Supported fields are explained above.
        :type filter: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._evaluate_context_instance_serialize(
            project_key=project_key,
            environment_key=environment_key,
            request_body=request_body,
            limit=limit,
            offset=offset,
            sort=sort,
            filter=filter,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextInstanceEvaluations",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '404': "NotFoundErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def evaluate_context_instance_without_preload_content(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        request_body: Dict[str, Any],
        limit: Annotated[Optional[StrictInt], Field(description="The number of feature flags to return. Defaults to -1, which returns all flags")] = None,
        offset: Annotated[Optional[StrictInt], Field(description="Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of filters. Each filter is of the form `field operator value`. Supported fields are explained above.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Evaluate flags for context instance

        Evaluate flags for a context instance, for example, to determine the expected flag variation. **Do not use this API instead of an SDK.** The LaunchDarkly SDKs are specialized for the tasks of evaluating feature flags in your application at scale and generating analytics events based on those evaluations. This API is not designed for that use case. Any evaluations you perform with this API will not be reflected in features such as flag statuses and flag insights. Context instances evaluated by this API will not appear in the Contexts list. To learn more, read [Comparing LaunchDarkly's SDKs and REST API](https://launchdarkly.com/docs/guides/api/comparing-sdk-rest-api).  ### Filtering  LaunchDarkly supports the `filter` query param for filtering, with the following fields:  - `query` filters for a string that matches against the flags' keys and names. It is not case sensitive. For example: `filter=query equals dark-mode`. - `tags` filters the list to flags that have all of the tags in the list. For example: `filter=tags contains [\"beta\",\"q1\"]`.  You can also apply multiple filters at once. For example, setting `filter=query equals dark-mode, tags contains [\"beta\",\"q1\"]` matches flags which match the key or name `dark-mode` and are tagged `beta` and `q1`. 

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param request_body: (required)
        :type request_body: Dict[str, object]
        :param limit: The number of feature flags to return. Defaults to -1, which returns all flags
        :type limit: int
        :param offset: Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`.
        :type offset: int
        :param sort: A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order
        :type sort: str
        :param filter: A comma-separated list of filters. Each filter is of the form `field operator value`. Supported fields are explained above.
        :type filter: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._evaluate_context_instance_serialize(
            project_key=project_key,
            environment_key=environment_key,
            request_body=request_body,
            limit=limit,
            offset=offset,
            sort=sort,
            filter=filter,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextInstanceEvaluations",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '404': "NotFoundErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _evaluate_context_instance_serialize(
        self,
        project_key,
        environment_key,
        request_body,
        limit,
        offset,
        sort,
        filter,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if project_key is not None:
            _path_params['projectKey'] = project_key
        if environment_key is not None:
            _path_params['environmentKey'] = environment_key
        # process the query parameters
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
        if sort is not None:
            
            _query_params.append(('sort', sort))
            
        if filter is not None:
            
            _query_params.append(('filter', filter))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if request_body is not None:
            _body_params = request_body


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'ApiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v2/projects/{projectKey}/environments/{environmentKey}/flags/evaluate',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_context_attribute_names(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. This endpoint only accepts `kind` filters, with the `equals` operator, and `name` filters, with the `startsWith` operator. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of items in the collection to return (max: 100, default: 100)")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ContextAttributeNamesCollection:
        """Get context attribute names

        Get context attribute names.

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param filter: A comma-separated list of context filters. This endpoint only accepts `kind` filters, with the `equals` operator, and `name` filters, with the `startsWith` operator. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param limit: Specifies the maximum number of items in the collection to return (max: 100, default: 100)
        :type limit: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_context_attribute_names_serialize(
            project_key=project_key,
            environment_key=environment_key,
            filter=filter,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextAttributeNamesCollection",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_context_attribute_names_with_http_info(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. This endpoint only accepts `kind` filters, with the `equals` operator, and `name` filters, with the `startsWith` operator. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of items in the collection to return (max: 100, default: 100)")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ContextAttributeNamesCollection]:
        """Get context attribute names

        Get context attribute names.

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param filter: A comma-separated list of context filters. This endpoint only accepts `kind` filters, with the `equals` operator, and `name` filters, with the `startsWith` operator. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param limit: Specifies the maximum number of items in the collection to return (max: 100, default: 100)
        :type limit: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_context_attribute_names_serialize(
            project_key=project_key,
            environment_key=environment_key,
            filter=filter,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextAttributeNamesCollection",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_context_attribute_names_without_preload_content(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. This endpoint only accepts `kind` filters, with the `equals` operator, and `name` filters, with the `startsWith` operator. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of items in the collection to return (max: 100, default: 100)")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get context attribute names

        Get context attribute names.

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param filter: A comma-separated list of context filters. This endpoint only accepts `kind` filters, with the `equals` operator, and `name` filters, with the `startsWith` operator. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param limit: Specifies the maximum number of items in the collection to return (max: 100, default: 100)
        :type limit: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_context_attribute_names_serialize(
            project_key=project_key,
            environment_key=environment_key,
            filter=filter,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextAttributeNamesCollection",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_context_attribute_names_serialize(
        self,
        project_key,
        environment_key,
        filter,
        limit,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if project_key is not None:
            _path_params['projectKey'] = project_key
        if environment_key is not None:
            _path_params['environmentKey'] = environment_key
        # process the query parameters
        if filter is not None:
            
            _query_params.append(('filter', filter))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v2/projects/{projectKey}/environments/{environmentKey}/context-attributes',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_context_attribute_values(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        attribute_name: Annotated[StrictStr, Field(description="The attribute name")],
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. This endpoint only accepts `kind` filters, with the `equals` operator, and `value` filters, with the `startsWith` operator. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of items in the collection to return (max: 100, default: 50)")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ContextAttributeValuesCollection:
        """Get context attribute values

        Get context attribute values.

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param attribute_name: The attribute name (required)
        :type attribute_name: str
        :param filter: A comma-separated list of context filters. This endpoint only accepts `kind` filters, with the `equals` operator, and `value` filters, with the `startsWith` operator. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param limit: Specifies the maximum number of items in the collection to return (max: 100, default: 50)
        :type limit: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_context_attribute_values_serialize(
            project_key=project_key,
            environment_key=environment_key,
            attribute_name=attribute_name,
            filter=filter,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextAttributeValuesCollection",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_context_attribute_values_with_http_info(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        attribute_name: Annotated[StrictStr, Field(description="The attribute name")],
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. This endpoint only accepts `kind` filters, with the `equals` operator, and `value` filters, with the `startsWith` operator. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of items in the collection to return (max: 100, default: 50)")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ContextAttributeValuesCollection]:
        """Get context attribute values

        Get context attribute values.

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param attribute_name: The attribute name (required)
        :type attribute_name: str
        :param filter: A comma-separated list of context filters. This endpoint only accepts `kind` filters, with the `equals` operator, and `value` filters, with the `startsWith` operator. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param limit: Specifies the maximum number of items in the collection to return (max: 100, default: 50)
        :type limit: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_context_attribute_values_serialize(
            project_key=project_key,
            environment_key=environment_key,
            attribute_name=attribute_name,
            filter=filter,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextAttributeValuesCollection",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_context_attribute_values_without_preload_content(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        attribute_name: Annotated[StrictStr, Field(description="The attribute name")],
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. This endpoint only accepts `kind` filters, with the `equals` operator, and `value` filters, with the `startsWith` operator. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of items in the collection to return (max: 100, default: 50)")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get context attribute values

        Get context attribute values.

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param attribute_name: The attribute name (required)
        :type attribute_name: str
        :param filter: A comma-separated list of context filters. This endpoint only accepts `kind` filters, with the `equals` operator, and `value` filters, with the `startsWith` operator. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param limit: Specifies the maximum number of items in the collection to return (max: 100, default: 50)
        :type limit: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_context_attribute_values_serialize(
            project_key=project_key,
            environment_key=environment_key,
            attribute_name=attribute_name,
            filter=filter,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextAttributeValuesCollection",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_context_attribute_values_serialize(
        self,
        project_key,
        environment_key,
        attribute_name,
        filter,
        limit,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if project_key is not None:
            _path_params['projectKey'] = project_key
        if environment_key is not None:
            _path_params['environmentKey'] = environment_key
        if attribute_name is not None:
            _path_params['attributeName'] = attribute_name
        # process the query parameters
        if filter is not None:
            
            _query_params.append(('filter', filter))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v2/projects/{projectKey}/environments/{environmentKey}/context-attributes/{attributeName}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_context_instances(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        id: Annotated[StrictStr, Field(description="The context instance ID")],
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of context instances to return (max: 50, default: 20)")] = None,
        continuation_token: Annotated[Optional[StrictStr], Field(description="Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        include_total_count: Annotated[Optional[StrictBool], Field(description="Specifies whether to include or omit the total count of matching context instances. Defaults to true.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ContextInstances:
        """Get context instances

        Get context instances by ID.

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param id: The context instance ID (required)
        :type id: str
        :param limit: Specifies the maximum number of context instances to return (max: 50, default: 20)
        :type limit: int
        :param continuation_token: Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.
        :type continuation_token: str
        :param sort: Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.
        :type sort: str
        :param filter: A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param include_total_count: Specifies whether to include or omit the total count of matching context instances. Defaults to true.
        :type include_total_count: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_context_instances_serialize(
            project_key=project_key,
            environment_key=environment_key,
            id=id,
            limit=limit,
            continuation_token=continuation_token,
            sort=sort,
            filter=filter,
            include_total_count=include_total_count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextInstances",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_context_instances_with_http_info(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        id: Annotated[StrictStr, Field(description="The context instance ID")],
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of context instances to return (max: 50, default: 20)")] = None,
        continuation_token: Annotated[Optional[StrictStr], Field(description="Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        include_total_count: Annotated[Optional[StrictBool], Field(description="Specifies whether to include or omit the total count of matching context instances. Defaults to true.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ContextInstances]:
        """Get context instances

        Get context instances by ID.

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param id: The context instance ID (required)
        :type id: str
        :param limit: Specifies the maximum number of context instances to return (max: 50, default: 20)
        :type limit: int
        :param continuation_token: Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.
        :type continuation_token: str
        :param sort: Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.
        :type sort: str
        :param filter: A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param include_total_count: Specifies whether to include or omit the total count of matching context instances. Defaults to true.
        :type include_total_count: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_context_instances_serialize(
            project_key=project_key,
            environment_key=environment_key,
            id=id,
            limit=limit,
            continuation_token=continuation_token,
            sort=sort,
            filter=filter,
            include_total_count=include_total_count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextInstances",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_context_instances_without_preload_content(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        id: Annotated[StrictStr, Field(description="The context instance ID")],
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of context instances to return (max: 50, default: 20)")] = None,
        continuation_token: Annotated[Optional[StrictStr], Field(description="Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        include_total_count: Annotated[Optional[StrictBool], Field(description="Specifies whether to include or omit the total count of matching context instances. Defaults to true.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get context instances

        Get context instances by ID.

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param id: The context instance ID (required)
        :type id: str
        :param limit: Specifies the maximum number of context instances to return (max: 50, default: 20)
        :type limit: int
        :param continuation_token: Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.
        :type continuation_token: str
        :param sort: Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.
        :type sort: str
        :param filter: A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param include_total_count: Specifies whether to include or omit the total count of matching context instances. Defaults to true.
        :type include_total_count: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_context_instances_serialize(
            project_key=project_key,
            environment_key=environment_key,
            id=id,
            limit=limit,
            continuation_token=continuation_token,
            sort=sort,
            filter=filter,
            include_total_count=include_total_count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextInstances",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_context_instances_serialize(
        self,
        project_key,
        environment_key,
        id,
        limit,
        continuation_token,
        sort,
        filter,
        include_total_count,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if project_key is not None:
            _path_params['projectKey'] = project_key
        if environment_key is not None:
            _path_params['environmentKey'] = environment_key
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if continuation_token is not None:
            
            _query_params.append(('continuationToken', continuation_token))
            
        if sort is not None:
            
            _query_params.append(('sort', sort))
            
        if filter is not None:
            
            _query_params.append(('filter', filter))
            
        if include_total_count is not None:
            
            _query_params.append(('includeTotalCount', include_total_count))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v2/projects/{projectKey}/environments/{environmentKey}/context-instances/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_context_kinds_by_project_key(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ContextKindsCollectionRep:
        """Get context kinds

        Get all context kinds for a given project.

        :param project_key: The project key (required)
        :type project_key: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_context_kinds_by_project_key_serialize(
            project_key=project_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextKindsCollectionRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '404': "NotFoundErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_context_kinds_by_project_key_with_http_info(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ContextKindsCollectionRep]:
        """Get context kinds

        Get all context kinds for a given project.

        :param project_key: The project key (required)
        :type project_key: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_context_kinds_by_project_key_serialize(
            project_key=project_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextKindsCollectionRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '404': "NotFoundErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_context_kinds_by_project_key_without_preload_content(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get context kinds

        Get all context kinds for a given project.

        :param project_key: The project key (required)
        :type project_key: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_context_kinds_by_project_key_serialize(
            project_key=project_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextKindsCollectionRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '404': "NotFoundErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_context_kinds_by_project_key_serialize(
        self,
        project_key,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if project_key is not None:
            _path_params['projectKey'] = project_key
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v2/projects/{projectKey}/context-kinds',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_contexts(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        kind: Annotated[StrictStr, Field(description="The context kind")],
        key: Annotated[StrictStr, Field(description="The context key")],
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of items in the collection to return (max: 50, default: 20)")] = None,
        continuation_token: Annotated[Optional[StrictStr], Field(description="Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        include_total_count: Annotated[Optional[StrictBool], Field(description="Specifies whether to include or omit the total count of matching contexts. Defaults to true.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Contexts:
        """Get contexts

        Get contexts based on kind and key.

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param kind: The context kind (required)
        :type kind: str
        :param key: The context key (required)
        :type key: str
        :param limit: Specifies the maximum number of items in the collection to return (max: 50, default: 20)
        :type limit: int
        :param continuation_token: Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.
        :type continuation_token: str
        :param sort: Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.
        :type sort: str
        :param filter: A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param include_total_count: Specifies whether to include or omit the total count of matching contexts. Defaults to true.
        :type include_total_count: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_contexts_serialize(
            project_key=project_key,
            environment_key=environment_key,
            kind=kind,
            key=key,
            limit=limit,
            continuation_token=continuation_token,
            sort=sort,
            filter=filter,
            include_total_count=include_total_count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Contexts",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_contexts_with_http_info(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        kind: Annotated[StrictStr, Field(description="The context kind")],
        key: Annotated[StrictStr, Field(description="The context key")],
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of items in the collection to return (max: 50, default: 20)")] = None,
        continuation_token: Annotated[Optional[StrictStr], Field(description="Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        include_total_count: Annotated[Optional[StrictBool], Field(description="Specifies whether to include or omit the total count of matching contexts. Defaults to true.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Contexts]:
        """Get contexts

        Get contexts based on kind and key.

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param kind: The context kind (required)
        :type kind: str
        :param key: The context key (required)
        :type key: str
        :param limit: Specifies the maximum number of items in the collection to return (max: 50, default: 20)
        :type limit: int
        :param continuation_token: Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.
        :type continuation_token: str
        :param sort: Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.
        :type sort: str
        :param filter: A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param include_total_count: Specifies whether to include or omit the total count of matching contexts. Defaults to true.
        :type include_total_count: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_contexts_serialize(
            project_key=project_key,
            environment_key=environment_key,
            kind=kind,
            key=key,
            limit=limit,
            continuation_token=continuation_token,
            sort=sort,
            filter=filter,
            include_total_count=include_total_count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Contexts",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_contexts_without_preload_content(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        kind: Annotated[StrictStr, Field(description="The context kind")],
        key: Annotated[StrictStr, Field(description="The context key")],
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of items in the collection to return (max: 50, default: 20)")] = None,
        continuation_token: Annotated[Optional[StrictStr], Field(description="Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        include_total_count: Annotated[Optional[StrictBool], Field(description="Specifies whether to include or omit the total count of matching contexts. Defaults to true.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get contexts

        Get contexts based on kind and key.

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param kind: The context kind (required)
        :type kind: str
        :param key: The context key (required)
        :type key: str
        :param limit: Specifies the maximum number of items in the collection to return (max: 50, default: 20)
        :type limit: int
        :param continuation_token: Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.
        :type continuation_token: str
        :param sort: Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.
        :type sort: str
        :param filter: A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param include_total_count: Specifies whether to include or omit the total count of matching contexts. Defaults to true.
        :type include_total_count: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_contexts_serialize(
            project_key=project_key,
            environment_key=environment_key,
            kind=kind,
            key=key,
            limit=limit,
            continuation_token=continuation_token,
            sort=sort,
            filter=filter,
            include_total_count=include_total_count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Contexts",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_contexts_serialize(
        self,
        project_key,
        environment_key,
        kind,
        key,
        limit,
        continuation_token,
        sort,
        filter,
        include_total_count,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if project_key is not None:
            _path_params['projectKey'] = project_key
        if environment_key is not None:
            _path_params['environmentKey'] = environment_key
        if kind is not None:
            _path_params['kind'] = kind
        if key is not None:
            _path_params['key'] = key
        # process the query parameters
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if continuation_token is not None:
            
            _query_params.append(('continuationToken', continuation_token))
            
        if sort is not None:
            
            _query_params.append(('sort', sort))
            
        if filter is not None:
            
            _query_params.append(('filter', filter))
            
        if include_total_count is not None:
            
            _query_params.append(('includeTotalCount', include_total_count))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKey'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v2/projects/{projectKey}/environments/{environmentKey}/contexts/{kind}/{key}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def put_context_kind(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        key: Annotated[StrictStr, Field(description="The context kind key")],
        upsert_context_kind_payload: UpsertContextKindPayload,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> UpsertResponseRep:
        """Create or update context kind

        Create or update a context kind by key. Only the included fields will be updated.

        :param project_key: The project key (required)
        :type project_key: str
        :param key: The context kind key (required)
        :type key: str
        :param upsert_context_kind_payload: (required)
        :type upsert_context_kind_payload: UpsertContextKindPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._put_context_kind_serialize(
            project_key=project_key,
            key=key,
            upsert_context_kind_payload=upsert_context_kind_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UpsertResponseRep",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '404': "NotFoundErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def put_context_kind_with_http_info(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        key: Annotated[StrictStr, Field(description="The context kind key")],
        upsert_context_kind_payload: UpsertContextKindPayload,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[UpsertResponseRep]:
        """Create or update context kind

        Create or update a context kind by key. Only the included fields will be updated.

        :param project_key: The project key (required)
        :type project_key: str
        :param key: The context kind key (required)
        :type key: str
        :param upsert_context_kind_payload: (required)
        :type upsert_context_kind_payload: UpsertContextKindPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._put_context_kind_serialize(
            project_key=project_key,
            key=key,
            upsert_context_kind_payload=upsert_context_kind_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UpsertResponseRep",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '404': "NotFoundErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def put_context_kind_without_preload_content(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        key: Annotated[StrictStr, Field(description="The context kind key")],
        upsert_context_kind_payload: UpsertContextKindPayload,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Create or update context kind

        Create or update a context kind by key. Only the included fields will be updated.

        :param project_key: The project key (required)
        :type project_key: str
        :param key: The context kind key (required)
        :type key: str
        :param upsert_context_kind_payload: (required)
        :type upsert_context_kind_payload: UpsertContextKindPayload
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._put_context_kind_serialize(
            project_key=project_key,
            key=key,
            upsert_context_kind_payload=upsert_context_kind_payload,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UpsertResponseRep",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '404': "NotFoundErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _put_context_kind_serialize(
        self,
        project_key,
        key,
        upsert_context_kind_payload,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if project_key is not None:
            _path_params['projectKey'] = project_key
        if key is not None:
            _path_params['key'] = key
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if upsert_context_kind_payload is not None:
            _body_params = upsert_context_kind_payload


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'ApiKey'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v2/projects/{projectKey}/context-kinds/{key}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def search_context_instances(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        context_instance_search: ContextInstanceSearch,
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of items in the collection to return (max: 50, default: 20)")] = None,
        continuation_token: Annotated[Optional[StrictStr], Field(description="Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        include_total_count: Annotated[Optional[StrictBool], Field(description="Specifies whether to include or omit the total count of matching context instances. Defaults to true.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ContextInstances:
        """Search for context instances

         Search for context instances.  You can use either the query parameters or the request body parameters. If both are provided, there is an error.  To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/api/contexts#filtering-contexts-and-context-instances). To learn more about context instances, read [Context instances](https://launchdarkly.com/docs/home/observability/multi-contexts#context-instances). 

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param context_instance_search: (required)
        :type context_instance_search: ContextInstanceSearch
        :param limit: Specifies the maximum number of items in the collection to return (max: 50, default: 20)
        :type limit: int
        :param continuation_token: Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.
        :type continuation_token: str
        :param sort: Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.
        :type sort: str
        :param filter: A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param include_total_count: Specifies whether to include or omit the total count of matching context instances. Defaults to true.
        :type include_total_count: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._search_context_instances_serialize(
            project_key=project_key,
            environment_key=environment_key,
            context_instance_search=context_instance_search,
            limit=limit,
            continuation_token=continuation_token,
            sort=sort,
            filter=filter,
            include_total_count=include_total_count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextInstances",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def search_context_instances_with_http_info(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        context_instance_search: ContextInstanceSearch,
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of items in the collection to return (max: 50, default: 20)")] = None,
        continuation_token: Annotated[Optional[StrictStr], Field(description="Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        include_total_count: Annotated[Optional[StrictBool], Field(description="Specifies whether to include or omit the total count of matching context instances. Defaults to true.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ContextInstances]:
        """Search for context instances

         Search for context instances.  You can use either the query parameters or the request body parameters. If both are provided, there is an error.  To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/api/contexts#filtering-contexts-and-context-instances). To learn more about context instances, read [Context instances](https://launchdarkly.com/docs/home/observability/multi-contexts#context-instances). 

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param context_instance_search: (required)
        :type context_instance_search: ContextInstanceSearch
        :param limit: Specifies the maximum number of items in the collection to return (max: 50, default: 20)
        :type limit: int
        :param continuation_token: Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.
        :type continuation_token: str
        :param sort: Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.
        :type sort: str
        :param filter: A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param include_total_count: Specifies whether to include or omit the total count of matching context instances. Defaults to true.
        :type include_total_count: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._search_context_instances_serialize(
            project_key=project_key,
            environment_key=environment_key,
            context_instance_search=context_instance_search,
            limit=limit,
            continuation_token=continuation_token,
            sort=sort,
            filter=filter,
            include_total_count=include_total_count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextInstances",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def search_context_instances_without_preload_content(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        context_instance_search: ContextInstanceSearch,
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of items in the collection to return (max: 50, default: 20)")] = None,
        continuation_token: Annotated[Optional[StrictStr], Field(description="Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        include_total_count: Annotated[Optional[StrictBool], Field(description="Specifies whether to include or omit the total count of matching context instances. Defaults to true.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Search for context instances

         Search for context instances.  You can use either the query parameters or the request body parameters. If both are provided, there is an error.  To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/api/contexts#filtering-contexts-and-context-instances). To learn more about context instances, read [Context instances](https://launchdarkly.com/docs/home/observability/multi-contexts#context-instances). 

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param context_instance_search: (required)
        :type context_instance_search: ContextInstanceSearch
        :param limit: Specifies the maximum number of items in the collection to return (max: 50, default: 20)
        :type limit: int
        :param continuation_token: Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.
        :type continuation_token: str
        :param sort: Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.
        :type sort: str
        :param filter: A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param include_total_count: Specifies whether to include or omit the total count of matching context instances. Defaults to true.
        :type include_total_count: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._search_context_instances_serialize(
            project_key=project_key,
            environment_key=environment_key,
            context_instance_search=context_instance_search,
            limit=limit,
            continuation_token=continuation_token,
            sort=sort,
            filter=filter,
            include_total_count=include_total_count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContextInstances",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _search_context_instances_serialize(
        self,
        project_key,
        environment_key,
        context_instance_search,
        limit,
        continuation_token,
        sort,
        filter,
        include_total_count,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if project_key is not None:
            _path_params['projectKey'] = project_key
        if environment_key is not None:
            _path_params['environmentKey'] = environment_key
        # process the query parameters
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if continuation_token is not None:
            
            _query_params.append(('continuationToken', continuation_token))
            
        if sort is not None:
            
            _query_params.append(('sort', sort))
            
        if filter is not None:
            
            _query_params.append(('filter', filter))
            
        if include_total_count is not None:
            
            _query_params.append(('includeTotalCount', include_total_count))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if context_instance_search is not None:
            _body_params = context_instance_search


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'ApiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v2/projects/{projectKey}/environments/{environmentKey}/context-instances/search',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def search_contexts(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        context_search: ContextSearch,
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of items in the collection to return (max: 50, default: 20)")] = None,
        continuation_token: Annotated[Optional[StrictStr], Field(description="Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        include_total_count: Annotated[Optional[StrictBool], Field(description="Specifies whether to include or omit the total count of matching contexts. Defaults to true.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Contexts:
        """Search for contexts

         Search for contexts.  You can use either the query parameters or the request body parameters. If both are provided, there is an error.  To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/api/contexts#filtering-contexts-and-context-instances). To learn more about contexts, read [Contexts and context kinds](https://launchdarkly.com/docs/home/observability/contexts#contexts-and-context-kinds). 

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param context_search: (required)
        :type context_search: ContextSearch
        :param limit: Specifies the maximum number of items in the collection to return (max: 50, default: 20)
        :type limit: int
        :param continuation_token: Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.
        :type continuation_token: str
        :param sort: Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.
        :type sort: str
        :param filter: A comma-separated list of context filters. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param include_total_count: Specifies whether to include or omit the total count of matching contexts. Defaults to true.
        :type include_total_count: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._search_contexts_serialize(
            project_key=project_key,
            environment_key=environment_key,
            context_search=context_search,
            limit=limit,
            continuation_token=continuation_token,
            sort=sort,
            filter=filter,
            include_total_count=include_total_count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Contexts",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def search_contexts_with_http_info(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        context_search: ContextSearch,
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of items in the collection to return (max: 50, default: 20)")] = None,
        continuation_token: Annotated[Optional[StrictStr], Field(description="Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        include_total_count: Annotated[Optional[StrictBool], Field(description="Specifies whether to include or omit the total count of matching contexts. Defaults to true.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Contexts]:
        """Search for contexts

         Search for contexts.  You can use either the query parameters or the request body parameters. If both are provided, there is an error.  To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/api/contexts#filtering-contexts-and-context-instances). To learn more about contexts, read [Contexts and context kinds](https://launchdarkly.com/docs/home/observability/contexts#contexts-and-context-kinds). 

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param context_search: (required)
        :type context_search: ContextSearch
        :param limit: Specifies the maximum number of items in the collection to return (max: 50, default: 20)
        :type limit: int
        :param continuation_token: Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.
        :type continuation_token: str
        :param sort: Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.
        :type sort: str
        :param filter: A comma-separated list of context filters. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param include_total_count: Specifies whether to include or omit the total count of matching contexts. Defaults to true.
        :type include_total_count: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._search_contexts_serialize(
            project_key=project_key,
            environment_key=environment_key,
            context_search=context_search,
            limit=limit,
            continuation_token=continuation_token,
            sort=sort,
            filter=filter,
            include_total_count=include_total_count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Contexts",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def search_contexts_without_preload_content(
        self,
        project_key: Annotated[StrictStr, Field(description="The project key")],
        environment_key: Annotated[StrictStr, Field(description="The environment key")],
        context_search: ContextSearch,
        limit: Annotated[Optional[StrictInt], Field(description="Specifies the maximum number of items in the collection to return (max: 50, default: 20)")] = None,
        continuation_token: Annotated[Optional[StrictStr], Field(description="Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="A comma-separated list of context filters. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).")] = None,
        include_total_count: Annotated[Optional[StrictBool], Field(description="Specifies whether to include or omit the total count of matching contexts. Defaults to true.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Search for contexts

         Search for contexts.  You can use either the query parameters or the request body parameters. If both are provided, there is an error.  To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/api/contexts#filtering-contexts-and-context-instances). To learn more about contexts, read [Contexts and context kinds](https://launchdarkly.com/docs/home/observability/contexts#contexts-and-context-kinds). 

        :param project_key: The project key (required)
        :type project_key: str
        :param environment_key: The environment key (required)
        :type environment_key: str
        :param context_search: (required)
        :type context_search: ContextSearch
        :param limit: Specifies the maximum number of items in the collection to return (max: 50, default: 20)
        :type limit: int
        :param continuation_token: Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead.
        :type continuation_token: str
        :param sort: Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`.
        :type sort: str
        :param filter: A comma-separated list of context filters. To learn more about the filter syntax, read [Filtering contexts and context instances](https://launchdarkly.com/docs/ld-docs/api/contexts#filtering-contexts-and-context-instances).
        :type filter: str
        :param include_total_count: Specifies whether to include or omit the total count of matching contexts. Defaults to true.
        :type include_total_count: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._search_contexts_serialize(
            project_key=project_key,
            environment_key=environment_key,
            context_search=context_search,
            limit=limit,
            continuation_token=continuation_token,
            sort=sort,
            filter=filter,
            include_total_count=include_total_count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Contexts",
            '400': "InvalidRequestErrorRep",
            '401': "UnauthorizedErrorRep",
            '403': "ForbiddenErrorRep",
            '429': "RateLimitedErrorRep",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _search_contexts_serialize(
        self,
        project_key,
        environment_key,
        context_search,
        limit,
        continuation_token,
        sort,
        filter,
        include_total_count,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if project_key is not None:
            _path_params['projectKey'] = project_key
        if environment_key is not None:
            _path_params['environmentKey'] = environment_key
        # process the query parameters
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if continuation_token is not None:
            
            _query_params.append(('continuationToken', continuation_token))
            
        if sort is not None:
            
            _query_params.append(('sort', sort))
            
        if filter is not None:
            
            _query_params.append(('filter', filter))
            
        if include_total_count is not None:
            
            _query_params.append(('includeTotalCount', include_total_count))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if context_search is not None:
            _body_params = context_search


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'ApiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v2/projects/{projectKey}/environments/{environmentKey}/contexts/search',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


