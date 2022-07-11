# launchdarkly_api.EnvironmentsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_environment**](EnvironmentsApi.md#delete_environment) | **DELETE** /api/v2/projects/{projectKey}/environments/{environmentKey} | Delete environment
[**get_environment**](EnvironmentsApi.md#get_environment) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey} | Get environment
[**get_environments_by_project**](EnvironmentsApi.md#get_environments_by_project) | **GET** /api/v2/projects/{projectKey}/environments | List environments
[**patch_environment**](EnvironmentsApi.md#patch_environment) | **PATCH** /api/v2/projects/{projectKey}/environments/{environmentKey} | Update environment
[**post_environment**](EnvironmentsApi.md#post_environment) | **POST** /api/v2/projects/{projectKey}/environments | Create environment
[**reset_environment_mobile_key**](EnvironmentsApi.md#reset_environment_mobile_key) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/mobileKey | Reset environment mobile SDK key
[**reset_environment_sdk_key**](EnvironmentsApi.md#reset_environment_sdk_key) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/apiKey | Reset environment SDK key


# **delete_environment**
> delete_environment(project_key, environment_key)

Delete environment

Delete a environment by key.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import environments_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = environments_api.EnvironmentsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key

    # example passing only required values which don't have defaults set
    try:
        # Delete environment
        api_instance.delete_environment(project_key, environment_key)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling EnvironmentsApi->delete_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Action succeeded |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment**
> Environment get_environment(project_key, environment_key)

Get environment

> ### Approval settings > > The `approvalSettings` key is only returned when the Flag Approvals feature is enabled.  Get an environment given a project and key. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import environments_api
from launchdarkly_api.model.environment import Environment
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = environments_api.EnvironmentsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key

    # example passing only required values which don't have defaults set
    try:
        # Get environment
        api_response = api_instance.get_environment(project_key, environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling EnvironmentsApi->get_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |

### Return type

[**Environment**](Environment.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Environment response JSON |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environments_by_project**
> Environments get_environments_by_project(project_key)

List environments

Return a list of environments for the specified project.  By default, this returns the first 20 environments. Page through this list with the `limit` parameter and by following the `first`, `prev`, `next`, and `last` links in the `_links` field that returns. If those links do not appear, the pages they refer to don't exist. For example, the `first` and `prev` links will be missing from the response on the first page, because there is no previous page and you cannot return to the first page when you are already on the first page.  ### Filtering environments  LaunchDarkly supports two fields for filters: - `query` is a string that matches against the environments' names and keys. It is not case sensitive. - `tags` is a `+` separate list of environment tags. It filters the list of environments that have all of the tags in the list.  For example, the filter `query:abc,tags:tag-1+tag-2` matches environments with the string `abc` in their name or key and also are tagged with `tag-1` and `tag-2`. The filter is not case-sensitive.  ### Sorting environments  LaunchDarkly supports two fields for sorting: - `name` sorts by environment name. - `createdOn` sorts by the creation date of the environment.  For example, `sort=name` sorts the response by environment name in ascending order. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import environments_api
from launchdarkly_api.model.environments import Environments
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = environments_api.EnvironmentsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    limit = 1 # int | The number of environments to return in the response. Defaults to 20. (optional)
    offset = 1 # int | Where to start in the list. This is for use with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = "filter_example" # str | A comma-separated list of filters. Each filter is of the form `field:value`. (optional)
    sort = "sort_example" # str | A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List environments
        api_response = api_instance.get_environments_by_project(project_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling EnvironmentsApi->get_environments_by_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List environments
        api_response = api_instance.get_environments_by_project(project_key, limit=limit, offset=offset, filter=filter, sort=sort)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling EnvironmentsApi->get_environments_by_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **limit** | **int**| The number of environments to return in the response. Defaults to 20. | [optional]
 **offset** | **int**| Where to start in the list. This is for use with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional]
 **filter** | **str**| A comma-separated list of filters. Each filter is of the form &#x60;field:value&#x60;. | [optional]
 **sort** | **str**| A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order. | [optional]

### Return type

[**Environments**](Environments.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project environments response JSON |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_environment**
> Environment patch_environment(project_key, environment_key, json_patch)

Update environment

 Update an environment. Requires a [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes to the environment.  To update fields in the environment object that are arrays, set the `path` to the name of the field and then append `/<array index>`. Using `/0` appends to the beginning of the array.  ### Approval settings  This request only returns the `approvalSettings` key if the [Flag Approvals](https://docs.launchdarkly.com/home/feature-workflows/approvals) feature is enabled.  Only the `canReviewOwnRequest`, `canApplyDeclinedChanges`, `minNumApprovals`, `required` and `requiredApprovalTagsfields` are editable.  If you try to patch the environment by setting both `required` and `requiredApprovalTags`, the request fails and an error appears. You can specify either required approvals for all flags in an environment or those with specific tags, but not both. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import environments_api
from launchdarkly_api.model.environment import Environment
from launchdarkly_api.model.json_patch import JSONPatch
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.status_conflict_error_rep import StatusConflictErrorRep
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = environments_api.EnvironmentsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    json_patch = JSONPatch([
        PatchOperation(
            op="replace",
            path="/exampleField",
            value=None,
        ),
    ]) # JSONPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update environment
        api_response = api_instance.patch_environment(project_key, environment_key, json_patch)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling EnvironmentsApi->patch_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **json_patch** | [**JSONPatch**](JSONPatch.md)|  |

### Return type

[**Environment**](Environment.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Environment response JSON |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_environment**
> Environment post_environment(project_key, environment_post)

Create environment

> ### Approval settings > > The `approvalSettings` key is only returned when the Flag Approvals feature is enabled. > > You cannot update approval settings when creating new environments. Update approval settings with the PATCH Environment API.  Create a new environment in a specified project with a given name, key, swatch color, and default TTL. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import environments_api
from launchdarkly_api.model.environment import Environment
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.environment_post import EnvironmentPost
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.status_conflict_error_rep import StatusConflictErrorRep
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = environments_api.EnvironmentsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_post = EnvironmentPost(
        name="My Environment",
        key="my-environment",
        color="F5A623",
        default_ttl=5,
        secure_mode=True,
        default_track_events=False,
        confirm_changes=False,
        require_comments=False,
        tags=["ops"],
        source=SourceEnv(
            key="key_example",
            version=1,
        ),
    ) # EnvironmentPost | 

    # example passing only required values which don't have defaults set
    try:
        # Create environment
        api_response = api_instance.post_environment(project_key, environment_post)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling EnvironmentsApi->post_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_post** | [**EnvironmentPost**](EnvironmentPost.md)|  |

### Return type

[**Environment**](Environment.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful environment response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_environment_mobile_key**
> Environment reset_environment_mobile_key(project_key, environment_key)

Reset environment mobile SDK key

Reset an environment's mobile key. The optional expiry for the old key is deprecated for this endpoint, so the old key will always expire immediately.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import environments_api
from launchdarkly_api.model.environment import Environment
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = environments_api.EnvironmentsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key

    # example passing only required values which don't have defaults set
    try:
        # Reset environment mobile SDK key
        api_response = api_instance.reset_environment_mobile_key(project_key, environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling EnvironmentsApi->reset_environment_mobile_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |

### Return type

[**Environment**](Environment.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful environment response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_environment_sdk_key**
> Environment reset_environment_sdk_key(project_key, environment_key)

Reset environment SDK key

Reset an environment's SDK key with an optional expiry time for the old key.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import environments_api
from launchdarkly_api.model.environment import Environment
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with launchdarkly_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = environments_api.EnvironmentsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    expiry = 1 # int | The time at which you want the old SDK key to expire, in UNIX milliseconds. By default, the key expires immediately. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reset environment SDK key
        api_response = api_instance.reset_environment_sdk_key(project_key, environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling EnvironmentsApi->reset_environment_sdk_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reset environment SDK key
        api_response = api_instance.reset_environment_sdk_key(project_key, environment_key, expiry=expiry)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling EnvironmentsApi->reset_environment_sdk_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **expiry** | **int**| The time at which you want the old SDK key to expire, in UNIX milliseconds. By default, the key expires immediately. | [optional]

### Return type

[**Environment**](Environment.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful environment response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

