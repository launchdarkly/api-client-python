# launchdarkly_api.EnvironmentReleasesBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_environment_release**](EnvironmentReleasesBetaApi.md#get_environment_release) | **GET** /api/v2/projects/{projectKey}/flags/{flagKey}/environments/{environmentKey}/releases/{releaseId} | Get an environment release
[**list_environment_releases**](EnvironmentReleasesBetaApi.md#list_environment_releases) | **GET** /api/v2/projects/{projectKey}/flags/{flagKey}/environments/{environmentKey}/releases | List environment releases
[**start_environment_release**](EnvironmentReleasesBetaApi.md#start_environment_release) | **POST** /api/v2/projects/{projectKey}/flags/{flagKey}/environments/{environmentKey}/releases | Start an environment release
[**stop_environment_release**](EnvironmentReleasesBetaApi.md#stop_environment_release) | **PUT** /api/v2/projects/{projectKey}/flags/{flagKey}/environments/{environmentKey}/releases/{releaseId}/stop | Stop an environment release


# **get_environment_release**
> EnvironmentRelease get_environment_release(ld_api_version, project_key, flag_key, environment_key, release_id, expand=expand)

Get an environment release

Returns an environment release and all its phases in phase-index order.
The release ID must belong to the flag and environment in the path.
Returns `404` for a release that ended more than 90 days ago.
Pass `expand=metrics` to attach each metric's definition to the top-level
`metrics` array. Analysis settings come from the version pinned when the
release started (`metricVersionId`); name, description, tags, maintainer,
and archive state reflect the current metric and may change afterwards.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.environment_release import EnvironmentRelease
from launchdarkly_api.rest import ApiException
from pprint import pprint

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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.EnvironmentReleasesBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    flag_key = 'flag_key_example' # str | 
    environment_key = 'environment_key_example' # str | 
    release_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    expand = ['expand_example'] # List[str] | Optional fields to expand. (optional)

    try:
        # Get an environment release
        api_response = api_instance.get_environment_release(ld_api_version, project_key, flag_key, environment_key, release_id, expand=expand)
        print("The response of EnvironmentReleasesBetaApi->get_environment_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentReleasesBetaApi->get_environment_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **flag_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **release_id** | **UUID**|  | 
 **expand** | [**List[str]**](str.md)| Optional fields to expand. | [optional] 

### Return type

[**EnvironmentRelease**](EnvironmentRelease.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Environment release. |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**429** | Rate limited |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_environment_releases**
> EnvironmentReleaseCollection list_environment_releases(ld_api_version, project_key, flag_key, environment_key, filter=filter, limit=limit, offset=offset, snapshot=snapshot)

List environment releases

Returns the environment releases for the flag in the environment, newest first.
Each release includes its phases in phase-index order.
Metric definitions are not included. To get them, call
`getEnvironmentRelease` with `expand=metrics`.
Returns an empty `items` array when the flag has no releases in the environment,
or when no release matches the `filter`.
Releases that ended more than 90 days ago are not returned.

Results are paginated. By default, the first 25 releases are returned. Use
`limit` and `offset` to page through the rest, and `totalCount` to learn how
many releases match in total. The `_links` object includes `first`, `prev`,
`next`, and `last` links where they apply.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.environment_release_collection import EnvironmentReleaseCollection
from launchdarkly_api.rest import ApiException
from pprint import pprint

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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.EnvironmentReleasesBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    flag_key = 'flag_key_example' # str | 
    environment_key = 'environment_key_example' # str | 
    filter = 'kind equals guarded' # str | A queryfilter expression that narrows the list. Supported fields and operators: `kind` (`equals`) with values `progressive` or `guarded`.  (optional)
    limit = 25 # int | The number of releases to return. Defaults to 25. Maximum is 100. (optional) (default to 25)
    offset = 0 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten releases and then returns the next releases in the list, up to the query `limit`. (optional) (default to 0)
    snapshot = 'snapshot_example' # str | Pins the read to a moment in time (nanoseconds since the Unix epoch) so pages walked in sequence reflect one consistent snapshot. Follow the pagination links rather than constructing this value. Out-of-range values are ignored. (optional)

    try:
        # List environment releases
        api_response = api_instance.list_environment_releases(ld_api_version, project_key, flag_key, environment_key, filter=filter, limit=limit, offset=offset, snapshot=snapshot)
        print("The response of EnvironmentReleasesBetaApi->list_environment_releases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentReleasesBetaApi->list_environment_releases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **flag_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **filter** | **str**| A queryfilter expression that narrows the list. Supported fields and operators: &#x60;kind&#x60; (&#x60;equals&#x60;) with values &#x60;progressive&#x60; or &#x60;guarded&#x60;.  | [optional] 
 **limit** | **int**| The number of releases to return. Defaults to 25. Maximum is 100. | [optional] [default to 25]
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten releases and then returns the next releases in the list, up to the query &#x60;limit&#x60;. | [optional] [default to 0]
 **snapshot** | **str**| Pins the read to a moment in time (nanoseconds since the Unix epoch) so pages walked in sequence reflect one consistent snapshot. Follow the pagination links rather than constructing this value. Out-of-range values are ignored. | [optional] 

### Return type

[**EnvironmentReleaseCollection**](EnvironmentReleaseCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Environment releases. |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**429** | Rate limited |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_environment_release**
> EnvironmentRelease start_environment_release(ld_api_version, project_key, flag_key, environment_key, start_environment_release_request)

Start an environment release

Creates and starts a release on a flag in an environment, either from
inline configuration or from an environment release plan. A release
has one or more phases. Each phase is an audience, targeted by one
flag rule, and has its own steps: the schedule of allocations at
which that rule serves the target variation. After all of a phase's
steps complete, the phase serves the target variation to 100% of its
contexts.

**Inline configuration.** Each entry in `phases` must specify exactly
one targeting mode:

- **Existing rule**: set `ruleId`. The rule must be enabled. Only a
  single-phase release can use an existing rule.
- **New rule**: set `clauses`, with an optional `description`. New
  rules are appended to the end of the flag's rule list. To insert
  them before an existing rule instead, set the top-level
  `beforeRuleId`, which applies to every phase.

Every phase's rule, including an existing rule passed by `ruleId`,
must include
`{"contextKind": "<randomizationUnit>", "attribute": "kind", "op": "in", "values": ["<randomizationUnit>"]}`,
not negated and with no other values, so the release only reaches
contexts of the `randomizationUnit` kind, or multi-contexts
containing the `randomizationUnit` kind. An existing rule needs the
clause even if its other clauses only match that context kind. A
phase without it returns `400`.

For multiple phases, set `phases` with at least two entries. Each phase
creates a rule. The first rule is enabled and starts immediately.
Subsequent rules stay disabled until the release advances to them:
automatically when `advancementMode` is `automatic`, or by an explicit
advance when it is `manual`. `advancementMode` is required for a
multi-phase release.

Releases on the flag's default rule are not supported. A phase that
omits both targeting modes is rejected.

The flag must be on in the environment, or the request returns
`409`. The release only reaches contexts that match a phase's rule.
Other contexts keep getting the flag's default rule, which may
already serve the target variation.

The release type is inferred from `metrics`: an omitted or empty array
creates a progressive release; one or more metrics creates a guarded
release. Metrics must be listed individually; metric groups are not
accepted.

Every start runs release health checks, described in
`ReleaseHealthCheckKind`. A flag that hasn't recently been
evaluated for contexts of the `randomizationUnit` kind fails
`flag_evaluations_with_context`, and one with no recent evaluations
at all also fails `flag_evaluations_any`. Guarded releases also
check that each metric receives events. A failing
check returns `400` with code `health_checks_failed`. To start the
release anyway, list the failing kinds in `bypassHealthChecks`.

**From a release plan.** Set `releasePlanKey` to start from a plan in
this environment instead of configuring the release inline; a request
that also sets fields the plan supplies is rejected. The plan's current
version runs as stored, with metric groups expanded into their members.
Health checks run against the plan's randomization unit and metrics.
Returns `400` if the plan is missing or incomplete, and `422` until
environment release plans are available for the account.

Requires the `updateRules` action on the flag in this environment, plus
`updateFallthrough` when `cleanupBehavior` is
`remove_rules_and_update_default_rule`. A release started from a plan
requires both. The start is recorded in the flag's audit log as a
targeting change that carries `comment`.

In an environment that requires approvals, this endpoint fails with
`405`. Tokens granted the `bypassRequiredApproval` action can still
call it to start the release directly.

This operation is not idempotent. Retrying a request that already
started a release returns `409` with code `release_already_active`.
The earlier request may have succeeded; call `listEnvironmentReleases`
to confirm the running release is yours.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.environment_release import EnvironmentRelease
from launchdarkly_api.models.start_environment_release_request import StartEnvironmentReleaseRequest
from launchdarkly_api.rest import ApiException
from pprint import pprint

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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.EnvironmentReleasesBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    flag_key = 'flag_key_example' # str | 
    environment_key = 'environment_key_example' # str | 
    start_environment_release_request = {"originalVariationId":"11111111-1111-1111-1111-111111111111","targetVariationId":"22222222-2222-2222-2222-222222222222","releasePlanKey":"production-guarded-rollout","comment":"Requested by the deployment automation"} # StartEnvironmentReleaseRequest | 

    try:
        # Start an environment release
        api_response = api_instance.start_environment_release(ld_api_version, project_key, flag_key, environment_key, start_environment_release_request)
        print("The response of EnvironmentReleasesBetaApi->start_environment_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentReleasesBetaApi->start_environment_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **flag_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **start_environment_release_request** | [**StartEnvironmentReleaseRequest**](StartEnvironmentReleaseRequest.md)|  | 

### Return type

[**EnvironmentRelease**](EnvironmentRelease.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Environment release created and started. |  -  |
**400** | The request is invalid. When &#x60;code&#x60; is &#x60;health_checks_failed&#x60;, &#x60;failingChecks&#x60; describes the release health checks that failed. Fix the failing checks, or list their kinds in &#x60;bypassHealthChecks&#x60; to start the release anyway.  |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**405** | Approval is required to make this change |  -  |
**409** | The flag&#39;s current state does not allow the start. &#x60;code&#x60; is &#x60;release_already_active&#x60; when a release is already running on the flag or on the targeted rule; if this is a retry, the first request may have succeeded, so call &#x60;listEnvironmentReleases&#x60; to confirm. Any other conflict returns &#x60;optimistic_locking_error&#x60; with the cause in &#x60;message&#x60;.  |  -  |
**422** | The request set &#x60;releasePlanKey&#x60; before environment release plans are available for the account. Configure the release inline instead.  |  -  |
**429** | Rate limited |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_environment_release**
> EnvironmentRelease stop_environment_release(ld_api_version, project_key, flag_key, environment_key, release_id, stop_environment_release_request)

Stop an environment release

Stops a release and resolves its phases according to the `resolution`
you specify. To learn how each resolution treats completed and pending
phases, read the `resolution` schema.

Requires the `updateRules` action on the flag in this environment, or
`updateFallthrough` for a historical release that ran on the default
rule. The stop is recorded in the flag's audit log as a targeting
change that names the resolution and carries `comment`.

In an environment that requires approvals, this endpoint fails with
`405`. Tokens granted the `bypassRequiredApproval` action can still
call it to stop the release directly.

Stopping a release that has already completed or been stopped returns
`200` and makes no changes. Returns `404` for a release that ended more
than 90 days ago.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.environment_release import EnvironmentRelease
from launchdarkly_api.models.stop_environment_release_request import StopEnvironmentReleaseRequest
from launchdarkly_api.rest import ApiException
from pprint import pprint

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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = launchdarkly_api.EnvironmentReleasesBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    flag_key = 'flag_key_example' # str | 
    environment_key = 'environment_key_example' # str | 
    release_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    stop_environment_release_request = {"resolution":"roll_back_all_phases_and_remove_pending_phases","comment":"Error rate regressed after the 10% step"} # StopEnvironmentReleaseRequest | 

    try:
        # Stop an environment release
        api_response = api_instance.stop_environment_release(ld_api_version, project_key, flag_key, environment_key, release_id, stop_environment_release_request)
        print("The response of EnvironmentReleasesBetaApi->stop_environment_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentReleasesBetaApi->stop_environment_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **flag_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **release_id** | **UUID**|  | 
 **stop_environment_release_request** | [**StopEnvironmentReleaseRequest**](StopEnvironmentReleaseRequest.md)|  | 

### Return type

[**EnvironmentRelease**](EnvironmentRelease.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Environment release stopped, or already in a terminal status. |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**405** | Approval is required to make this change |  -  |
**409** | The flag&#39;s current state does not allow the stop. The response returns &#x60;optimistic_locking_error&#x60; with the cause in &#x60;message&#x60;. Resolve the cause, then retry.  |  -  |
**429** | Rate limited |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

