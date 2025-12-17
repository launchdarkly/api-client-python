# coding: utf-8

# flake8: noqa

"""
    LaunchDarkly REST API

    This documentation describes LaunchDarkly's REST API. To access the complete OpenAPI spec directly, use [Get OpenAPI spec](https://launchdarkly.com/docs/api/other/get-openapi-spec).  To learn how to use LaunchDarkly using the user interface (UI) instead, read our [product documentation](https://launchdarkly.com/docs/home).  ## Authentication  LaunchDarkly's REST API uses the HTTPS protocol with a minimum TLS version of 1.2.  All REST API resources are authenticated with either [personal or service access tokens](https://launchdarkly.com/docs/home/account/api), or session cookies. Other authentication mechanisms are not supported. You can manage personal access tokens on your [**Authorization**](https://app.launchdarkly.com/settings/authorization) page in the LaunchDarkly UI.  LaunchDarkly also has SDK keys, mobile keys, and client-side IDs that are used by our server-side SDKs, mobile SDKs, and JavaScript-based SDKs, respectively. **These keys cannot be used to access our REST API**. These keys are environment-specific, and can only perform read-only operations such as fetching feature flag settings.  | Auth mechanism                                                                                  | Allowed resources                                                                                     | Use cases                                          | | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------- | | [Personal or service access tokens](https://launchdarkly.com/docs/home/account/api) | Can be customized on a per-token basis                                                                | Building scripts, custom integrations, data export. | | SDK keys                                                                                        | Can only access read-only resources specific to server-side SDKs. Restricted to a single environment. | Server-side SDKs                     | | Mobile keys                                                                                     | Can only access read-only resources specific to mobile SDKs, and only for flags marked available to mobile keys. Restricted to a single environment.           | Mobile SDKs                                        | | Client-side ID                                                                                  | Can only access read-only resources specific to JavaScript-based client-side SDKs, and only for flags marked available to client-side. Restricted to a single environment.           | Client-side JavaScript                             |  > #### Keep your access tokens and SDK keys private > > Access tokens should _never_ be exposed in untrusted contexts. Never put an access token in client-side JavaScript, or embed it in a mobile application. LaunchDarkly has special mobile keys that you can embed in mobile apps. If you accidentally expose an access token or SDK key, you can reset it from your [**Authorization**](https://app.launchdarkly.com/settings/authorization) page. > > The client-side ID is safe to embed in untrusted contexts. It's designed for use in client-side JavaScript.  ### Authentication using request header  The preferred way to authenticate with the API is by adding an `Authorization` header containing your access token to your requests. The value of the `Authorization` header must be your access token.  Manage personal access tokens from the [**Authorization**](https://app.launchdarkly.com/settings/authorization) page.  ### Authentication using session cookie  For testing purposes, you can make API calls directly from your web browser. If you are logged in to the LaunchDarkly application, the API will use your existing session to authenticate calls.  Depending on the permissions granted as part of your [role](https://launchdarkly.com/docs/home/account/roles), you may not have permission to perform some API calls. You will receive a `401` response code in that case.  > ### Modifying the Origin header causes an error > > LaunchDarkly validates that the Origin header for any API request authenticated by a session cookie matches the expected Origin header. The expected Origin header is `https://app.launchdarkly.com`. > > If the Origin header does not match what's expected, LaunchDarkly returns an error. This error can prevent the LaunchDarkly app from working correctly. > > Any browser extension that intentionally changes the Origin header can cause this problem. For example, the `Allow-Control-Allow-Origin: *` Chrome extension changes the Origin header to `http://evil.com` and causes the app to fail. > > To prevent this error, do not modify your Origin header. > > LaunchDarkly does not require origin matching when authenticating with an access token, so this issue does not affect normal API usage.  ## Representations  All resources expect and return JSON response bodies. Error responses also send a JSON body. To learn more about the error format of the API, read [Errors](https://launchdarkly.com/docs/api#errors).  In practice this means that you always get a response with a `Content-Type` header set to `application/json`.  In addition, request bodies for `PATCH`, `POST`, and `PUT` requests must be encoded as JSON with a `Content-Type` header set to `application/json`.  ### Summary and detailed representations  When you fetch a list of resources, the response includes only the most important attributes of each resource. This is a _summary representation_ of the resource. When you fetch an individual resource, such as a single feature flag, you receive a _detailed representation_ of the resource.  The best way to find a detailed representation is to follow links. Every summary representation includes a link to its detailed representation.  ### Expanding responses  Sometimes the detailed representation of a resource does not include all of the attributes of the resource by default. If this is the case, the request method will clearly document this and describe which attributes you can include in an expanded response.  To include the additional attributes, append the `expand` request parameter to your request and add a comma-separated list of the attributes to include. For example, when you append `?expand=members,maintainers` to the [Get team](https://launchdarkly.com/docs/api/teams/get-team) endpoint, the expanded response includes both of these attributes.  ### Links and addressability  The best way to navigate the API is by following links. These are attributes in representations that link to other resources. The API always uses the same format for links:  - Links to other resources within the API are encapsulated in a `_links` object - If the resource has a corresponding link to HTML content on the site, it is stored in a special `_site` link  Each link has two attributes:  - An `href`, which contains the URL - A `type`, which describes the content type  For example, a feature resource might return the following:  ```json {   \"_links\": {     \"parent\": {       \"href\": \"/api/features\",       \"type\": \"application/json\"     },     \"self\": {       \"href\": \"/api/features/sort.order\",       \"type\": \"application/json\"     }   },   \"_site\": {     \"href\": \"/features/sort.order\",     \"type\": \"text/html\"   } } ```  From this, you can navigate to the parent collection of features by following the `parent` link, or navigate to the site page for the feature by following the `_site` link.  Collections are always represented as a JSON object with an `items` attribute containing an array of representations. Like all other representations, collections have `_links` defined at the top level.  Paginated collections include `first`, `last`, `next`, and `prev` links containing a URL with the respective set of elements in the collection.  ## Updates  Resources that accept partial updates use the `PATCH` verb. Most resources support the [JSON patch](https://launchdarkly.com/docs/api#updates-using-json-patch) format. Some resources also support the [JSON merge patch](https://launchdarkly.com/docs/api#updates-using-json-merge-patch) format, and some resources support the [semantic patch](https://launchdarkly.com/docs/api#updates-using-semantic-patch) format, which is a way to specify the modifications to perform as a set of executable instructions. Each resource supports optional [comments](https://launchdarkly.com/docs/api#updates-with-comments) that you can submit with updates. Comments appear in outgoing webhooks, the audit log, and other integrations.  When a resource supports both JSON patch and semantic patch, we document both in the request method. However, the specific request body fields and descriptions included in our documentation only match one type of patch or the other.  ### Updates using JSON patch  [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) is a way to specify the modifications to perform on a resource. JSON patch uses paths and a limited set of operations to describe how to transform the current state of the resource into a new state. JSON patch documents are always arrays, where each element contains an operation, a path to the field to update, and the new value.  For example, in this feature flag representation:  ```json {     \"name\": \"New recommendations engine\",     \"key\": \"engine.enable\",     \"description\": \"This is the description\",     ... } ``` You can change the feature flag's description with the following patch document:  ```json [{ \"op\": \"replace\", \"path\": \"/description\", \"value\": \"This is the new description\" }] ```  You can specify multiple modifications to perform in a single request. You can also test that certain preconditions are met before applying the patch:  ```json [   { \"op\": \"test\", \"path\": \"/version\", \"value\": 10 },   { \"op\": \"replace\", \"path\": \"/description\", \"value\": \"The new description\" } ] ```  The above patch request tests whether the feature flag's `version` is `10`, and if so, changes the feature flag's description.  Attributes that are not editable, such as a resource's `_links`, have names that start with an underscore.  ### Updates using JSON merge patch  [JSON merge patch](https://datatracker.ietf.org/doc/html/rfc7386) is another format for specifying the modifications to perform on a resource. JSON merge patch is less expressive than JSON patch. However, in many cases it is simpler to construct a merge patch document. For example, you can change a feature flag's description with the following merge patch document:  ```json {   \"description\": \"New flag description\" } ```  ### Updates using semantic patch  Some resources support the semantic patch format. A semantic patch is a way to specify the modifications to perform on a resource as a set of executable instructions.  Semantic patch allows you to be explicit about intent using precise, custom instructions. In many cases, you can define semantic patch instructions independently of the current state of the resource. This can be useful when defining a change that may be applied at a future date.  To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header.  Here's how:  ``` Content-Type: application/json; domain-model=launchdarkly.semanticpatch ```  If you call a semantic patch resource without this header, you will receive a `400` response because your semantic patch will be interpreted as a JSON patch.  The body of a semantic patch request takes the following properties:  * `comment` (string): (Optional) A description of the update. * `environmentKey` (string): (Required for some resources only) The environment key. * `instructions` (array): (Required) A list of actions the update should perform. Each action in the list must be an object with a `kind` property that indicates the instruction. If the instruction requires parameters, you must include those parameters as additional fields in the object. The documentation for each resource that supports semantic patch includes the available instructions and any additional parameters.  For example:  ```json {   \"comment\": \"optional comment\",   \"instructions\": [ {\"kind\": \"turnFlagOn\"} ] } ```  Semantic patches are not applied partially; either all of the instructions are applied or none of them are. If **any** instruction is invalid, the endpoint returns an error and will not change the resource. If all instructions are valid, the request succeeds and the resources are updated if necessary, or left unchanged if they are already in the state you request.  ### Updates with comments  You can submit optional comments with `PATCH` changes.  To submit a comment along with a JSON patch document, use the following format:  ```json {   \"comment\": \"This is a comment string\",   \"patch\": [{ \"op\": \"replace\", \"path\": \"/description\", \"value\": \"The new description\" }] } ```  To submit a comment along with a JSON merge patch document, use the following format:  ```json {   \"comment\": \"This is a comment string\",   \"merge\": { \"description\": \"New flag description\" } } ```  To submit a comment along with a semantic patch, use the following format:  ```json {   \"comment\": \"This is a comment string\",   \"instructions\": [ {\"kind\": \"turnFlagOn\"} ] } ```  ## Errors  The API always returns errors in a common format. Here's an example:  ```json {   \"code\": \"invalid_request\",   \"message\": \"A feature with that key already exists\",   \"id\": \"30ce6058-87da-11e4-b116-123b93f75cba\" } ```  The `code` indicates the general class of error. The `message` is a human-readable explanation of what went wrong. The `id` is a unique identifier. Use it when you're working with LaunchDarkly Support to debug a problem with a specific API call.  ### HTTP status error response codes  | Code | Definition        | Description                                                                                       | Possible Solution                                                | | ---- | ----------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | | 400  | Invalid request       | The request cannot be understood.                                    | Ensure JSON syntax in request body is correct.                   | | 401  | Invalid access token      | Requestor is unauthorized or does not have permission for this API call.                                                | Ensure your API access token is valid and has the appropriate permissions.                                     | | 403  | Forbidden         | Requestor does not have access to this resource.                                                | Ensure that the account member or access token has proper permissions set. | | 404  | Invalid resource identifier | The requested resource is not valid. | Ensure that the resource is correctly identified by ID or key. | | 405  | Method not allowed | The request method is not allowed on this resource. | Ensure that the HTTP verb is correct. | | 409  | Conflict          | The API request can not be completed because it conflicts with a concurrent API request. | Retry your request.                                              | | 422  | Unprocessable entity | The API request can not be completed because the update description can not be understood. | Ensure that the request body is correct for the type of patch you are using, either JSON patch or semantic patch. | 429  | Too many requests | Read [Rate limiting](https://launchdarkly.com/docs/api#rate-limiting).                                               | Wait and try again later.                                        |  ## CORS  The LaunchDarkly API supports Cross Origin Resource Sharing (CORS) for AJAX requests from any origin. If an `Origin` header is given in a request, it will be echoed as an explicitly allowed origin. Otherwise the request returns a wildcard, `Access-Control-Allow-Origin: *`. For more information on CORS, read the [CORS W3C Recommendation](http://www.w3.org/TR/cors). Example CORS headers might look like:  ```http Access-Control-Allow-Headers: Accept, Content-Type, Content-Length, Accept-Encoding, Authorization Access-Control-Allow-Methods: OPTIONS, GET, DELETE, PATCH Access-Control-Allow-Origin: * Access-Control-Max-Age: 300 ```  You can make authenticated CORS calls just as you would make same-origin calls, using either [token or session-based authentication](https://launchdarkly.com/docs/api#authentication). If you are using session authentication, you should set the `withCredentials` property for your `xhr` request to `true`. You should never expose your access tokens to untrusted entities.  ## Rate limiting  We use several rate limiting strategies to ensure the availability of our APIs. Rate-limited calls to our APIs return a `429` status code. Calls to our APIs include headers indicating the current rate limit status. The specific headers returned depend on the API route being called. The limits differ based on the route, authentication mechanism, and other factors. Routes that are not rate limited may not contain any of the headers described below.  > ### Rate limiting and SDKs > > LaunchDarkly SDKs are never rate limited and do not use the API endpoints defined here. LaunchDarkly uses a different set of approaches, including streaming/server-sent events and a global CDN, to ensure availability to the routes used by LaunchDarkly SDKs.  ### Global rate limits  Authenticated requests are subject to a global limit. This is the maximum number of calls that your account can make to the API per ten seconds. All service and personal access tokens on the account share this limit, so exceeding the limit with one access token will impact other tokens. Calls that are subject to global rate limits may return the headers below:  | Header name                    | Description                                                                      | | ------------------------------ | -------------------------------------------------------------------------------- | | `X-Ratelimit-Global-Remaining` | The maximum number of requests the account is permitted to make per ten seconds. | | `X-Ratelimit-Reset`            | The time at which the current rate limit window resets in epoch milliseconds.    |  We do not publicly document the specific number of calls that can be made globally. This limit may change, and we encourage clients to program against the specification, relying on the two headers defined above, rather than hardcoding to the current limit.  ### Route-level rate limits  Some authenticated routes have custom rate limits. These also reset every ten seconds. Any service or personal access tokens hitting the same route share this limit, so exceeding the limit with one access token may impact other tokens. Calls that are subject to route-level rate limits return the headers below:  | Header name                   | Description                                                                                           | | ----------------------------- | ----------------------------------------------------------------------------------------------------- | | `X-Ratelimit-Route-Remaining` | The maximum number of requests to the current route the account is permitted to make per ten seconds. | | `X-Ratelimit-Reset`           | The time at which the current rate limit window resets in epoch milliseconds.                         |  A _route_ represents a specific URL pattern and verb. For example, the [Delete environment](https://launchdarkly.com/docs/api/environments/delete-environment) endpoint is considered a single route, and each call to delete an environment counts against your route-level rate limit for that route.  We do not publicly document the specific number of calls that an account can make to each endpoint per ten seconds. These limits may change, and we encourage clients to program against the specification, relying on the two headers defined above, rather than hardcoding to the current limits.  ### IP-based rate limiting  We also employ IP-based rate limiting on some API routes. If you hit an IP-based rate limit, your API response will include a `Retry-After` header indicating how long to wait before re-trying the call. Clients must wait at least `Retry-After` seconds before making additional calls to our API, and should employ jitter and backoff strategies to avoid triggering rate limits again.  ## OpenAPI (Swagger) and client libraries  We have a [complete OpenAPI (Swagger) specification](https://app.launchdarkly.com/api/v2/openapi.json) for our API.  We auto-generate multiple client libraries based on our OpenAPI specification. To learn more, visit the [collection of client libraries on GitHub](https://github.com/search?q=topic%3Alaunchdarkly-api+org%3Alaunchdarkly&type=Repositories). You can also use this specification to generate client libraries to interact with our REST API in your language of choice.  Our OpenAPI specification is supported by several API-based tools such as Postman and Insomnia. In many cases, you can directly import our specification to explore our APIs.  ## Method overriding  Some firewalls and HTTP clients restrict the use of verbs other than `GET` and `POST`. In those environments, our API endpoints that use `DELETE`, `PATCH`, and `PUT` verbs are inaccessible.  To avoid this issue, our API supports the `X-HTTP-Method-Override` header, allowing clients to \"tunnel\" `DELETE`, `PATCH`, and `PUT` requests using a `POST` request.  For example, to call a `PATCH` endpoint using a `POST` request, you can include `X-HTTP-Method-Override:PATCH` as a header.  ## Beta resources  We sometimes release new API resources in **beta** status before we release them with general availability.  Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.  We try to promote resources into general availability as quickly as possible. This happens after sufficient testing and when we're satisfied that we no longer need to make backwards-incompatible changes.  We mark beta resources with a \"Beta\" callout in our documentation, pictured below:  > ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](https://launchdarkly.com/docs/api#beta-resources). > > Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.  ### Using beta resources  To use a beta resource, you must include a header in the request. If you call a beta resource without this header, you receive a `403` response.  Use this header:  ``` LD-API-Version: beta ```  ## Federal and EU environments  In addition to the commercial versions, LaunchDarkly offers instances for federal agencies and those based in the European Union (EU).  ### Federal environments  The version of LaunchDarkly that is available on domains controlled by the United States government is different from the version of LaunchDarkly available to the general public. If you are an employee or contractor for a United States federal agency and use LaunchDarkly in your work, you likely use the federal instance of LaunchDarkly.  If you are working in the federal instance of LaunchDarkly, the base URI for each request is `https://app.launchdarkly.us`.  To learn more, read [LaunchDarkly in federal environments](https://launchdarkly.com/docs/home/infrastructure/federal).  ### EU environments  The version of LaunchDarkly that is available in the EU is different from the version of LaunchDarkly available to other regions. If you are based in the EU, you likely use the EU instance of LaunchDarkly. The LaunchDarkly EU instance complies with EU data residency principles, including the protection and confidentiality of EU customer information.  If you are working in the EU instance of LaunchDarkly, the base URI for each request is `https://app.eu.launchdarkly.com`.  To learn more, read [LaunchDarkly in the European Union (EU)](https://launchdarkly.com/docs/home/infrastructure/eu).  ## Versioning  We try hard to keep our REST API backwards compatible, but we occasionally have to make backwards-incompatible changes in the process of shipping new features. These breaking changes can cause unexpected behavior if you don't prepare for them accordingly.  Updates to our REST API include support for the latest features in LaunchDarkly. We also release a new version of our REST API every time we make a breaking change. We provide simultaneous support for multiple API versions so you can migrate from your current API version to a new version at your own pace.  ### Setting the API version per request  You can set the API version on a specific request by sending an `LD-API-Version` header, as shown in the example below:  ``` LD-API-Version: 20240415 ```  The header value is the version number of the API version you would like to request. The number for each version corresponds to the date the version was released in `yyyymmdd` format. In the example above the version `20240415` corresponds to April 15, 2024.  ### Setting the API version per access token  When you create an access token, you must specify a specific version of the API to use. This ensures that integrations using this token cannot be broken by version changes.  Tokens created before versioning was released have their version set to `20160426`, which is the version of the API that existed before the current versioning scheme, so that they continue working the same way they did before versioning.  If you would like to upgrade your integration to use a new API version, you can explicitly set the header described above.  > ### Best practice: Set the header for every client or integration > > We recommend that you set the API version header explicitly in any client or integration you build. > > Only rely on the access token API version during manual testing.  ### API version changelog  <table>   <tr>     <th>Version</th>     <th>Changes</th>     <th>End of life (EOL)</th>   </tr>   <tr>     <td>`20240415`</td>     <td>       <ul><li>Changed several endpoints from unpaginated to paginated. Use the `limit` and `offset` query parameters to page through the results.</li> <li>Changed the [list access tokens](https://launchdarkly.com/docs/api/access-tokens/get-tokens) endpoint: <ul><li>Response is now paginated with a default limit of `25`</li></ul></li> <li>Changed the [list account members](https://launchdarkly.com/docs/api/account-members/get-members) endpoint: <ul><li>The `accessCheck` filter is no longer available</li></ul></li> <li>Changed the [list custom roles](https://launchdarkly.com/docs/api/custom-roles/get-custom-roles) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li></ul></li> <li>Changed the [list feature flags](https://launchdarkly.com/docs/api/feature-flags/get-feature-flags) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li><li>The `environments` field is now only returned if the request is filtered by environment, using the `filterEnv` query parameter</li><li>The `followerId`, `hasDataExport`, `status`, `contextKindTargeted`, and `segmentTargeted` filters are no longer available</li><li>The `compare` query parameter is no longer available</li></ul></li> <li>Changed the [list segments](https://launchdarkly.com/docs/api/segments/get-segments) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li></ul></li> <li>Changed the [list teams](https://launchdarkly.com/docs/api/teams/get-teams) endpoint: <ul><li>The `expand` parameter no longer supports including `projects` or `roles`</li><li>In paginated results, the maximum page size is now 100</li></ul></li> <li>Changed the [get workflows](https://launchdarkly.com/docs/api/workflows/get-workflows) endpoint: <ul><li>Response is now paginated with a default limit of `20`</li><li>The `_conflicts` field in the response is no longer available</li></ul></li> </ul>     </td>     <td>Current</td>   </tr>   <tr>     <td>`20220603`</td>     <td>       <ul><li>Changed the [list projects](https://launchdarkly.com/docs/api/projects/get-projects) return value:<ul><li>Response is now paginated with a default limit of `20`.</li><li>Added support for filter and sort.</li><li>The project `environments` field is now expandable. This field is omitted by default.</li></ul></li><li>Changed the [get project](https://launchdarkly.com/docs/api/projects/get-project) return value:<ul><li>The `environments` field is now expandable. This field is omitted by default.</li></ul></li></ul>     </td>     <td>2025-04-15</td>   </tr>   <tr>     <td>`20210729`</td>     <td>       <ul><li>Changed the [create approval request](https://launchdarkly.com/docs/api/approvals/post-approval-request) return value. It now returns HTTP Status Code `201` instead of `200`.</li><li> Changed the [get user](https://launchdarkly.com/docs/api/users/get-user) return value. It now returns a user record, not a user. </li><li>Added additional optional fields to environment, segments, flags, members, and segments, including the ability to create big segments. </li><li> Added default values for flag variations when new environments are created. </li><li>Added filtering and pagination for getting flags and members, including `limit`, `number`, `filter`, and `sort` query parameters. </li><li>Added endpoints for expiring user targets for flags and segments, scheduled changes, access tokens, Relay Proxy configuration, integrations and subscriptions, and approvals. </li></ul>     </td>     <td>2023-06-03</td>   </tr>   <tr>     <td>`20191212`</td>     <td>       <ul><li>[List feature flags](https://launchdarkly.com/docs/api/feature-flags/get-feature-flags) now defaults to sending summaries of feature flag configurations, equivalent to setting the query parameter `summary=true`. Summaries omit flag targeting rules and individual user targets from the payload. </li><li> Added endpoints for flags, flag status, projects, environments, audit logs, members, users, custom roles, segments, usage, streams, events, and data export. </li></ul>     </td>     <td>2022-07-29</td>   </tr>   <tr>     <td>`20160426`</td>     <td>       <ul><li>Initial versioning of API. Tokens created before versioning have their version set to this.</li></ul>     </td>     <td>2020-12-12</td>   </tr> </table>  To learn more about how EOL is determined, read LaunchDarkly's [End of Life (EOL) Policy](https://launchdarkly.com/policies/end-of-life-policy/). 

    The version of the OpenAPI document: 2.0
    Contact: support@launchdarkly.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "20.0.0"

# Define package exports
__all__ = [
    "AIConfigsBetaApi",
    "AccessTokensApi",
    "AccountMembersApi",
    "AccountUsageBetaApi",
    "AnnouncementsApi",
    "ApplicationsBetaApi",
    "ApprovalsApi",
    "ApprovalsBetaApi",
    "AuditLogApi",
    "CodeReferencesApi",
    "ContextSettingsApi",
    "ContextsApi",
    "CustomRolesApi",
    "DataExportDestinationsApi",
    "EnvironmentsApi",
    "ExperimentsApi",
    "FeatureFlagsApi",
    "FeatureFlagsBetaApi",
    "FlagImportConfigurationsBetaApi",
    "FlagLinksBetaApi",
    "FlagTriggersApi",
    "FollowFlagsApi",
    "HoldoutsBetaApi",
    "InsightsChartsBetaApi",
    "InsightsDeploymentsBetaApi",
    "InsightsFlagEventsBetaApi",
    "InsightsPullRequestsBetaApi",
    "InsightsRepositoriesBetaApi",
    "InsightsScoresBetaApi",
    "IntegrationAuditLogSubscriptionsApi",
    "IntegrationDeliveryConfigurationsBetaApi",
    "IntegrationsBetaApi",
    "LayersApi",
    "MetricsApi",
    "MetricsBetaApi",
    "OAuth2ClientsApi",
    "OtherApi",
    "PersistentStoreIntegrationsBetaApi",
    "ProjectsApi",
    "RelayProxyConfigurationsApi",
    "ReleasePipelinesBetaApi",
    "ReleasePoliciesBetaApi",
    "ReleasesBetaApi",
    "ScheduledChangesApi",
    "SegmentsApi",
    "TagsApi",
    "TeamsApi",
    "TeamsBetaApi",
    "UserSettingsApi",
    "UsersApi",
    "UsersBetaApi",
    "ViewsBetaApi",
    "WebhooksApi",
    "WorkflowTemplatesApi",
    "WorkflowsApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "AIConfig",
    "AIConfigMaintainer",
    "AIConfigPatch",
    "AIConfigPost",
    "AIConfigRep",
    "AIConfigTargeting",
    "AIConfigTargetingDefaults",
    "AIConfigTargetingEnvironment",
    "AIConfigTargetingEnvironmentFallthrough",
    "AIConfigTargetingEnvironmentFallthroughRollout",
    "AIConfigTargetingEnvironmentFallthroughRolloutExperimentationAllocation",
    "AIConfigTargetingEnvironmentFallthroughRolloutVariation",
    "AIConfigTargetingEnvironmentRule",
    "AIConfigTargetingEnvironmentRuleClause",
    "AIConfigTargetingEnvironmentTarget",
    "AIConfigTargetingPatch",
    "AIConfigTargetingVariation",
    "AIConfigTargetingVariationValue",
    "AIConfigVariation",
    "AIConfigVariationPatch",
    "AIConfigVariationPost",
    "AIConfigVariationsResponse",
    "AIConfigs",
    "AIConfigsSummary",
    "AITool",
    "AIToolPatch",
    "AIToolPost",
    "AITools",
    "Access",
    "AccessAllowedReason",
    "AccessAllowedRep",
    "AccessDenied",
    "AccessDeniedReason",
    "AccessTokenPost",
    "ActionInput",
    "ActionOutput",
    "AgentGraph",
    "AgentGraphEdge",
    "AgentGraphEdgePost",
    "AgentGraphPatch",
    "AgentGraphPost",
    "AgentGraphs",
    "AiConfigsAccess",
    "AiConfigsAccessAllowedReason",
    "AiConfigsAccessAllowedRep",
    "AiConfigsAccessDenied",
    "AiConfigsAccessDeniedReason",
    "AiConfigsExperimentEnabledPeriodRep",
    "AiConfigsExperimentEnvironmentSettingRep",
    "AiConfigsExperimentInfoRep",
    "AiConfigsFilter",
    "AiConfigsLegacyExperimentRep",
    "AiConfigsLink",
    "AiConfigsMaintainerTeam",
    "AiConfigsMemberSummary",
    "AiConfigsMetricDataSourceRefRep",
    "AiConfigsMetricEventDefaultRep",
    "AiConfigsMetricListingRep",
    "AiConfigsModification",
    "AnnouncementAccess",
    "AnnouncementAccessAllowedReason",
    "AnnouncementAccessAllowedRep",
    "AnnouncementAccessDenied",
    "AnnouncementAccessDeniedReason",
    "AnnouncementAccessRep",
    "AnnouncementLink",
    "AnnouncementPaginatedLinks",
    "AnnouncementPatchOperation",
    "AnnouncementResponse",
    "AnnouncementResponseLinks",
    "ApplicationCollectionRep",
    "ApplicationFlagCollectionRep",
    "ApplicationRep",
    "ApplicationVersionRep",
    "ApplicationVersionsCollectionRep",
    "ApprovalRequestResponse",
    "ApprovalRequestSetting",
    "ApprovalRequestSettingWithEnvs",
    "ApprovalRequestSettingsPatch",
    "ApprovalSettings",
    "ApprovalsCapabilityConfig",
    "AssignedToRep",
    "Audience",
    "AudienceConfiguration",
    "AudiencePost",
    "AuditLogEntryListingRep",
    "AuditLogEntryListingRepCollection",
    "AuditLogEntryRep",
    "AuditLogEventsHookCapabilityConfigPost",
    "AuditLogEventsHookCapabilityConfigRep",
    "AuthorizedAppDataRep",
    "BigSegmentStoreIntegration",
    "BigSegmentStoreIntegrationCollection",
    "BigSegmentStoreIntegrationCollectionLinks",
    "BigSegmentStoreIntegrationLinks",
    "BigSegmentStoreStatus",
    "BigSegmentTarget",
    "BooleanDefaults",
    "BooleanFlagDefaults",
    "BranchCollectionRep",
    "BranchRep",
    "BulkEditMembersRep",
    "BulkEditTeamsRep",
    "CallerIdentityRep",
    "CapabilityConfigPost",
    "CapabilityConfigRep",
    "Clause",
    "Client",
    "ClientCollection",
    "ClientSideAvailability",
    "ClientSideAvailabilityPost",
    "CompletedBy",
    "ConditionInput",
    "ConditionOutput",
    "Conflict",
    "ConflictOutput",
    "ContextAttributeName",
    "ContextAttributeNames",
    "ContextAttributeNamesCollection",
    "ContextAttributeValue",
    "ContextAttributeValues",
    "ContextAttributeValuesCollection",
    "ContextInstanceEvaluation",
    "ContextInstanceEvaluationReason",
    "ContextInstanceEvaluations",
    "ContextInstanceRecord",
    "ContextInstanceSearch",
    "ContextInstanceSegmentMembership",
    "ContextInstanceSegmentMemberships",
    "ContextInstances",
    "ContextKindRep",
    "ContextKindsCollectionRep",
    "ContextRecord",
    "ContextSearch",
    "Contexts",
    "CopiedFromEnv",
    "CoreLink",
    "CreateAnnouncementBody",
    "CreateApprovalRequestRequest",
    "CreateCopyFlagConfigApprovalRequestRequest",
    "CreateFlagConfigApprovalRequestRequest",
    "CreatePhaseInput",
    "CreateReleaseInput",
    "CreateReleasePipelineInput",
    "CreateWorkflowTemplateInput",
    "CustomProperty",
    "CustomRole",
    "CustomRolePost",
    "CustomRoles",
    "CustomWorkflowInput",
    "CustomWorkflowMeta",
    "CustomWorkflowOutput",
    "CustomWorkflowStageMeta",
    "CustomWorkflowsListingOutput",
    "DefaultClientSideAvailability",
    "DefaultClientSideAvailabilityPost",
    "Defaults",
    "DependentExperimentRep",
    "DependentFlag",
    "DependentFlagEnvironment",
    "DependentFlagsByEnvironment",
    "DependentMeasuredRolloutRep",
    "DependentMetricGroupRep",
    "DependentMetricGroupRepWithMetrics",
    "DependentMetricOrMetricGroupRep",
    "DeploymentCollectionRep",
    "DeploymentRep",
    "Destination",
    "DestinationPost",
    "Destinations",
    "DynamicOptions",
    "DynamicOptionsParser",
    "Endpoint",
    "Environment",
    "EnvironmentPost",
    "EnvironmentSummary",
    "Environments",
    "Error",
    "EvaluationReason",
    "EvaluationsSummary",
    "EventFilter",
    "ExecutionOutput",
    "ExpandableApprovalRequestResponse",
    "ExpandableApprovalRequestsResponse",
    "ExpandedAIConfig",
    "ExpandedDirectlyLinkedFlag",
    "ExpandedDirectlyLinkedFlags",
    "ExpandedDirectlyLinkedSegment",
    "ExpandedDirectlyLinkedSegments",
    "ExpandedFlag",
    "ExpandedFlagRep",
    "ExpandedLinkedAIConfigs",
    "ExpandedLinkedFlags",
    "ExpandedLinkedMetrics",
    "ExpandedLinkedResources",
    "ExpandedLinkedResourcesAIConfigs",
    "ExpandedLinkedResourcesFlags",
    "ExpandedLinkedResourcesItems",
    "ExpandedLinkedResourcesMetrics",
    "ExpandedLinkedResourcesSegments",
    "ExpandedLinkedSegments",
    "ExpandedMetric",
    "ExpandedResourceRep",
    "ExpandedSegment",
    "Experiment",
    "ExperimentAllocationRep",
    "ExperimentCollectionRep",
    "ExperimentEnabledPeriodRep",
    "ExperimentEnvironmentSettingRep",
    "ExperimentInfoRep",
    "ExperimentPatchInput",
    "ExperimentPost",
    "ExpiringTarget",
    "ExpiringTargetError",
    "ExpiringTargetGetResponse",
    "ExpiringTargetPatchResponse",
    "ExpiringUserTargetGetResponse",
    "ExpiringUserTargetItem",
    "ExpiringUserTargetPatchResponse",
    "Export",
    "Extinction",
    "ExtinctionCollectionRep",
    "FailedResourceLink",
    "FailureReasonRep",
    "FeatureFlag",
    "FeatureFlagBody",
    "FeatureFlagConfig",
    "FeatureFlagScheduledChange",
    "FeatureFlagScheduledChanges",
    "FeatureFlagStatus",
    "FeatureFlagStatusAcrossEnvironments",
    "FeatureFlagStatuses",
    "FeatureFlags",
    "FileRep",
    "Filter",
    "FlagConfigApprovalRequestResponse",
    "FlagConfigApprovalRequestsResponse",
    "FlagConfigEvaluation",
    "FlagConfigMigrationSettingsRep",
    "FlagCopyConfigEnvironment",
    "FlagCopyConfigPost",
    "FlagDefaultsRep",
    "FlagEventCollectionRep",
    "FlagEventExperiment",
    "FlagEventExperimentCollection",
    "FlagEventExperimentIteration",
    "FlagEventImpactRep",
    "FlagEventMemberRep",
    "FlagEventRep",
    "FlagFollowersByProjEnvGetRep",
    "FlagFollowersGetRep",
    "FlagImportConfigurationPost",
    "FlagImportIntegration",
    "FlagImportIntegrationCollection",
    "FlagImportIntegrationCollectionLinks",
    "FlagImportIntegrationLinks",
    "FlagImportStatus",
    "FlagInput",
    "FlagLinkCollectionRep",
    "FlagLinkMember",
    "FlagLinkPost",
    "FlagLinkRep",
    "FlagListingRep",
    "FlagMigrationSettingsRep",
    "FlagPrerequisitePost",
    "FlagReferenceCollectionRep",
    "FlagReferenceRep",
    "FlagRep",
    "FlagScheduledChangesInput",
    "FlagSempatch",
    "FlagStatusRep",
    "FlagSummary",
    "FlagTriggerInput",
    "FlagsSummary",
    "FollowFlagMember",
    "FollowersPerFlag",
    "ForbiddenErrorRep",
    "FormVariable",
    "GenerateTrustPolicyPostRep",
    "GenerateWarehouseDestinationKeyPairPostRep",
    "GetAnnouncementsPublic200Response",
    "GuardedReleaseConfig",
    "HMACSignature",
    "HeaderItems",
    "HoldoutDetailRep",
    "HoldoutPatchInput",
    "HoldoutPostRequest",
    "HoldoutRep",
    "HoldoutsCollectionRep",
    "HunkRep",
    "InitiatorRep",
    "InsightGroup",
    "InsightGroupCollection",
    "InsightGroupCollectionMetadata",
    "InsightGroupCollectionScoreMetadata",
    "InsightGroupScores",
    "InsightGroupsCountByIndicator",
    "InsightPeriod",
    "InsightScores",
    "InsightsChart",
    "InsightsChartBounds",
    "InsightsChartMetadata",
    "InsightsChartMetric",
    "InsightsChartSeries",
    "InsightsChartSeriesDataPoint",
    "InsightsChartSeriesMetadata",
    "InsightsChartSeriesMetadataAxis",
    "InsightsMetricIndicatorRange",
    "InsightsMetricScore",
    "InsightsMetricTierDefinition",
    "InsightsRepository",
    "InsightsRepositoryCollection",
    "InsightsRepositoryProject",
    "InsightsRepositoryProjectCollection",
    "InsightsRepositoryProjectMappings",
    "InstructionUserRequest",
    "Integration",
    "IntegrationConfigurationCollectionRep",
    "IntegrationConfigurationPost",
    "IntegrationConfigurationsRep",
    "IntegrationDeliveryConfiguration",
    "IntegrationDeliveryConfigurationCollection",
    "IntegrationDeliveryConfigurationCollectionLinks",
    "IntegrationDeliveryConfigurationLinks",
    "IntegrationDeliveryConfigurationPost",
    "IntegrationDeliveryConfigurationResponse",
    "IntegrationMetadata",
    "IntegrationStatus",
    "IntegrationStatusRep",
    "IntegrationSubscriptionStatusRep",
    "Integrations",
    "InvalidRequestErrorRep",
    "IpList",
    "IterationInput",
    "IterationRep",
    "JudgeAttachment",
    "JudgeConfiguration",
    "LastSeenMetadata",
    "LayerCollectionRep",
    "LayerConfigurationRep",
    "LayerPatchInput",
    "LayerPost",
    "LayerRep",
    "LayerReservationRep",
    "LayerSnapshotRep",
    "LeadTimeStagesRep",
    "LegacyExperimentRep",
    "Link",
    "LinkResourceSuccessResponse",
    "Maintainer",
    "MaintainerMember",
    "MaintainerRep",
    "MaintainerTeam",
    "Member",
    "MemberDataRep",
    "MemberImportItem",
    "MemberPermissionGrantSummaryRep",
    "MemberSummary",
    "MemberTeamSummaryRep",
    "MemberTeamsPostInput",
    "Members",
    "MembersPatchInput",
    "Message",
    "MethodNotAllowedErrorRep",
    "MetricByVariation",
    "MetricCollectionRep",
    "MetricDataSourceRefRep",
    "MetricEventDefaultRep",
    "MetricGroupCollectionRep",
    "MetricGroupPost",
    "MetricGroupRep",
    "MetricInGroupRep",
    "MetricInMetricGroupInput",
    "MetricInput",
    "MetricListingRep",
    "MetricPost",
    "MetricRep",
    "MetricV2Rep",
    "Metrics",
    "MetricsSummary",
    "MigrationSafetyIssueRep",
    "MigrationSettingsPost",
    "ModelConfig",
    "ModelConfigPost",
    "ModelImport",
    "Modification",
    "MultiEnvironmentDependentFlag",
    "MultiEnvironmentDependentFlags",
    "NamingConvention",
    "NewMemberForm",
    "NotFoundErrorRep",
    "OauthClientPost",
    "OptionsArray",
    "PaginatedLinks",
    "ParameterDefault",
    "ParameterRep",
    "ParentAndSelfLinks",
    "ParentLink",
    "ParentResourceRep",
    "PatchFailedErrorRep",
    "PatchFlagsRequest",
    "PatchOperation",
    "PatchSegmentExpiringTargetInputRep",
    "PatchSegmentExpiringTargetInstruction",
    "PatchSegmentInstruction",
    "PatchSegmentRequest",
    "PatchUsersRequest",
    "PatchWithComment",
    "PermissionGrantInput",
    "Phase",
    "PhaseInfo",
    "PostApprovalRequestApplyRequest",
    "PostApprovalRequestReviewRequest",
    "PostDeploymentEventInput",
    "PostFlagScheduledChangesInput",
    "PostInsightGroupParams",
    "PostReleasePolicyRequest",
    "Prerequisite",
    "ProgressiveReleaseConfig",
    "Project",
    "ProjectPost",
    "ProjectRep",
    "ProjectSummary",
    "ProjectSummaryCollection",
    "Projects",
    "PullRequestCollectionRep",
    "PullRequestLeadTimeRep",
    "PullRequestRep",
    "PutBranch",
    "PutReleasePolicyRequest",
    "RandomizationSettingsPut",
    "RandomizationSettingsRep",
    "RandomizationUnitInput",
    "RandomizationUnitRep",
    "RateLimitedErrorRep",
    "RecentTriggerBody",
    "ReferenceRep",
    "RelatedExperimentRep",
    "RelayAutoConfigCollectionRep",
    "RelayAutoConfigPost",
    "RelayAutoConfigRep",
    "Release",
    "ReleaseAudience",
    "ReleaseGuardianConfiguration",
    "ReleaseGuardianConfigurationInput",
    "ReleaseMethod",
    "ReleasePhase",
    "ReleasePipeline",
    "ReleasePipelineCollection",
    "ReleasePoliciesAccess",
    "ReleasePoliciesAccessAllowedReason",
    "ReleasePoliciesAccessAllowedRep",
    "ReleasePoliciesAccessDenied",
    "ReleasePoliciesAccessDeniedReason",
    "ReleasePoliciesAccessRep",
    "ReleasePoliciesResponse",
    "ReleasePolicy",
    "ReleasePolicyScope",
    "ReleasePolicyStage",
    "ReleaseProgression",
    "ReleaseProgressionCollection",
    "ReleaserAudienceConfigInput",
    "RepositoryCollectionRep",
    "RepositoryPost",
    "RepositoryRep",
    "ResourceAccess",
    "ResourceIDResponse",
    "ResourceId",
    "ResourceSummary",
    "RestrictedModelError",
    "RestrictedModelsRequest",
    "RestrictedModelsResponse",
    "ReviewOutput",
    "ReviewResponse",
    "Rollout",
    "RootResponse",
    "Rule",
    "RuleClause",
    "SdkListRep",
    "SdkVersionListRep",
    "SdkVersionRep",
    "SegmentBody",
    "SegmentMetadata",
    "SegmentTarget",
    "SegmentUserList",
    "SegmentUserState",
    "SegmentsSummary",
    "SeriesListRep",
    "SeriesListRepFloat",
    "SimpleHoldoutRep",
    "SourceEnv",
    "SourceFlag",
    "StageInput",
    "StageOutput",
    "Statement",
    "StatementPost",
    "StatisticCollectionRep",
    "StatisticRep",
    "StatisticsRoot",
    "StatusConflictErrorRep",
    "StatusResponse",
    "StatusServiceUnavailable",
    "StoreIntegrationError",
    "SubjectDataRep",
    "SubscriptionPost",
    "TagsCollection",
    "TagsLink",
    "Target",
    "TargetResourceRep",
    "Team",
    "TeamCustomRole",
    "TeamCustomRoles",
    "TeamImportsRep",
    "TeamMaintainers",
    "TeamMembers",
    "TeamPatchInput",
    "TeamPostInput",
    "TeamProjects",
    "Teams",
    "TeamsPatchInput",
    "TimestampRep",
    "Token",
    "TokenSummary",
    "Tokens",
    "TreatmentInput",
    "TreatmentParameterInput",
    "TreatmentRep",
    "TriggerPost",
    "TriggerWorkflowCollectionRep",
    "TriggerWorkflowRep",
    "TrustPolicyDetails",
    "TrustPolicyStatement",
    "UnauthorizedErrorRep",
    "UnlinkResourceSuccessResponse",
    "UpdatePhaseStatusInput",
    "UpdateReleasePipelineInput",
    "UpsertContextKindPayload",
    "UpsertFlagDefaultsPayload",
    "UpsertPayloadRep",
    "UpsertResponseRep",
    "UrlPost",
    "User",
    "UserAttributeNamesRep",
    "UserFlagSetting",
    "UserFlagSettings",
    "UserRecord",
    "UserSegment",
    "UserSegmentRule",
    "UserSegments",
    "Users",
    "UsersRep",
    "ValidationFailedErrorRep",
    "ValuePut",
    "Variation",
    "VariationEvalSummary",
    "VariationOrRolloutRep",
    "VariationSummary",
    "VariationTool",
    "VariationToolPost",
    "VersionsRep",
    "View",
    "ViewLinkRequest",
    "ViewLinkRequestKeys",
    "ViewLinkRequestSegmentIdentifier",
    "ViewLinkRequestSegmentIdentifiers",
    "ViewLinkedResource",
    "ViewLinkedResourceDetails",
    "ViewLinkedResources",
    "ViewPatch",
    "ViewPost",
    "Views",
    "ViewsAccess",
    "ViewsAccessAllowedReason",
    "ViewsAccessAllowedRep",
    "ViewsAccessDenied",
    "ViewsAccessDeniedReason",
    "ViewsAccessRep",
    "ViewsLink",
    "ViewsMaintainerMember",
    "ViewsMaintainerTeam",
    "ViewsPaginatedLinks",
    "ViewsSelfLink",
    "Webhook",
    "WebhookPost",
    "Webhooks",
    "WeightedVariation",
    "WorkflowTemplateMetadata",
    "WorkflowTemplateOutput",
    "WorkflowTemplateParameter",
    "WorkflowTemplatesListingOutputRep",
]

# import apis into sdk package
from launchdarkly_api.api.ai_configs_beta_api import AIConfigsBetaApi as AIConfigsBetaApi
from launchdarkly_api.api.access_tokens_api import AccessTokensApi as AccessTokensApi
from launchdarkly_api.api.account_members_api import AccountMembersApi as AccountMembersApi
from launchdarkly_api.api.account_usage_beta_api import AccountUsageBetaApi as AccountUsageBetaApi
from launchdarkly_api.api.announcements_api import AnnouncementsApi as AnnouncementsApi
from launchdarkly_api.api.applications_beta_api import ApplicationsBetaApi as ApplicationsBetaApi
from launchdarkly_api.api.approvals_api import ApprovalsApi as ApprovalsApi
from launchdarkly_api.api.approvals_beta_api import ApprovalsBetaApi as ApprovalsBetaApi
from launchdarkly_api.api.audit_log_api import AuditLogApi as AuditLogApi
from launchdarkly_api.api.code_references_api import CodeReferencesApi as CodeReferencesApi
from launchdarkly_api.api.context_settings_api import ContextSettingsApi as ContextSettingsApi
from launchdarkly_api.api.contexts_api import ContextsApi as ContextsApi
from launchdarkly_api.api.custom_roles_api import CustomRolesApi as CustomRolesApi
from launchdarkly_api.api.data_export_destinations_api import DataExportDestinationsApi as DataExportDestinationsApi
from launchdarkly_api.api.environments_api import EnvironmentsApi as EnvironmentsApi
from launchdarkly_api.api.experiments_api import ExperimentsApi as ExperimentsApi
from launchdarkly_api.api.feature_flags_api import FeatureFlagsApi as FeatureFlagsApi
from launchdarkly_api.api.feature_flags_beta_api import FeatureFlagsBetaApi as FeatureFlagsBetaApi
from launchdarkly_api.api.flag_import_configurations_beta_api import FlagImportConfigurationsBetaApi as FlagImportConfigurationsBetaApi
from launchdarkly_api.api.flag_links_beta_api import FlagLinksBetaApi as FlagLinksBetaApi
from launchdarkly_api.api.flag_triggers_api import FlagTriggersApi as FlagTriggersApi
from launchdarkly_api.api.follow_flags_api import FollowFlagsApi as FollowFlagsApi
from launchdarkly_api.api.holdouts_beta_api import HoldoutsBetaApi as HoldoutsBetaApi
from launchdarkly_api.api.insights_charts_beta_api import InsightsChartsBetaApi as InsightsChartsBetaApi
from launchdarkly_api.api.insights_deployments_beta_api import InsightsDeploymentsBetaApi as InsightsDeploymentsBetaApi
from launchdarkly_api.api.insights_flag_events_beta_api import InsightsFlagEventsBetaApi as InsightsFlagEventsBetaApi
from launchdarkly_api.api.insights_pull_requests_beta_api import InsightsPullRequestsBetaApi as InsightsPullRequestsBetaApi
from launchdarkly_api.api.insights_repositories_beta_api import InsightsRepositoriesBetaApi as InsightsRepositoriesBetaApi
from launchdarkly_api.api.insights_scores_beta_api import InsightsScoresBetaApi as InsightsScoresBetaApi
from launchdarkly_api.api.integration_audit_log_subscriptions_api import IntegrationAuditLogSubscriptionsApi as IntegrationAuditLogSubscriptionsApi
from launchdarkly_api.api.integration_delivery_configurations_beta_api import IntegrationDeliveryConfigurationsBetaApi as IntegrationDeliveryConfigurationsBetaApi
from launchdarkly_api.api.integrations_beta_api import IntegrationsBetaApi as IntegrationsBetaApi
from launchdarkly_api.api.layers_api import LayersApi as LayersApi
from launchdarkly_api.api.metrics_api import MetricsApi as MetricsApi
from launchdarkly_api.api.metrics_beta_api import MetricsBetaApi as MetricsBetaApi
from launchdarkly_api.api.o_auth2_clients_api import OAuth2ClientsApi as OAuth2ClientsApi
from launchdarkly_api.api.other_api import OtherApi as OtherApi
from launchdarkly_api.api.persistent_store_integrations_beta_api import PersistentStoreIntegrationsBetaApi as PersistentStoreIntegrationsBetaApi
from launchdarkly_api.api.projects_api import ProjectsApi as ProjectsApi
from launchdarkly_api.api.relay_proxy_configurations_api import RelayProxyConfigurationsApi as RelayProxyConfigurationsApi
from launchdarkly_api.api.release_pipelines_beta_api import ReleasePipelinesBetaApi as ReleasePipelinesBetaApi
from launchdarkly_api.api.release_policies_beta_api import ReleasePoliciesBetaApi as ReleasePoliciesBetaApi
from launchdarkly_api.api.releases_beta_api import ReleasesBetaApi as ReleasesBetaApi
from launchdarkly_api.api.scheduled_changes_api import ScheduledChangesApi as ScheduledChangesApi
from launchdarkly_api.api.segments_api import SegmentsApi as SegmentsApi
from launchdarkly_api.api.tags_api import TagsApi as TagsApi
from launchdarkly_api.api.teams_api import TeamsApi as TeamsApi
from launchdarkly_api.api.teams_beta_api import TeamsBetaApi as TeamsBetaApi
from launchdarkly_api.api.user_settings_api import UserSettingsApi as UserSettingsApi
from launchdarkly_api.api.users_api import UsersApi as UsersApi
from launchdarkly_api.api.users_beta_api import UsersBetaApi as UsersBetaApi
from launchdarkly_api.api.views_beta_api import ViewsBetaApi as ViewsBetaApi
from launchdarkly_api.api.webhooks_api import WebhooksApi as WebhooksApi
from launchdarkly_api.api.workflow_templates_api import WorkflowTemplatesApi as WorkflowTemplatesApi
from launchdarkly_api.api.workflows_api import WorkflowsApi as WorkflowsApi

# import ApiClient
from launchdarkly_api.api_response import ApiResponse as ApiResponse
from launchdarkly_api.api_client import ApiClient as ApiClient
from launchdarkly_api.configuration import Configuration as Configuration
from launchdarkly_api.exceptions import OpenApiException as OpenApiException
from launchdarkly_api.exceptions import ApiTypeError as ApiTypeError
from launchdarkly_api.exceptions import ApiValueError as ApiValueError
from launchdarkly_api.exceptions import ApiKeyError as ApiKeyError
from launchdarkly_api.exceptions import ApiAttributeError as ApiAttributeError
from launchdarkly_api.exceptions import ApiException as ApiException

# import models into sdk package
from launchdarkly_api.models.ai_config import AIConfig as AIConfig
from launchdarkly_api.models.ai_config_maintainer import AIConfigMaintainer as AIConfigMaintainer
from launchdarkly_api.models.ai_config_patch import AIConfigPatch as AIConfigPatch
from launchdarkly_api.models.ai_config_post import AIConfigPost as AIConfigPost
from launchdarkly_api.models.ai_config_rep import AIConfigRep as AIConfigRep
from launchdarkly_api.models.ai_config_targeting import AIConfigTargeting as AIConfigTargeting
from launchdarkly_api.models.ai_config_targeting_defaults import AIConfigTargetingDefaults as AIConfigTargetingDefaults
from launchdarkly_api.models.ai_config_targeting_environment import AIConfigTargetingEnvironment as AIConfigTargetingEnvironment
from launchdarkly_api.models.ai_config_targeting_environment_fallthrough import AIConfigTargetingEnvironmentFallthrough as AIConfigTargetingEnvironmentFallthrough
from launchdarkly_api.models.ai_config_targeting_environment_fallthrough_rollout import AIConfigTargetingEnvironmentFallthroughRollout as AIConfigTargetingEnvironmentFallthroughRollout
from launchdarkly_api.models.ai_config_targeting_environment_fallthrough_rollout_experimentation_allocation import AIConfigTargetingEnvironmentFallthroughRolloutExperimentationAllocation as AIConfigTargetingEnvironmentFallthroughRolloutExperimentationAllocation
from launchdarkly_api.models.ai_config_targeting_environment_fallthrough_rollout_variation import AIConfigTargetingEnvironmentFallthroughRolloutVariation as AIConfigTargetingEnvironmentFallthroughRolloutVariation
from launchdarkly_api.models.ai_config_targeting_environment_rule import AIConfigTargetingEnvironmentRule as AIConfigTargetingEnvironmentRule
from launchdarkly_api.models.ai_config_targeting_environment_rule_clause import AIConfigTargetingEnvironmentRuleClause as AIConfigTargetingEnvironmentRuleClause
from launchdarkly_api.models.ai_config_targeting_environment_target import AIConfigTargetingEnvironmentTarget as AIConfigTargetingEnvironmentTarget
from launchdarkly_api.models.ai_config_targeting_patch import AIConfigTargetingPatch as AIConfigTargetingPatch
from launchdarkly_api.models.ai_config_targeting_variation import AIConfigTargetingVariation as AIConfigTargetingVariation
from launchdarkly_api.models.ai_config_targeting_variation_value import AIConfigTargetingVariationValue as AIConfigTargetingVariationValue
from launchdarkly_api.models.ai_config_variation import AIConfigVariation as AIConfigVariation
from launchdarkly_api.models.ai_config_variation_patch import AIConfigVariationPatch as AIConfigVariationPatch
from launchdarkly_api.models.ai_config_variation_post import AIConfigVariationPost as AIConfigVariationPost
from launchdarkly_api.models.ai_config_variations_response import AIConfigVariationsResponse as AIConfigVariationsResponse
from launchdarkly_api.models.ai_configs import AIConfigs as AIConfigs
from launchdarkly_api.models.ai_configs_summary import AIConfigsSummary as AIConfigsSummary
from launchdarkly_api.models.ai_tool import AITool as AITool
from launchdarkly_api.models.ai_tool_patch import AIToolPatch as AIToolPatch
from launchdarkly_api.models.ai_tool_post import AIToolPost as AIToolPost
from launchdarkly_api.models.ai_tools import AITools as AITools
from launchdarkly_api.models.access import Access as Access
from launchdarkly_api.models.access_allowed_reason import AccessAllowedReason as AccessAllowedReason
from launchdarkly_api.models.access_allowed_rep import AccessAllowedRep as AccessAllowedRep
from launchdarkly_api.models.access_denied import AccessDenied as AccessDenied
from launchdarkly_api.models.access_denied_reason import AccessDeniedReason as AccessDeniedReason
from launchdarkly_api.models.access_token_post import AccessTokenPost as AccessTokenPost
from launchdarkly_api.models.action_input import ActionInput as ActionInput
from launchdarkly_api.models.action_output import ActionOutput as ActionOutput
from launchdarkly_api.models.agent_graph import AgentGraph as AgentGraph
from launchdarkly_api.models.agent_graph_edge import AgentGraphEdge as AgentGraphEdge
from launchdarkly_api.models.agent_graph_edge_post import AgentGraphEdgePost as AgentGraphEdgePost
from launchdarkly_api.models.agent_graph_patch import AgentGraphPatch as AgentGraphPatch
from launchdarkly_api.models.agent_graph_post import AgentGraphPost as AgentGraphPost
from launchdarkly_api.models.agent_graphs import AgentGraphs as AgentGraphs
from launchdarkly_api.models.ai_configs_access import AiConfigsAccess as AiConfigsAccess
from launchdarkly_api.models.ai_configs_access_allowed_reason import AiConfigsAccessAllowedReason as AiConfigsAccessAllowedReason
from launchdarkly_api.models.ai_configs_access_allowed_rep import AiConfigsAccessAllowedRep as AiConfigsAccessAllowedRep
from launchdarkly_api.models.ai_configs_access_denied import AiConfigsAccessDenied as AiConfigsAccessDenied
from launchdarkly_api.models.ai_configs_access_denied_reason import AiConfigsAccessDeniedReason as AiConfigsAccessDeniedReason
from launchdarkly_api.models.ai_configs_experiment_enabled_period_rep import AiConfigsExperimentEnabledPeriodRep as AiConfigsExperimentEnabledPeriodRep
from launchdarkly_api.models.ai_configs_experiment_environment_setting_rep import AiConfigsExperimentEnvironmentSettingRep as AiConfigsExperimentEnvironmentSettingRep
from launchdarkly_api.models.ai_configs_experiment_info_rep import AiConfigsExperimentInfoRep as AiConfigsExperimentInfoRep
from launchdarkly_api.models.ai_configs_filter import AiConfigsFilter as AiConfigsFilter
from launchdarkly_api.models.ai_configs_legacy_experiment_rep import AiConfigsLegacyExperimentRep as AiConfigsLegacyExperimentRep
from launchdarkly_api.models.ai_configs_link import AiConfigsLink as AiConfigsLink
from launchdarkly_api.models.ai_configs_maintainer_team import AiConfigsMaintainerTeam as AiConfigsMaintainerTeam
from launchdarkly_api.models.ai_configs_member_summary import AiConfigsMemberSummary as AiConfigsMemberSummary
from launchdarkly_api.models.ai_configs_metric_data_source_ref_rep import AiConfigsMetricDataSourceRefRep as AiConfigsMetricDataSourceRefRep
from launchdarkly_api.models.ai_configs_metric_event_default_rep import AiConfigsMetricEventDefaultRep as AiConfigsMetricEventDefaultRep
from launchdarkly_api.models.ai_configs_metric_listing_rep import AiConfigsMetricListingRep as AiConfigsMetricListingRep
from launchdarkly_api.models.ai_configs_modification import AiConfigsModification as AiConfigsModification
from launchdarkly_api.models.announcement_access import AnnouncementAccess as AnnouncementAccess
from launchdarkly_api.models.announcement_access_allowed_reason import AnnouncementAccessAllowedReason as AnnouncementAccessAllowedReason
from launchdarkly_api.models.announcement_access_allowed_rep import AnnouncementAccessAllowedRep as AnnouncementAccessAllowedRep
from launchdarkly_api.models.announcement_access_denied import AnnouncementAccessDenied as AnnouncementAccessDenied
from launchdarkly_api.models.announcement_access_denied_reason import AnnouncementAccessDeniedReason as AnnouncementAccessDeniedReason
from launchdarkly_api.models.announcement_access_rep import AnnouncementAccessRep as AnnouncementAccessRep
from launchdarkly_api.models.announcement_link import AnnouncementLink as AnnouncementLink
from launchdarkly_api.models.announcement_paginated_links import AnnouncementPaginatedLinks as AnnouncementPaginatedLinks
from launchdarkly_api.models.announcement_patch_operation import AnnouncementPatchOperation as AnnouncementPatchOperation
from launchdarkly_api.models.announcement_response import AnnouncementResponse as AnnouncementResponse
from launchdarkly_api.models.announcement_response_links import AnnouncementResponseLinks as AnnouncementResponseLinks
from launchdarkly_api.models.application_collection_rep import ApplicationCollectionRep as ApplicationCollectionRep
from launchdarkly_api.models.application_flag_collection_rep import ApplicationFlagCollectionRep as ApplicationFlagCollectionRep
from launchdarkly_api.models.application_rep import ApplicationRep as ApplicationRep
from launchdarkly_api.models.application_version_rep import ApplicationVersionRep as ApplicationVersionRep
from launchdarkly_api.models.application_versions_collection_rep import ApplicationVersionsCollectionRep as ApplicationVersionsCollectionRep
from launchdarkly_api.models.approval_request_response import ApprovalRequestResponse as ApprovalRequestResponse
from launchdarkly_api.models.approval_request_setting import ApprovalRequestSetting as ApprovalRequestSetting
from launchdarkly_api.models.approval_request_setting_with_envs import ApprovalRequestSettingWithEnvs as ApprovalRequestSettingWithEnvs
from launchdarkly_api.models.approval_request_settings_patch import ApprovalRequestSettingsPatch as ApprovalRequestSettingsPatch
from launchdarkly_api.models.approval_settings import ApprovalSettings as ApprovalSettings
from launchdarkly_api.models.approvals_capability_config import ApprovalsCapabilityConfig as ApprovalsCapabilityConfig
from launchdarkly_api.models.assigned_to_rep import AssignedToRep as AssignedToRep
from launchdarkly_api.models.audience import Audience as Audience
from launchdarkly_api.models.audience_configuration import AudienceConfiguration as AudienceConfiguration
from launchdarkly_api.models.audience_post import AudiencePost as AudiencePost
from launchdarkly_api.models.audit_log_entry_listing_rep import AuditLogEntryListingRep as AuditLogEntryListingRep
from launchdarkly_api.models.audit_log_entry_listing_rep_collection import AuditLogEntryListingRepCollection as AuditLogEntryListingRepCollection
from launchdarkly_api.models.audit_log_entry_rep import AuditLogEntryRep as AuditLogEntryRep
from launchdarkly_api.models.audit_log_events_hook_capability_config_post import AuditLogEventsHookCapabilityConfigPost as AuditLogEventsHookCapabilityConfigPost
from launchdarkly_api.models.audit_log_events_hook_capability_config_rep import AuditLogEventsHookCapabilityConfigRep as AuditLogEventsHookCapabilityConfigRep
from launchdarkly_api.models.authorized_app_data_rep import AuthorizedAppDataRep as AuthorizedAppDataRep
from launchdarkly_api.models.big_segment_store_integration import BigSegmentStoreIntegration as BigSegmentStoreIntegration
from launchdarkly_api.models.big_segment_store_integration_collection import BigSegmentStoreIntegrationCollection as BigSegmentStoreIntegrationCollection
from launchdarkly_api.models.big_segment_store_integration_collection_links import BigSegmentStoreIntegrationCollectionLinks as BigSegmentStoreIntegrationCollectionLinks
from launchdarkly_api.models.big_segment_store_integration_links import BigSegmentStoreIntegrationLinks as BigSegmentStoreIntegrationLinks
from launchdarkly_api.models.big_segment_store_status import BigSegmentStoreStatus as BigSegmentStoreStatus
from launchdarkly_api.models.big_segment_target import BigSegmentTarget as BigSegmentTarget
from launchdarkly_api.models.boolean_defaults import BooleanDefaults as BooleanDefaults
from launchdarkly_api.models.boolean_flag_defaults import BooleanFlagDefaults as BooleanFlagDefaults
from launchdarkly_api.models.branch_collection_rep import BranchCollectionRep as BranchCollectionRep
from launchdarkly_api.models.branch_rep import BranchRep as BranchRep
from launchdarkly_api.models.bulk_edit_members_rep import BulkEditMembersRep as BulkEditMembersRep
from launchdarkly_api.models.bulk_edit_teams_rep import BulkEditTeamsRep as BulkEditTeamsRep
from launchdarkly_api.models.caller_identity_rep import CallerIdentityRep as CallerIdentityRep
from launchdarkly_api.models.capability_config_post import CapabilityConfigPost as CapabilityConfigPost
from launchdarkly_api.models.capability_config_rep import CapabilityConfigRep as CapabilityConfigRep
from launchdarkly_api.models.clause import Clause as Clause
from launchdarkly_api.models.client import Client as Client
from launchdarkly_api.models.client_collection import ClientCollection as ClientCollection
from launchdarkly_api.models.client_side_availability import ClientSideAvailability as ClientSideAvailability
from launchdarkly_api.models.client_side_availability_post import ClientSideAvailabilityPost as ClientSideAvailabilityPost
from launchdarkly_api.models.completed_by import CompletedBy as CompletedBy
from launchdarkly_api.models.condition_input import ConditionInput as ConditionInput
from launchdarkly_api.models.condition_output import ConditionOutput as ConditionOutput
from launchdarkly_api.models.conflict import Conflict as Conflict
from launchdarkly_api.models.conflict_output import ConflictOutput as ConflictOutput
from launchdarkly_api.models.context_attribute_name import ContextAttributeName as ContextAttributeName
from launchdarkly_api.models.context_attribute_names import ContextAttributeNames as ContextAttributeNames
from launchdarkly_api.models.context_attribute_names_collection import ContextAttributeNamesCollection as ContextAttributeNamesCollection
from launchdarkly_api.models.context_attribute_value import ContextAttributeValue as ContextAttributeValue
from launchdarkly_api.models.context_attribute_values import ContextAttributeValues as ContextAttributeValues
from launchdarkly_api.models.context_attribute_values_collection import ContextAttributeValuesCollection as ContextAttributeValuesCollection
from launchdarkly_api.models.context_instance_evaluation import ContextInstanceEvaluation as ContextInstanceEvaluation
from launchdarkly_api.models.context_instance_evaluation_reason import ContextInstanceEvaluationReason as ContextInstanceEvaluationReason
from launchdarkly_api.models.context_instance_evaluations import ContextInstanceEvaluations as ContextInstanceEvaluations
from launchdarkly_api.models.context_instance_record import ContextInstanceRecord as ContextInstanceRecord
from launchdarkly_api.models.context_instance_search import ContextInstanceSearch as ContextInstanceSearch
from launchdarkly_api.models.context_instance_segment_membership import ContextInstanceSegmentMembership as ContextInstanceSegmentMembership
from launchdarkly_api.models.context_instance_segment_memberships import ContextInstanceSegmentMemberships as ContextInstanceSegmentMemberships
from launchdarkly_api.models.context_instances import ContextInstances as ContextInstances
from launchdarkly_api.models.context_kind_rep import ContextKindRep as ContextKindRep
from launchdarkly_api.models.context_kinds_collection_rep import ContextKindsCollectionRep as ContextKindsCollectionRep
from launchdarkly_api.models.context_record import ContextRecord as ContextRecord
from launchdarkly_api.models.context_search import ContextSearch as ContextSearch
from launchdarkly_api.models.contexts import Contexts as Contexts
from launchdarkly_api.models.copied_from_env import CopiedFromEnv as CopiedFromEnv
from launchdarkly_api.models.core_link import CoreLink as CoreLink
from launchdarkly_api.models.create_announcement_body import CreateAnnouncementBody as CreateAnnouncementBody
from launchdarkly_api.models.create_approval_request_request import CreateApprovalRequestRequest as CreateApprovalRequestRequest
from launchdarkly_api.models.create_copy_flag_config_approval_request_request import CreateCopyFlagConfigApprovalRequestRequest as CreateCopyFlagConfigApprovalRequestRequest
from launchdarkly_api.models.create_flag_config_approval_request_request import CreateFlagConfigApprovalRequestRequest as CreateFlagConfigApprovalRequestRequest
from launchdarkly_api.models.create_phase_input import CreatePhaseInput as CreatePhaseInput
from launchdarkly_api.models.create_release_input import CreateReleaseInput as CreateReleaseInput
from launchdarkly_api.models.create_release_pipeline_input import CreateReleasePipelineInput as CreateReleasePipelineInput
from launchdarkly_api.models.create_workflow_template_input import CreateWorkflowTemplateInput as CreateWorkflowTemplateInput
from launchdarkly_api.models.custom_property import CustomProperty as CustomProperty
from launchdarkly_api.models.custom_role import CustomRole as CustomRole
from launchdarkly_api.models.custom_role_post import CustomRolePost as CustomRolePost
from launchdarkly_api.models.custom_roles import CustomRoles as CustomRoles
from launchdarkly_api.models.custom_workflow_input import CustomWorkflowInput as CustomWorkflowInput
from launchdarkly_api.models.custom_workflow_meta import CustomWorkflowMeta as CustomWorkflowMeta
from launchdarkly_api.models.custom_workflow_output import CustomWorkflowOutput as CustomWorkflowOutput
from launchdarkly_api.models.custom_workflow_stage_meta import CustomWorkflowStageMeta as CustomWorkflowStageMeta
from launchdarkly_api.models.custom_workflows_listing_output import CustomWorkflowsListingOutput as CustomWorkflowsListingOutput
from launchdarkly_api.models.default_client_side_availability import DefaultClientSideAvailability as DefaultClientSideAvailability
from launchdarkly_api.models.default_client_side_availability_post import DefaultClientSideAvailabilityPost as DefaultClientSideAvailabilityPost
from launchdarkly_api.models.defaults import Defaults as Defaults
from launchdarkly_api.models.dependent_experiment_rep import DependentExperimentRep as DependentExperimentRep
from launchdarkly_api.models.dependent_flag import DependentFlag as DependentFlag
from launchdarkly_api.models.dependent_flag_environment import DependentFlagEnvironment as DependentFlagEnvironment
from launchdarkly_api.models.dependent_flags_by_environment import DependentFlagsByEnvironment as DependentFlagsByEnvironment
from launchdarkly_api.models.dependent_measured_rollout_rep import DependentMeasuredRolloutRep as DependentMeasuredRolloutRep
from launchdarkly_api.models.dependent_metric_group_rep import DependentMetricGroupRep as DependentMetricGroupRep
from launchdarkly_api.models.dependent_metric_group_rep_with_metrics import DependentMetricGroupRepWithMetrics as DependentMetricGroupRepWithMetrics
from launchdarkly_api.models.dependent_metric_or_metric_group_rep import DependentMetricOrMetricGroupRep as DependentMetricOrMetricGroupRep
from launchdarkly_api.models.deployment_collection_rep import DeploymentCollectionRep as DeploymentCollectionRep
from launchdarkly_api.models.deployment_rep import DeploymentRep as DeploymentRep
from launchdarkly_api.models.destination import Destination as Destination
from launchdarkly_api.models.destination_post import DestinationPost as DestinationPost
from launchdarkly_api.models.destinations import Destinations as Destinations
from launchdarkly_api.models.dynamic_options import DynamicOptions as DynamicOptions
from launchdarkly_api.models.dynamic_options_parser import DynamicOptionsParser as DynamicOptionsParser
from launchdarkly_api.models.endpoint import Endpoint as Endpoint
from launchdarkly_api.models.environment import Environment as Environment
from launchdarkly_api.models.environment_post import EnvironmentPost as EnvironmentPost
from launchdarkly_api.models.environment_summary import EnvironmentSummary as EnvironmentSummary
from launchdarkly_api.models.environments import Environments as Environments
from launchdarkly_api.models.error import Error as Error
from launchdarkly_api.models.evaluation_reason import EvaluationReason as EvaluationReason
from launchdarkly_api.models.evaluations_summary import EvaluationsSummary as EvaluationsSummary
from launchdarkly_api.models.event_filter import EventFilter as EventFilter
from launchdarkly_api.models.execution_output import ExecutionOutput as ExecutionOutput
from launchdarkly_api.models.expandable_approval_request_response import ExpandableApprovalRequestResponse as ExpandableApprovalRequestResponse
from launchdarkly_api.models.expandable_approval_requests_response import ExpandableApprovalRequestsResponse as ExpandableApprovalRequestsResponse
from launchdarkly_api.models.expanded_ai_config import ExpandedAIConfig as ExpandedAIConfig
from launchdarkly_api.models.expanded_directly_linked_flag import ExpandedDirectlyLinkedFlag as ExpandedDirectlyLinkedFlag
from launchdarkly_api.models.expanded_directly_linked_flags import ExpandedDirectlyLinkedFlags as ExpandedDirectlyLinkedFlags
from launchdarkly_api.models.expanded_directly_linked_segment import ExpandedDirectlyLinkedSegment as ExpandedDirectlyLinkedSegment
from launchdarkly_api.models.expanded_directly_linked_segments import ExpandedDirectlyLinkedSegments as ExpandedDirectlyLinkedSegments
from launchdarkly_api.models.expanded_flag import ExpandedFlag as ExpandedFlag
from launchdarkly_api.models.expanded_flag_rep import ExpandedFlagRep as ExpandedFlagRep
from launchdarkly_api.models.expanded_linked_ai_configs import ExpandedLinkedAIConfigs as ExpandedLinkedAIConfigs
from launchdarkly_api.models.expanded_linked_flags import ExpandedLinkedFlags as ExpandedLinkedFlags
from launchdarkly_api.models.expanded_linked_metrics import ExpandedLinkedMetrics as ExpandedLinkedMetrics
from launchdarkly_api.models.expanded_linked_resources import ExpandedLinkedResources as ExpandedLinkedResources
from launchdarkly_api.models.expanded_linked_resources_ai_configs import ExpandedLinkedResourcesAIConfigs as ExpandedLinkedResourcesAIConfigs
from launchdarkly_api.models.expanded_linked_resources_flags import ExpandedLinkedResourcesFlags as ExpandedLinkedResourcesFlags
from launchdarkly_api.models.expanded_linked_resources_items import ExpandedLinkedResourcesItems as ExpandedLinkedResourcesItems
from launchdarkly_api.models.expanded_linked_resources_metrics import ExpandedLinkedResourcesMetrics as ExpandedLinkedResourcesMetrics
from launchdarkly_api.models.expanded_linked_resources_segments import ExpandedLinkedResourcesSegments as ExpandedLinkedResourcesSegments
from launchdarkly_api.models.expanded_linked_segments import ExpandedLinkedSegments as ExpandedLinkedSegments
from launchdarkly_api.models.expanded_metric import ExpandedMetric as ExpandedMetric
from launchdarkly_api.models.expanded_resource_rep import ExpandedResourceRep as ExpandedResourceRep
from launchdarkly_api.models.expanded_segment import ExpandedSegment as ExpandedSegment
from launchdarkly_api.models.experiment import Experiment as Experiment
from launchdarkly_api.models.experiment_allocation_rep import ExperimentAllocationRep as ExperimentAllocationRep
from launchdarkly_api.models.experiment_collection_rep import ExperimentCollectionRep as ExperimentCollectionRep
from launchdarkly_api.models.experiment_enabled_period_rep import ExperimentEnabledPeriodRep as ExperimentEnabledPeriodRep
from launchdarkly_api.models.experiment_environment_setting_rep import ExperimentEnvironmentSettingRep as ExperimentEnvironmentSettingRep
from launchdarkly_api.models.experiment_info_rep import ExperimentInfoRep as ExperimentInfoRep
from launchdarkly_api.models.experiment_patch_input import ExperimentPatchInput as ExperimentPatchInput
from launchdarkly_api.models.experiment_post import ExperimentPost as ExperimentPost
from launchdarkly_api.models.expiring_target import ExpiringTarget as ExpiringTarget
from launchdarkly_api.models.expiring_target_error import ExpiringTargetError as ExpiringTargetError
from launchdarkly_api.models.expiring_target_get_response import ExpiringTargetGetResponse as ExpiringTargetGetResponse
from launchdarkly_api.models.expiring_target_patch_response import ExpiringTargetPatchResponse as ExpiringTargetPatchResponse
from launchdarkly_api.models.expiring_user_target_get_response import ExpiringUserTargetGetResponse as ExpiringUserTargetGetResponse
from launchdarkly_api.models.expiring_user_target_item import ExpiringUserTargetItem as ExpiringUserTargetItem
from launchdarkly_api.models.expiring_user_target_patch_response import ExpiringUserTargetPatchResponse as ExpiringUserTargetPatchResponse
from launchdarkly_api.models.export import Export as Export
from launchdarkly_api.models.extinction import Extinction as Extinction
from launchdarkly_api.models.extinction_collection_rep import ExtinctionCollectionRep as ExtinctionCollectionRep
from launchdarkly_api.models.failed_resource_link import FailedResourceLink as FailedResourceLink
from launchdarkly_api.models.failure_reason_rep import FailureReasonRep as FailureReasonRep
from launchdarkly_api.models.feature_flag import FeatureFlag as FeatureFlag
from launchdarkly_api.models.feature_flag_body import FeatureFlagBody as FeatureFlagBody
from launchdarkly_api.models.feature_flag_config import FeatureFlagConfig as FeatureFlagConfig
from launchdarkly_api.models.feature_flag_scheduled_change import FeatureFlagScheduledChange as FeatureFlagScheduledChange
from launchdarkly_api.models.feature_flag_scheduled_changes import FeatureFlagScheduledChanges as FeatureFlagScheduledChanges
from launchdarkly_api.models.feature_flag_status import FeatureFlagStatus as FeatureFlagStatus
from launchdarkly_api.models.feature_flag_status_across_environments import FeatureFlagStatusAcrossEnvironments as FeatureFlagStatusAcrossEnvironments
from launchdarkly_api.models.feature_flag_statuses import FeatureFlagStatuses as FeatureFlagStatuses
from launchdarkly_api.models.feature_flags import FeatureFlags as FeatureFlags
from launchdarkly_api.models.file_rep import FileRep as FileRep
from launchdarkly_api.models.filter import Filter as Filter
from launchdarkly_api.models.flag_config_approval_request_response import FlagConfigApprovalRequestResponse as FlagConfigApprovalRequestResponse
from launchdarkly_api.models.flag_config_approval_requests_response import FlagConfigApprovalRequestsResponse as FlagConfigApprovalRequestsResponse
from launchdarkly_api.models.flag_config_evaluation import FlagConfigEvaluation as FlagConfigEvaluation
from launchdarkly_api.models.flag_config_migration_settings_rep import FlagConfigMigrationSettingsRep as FlagConfigMigrationSettingsRep
from launchdarkly_api.models.flag_copy_config_environment import FlagCopyConfigEnvironment as FlagCopyConfigEnvironment
from launchdarkly_api.models.flag_copy_config_post import FlagCopyConfigPost as FlagCopyConfigPost
from launchdarkly_api.models.flag_defaults_rep import FlagDefaultsRep as FlagDefaultsRep
from launchdarkly_api.models.flag_event_collection_rep import FlagEventCollectionRep as FlagEventCollectionRep
from launchdarkly_api.models.flag_event_experiment import FlagEventExperiment as FlagEventExperiment
from launchdarkly_api.models.flag_event_experiment_collection import FlagEventExperimentCollection as FlagEventExperimentCollection
from launchdarkly_api.models.flag_event_experiment_iteration import FlagEventExperimentIteration as FlagEventExperimentIteration
from launchdarkly_api.models.flag_event_impact_rep import FlagEventImpactRep as FlagEventImpactRep
from launchdarkly_api.models.flag_event_member_rep import FlagEventMemberRep as FlagEventMemberRep
from launchdarkly_api.models.flag_event_rep import FlagEventRep as FlagEventRep
from launchdarkly_api.models.flag_followers_by_proj_env_get_rep import FlagFollowersByProjEnvGetRep as FlagFollowersByProjEnvGetRep
from launchdarkly_api.models.flag_followers_get_rep import FlagFollowersGetRep as FlagFollowersGetRep
from launchdarkly_api.models.flag_import_configuration_post import FlagImportConfigurationPost as FlagImportConfigurationPost
from launchdarkly_api.models.flag_import_integration import FlagImportIntegration as FlagImportIntegration
from launchdarkly_api.models.flag_import_integration_collection import FlagImportIntegrationCollection as FlagImportIntegrationCollection
from launchdarkly_api.models.flag_import_integration_collection_links import FlagImportIntegrationCollectionLinks as FlagImportIntegrationCollectionLinks
from launchdarkly_api.models.flag_import_integration_links import FlagImportIntegrationLinks as FlagImportIntegrationLinks
from launchdarkly_api.models.flag_import_status import FlagImportStatus as FlagImportStatus
from launchdarkly_api.models.flag_input import FlagInput as FlagInput
from launchdarkly_api.models.flag_link_collection_rep import FlagLinkCollectionRep as FlagLinkCollectionRep
from launchdarkly_api.models.flag_link_member import FlagLinkMember as FlagLinkMember
from launchdarkly_api.models.flag_link_post import FlagLinkPost as FlagLinkPost
from launchdarkly_api.models.flag_link_rep import FlagLinkRep as FlagLinkRep
from launchdarkly_api.models.flag_listing_rep import FlagListingRep as FlagListingRep
from launchdarkly_api.models.flag_migration_settings_rep import FlagMigrationSettingsRep as FlagMigrationSettingsRep
from launchdarkly_api.models.flag_prerequisite_post import FlagPrerequisitePost as FlagPrerequisitePost
from launchdarkly_api.models.flag_reference_collection_rep import FlagReferenceCollectionRep as FlagReferenceCollectionRep
from launchdarkly_api.models.flag_reference_rep import FlagReferenceRep as FlagReferenceRep
from launchdarkly_api.models.flag_rep import FlagRep as FlagRep
from launchdarkly_api.models.flag_scheduled_changes_input import FlagScheduledChangesInput as FlagScheduledChangesInput
from launchdarkly_api.models.flag_sempatch import FlagSempatch as FlagSempatch
from launchdarkly_api.models.flag_status_rep import FlagStatusRep as FlagStatusRep
from launchdarkly_api.models.flag_summary import FlagSummary as FlagSummary
from launchdarkly_api.models.flag_trigger_input import FlagTriggerInput as FlagTriggerInput
from launchdarkly_api.models.flags_summary import FlagsSummary as FlagsSummary
from launchdarkly_api.models.follow_flag_member import FollowFlagMember as FollowFlagMember
from launchdarkly_api.models.followers_per_flag import FollowersPerFlag as FollowersPerFlag
from launchdarkly_api.models.forbidden_error_rep import ForbiddenErrorRep as ForbiddenErrorRep
from launchdarkly_api.models.form_variable import FormVariable as FormVariable
from launchdarkly_api.models.generate_trust_policy_post_rep import GenerateTrustPolicyPostRep as GenerateTrustPolicyPostRep
from launchdarkly_api.models.generate_warehouse_destination_key_pair_post_rep import GenerateWarehouseDestinationKeyPairPostRep as GenerateWarehouseDestinationKeyPairPostRep
from launchdarkly_api.models.get_announcements_public200_response import GetAnnouncementsPublic200Response as GetAnnouncementsPublic200Response
from launchdarkly_api.models.guarded_release_config import GuardedReleaseConfig as GuardedReleaseConfig
from launchdarkly_api.models.hmac_signature import HMACSignature as HMACSignature
from launchdarkly_api.models.header_items import HeaderItems as HeaderItems
from launchdarkly_api.models.holdout_detail_rep import HoldoutDetailRep as HoldoutDetailRep
from launchdarkly_api.models.holdout_patch_input import HoldoutPatchInput as HoldoutPatchInput
from launchdarkly_api.models.holdout_post_request import HoldoutPostRequest as HoldoutPostRequest
from launchdarkly_api.models.holdout_rep import HoldoutRep as HoldoutRep
from launchdarkly_api.models.holdouts_collection_rep import HoldoutsCollectionRep as HoldoutsCollectionRep
from launchdarkly_api.models.hunk_rep import HunkRep as HunkRep
from launchdarkly_api.models.initiator_rep import InitiatorRep as InitiatorRep
from launchdarkly_api.models.insight_group import InsightGroup as InsightGroup
from launchdarkly_api.models.insight_group_collection import InsightGroupCollection as InsightGroupCollection
from launchdarkly_api.models.insight_group_collection_metadata import InsightGroupCollectionMetadata as InsightGroupCollectionMetadata
from launchdarkly_api.models.insight_group_collection_score_metadata import InsightGroupCollectionScoreMetadata as InsightGroupCollectionScoreMetadata
from launchdarkly_api.models.insight_group_scores import InsightGroupScores as InsightGroupScores
from launchdarkly_api.models.insight_groups_count_by_indicator import InsightGroupsCountByIndicator as InsightGroupsCountByIndicator
from launchdarkly_api.models.insight_period import InsightPeriod as InsightPeriod
from launchdarkly_api.models.insight_scores import InsightScores as InsightScores
from launchdarkly_api.models.insights_chart import InsightsChart as InsightsChart
from launchdarkly_api.models.insights_chart_bounds import InsightsChartBounds as InsightsChartBounds
from launchdarkly_api.models.insights_chart_metadata import InsightsChartMetadata as InsightsChartMetadata
from launchdarkly_api.models.insights_chart_metric import InsightsChartMetric as InsightsChartMetric
from launchdarkly_api.models.insights_chart_series import InsightsChartSeries as InsightsChartSeries
from launchdarkly_api.models.insights_chart_series_data_point import InsightsChartSeriesDataPoint as InsightsChartSeriesDataPoint
from launchdarkly_api.models.insights_chart_series_metadata import InsightsChartSeriesMetadata as InsightsChartSeriesMetadata
from launchdarkly_api.models.insights_chart_series_metadata_axis import InsightsChartSeriesMetadataAxis as InsightsChartSeriesMetadataAxis
from launchdarkly_api.models.insights_metric_indicator_range import InsightsMetricIndicatorRange as InsightsMetricIndicatorRange
from launchdarkly_api.models.insights_metric_score import InsightsMetricScore as InsightsMetricScore
from launchdarkly_api.models.insights_metric_tier_definition import InsightsMetricTierDefinition as InsightsMetricTierDefinition
from launchdarkly_api.models.insights_repository import InsightsRepository as InsightsRepository
from launchdarkly_api.models.insights_repository_collection import InsightsRepositoryCollection as InsightsRepositoryCollection
from launchdarkly_api.models.insights_repository_project import InsightsRepositoryProject as InsightsRepositoryProject
from launchdarkly_api.models.insights_repository_project_collection import InsightsRepositoryProjectCollection as InsightsRepositoryProjectCollection
from launchdarkly_api.models.insights_repository_project_mappings import InsightsRepositoryProjectMappings as InsightsRepositoryProjectMappings
from launchdarkly_api.models.instruction_user_request import InstructionUserRequest as InstructionUserRequest
from launchdarkly_api.models.integration import Integration as Integration
from launchdarkly_api.models.integration_configuration_collection_rep import IntegrationConfigurationCollectionRep as IntegrationConfigurationCollectionRep
from launchdarkly_api.models.integration_configuration_post import IntegrationConfigurationPost as IntegrationConfigurationPost
from launchdarkly_api.models.integration_configurations_rep import IntegrationConfigurationsRep as IntegrationConfigurationsRep
from launchdarkly_api.models.integration_delivery_configuration import IntegrationDeliveryConfiguration as IntegrationDeliveryConfiguration
from launchdarkly_api.models.integration_delivery_configuration_collection import IntegrationDeliveryConfigurationCollection as IntegrationDeliveryConfigurationCollection
from launchdarkly_api.models.integration_delivery_configuration_collection_links import IntegrationDeliveryConfigurationCollectionLinks as IntegrationDeliveryConfigurationCollectionLinks
from launchdarkly_api.models.integration_delivery_configuration_links import IntegrationDeliveryConfigurationLinks as IntegrationDeliveryConfigurationLinks
from launchdarkly_api.models.integration_delivery_configuration_post import IntegrationDeliveryConfigurationPost as IntegrationDeliveryConfigurationPost
from launchdarkly_api.models.integration_delivery_configuration_response import IntegrationDeliveryConfigurationResponse as IntegrationDeliveryConfigurationResponse
from launchdarkly_api.models.integration_metadata import IntegrationMetadata as IntegrationMetadata
from launchdarkly_api.models.integration_status import IntegrationStatus as IntegrationStatus
from launchdarkly_api.models.integration_status_rep import IntegrationStatusRep as IntegrationStatusRep
from launchdarkly_api.models.integration_subscription_status_rep import IntegrationSubscriptionStatusRep as IntegrationSubscriptionStatusRep
from launchdarkly_api.models.integrations import Integrations as Integrations
from launchdarkly_api.models.invalid_request_error_rep import InvalidRequestErrorRep as InvalidRequestErrorRep
from launchdarkly_api.models.ip_list import IpList as IpList
from launchdarkly_api.models.iteration_input import IterationInput as IterationInput
from launchdarkly_api.models.iteration_rep import IterationRep as IterationRep
from launchdarkly_api.models.judge_attachment import JudgeAttachment as JudgeAttachment
from launchdarkly_api.models.judge_configuration import JudgeConfiguration as JudgeConfiguration
from launchdarkly_api.models.last_seen_metadata import LastSeenMetadata as LastSeenMetadata
from launchdarkly_api.models.layer_collection_rep import LayerCollectionRep as LayerCollectionRep
from launchdarkly_api.models.layer_configuration_rep import LayerConfigurationRep as LayerConfigurationRep
from launchdarkly_api.models.layer_patch_input import LayerPatchInput as LayerPatchInput
from launchdarkly_api.models.layer_post import LayerPost as LayerPost
from launchdarkly_api.models.layer_rep import LayerRep as LayerRep
from launchdarkly_api.models.layer_reservation_rep import LayerReservationRep as LayerReservationRep
from launchdarkly_api.models.layer_snapshot_rep import LayerSnapshotRep as LayerSnapshotRep
from launchdarkly_api.models.lead_time_stages_rep import LeadTimeStagesRep as LeadTimeStagesRep
from launchdarkly_api.models.legacy_experiment_rep import LegacyExperimentRep as LegacyExperimentRep
from launchdarkly_api.models.link import Link as Link
from launchdarkly_api.models.link_resource_success_response import LinkResourceSuccessResponse as LinkResourceSuccessResponse
from launchdarkly_api.models.maintainer import Maintainer as Maintainer
from launchdarkly_api.models.maintainer_member import MaintainerMember as MaintainerMember
from launchdarkly_api.models.maintainer_rep import MaintainerRep as MaintainerRep
from launchdarkly_api.models.maintainer_team import MaintainerTeam as MaintainerTeam
from launchdarkly_api.models.member import Member as Member
from launchdarkly_api.models.member_data_rep import MemberDataRep as MemberDataRep
from launchdarkly_api.models.member_import_item import MemberImportItem as MemberImportItem
from launchdarkly_api.models.member_permission_grant_summary_rep import MemberPermissionGrantSummaryRep as MemberPermissionGrantSummaryRep
from launchdarkly_api.models.member_summary import MemberSummary as MemberSummary
from launchdarkly_api.models.member_team_summary_rep import MemberTeamSummaryRep as MemberTeamSummaryRep
from launchdarkly_api.models.member_teams_post_input import MemberTeamsPostInput as MemberTeamsPostInput
from launchdarkly_api.models.members import Members as Members
from launchdarkly_api.models.members_patch_input import MembersPatchInput as MembersPatchInput
from launchdarkly_api.models.message import Message as Message
from launchdarkly_api.models.method_not_allowed_error_rep import MethodNotAllowedErrorRep as MethodNotAllowedErrorRep
from launchdarkly_api.models.metric_by_variation import MetricByVariation as MetricByVariation
from launchdarkly_api.models.metric_collection_rep import MetricCollectionRep as MetricCollectionRep
from launchdarkly_api.models.metric_data_source_ref_rep import MetricDataSourceRefRep as MetricDataSourceRefRep
from launchdarkly_api.models.metric_event_default_rep import MetricEventDefaultRep as MetricEventDefaultRep
from launchdarkly_api.models.metric_group_collection_rep import MetricGroupCollectionRep as MetricGroupCollectionRep
from launchdarkly_api.models.metric_group_post import MetricGroupPost as MetricGroupPost
from launchdarkly_api.models.metric_group_rep import MetricGroupRep as MetricGroupRep
from launchdarkly_api.models.metric_in_group_rep import MetricInGroupRep as MetricInGroupRep
from launchdarkly_api.models.metric_in_metric_group_input import MetricInMetricGroupInput as MetricInMetricGroupInput
from launchdarkly_api.models.metric_input import MetricInput as MetricInput
from launchdarkly_api.models.metric_listing_rep import MetricListingRep as MetricListingRep
from launchdarkly_api.models.metric_post import MetricPost as MetricPost
from launchdarkly_api.models.metric_rep import MetricRep as MetricRep
from launchdarkly_api.models.metric_v2_rep import MetricV2Rep as MetricV2Rep
from launchdarkly_api.models.metrics import Metrics as Metrics
from launchdarkly_api.models.metrics_summary import MetricsSummary as MetricsSummary
from launchdarkly_api.models.migration_safety_issue_rep import MigrationSafetyIssueRep as MigrationSafetyIssueRep
from launchdarkly_api.models.migration_settings_post import MigrationSettingsPost as MigrationSettingsPost
from launchdarkly_api.models.model_config import ModelConfig as ModelConfig
from launchdarkly_api.models.model_config_post import ModelConfigPost as ModelConfigPost
from launchdarkly_api.models.model_import import ModelImport as ModelImport
from launchdarkly_api.models.modification import Modification as Modification
from launchdarkly_api.models.multi_environment_dependent_flag import MultiEnvironmentDependentFlag as MultiEnvironmentDependentFlag
from launchdarkly_api.models.multi_environment_dependent_flags import MultiEnvironmentDependentFlags as MultiEnvironmentDependentFlags
from launchdarkly_api.models.naming_convention import NamingConvention as NamingConvention
from launchdarkly_api.models.new_member_form import NewMemberForm as NewMemberForm
from launchdarkly_api.models.not_found_error_rep import NotFoundErrorRep as NotFoundErrorRep
from launchdarkly_api.models.oauth_client_post import OauthClientPost as OauthClientPost
from launchdarkly_api.models.options_array import OptionsArray as OptionsArray
from launchdarkly_api.models.paginated_links import PaginatedLinks as PaginatedLinks
from launchdarkly_api.models.parameter_default import ParameterDefault as ParameterDefault
from launchdarkly_api.models.parameter_rep import ParameterRep as ParameterRep
from launchdarkly_api.models.parent_and_self_links import ParentAndSelfLinks as ParentAndSelfLinks
from launchdarkly_api.models.parent_link import ParentLink as ParentLink
from launchdarkly_api.models.parent_resource_rep import ParentResourceRep as ParentResourceRep
from launchdarkly_api.models.patch_failed_error_rep import PatchFailedErrorRep as PatchFailedErrorRep
from launchdarkly_api.models.patch_flags_request import PatchFlagsRequest as PatchFlagsRequest
from launchdarkly_api.models.patch_operation import PatchOperation as PatchOperation
from launchdarkly_api.models.patch_segment_expiring_target_input_rep import PatchSegmentExpiringTargetInputRep as PatchSegmentExpiringTargetInputRep
from launchdarkly_api.models.patch_segment_expiring_target_instruction import PatchSegmentExpiringTargetInstruction as PatchSegmentExpiringTargetInstruction
from launchdarkly_api.models.patch_segment_instruction import PatchSegmentInstruction as PatchSegmentInstruction
from launchdarkly_api.models.patch_segment_request import PatchSegmentRequest as PatchSegmentRequest
from launchdarkly_api.models.patch_users_request import PatchUsersRequest as PatchUsersRequest
from launchdarkly_api.models.patch_with_comment import PatchWithComment as PatchWithComment
from launchdarkly_api.models.permission_grant_input import PermissionGrantInput as PermissionGrantInput
from launchdarkly_api.models.phase import Phase as Phase
from launchdarkly_api.models.phase_info import PhaseInfo as PhaseInfo
from launchdarkly_api.models.post_approval_request_apply_request import PostApprovalRequestApplyRequest as PostApprovalRequestApplyRequest
from launchdarkly_api.models.post_approval_request_review_request import PostApprovalRequestReviewRequest as PostApprovalRequestReviewRequest
from launchdarkly_api.models.post_deployment_event_input import PostDeploymentEventInput as PostDeploymentEventInput
from launchdarkly_api.models.post_flag_scheduled_changes_input import PostFlagScheduledChangesInput as PostFlagScheduledChangesInput
from launchdarkly_api.models.post_insight_group_params import PostInsightGroupParams as PostInsightGroupParams
from launchdarkly_api.models.post_release_policy_request import PostReleasePolicyRequest as PostReleasePolicyRequest
from launchdarkly_api.models.prerequisite import Prerequisite as Prerequisite
from launchdarkly_api.models.progressive_release_config import ProgressiveReleaseConfig as ProgressiveReleaseConfig
from launchdarkly_api.models.project import Project as Project
from launchdarkly_api.models.project_post import ProjectPost as ProjectPost
from launchdarkly_api.models.project_rep import ProjectRep as ProjectRep
from launchdarkly_api.models.project_summary import ProjectSummary as ProjectSummary
from launchdarkly_api.models.project_summary_collection import ProjectSummaryCollection as ProjectSummaryCollection
from launchdarkly_api.models.projects import Projects as Projects
from launchdarkly_api.models.pull_request_collection_rep import PullRequestCollectionRep as PullRequestCollectionRep
from launchdarkly_api.models.pull_request_lead_time_rep import PullRequestLeadTimeRep as PullRequestLeadTimeRep
from launchdarkly_api.models.pull_request_rep import PullRequestRep as PullRequestRep
from launchdarkly_api.models.put_branch import PutBranch as PutBranch
from launchdarkly_api.models.put_release_policy_request import PutReleasePolicyRequest as PutReleasePolicyRequest
from launchdarkly_api.models.randomization_settings_put import RandomizationSettingsPut as RandomizationSettingsPut
from launchdarkly_api.models.randomization_settings_rep import RandomizationSettingsRep as RandomizationSettingsRep
from launchdarkly_api.models.randomization_unit_input import RandomizationUnitInput as RandomizationUnitInput
from launchdarkly_api.models.randomization_unit_rep import RandomizationUnitRep as RandomizationUnitRep
from launchdarkly_api.models.rate_limited_error_rep import RateLimitedErrorRep as RateLimitedErrorRep
from launchdarkly_api.models.recent_trigger_body import RecentTriggerBody as RecentTriggerBody
from launchdarkly_api.models.reference_rep import ReferenceRep as ReferenceRep
from launchdarkly_api.models.related_experiment_rep import RelatedExperimentRep as RelatedExperimentRep
from launchdarkly_api.models.relay_auto_config_collection_rep import RelayAutoConfigCollectionRep as RelayAutoConfigCollectionRep
from launchdarkly_api.models.relay_auto_config_post import RelayAutoConfigPost as RelayAutoConfigPost
from launchdarkly_api.models.relay_auto_config_rep import RelayAutoConfigRep as RelayAutoConfigRep
from launchdarkly_api.models.release import Release as Release
from launchdarkly_api.models.release_audience import ReleaseAudience as ReleaseAudience
from launchdarkly_api.models.release_guardian_configuration import ReleaseGuardianConfiguration as ReleaseGuardianConfiguration
from launchdarkly_api.models.release_guardian_configuration_input import ReleaseGuardianConfigurationInput as ReleaseGuardianConfigurationInput
from launchdarkly_api.models.release_method import ReleaseMethod as ReleaseMethod
from launchdarkly_api.models.release_phase import ReleasePhase as ReleasePhase
from launchdarkly_api.models.release_pipeline import ReleasePipeline as ReleasePipeline
from launchdarkly_api.models.release_pipeline_collection import ReleasePipelineCollection as ReleasePipelineCollection
from launchdarkly_api.models.release_policies_access import ReleasePoliciesAccess as ReleasePoliciesAccess
from launchdarkly_api.models.release_policies_access_allowed_reason import ReleasePoliciesAccessAllowedReason as ReleasePoliciesAccessAllowedReason
from launchdarkly_api.models.release_policies_access_allowed_rep import ReleasePoliciesAccessAllowedRep as ReleasePoliciesAccessAllowedRep
from launchdarkly_api.models.release_policies_access_denied import ReleasePoliciesAccessDenied as ReleasePoliciesAccessDenied
from launchdarkly_api.models.release_policies_access_denied_reason import ReleasePoliciesAccessDeniedReason as ReleasePoliciesAccessDeniedReason
from launchdarkly_api.models.release_policies_access_rep import ReleasePoliciesAccessRep as ReleasePoliciesAccessRep
from launchdarkly_api.models.release_policies_response import ReleasePoliciesResponse as ReleasePoliciesResponse
from launchdarkly_api.models.release_policy import ReleasePolicy as ReleasePolicy
from launchdarkly_api.models.release_policy_scope import ReleasePolicyScope as ReleasePolicyScope
from launchdarkly_api.models.release_policy_stage import ReleasePolicyStage as ReleasePolicyStage
from launchdarkly_api.models.release_progression import ReleaseProgression as ReleaseProgression
from launchdarkly_api.models.release_progression_collection import ReleaseProgressionCollection as ReleaseProgressionCollection
from launchdarkly_api.models.releaser_audience_config_input import ReleaserAudienceConfigInput as ReleaserAudienceConfigInput
from launchdarkly_api.models.repository_collection_rep import RepositoryCollectionRep as RepositoryCollectionRep
from launchdarkly_api.models.repository_post import RepositoryPost as RepositoryPost
from launchdarkly_api.models.repository_rep import RepositoryRep as RepositoryRep
from launchdarkly_api.models.resource_access import ResourceAccess as ResourceAccess
from launchdarkly_api.models.resource_id_response import ResourceIDResponse as ResourceIDResponse
from launchdarkly_api.models.resource_id import ResourceId as ResourceId
from launchdarkly_api.models.resource_summary import ResourceSummary as ResourceSummary
from launchdarkly_api.models.restricted_model_error import RestrictedModelError as RestrictedModelError
from launchdarkly_api.models.restricted_models_request import RestrictedModelsRequest as RestrictedModelsRequest
from launchdarkly_api.models.restricted_models_response import RestrictedModelsResponse as RestrictedModelsResponse
from launchdarkly_api.models.review_output import ReviewOutput as ReviewOutput
from launchdarkly_api.models.review_response import ReviewResponse as ReviewResponse
from launchdarkly_api.models.rollout import Rollout as Rollout
from launchdarkly_api.models.root_response import RootResponse as RootResponse
from launchdarkly_api.models.rule import Rule as Rule
from launchdarkly_api.models.rule_clause import RuleClause as RuleClause
from launchdarkly_api.models.sdk_list_rep import SdkListRep as SdkListRep
from launchdarkly_api.models.sdk_version_list_rep import SdkVersionListRep as SdkVersionListRep
from launchdarkly_api.models.sdk_version_rep import SdkVersionRep as SdkVersionRep
from launchdarkly_api.models.segment_body import SegmentBody as SegmentBody
from launchdarkly_api.models.segment_metadata import SegmentMetadata as SegmentMetadata
from launchdarkly_api.models.segment_target import SegmentTarget as SegmentTarget
from launchdarkly_api.models.segment_user_list import SegmentUserList as SegmentUserList
from launchdarkly_api.models.segment_user_state import SegmentUserState as SegmentUserState
from launchdarkly_api.models.segments_summary import SegmentsSummary as SegmentsSummary
from launchdarkly_api.models.series_list_rep import SeriesListRep as SeriesListRep
from launchdarkly_api.models.series_list_rep_float import SeriesListRepFloat as SeriesListRepFloat
from launchdarkly_api.models.simple_holdout_rep import SimpleHoldoutRep as SimpleHoldoutRep
from launchdarkly_api.models.source_env import SourceEnv as SourceEnv
from launchdarkly_api.models.source_flag import SourceFlag as SourceFlag
from launchdarkly_api.models.stage_input import StageInput as StageInput
from launchdarkly_api.models.stage_output import StageOutput as StageOutput
from launchdarkly_api.models.statement import Statement as Statement
from launchdarkly_api.models.statement_post import StatementPost as StatementPost
from launchdarkly_api.models.statistic_collection_rep import StatisticCollectionRep as StatisticCollectionRep
from launchdarkly_api.models.statistic_rep import StatisticRep as StatisticRep
from launchdarkly_api.models.statistics_root import StatisticsRoot as StatisticsRoot
from launchdarkly_api.models.status_conflict_error_rep import StatusConflictErrorRep as StatusConflictErrorRep
from launchdarkly_api.models.status_response import StatusResponse as StatusResponse
from launchdarkly_api.models.status_service_unavailable import StatusServiceUnavailable as StatusServiceUnavailable
from launchdarkly_api.models.store_integration_error import StoreIntegrationError as StoreIntegrationError
from launchdarkly_api.models.subject_data_rep import SubjectDataRep as SubjectDataRep
from launchdarkly_api.models.subscription_post import SubscriptionPost as SubscriptionPost
from launchdarkly_api.models.tags_collection import TagsCollection as TagsCollection
from launchdarkly_api.models.tags_link import TagsLink as TagsLink
from launchdarkly_api.models.target import Target as Target
from launchdarkly_api.models.target_resource_rep import TargetResourceRep as TargetResourceRep
from launchdarkly_api.models.team import Team as Team
from launchdarkly_api.models.team_custom_role import TeamCustomRole as TeamCustomRole
from launchdarkly_api.models.team_custom_roles import TeamCustomRoles as TeamCustomRoles
from launchdarkly_api.models.team_imports_rep import TeamImportsRep as TeamImportsRep
from launchdarkly_api.models.team_maintainers import TeamMaintainers as TeamMaintainers
from launchdarkly_api.models.team_members import TeamMembers as TeamMembers
from launchdarkly_api.models.team_patch_input import TeamPatchInput as TeamPatchInput
from launchdarkly_api.models.team_post_input import TeamPostInput as TeamPostInput
from launchdarkly_api.models.team_projects import TeamProjects as TeamProjects
from launchdarkly_api.models.teams import Teams as Teams
from launchdarkly_api.models.teams_patch_input import TeamsPatchInput as TeamsPatchInput
from launchdarkly_api.models.timestamp_rep import TimestampRep as TimestampRep
from launchdarkly_api.models.token import Token as Token
from launchdarkly_api.models.token_summary import TokenSummary as TokenSummary
from launchdarkly_api.models.tokens import Tokens as Tokens
from launchdarkly_api.models.treatment_input import TreatmentInput as TreatmentInput
from launchdarkly_api.models.treatment_parameter_input import TreatmentParameterInput as TreatmentParameterInput
from launchdarkly_api.models.treatment_rep import TreatmentRep as TreatmentRep
from launchdarkly_api.models.trigger_post import TriggerPost as TriggerPost
from launchdarkly_api.models.trigger_workflow_collection_rep import TriggerWorkflowCollectionRep as TriggerWorkflowCollectionRep
from launchdarkly_api.models.trigger_workflow_rep import TriggerWorkflowRep as TriggerWorkflowRep
from launchdarkly_api.models.trust_policy_details import TrustPolicyDetails as TrustPolicyDetails
from launchdarkly_api.models.trust_policy_statement import TrustPolicyStatement as TrustPolicyStatement
from launchdarkly_api.models.unauthorized_error_rep import UnauthorizedErrorRep as UnauthorizedErrorRep
from launchdarkly_api.models.unlink_resource_success_response import UnlinkResourceSuccessResponse as UnlinkResourceSuccessResponse
from launchdarkly_api.models.update_phase_status_input import UpdatePhaseStatusInput as UpdatePhaseStatusInput
from launchdarkly_api.models.update_release_pipeline_input import UpdateReleasePipelineInput as UpdateReleasePipelineInput
from launchdarkly_api.models.upsert_context_kind_payload import UpsertContextKindPayload as UpsertContextKindPayload
from launchdarkly_api.models.upsert_flag_defaults_payload import UpsertFlagDefaultsPayload as UpsertFlagDefaultsPayload
from launchdarkly_api.models.upsert_payload_rep import UpsertPayloadRep as UpsertPayloadRep
from launchdarkly_api.models.upsert_response_rep import UpsertResponseRep as UpsertResponseRep
from launchdarkly_api.models.url_post import UrlPost as UrlPost
from launchdarkly_api.models.user import User as User
from launchdarkly_api.models.user_attribute_names_rep import UserAttributeNamesRep as UserAttributeNamesRep
from launchdarkly_api.models.user_flag_setting import UserFlagSetting as UserFlagSetting
from launchdarkly_api.models.user_flag_settings import UserFlagSettings as UserFlagSettings
from launchdarkly_api.models.user_record import UserRecord as UserRecord
from launchdarkly_api.models.user_segment import UserSegment as UserSegment
from launchdarkly_api.models.user_segment_rule import UserSegmentRule as UserSegmentRule
from launchdarkly_api.models.user_segments import UserSegments as UserSegments
from launchdarkly_api.models.users import Users as Users
from launchdarkly_api.models.users_rep import UsersRep as UsersRep
from launchdarkly_api.models.validation_failed_error_rep import ValidationFailedErrorRep as ValidationFailedErrorRep
from launchdarkly_api.models.value_put import ValuePut as ValuePut
from launchdarkly_api.models.variation import Variation as Variation
from launchdarkly_api.models.variation_eval_summary import VariationEvalSummary as VariationEvalSummary
from launchdarkly_api.models.variation_or_rollout_rep import VariationOrRolloutRep as VariationOrRolloutRep
from launchdarkly_api.models.variation_summary import VariationSummary as VariationSummary
from launchdarkly_api.models.variation_tool import VariationTool as VariationTool
from launchdarkly_api.models.variation_tool_post import VariationToolPost as VariationToolPost
from launchdarkly_api.models.versions_rep import VersionsRep as VersionsRep
from launchdarkly_api.models.view import View as View
from launchdarkly_api.models.view_link_request import ViewLinkRequest as ViewLinkRequest
from launchdarkly_api.models.view_link_request_keys import ViewLinkRequestKeys as ViewLinkRequestKeys
from launchdarkly_api.models.view_link_request_segment_identifier import ViewLinkRequestSegmentIdentifier as ViewLinkRequestSegmentIdentifier
from launchdarkly_api.models.view_link_request_segment_identifiers import ViewLinkRequestSegmentIdentifiers as ViewLinkRequestSegmentIdentifiers
from launchdarkly_api.models.view_linked_resource import ViewLinkedResource as ViewLinkedResource
from launchdarkly_api.models.view_linked_resource_details import ViewLinkedResourceDetails as ViewLinkedResourceDetails
from launchdarkly_api.models.view_linked_resources import ViewLinkedResources as ViewLinkedResources
from launchdarkly_api.models.view_patch import ViewPatch as ViewPatch
from launchdarkly_api.models.view_post import ViewPost as ViewPost
from launchdarkly_api.models.views import Views as Views
from launchdarkly_api.models.views_access import ViewsAccess as ViewsAccess
from launchdarkly_api.models.views_access_allowed_reason import ViewsAccessAllowedReason as ViewsAccessAllowedReason
from launchdarkly_api.models.views_access_allowed_rep import ViewsAccessAllowedRep as ViewsAccessAllowedRep
from launchdarkly_api.models.views_access_denied import ViewsAccessDenied as ViewsAccessDenied
from launchdarkly_api.models.views_access_denied_reason import ViewsAccessDeniedReason as ViewsAccessDeniedReason
from launchdarkly_api.models.views_access_rep import ViewsAccessRep as ViewsAccessRep
from launchdarkly_api.models.views_link import ViewsLink as ViewsLink
from launchdarkly_api.models.views_maintainer_member import ViewsMaintainerMember as ViewsMaintainerMember
from launchdarkly_api.models.views_maintainer_team import ViewsMaintainerTeam as ViewsMaintainerTeam
from launchdarkly_api.models.views_paginated_links import ViewsPaginatedLinks as ViewsPaginatedLinks
from launchdarkly_api.models.views_self_link import ViewsSelfLink as ViewsSelfLink
from launchdarkly_api.models.webhook import Webhook as Webhook
from launchdarkly_api.models.webhook_post import WebhookPost as WebhookPost
from launchdarkly_api.models.webhooks import Webhooks as Webhooks
from launchdarkly_api.models.weighted_variation import WeightedVariation as WeightedVariation
from launchdarkly_api.models.workflow_template_metadata import WorkflowTemplateMetadata as WorkflowTemplateMetadata
from launchdarkly_api.models.workflow_template_output import WorkflowTemplateOutput as WorkflowTemplateOutput
from launchdarkly_api.models.workflow_template_parameter import WorkflowTemplateParameter as WorkflowTemplateParameter
from launchdarkly_api.models.workflow_templates_listing_output_rep import WorkflowTemplatesListingOutputRep as WorkflowTemplatesListingOutputRep

