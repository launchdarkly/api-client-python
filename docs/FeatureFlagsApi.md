# launchdarkly_api.FeatureFlagsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_feature_flag**](FeatureFlagsApi.md#copy_feature_flag) | **POST** /api/v2/flags/{projectKey}/{featureFlagKey}/copy | Copy feature flag
[**delete_feature_flag**](FeatureFlagsApi.md#delete_feature_flag) | **DELETE** /api/v2/flags/{projectKey}/{featureFlagKey} | Delete feature flag
[**get_expiring_user_targets**](FeatureFlagsApi.md#get_expiring_user_targets) | **GET** /api/v2/flags/{projectKey}/{featureFlagKey}/expiring-user-targets/{environmentKey} | Get expiring user targets for feature flag
[**get_feature_flag**](FeatureFlagsApi.md#get_feature_flag) | **GET** /api/v2/flags/{projectKey}/{featureFlagKey} | Get feature flag
[**get_feature_flag_status**](FeatureFlagsApi.md#get_feature_flag_status) | **GET** /api/v2/flag-statuses/{projectKey}/{environmentKey}/{featureFlagKey} | Get feature flag status
[**get_feature_flag_status_across_environments**](FeatureFlagsApi.md#get_feature_flag_status_across_environments) | **GET** /api/v2/flag-status/{projectKey}/{featureFlagKey} | Get flag status across environments
[**get_feature_flag_statuses**](FeatureFlagsApi.md#get_feature_flag_statuses) | **GET** /api/v2/flag-statuses/{projectKey}/{environmentKey} | List feature flag statuses
[**get_feature_flags**](FeatureFlagsApi.md#get_feature_flags) | **GET** /api/v2/flags/{projectKey} | List feature flags
[**patch_expiring_user_targets**](FeatureFlagsApi.md#patch_expiring_user_targets) | **PATCH** /api/v2/flags/{projectKey}/{featureFlagKey}/expiring-user-targets/{environmentKey} | Update expiring user targets on feature flag
[**patch_feature_flag**](FeatureFlagsApi.md#patch_feature_flag) | **PATCH** /api/v2/flags/{projectKey}/{featureFlagKey} | Update feature flag
[**post_feature_flag**](FeatureFlagsApi.md#post_feature_flag) | **POST** /api/v2/flags/{projectKey} | Create a feature flag


# **copy_feature_flag**
> FeatureFlag copy_feature_flag(project_key, feature_flag_key, flag_copy_config_post)

Copy feature flag

 > ### Copying flag settings is an Enterprise feature > > Copying flag settings is available to customers on an Enterprise plan. To learn more, [read about our pricing](https://launchdarkly.com/pricing/). To upgrade your plan, [contact Sales](https://launchdarkly.com/contact-sales/).  Copy flag settings from a source environment to a target environment.  By default, this operation copies the entire flag configuration. You can use the `includedActions` or `excludedActions` to specify that only part of the flag configuration is copied.  If you provide the optional `currentVersion` of a flag, this operation tests to ensure that the current flag version in the environment matches the version you've specified. The operation rejects attempts to copy flag settings if the environment's current version  of the flag does not match the version you've specified. You can use this to enforce optimistic locking on copy attempts. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.flag_copy_config_post import FlagCopyConfigPost
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.feature_flag import FeatureFlag
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
    api_instance = feature_flags_api.FeatureFlagsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key. The key identifies the flag in your code.
    flag_copy_config_post = FlagCopyConfigPost(
        source=FlagCopyConfigEnvironment(
            key="key_example",
            current_version=1,
        ),
        target=FlagCopyConfigEnvironment(
            key="key_example",
            current_version=1,
        ),
        comment="comment_example",
        included_actions=["updateOn"],
        excluded_actions=["updateOn"],
    ) # FlagCopyConfigPost | 

    # example passing only required values which don't have defaults set
    try:
        # Copy feature flag
        api_response = api_instance.copy_feature_flag(project_key, feature_flag_key, flag_copy_config_post)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->copy_feature_flag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key. The key identifies the flag in your code. |
 **flag_copy_config_post** | [**FlagCopyConfigPost**](FlagCopyConfigPost.md)|  |

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Global flag response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**405** | Method not allowed |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feature_flag**
> delete_feature_flag(project_key, feature_flag_key)

Delete feature flag

Delete a feature flag in all environments. Use with caution: only delete feature flags your application no longer uses.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
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
    api_instance = feature_flags_api.FeatureFlagsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key. The key identifies the flag in your code.

    # example passing only required values which don't have defaults set
    try:
        # Delete feature flag
        api_instance.delete_feature_flag(project_key, feature_flag_key)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->delete_feature_flag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key. The key identifies the flag in your code. |

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
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expiring_user_targets**
> ExpiringUserTargetGetResponse get_expiring_user_targets(project_key, environment_key, feature_flag_key)

Get expiring user targets for feature flag

Get a list of user targets on a feature flag that are scheduled for removal.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.expiring_user_target_get_response import ExpiringUserTargetGetResponse
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
    api_instance = feature_flags_api.FeatureFlagsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key

    # example passing only required values which don't have defaults set
    try:
        # Get expiring user targets for feature flag
        api_response = api_instance.get_expiring_user_targets(project_key, environment_key, feature_flag_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_expiring_user_targets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **feature_flag_key** | **str**| The feature flag key |

### Return type

[**ExpiringUserTargetGetResponse**](ExpiringUserTargetGetResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expiring user target response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flag**
> FeatureFlag get_feature_flag(project_key, feature_flag_key)

Get feature flag

Get a single feature flag by key. By default, this returns the configurations for all environments. You can filter environments with the `env` query parameter. For example, setting `env=production` restricts the returned configurations to just the `production` environment.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.feature_flag import FeatureFlag
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
    api_instance = feature_flags_api.FeatureFlagsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    env = "env_example" # str | Filter configurations by environment (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get feature flag
        api_response = api_instance.get_feature_flag(project_key, feature_flag_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get feature flag
        api_response = api_instance.get_feature_flag(project_key, feature_flag_key, env=env)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **env** | **str**| Filter configurations by environment | [optional]

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Global flag response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flag_status**
> FlagStatusRep get_feature_flag_status(project_key, environment_key, feature_flag_key)

Get feature flag status

Get the status for a particular feature flag.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.flag_status_rep import FlagStatusRep
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
    api_instance = feature_flags_api.FeatureFlagsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key

    # example passing only required values which don't have defaults set
    try:
        # Get feature flag status
        api_response = api_instance.get_feature_flag_status(project_key, environment_key, feature_flag_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flag_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **feature_flag_key** | **str**| The feature flag key |

### Return type

[**FlagStatusRep**](FlagStatusRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag status response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flag_status_across_environments**
> FeatureFlagStatusAcrossEnvironments get_feature_flag_status_across_environments(project_key, feature_flag_key)

Get flag status across environments

Get the status for a particular feature flag across environments.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.feature_flag_status_across_environments import FeatureFlagStatusAcrossEnvironments
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
    api_instance = feature_flags_api.FeatureFlagsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    env = "env_example" # str | Optional environment filter (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get flag status across environments
        api_response = api_instance.get_feature_flag_status_across_environments(project_key, feature_flag_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flag_status_across_environments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get flag status across environments
        api_response = api_instance.get_feature_flag_status_across_environments(project_key, feature_flag_key, env=env)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flag_status_across_environments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **env** | **str**| Optional environment filter | [optional]

### Return type

[**FeatureFlagStatusAcrossEnvironments**](FeatureFlagStatusAcrossEnvironments.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag status across environments response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flag_statuses**
> FeatureFlagStatuses get_feature_flag_statuses(project_key, environment_key)

List feature flag statuses

Get a list of statuses for all feature flags. The status includes the last time the feature flag was requested, as well as a state, which is one of the following:  - `new`: the feature flag was created within the last seven days, and has not been requested yet - `active`: the feature flag was requested by your servers or clients within the last seven days - `inactive`: the feature flag was created more than seven days ago, and hasn't been requested by your servers or clients within the past seven days - `launched`: one variation of the feature flag has been rolled out to all your users for at least 7 days 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.feature_flag_statuses import FeatureFlagStatuses
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
    api_instance = feature_flags_api.FeatureFlagsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key

    # example passing only required values which don't have defaults set
    try:
        # List feature flag statuses
        api_response = api_instance.get_feature_flag_statuses(project_key, environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flag_statuses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |

### Return type

[**FeatureFlagStatuses**](FeatureFlagStatuses.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag Statuses collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flags**
> FeatureFlags get_feature_flags(project_key)

List feature flags

Get a list of all features in the given project. By default, each feature includes configurations for each environment. You can filter environments with the `env` query parameter. For example, setting `env=production` restricts the returned configurations to just your production environment. You can also filter feature flags by tag with the tag query parameter.  ### Filtering flags  You can filter on certain fields using the `filter` query parameter. For example, setting `filter=query:dark-mode,tags:beta+test` matches flags with the string `dark-mode` in their key or name, ignoring case, which also have the tags `beta` and `test`.  The `filter` query parameter supports the following arguments:  - `query` is a string that matches against the flags' keys and names. It is not case sensitive. - `archived` is a boolean with values of `true` or `false` that filters the list to archived flags. Setting the value to `true` returns only archived flags. When this is absent, only unarchived flags are returned. - `type` is a string allowing filtering to `temporary` or `permanent` flags. - `status` is a string allowing filtering to `new`, `inactive`, `active`, or `launched` flags in the specified environment. This filter also requires a `filterEnv` field to be set to a valid environment. For example: `filter=status:active,filterEnv:production`. - `tags` is a `+` separated list of tags. It filters the list to members who have all of the tags in the list. For example: `filter=tags:beta+test`. - `hasExperiment` is a boolean with values of `true` or `false` that returns any flags that are used in an experiment. - `hasDataExport` is a boolean with values of `true` or `false` that returns any flags that are exporting data in the specified environment. This includes flags that are exporting data from Experimentation. This filter also requires that you set a `filterEnv` field to a valid environment key. For example: `filter=hasDataExport:true,filterEnv:production` - `evaluated` is an object that contains a key of `after` and a value in Unix time in milliseconds. This returns all flags that have been evaluated since the time you specify in the environment provided. This filter also requires you to set a `filterEnv` field to a valid environment. For example: `filter=evaluated:{\"after\": 1590768455282},filterEnv:production`. - `filterEnv` is a string with the key of a valid environment. You can use the `filterEnv` field for filters that are environment-specific. If there are multiple environment-specific filters, you should only declare this parameter once. For example: `filter=evaluated:{\"after\": 1590768455282},filterEnv:production,status:active`.  By default, this returns all flags. You can page through the list with the `limit` parameter and by following the `first`, `prev`, `next`, and `last` links in the returned `_links` field. These links will not be present if the pages they refer to don't exist. For example, the `first` and `prev` links will be missing from the response on the first page.  ### Sorting flags  You can sort flags based on the following fields:  - `creationDate` sorts by the creation date of the flag. - `key` sorts by the key of the flag. - `maintainerId` sorts by the flag maintainer. - `name` sorts by flag name. - `tags` sorts by tags. - `targetingModifiedDate` sorts by the date that the flag's targeting rules were last modified in a given environment. It must be used with `env` parameter and it can not be combined with any other sort. If multiple `env` values are provided, it will perform sort using the first one. For example, `sort=-targetingModifiedDate&env=production&env=staging` returns results sorted by `targetingModifiedDate` for the `production` environment. - `type` sorts by flag type  All fields are sorted in ascending order by default. To sort in descending order, prefix the field with a dash ( - ). For example, `sort=-name` sorts the response by flag name in descending order. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.feature_flags import FeatureFlags
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
    api_instance = feature_flags_api.FeatureFlagsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    env = "env_example" # str | Filter configurations by environment (optional)
    tag = "tag_example" # str | Filter feature flags by tag (optional)
    limit = 1 # int | The number of feature flags to return. Defaults to -1, which returns all flags (optional)
    offset = 1 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    archived = True # bool | A boolean to filter the list to archived flags. When this is absent, only unarchived flags will be returned (optional)
    summary = True # bool | By default in API version >= 1, flags will _not_ include their list of prerequisites, targets or rules.  Set summary=0 to include these fields for each flag returned (optional)
    filter = "filter_example" # str | A comma-separated list of filters. Each filter is of the form field:value. Read the endpoint description for a full list of available filter fields. (optional)
    sort = "sort_example" # str | A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order. Read the endpoint description for a full list of available sort fields. (optional)
    compare = True # bool | A boolean to filter results by only flags that have differences between environments (optional)

    # example passing only required values which don't have defaults set
    try:
        # List feature flags
        api_response = api_instance.get_feature_flags(project_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List feature flags
        api_response = api_instance.get_feature_flags(project_key, env=env, tag=tag, limit=limit, offset=offset, archived=archived, summary=summary, filter=filter, sort=sort, compare=compare)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **env** | **str**| Filter configurations by environment | [optional]
 **tag** | **str**| Filter feature flags by tag | [optional]
 **limit** | **int**| The number of feature flags to return. Defaults to -1, which returns all flags | [optional]
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional]
 **archived** | **bool**| A boolean to filter the list to archived flags. When this is absent, only unarchived flags will be returned | [optional]
 **summary** | **bool**| By default in API version &gt;&#x3D; 1, flags will _not_ include their list of prerequisites, targets or rules.  Set summary&#x3D;0 to include these fields for each flag returned | [optional]
 **filter** | **str**| A comma-separated list of filters. Each filter is of the form field:value. Read the endpoint description for a full list of available filter fields. | [optional]
 **sort** | **str**| A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order. Read the endpoint description for a full list of available sort fields. | [optional]
 **compare** | **bool**| A boolean to filter results by only flags that have differences between environments | [optional]

### Return type

[**FeatureFlags**](FeatureFlags.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Global flags collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_expiring_user_targets**
> ExpiringUserTargetPatchResponse patch_expiring_user_targets(project_key, environment_key, feature_flag_key, patch_flags_request)

Update expiring user targets on feature flag

Schedule a user for removal from individual targeting on a feature flag. The flag must already individually target the user.  You can add, update, or remove a scheduled removal date. You can only schedule a user for removal on a single variation per flag.  This request only supports semantic patches. To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](/reference#updates-using-semantic-patch).  ### Instructions  #### addExpireUserTargetDate  Adds a date and time that LaunchDarkly will remove the user from the flag's individual targeting.  ##### Parameters  * `value`: The time, in Unix milliseconds, when LaunchDarkly should remove the user from individual targeting for this flag * `variationId`: The version of the flag variation to update. You can retrieve this by making a GET request for the flag. * `userKey`: The user key for the user to remove from individual targeting  #### updateExpireUserTargetDate  Updates the date and time that LaunchDarkly will remove the user from the flag's individual targeting.  ##### Parameters  * `value`: The time, in Unix milliseconds, when LaunchDarkly should remove the user from individual targeting for this flag * `variationId`: The version of the flag variation to update. You can retrieve this by making a GET request for the flag. * `userKey`: The user key for the user to remove from individual targeting  #### removeExpireUserTargetDate  Removes the scheduled removal of the user from the flag's individual targeting. The user will remain part of the flag's individual targeting until you explicitly remove them, or until you schedule another removal.  ##### Parameters  * `variationId`: The version of the flag variation to update. You can retrieve this by making a GET request for the flag. * `userKey`: The user key for the user to remove from individual targeting 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.expiring_user_target_patch_response import ExpiringUserTargetPatchResponse
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.patch_flags_request import PatchFlagsRequest
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
    api_instance = feature_flags_api.FeatureFlagsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    patch_flags_request = PatchFlagsRequest(
        comment="optional comment",
        instructions=[
            Instruction(
                key=None,
            ),
        ],
    ) # PatchFlagsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update expiring user targets on feature flag
        api_response = api_instance.patch_expiring_user_targets(project_key, environment_key, feature_flag_key, patch_flags_request)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->patch_expiring_user_targets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **feature_flag_key** | **str**| The feature flag key |
 **patch_flags_request** | [**PatchFlagsRequest**](PatchFlagsRequest.md)|  |

### Return type

[**ExpiringUserTargetPatchResponse**](ExpiringUserTargetPatchResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expiring user target response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_feature_flag**
> FeatureFlag patch_feature_flag(project_key, feature_flag_key, patch_with_comment)

Update feature flag

Perform a partial update to a feature flag. The request body must be a valid semantic patch or JSON patch.  ### Using semantic patches on a feature flag  To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](/reference#updates-using-semantic-patch).  The body of a semantic patch request for updating feature flags requires an `environmentKey` in addition to `instructions` and an optional `comment`. The body of the request takes the following properties:  * `comment` (string): (Optional) A description of the update. * `environmentKey` (string): (Required) The key of the LaunchDarkly environment. * `instructions` (array): (Required) A list of actions the update should perform. Each action in the list must be an object with a `kind` property that indicates the instruction. If the action requires parameters, you must include those parameters as additional fields in the object.  ### Instructions  Semantic patch requests support the following `kind` instructions for updating feature flags.  <details> <summary>Click to expand instructions for turning flags on and off</summary>  #### turnFlagOff  Sets the flag's targeting state to **Off**.  For example, to turn a flag off, use this request body:  ```json {   \"environmentKey\": \"example-environment-key\",   \"instructions\": [ { \"kind\": \"turnFlagOff\" } ] } ```  #### turnFlagOn  Sets the flag's targeting state to **On**.  For example, to turn a flag on, use this request body:  ```json {   \"environmentKey\": \"example-environment-key\",   \"instructions\": [ { \"kind\": \"turnFlagOn\" } ] } ```  </details><br />  <details> <summary>Click to expand instructions for working with targeting and variations</summary>  #### addClauses  Adds the given clauses to the rule indicated by `ruleId`.  ##### Parameters  - `ruleId`: ID of a rule in the flag. - `clauses`: Array of clause objects, with `attribute` (string), `op` (string), `negate` (boolean), and `values` (array of strings, numbers, or dates) properties.  #### addPrerequisite  Adds the flag indicated by `key` with variation `variationId` as a prerequisite to the flag in the path parameter.  ##### Parameters  - `key`: Flag key of the prerequisite flag. - `variationId`: ID of a variation of the prerequisite flag.  #### addRule  Adds a new targeting rule to the flag. The rule may contain `clauses` and serve the variation that `variationId` indicates, or serve a percentage rollout that `rolloutWeights` and `rolloutBucketBy` indicate.  If you set `beforeRuleId`, this adds the new rule before the indicated rule. Otherwise, adds the new rule to the end of the list.  ##### Parameters  - `clauses`: Array of clause objects, with `attribute` (string), `op` (string), `negate` (boolean), and `values` (array of strings, numbers, or dates) properties. - `beforeRuleId`: (Optional) ID of a flag rule. - `variationId`: ID of a variation of the flag. - `rolloutWeights`: Map of `variationId` to weight, in thousandths of a percent (0-100000). - `rolloutBucketBy`: (Optional) User attribute.  #### addUserTargets  Adds user keys to the individual user targets for the variation that `variationId` specifies. Returns an error if this causes the flag to target the same user key in multiple variations.  ##### Parameters  - `values`: List of user keys. - `variationId`: ID of a variation on the flag.  #### addValuesToClause  Adds `values` to the values of the clause that `ruleId` and `clauseId` indicate.  ##### Parameters  - `ruleId`: ID of a rule in the flag. - `clauseId`: ID of a clause in that rule. - `values`: Array of strings.  #### clearUserTargets  Removes all individual user targets from the variation that `variationId` specifies.  ##### Parameters  - `variationId`: ID of a variation on the flag.  #### removeClauses  Removes the clauses specified by `clauseIds` from the rule indicated by `ruleId`.  ##### Parameters  - `ruleId`: ID of a rule in the flag. - `clauseIds`: Array of IDs of clauses in the rule.  #### removePrerequisite  Removes the prerequisite flag indicated by `key`. Does nothing if this prerequisite does not exist.  ##### Parameters  - `key`: Flag key of an existing prerequisite flag.  #### removeRule  Removes the targeting rule specified by `ruleId`. Does nothing if the rule does not exist.  ##### Parameters  - `ruleId`: ID of a rule in the flag.  #### removeUserTargets  Removes user keys from the individual user targets for the variation that `variationId` specifies. Does nothing if the flag does not target the user keys.  ##### Parameters  - `values`: List of user keys. - `variationId`: ID of a flag variation.  #### removeValuesFromClause  Removes `values` from the values of the clause indicated by `ruleId` and `clauseId`.  ##### Parameters  - `ruleId`: ID of a rule in the flag. - `clauseId`: ID of a clause in that rule. - `values`: Array of strings.  #### reorderRules  Rearranges the rules to match the order given in `ruleIds`. Returns an error if `ruleIds` does not match the current set of rules on the flag.  ##### Parameters  - `ruleIds`: Array of IDs of all rules in the flag.  #### replacePrerequisites  Removes all existing prerequisites and replaces them with the list you provide.  ##### Parameters  - `prerequisites`: A list of prerequisites. Each item in the list must include a flag `key` and `variationId`.  For example, to replace prerequisites, use this request body:  ```json {   \"environmentKey\": \"example-environment-key\",   \"instructions\": [     {       \"kind\": \"replacePrerequisites\",       \"prerequisites\": [         {           \"key\": \"prereq-flag-key\",           \"variationId\": \"variation-1\"         },         {           \"key\": \"another-prereq-flag-key\",           \"variationId\": \"variation-2\"         }       ]     }   ] } ```  #### replaceRules  Removes all targeting rules for the flag and replaces them with the list you provide.  ##### Parameters  - `rules`: A list of rules.  For example, to replace rules, use this request body:  ```json {   \"environmentKey\": \"example-environment-key\",   \"instructions\": [     {       \"kind\": \"replaceRules\",       \"rules\": [         {           \"variationId\": \"variation-1\",           \"description\": \"myRule\",           \"clauses\": [             {               \"attribute\": \"segmentMatch\",               \"op\": \"segmentMatch\",               \"values\": [\"test\"]             }           ],           \"trackEvents\": true         }       ]     }   ] } ```  #### replaceUserTargets  Removes all existing user targeting and replaces it with the list of targets you provide.  ##### Parameters  - `targets`: A list of user targeting. Each item in the list must include a `variationId` and a list of `values`.  For example, to replace user targets, use this request body:  ```json {   \"environmentKey\": \"example-environment-key\",   \"instructions\": [     {       \"kind\": \"replaceUserTargets\",       \"targets\": [         {           \"variationId\": \"variation-1\",           \"values\": [\"blah\", \"foo\", \"bar\"]         },         {           \"variationId\": \"variation-2\",           \"values\": [\"abc\", \"def\"]         }       ]     }       ] } ```  #### updateClause  Replaces the clause indicated by `ruleId` and `clauseId` with `clause`.  ##### Parameters  - `ruleId`: ID of a rule in the flag. - `clauseId`: ID of a clause in that rule. - `clause`: New `clause` object, with `attribute` (string), `op` (string), `negate` (boolean), and `values` (array of strings, numbers, or dates) properties.  #### updateFallthroughVariationOrRollout  Updates the default or \"fallthrough\" rule for the flag, which the flag serves when a user matches none of the targeting rules. The rule can serve either the variation that `variationId` indicates, or a percent rollout that `rolloutWeights` and `rolloutBucketBy` indicate.  ##### Parameters  - `variationId`: ID of a variation of the flag. or - `rolloutWeights`: Map of `variationId` to weight, in thousandths of a percent (0-100000). - `rolloutBucketBy`: Optional user attribute.  #### updateOffVariation  Updates the default off variation to `variationId`. The flag serves the default off variation when the flag's targeting is **Off**.  ##### Parameters  - `variationId`: ID of a variation of the flag.  #### updatePrerequisite  Changes the prerequisite flag that `key` indicates to use the variation that `variationId` indicates. Returns an error if this prerequisite does not exist.  ##### Parameters  - `key`: Flag key of an existing prerequisite flag. - `variationId`: ID of a variation of the prerequisite flag.  #### updateRuleDescription  Updates the description of the feature flag rule.  ##### Parameters  - `description`: The new human-readable description for this rule. - `ruleId`: The ID of the rule. You can retrieve this by making a GET request for the flag.  #### updateRuleTrackEvents  Updates whether or not LaunchDarkly tracks events for the feature flag associated with this rule.  ##### Parameters  - `ruleId`: The ID of the rule. You can retrieve this by making a GET request for the flag. - `trackEvents`: Whether or not events are tracked.  #### updateRuleVariationOrRollout  Updates what `ruleId` serves when its clauses evaluate to true. The rule can serve either the variation that `variationId` indicates, or a percent rollout that `rolloutWeights` and `rolloutBucketBy` indicate.  ##### Parameters  - `ruleId`: ID of a rule in the flag. - `variationId`: ID of a variation of the flag.    or  - `rolloutWeights`: Map of `variationId` to weight, in thousandths of a percent (0-100000). - `rolloutBucketBy`: Optional user attribute.  #### updateTrackEvents  Updates whether or not LaunchDarkly tracks events for the feature flag, for all rules.  ##### Parameters  - `trackEvents`: Whether or not events are tracked.  #### updateTrackEventsFallthrough  Updates whether or not LaunchDarkly tracks events for the feature flag, for the default rule.  ##### Parameters  - `trackEvents`: Whether or not events are tracked.  </details><br />  <details> <summary>Click to expand instructions for updating flag settings</summary>  #### addTags  Adds tags to the feature flag.  ##### Parameters  - `values`: A list of tags to add.  #### makeFlagPermanent  Marks the feature flag as permanent. LaunchDarkly does not prompt you to remove permanent flags, even if one variation is rolled out to all your users.  #### makeFlagTemporary  Marks the feature flag as temporary.  #### removeMaintainer  Removes the flag's maintainer. To set a new maintainer, use the flag's **Settings** tab in the LaunchDarkly user interface.  #### removeTags  Removes tags from the feature flag.  ##### Parameters  - `values`: A list of tags to remove.  #### turnOffClientSideAvailability  Turns off client-side SDK availability for the flag. This is equivalent to unchecking the **SDKs using Mobile Key** and/or **SDKs using client-side ID** boxes for the flag. If you're using a client-side or mobile SDK, you must expose your feature flags in order for the client-side or mobile SDKs to evaluate them.  ##### Parameters  - `value`: Use \"usingMobileKey\" to turn on availability for mobile SDKs. Use \"usingEnvironmentId\" to turn on availability for client-side SDKs.  #### turnOnClientSideAvailability  Turns on client-side SDK availability for the flag. This is equivalent to unchecking the **SDKs using Mobile Key** and/or **SDKs using client-side ID** boxes for the flag. If you're using a client-side or mobile SDK, you must expose your feature flags in order for the client-side or mobile SDKs to evaluate them.  ##### Parameters  - `value`: Use \"usingMobileKey\" to turn on availability for mobile SDKs. Use \"usingEnvironmentId\" to turn on availability for client-side SDKs.  #### updateDescription  Updates the feature flag description.  ##### Parameters  - `value`: The new description.  #### updateName  Updates the feature flag name.  ##### Parameters  - `value`: The new name.  </details><br />  <details> <summary>Click to expand instructions for updating the flag lifecycle</summary>  #### archiveFlag  Archives the feature flag. This retires it from LaunchDarkly without deleting it. You cannot archive a flag that is a prerequisite of other flags.  #### deleteFlag  Deletes the feature flag and its rules. You cannot restore a deleted flag. If this flag is requested again, the flag value defined in code will be returned for all users.  #### restoreFlag  Restores the feature flag if it was previously archived.  </details>  ### Example  The body of a single semantic patch can contain many different instructions.  <details> <summary>Click to expand example semantic patch request body</summary>  ```json {   \"environmentKey\": \"production\",   \"instructions\": [     {       \"kind\": \"turnFlagOn\"     },     {       \"kind\": \"turnFlagOff\"     },     {       \"kind\": \"addUserTargets\",       \"variationId\": \"8bfb304e-d516-47e5-8727-e7f798e8992d\",       \"values\": [\"userId\", \"userId2\"]     },     {       \"kind\": \"removeUserTargets\",       \"variationId\": \"8bfb304e-d516-47e5-8727-e7f798e8992d\",       \"values\": [\"userId3\", \"userId4\"]     },     {       \"kind\": \"updateFallthroughVariationOrRollout\",       \"rolloutWeights\": {         \"variationId\": 50000,         \"variationId2\": 50000       },       \"rolloutBucketBy\": null     },     {       \"kind\": \"addRule\",       \"clauses\": [         {           \"attribute\": \"segmentMatch\",           \"negate\": false,           \"values\": [\"test-segment\"]         }       ],       \"variationId\": null,       \"rolloutWeights\": {         \"variationId\": 50000,         \"variationId2\": 50000       },       \"rolloutBucketBy\": \"key\"     },     {       \"kind\": \"removeRule\",       \"ruleId\": \"99f12464-a429-40fc-86cc-b27612188955\"     },     {       \"kind\": \"reorderRules\",       \"ruleIds\": [\"2f72974e-de68-4243-8dd3-739582147a1f\", \"8bfb304e-d516-47e5-8727-e7f798e8992d\"]     },     {       \"kind\": \"addClauses\",       \"ruleId\": \"1134\",       \"clauses\": [         {           \"attribute\": \"email\",           \"op\": \"in\",           \"negate\": false,           \"values\": [\"test@test.com\"]         }       ]     },     {       \"kind\": \"removeClauses\",       \"ruleId\": \"1242529\",       \"clauseIds\": [\"8bfb304e-d516-47e5-8727-e7f798e8992d\"]     },     {       \"kind\": \"updateClause\",       \"ruleId\": \"2f72974e-de68-4243-8dd3-739582147a1f\",       \"clauseId\": \"309845\",       \"clause\": {         \"attribute\": \"segmentMatch\",         \"negate\": false,         \"values\": [\"test-segment\"]       }     },     {       \"kind\": \"updateRuleVariationOrRollout\",       \"ruleId\": \"2342\",       \"rolloutWeights\": null,       \"rolloutBucketBy\": null     },     {       \"kind\": \"updateOffVariation\",       \"variationId\": \"3242453\"     },     {       \"kind\": \"addPrerequisite\",       \"variationId\": \"234235\",       \"key\": \"flagKey2\"     },     {       \"kind\": \"updatePrerequisite\",       \"variationId\": \"234235\",       \"key\": \"flagKey2\"     },     {       \"kind\": \"removePrerequisite\",       \"key\": \"flagKey\"     }   ] } ``` </details>  ### Using JSON Patches on a feature flag If you do not include the header described above, you can use [JSON patch](/reference#updates-using-json-patch).  When using the update feature flag endpoint to add individual users to a specific variation, there are two different patch documents, depending on whether users are already being individually targeted for the variation.  If a flag variation already has users individually targeted, the path for the JSON Patch operation is:  ```json {   \"op\": \"add\",   \"path\": \"/environments/devint/targets/0/values/-\",   \"value\": \"TestClient10\" } ```  If a flag variation does not already have users individually targeted, the path for the JSON Patch operation is:  ```json [   {     \"op\": \"add\",     \"path\": \"/environments/devint/targets/-\",     \"value\": { \"variation\": 0, \"values\": [\"TestClient10\"] }   } ] ```   ### Required approvals If a request attempts to alter a flag configuration in an environment where approvals are required for the flag, the request will fail with a 405. Changes to the flag configuration in that environment will require creating an [approval request](/tag/Approvals) or a [workflow](/tag/Workflows-(beta)).  ### Conflicts If a flag configuration change made through this endpoint would cause a pending scheduled change or approval request to fail, this endpoint will return a 400. You can ignore this check by adding an `ignoreConflicts` query parameter set to `true`. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.patch_with_comment import PatchWithComment
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.feature_flag import FeatureFlag
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
    api_instance = feature_flags_api.FeatureFlagsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key. The key identifies the flag in your code.
    patch_with_comment = PatchWithComment(
        patch=JSONPatch([
            PatchOperation(
                op="replace",
                path="/exampleField",
                value=None,
            ),
        ]),
        comment="comment_example",
    ) # PatchWithComment | 

    # example passing only required values which don't have defaults set
    try:
        # Update feature flag
        api_response = api_instance.patch_feature_flag(project_key, feature_flag_key, patch_with_comment)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->patch_feature_flag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key. The key identifies the flag in your code. |
 **patch_with_comment** | [**PatchWithComment**](PatchWithComment.md)|  |

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Global flag response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Approval is required to make this request |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_feature_flag**
> FeatureFlag post_feature_flag(project_key, feature_flag_body)

Create a feature flag

Create a feature flag with the given name, key, and variations.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.feature_flag_body import FeatureFlagBody
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.feature_flag import FeatureFlag
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
    api_instance = feature_flags_api.FeatureFlagsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_body = FeatureFlagBody(
        name="My flag",
        key="my-flag",
        description="This flag controls the example widgets",
        include_in_snippet=True,
        client_side_availability=ClientSideAvailabilityPost(
            using_environment_id=True,
            using_mobile_key=True,
        ),
        variations=[
            Variation(
                id="id_example",
                value=None,
                description="description_example",
                name="name_example",
            ),
        ],
        temporary=False,
        tags=["example-tag"],
        custom_properties=CustomProperties(
            key=CustomProperty(
                name="Jira issues",
                value=["is-123","is-456"],
            ),
        ),
        defaults=Defaults(
            on_variation=0,
            off_variation=1,
        ),
    ) # FeatureFlagBody | 
    clone = "clone_example" # str | The key of the feature flag to be cloned. The key identifies the flag in your code. For example, setting `clone=flagKey` copies the full targeting configuration for all environments, including `on/off` state, from the original flag to the new flag. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a feature flag
        api_response = api_instance.post_feature_flag(project_key, feature_flag_body)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->post_feature_flag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a feature flag
        api_response = api_instance.post_feature_flag(project_key, feature_flag_body, clone=clone)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->post_feature_flag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_body** | [**FeatureFlagBody**](FeatureFlagBody.md)|  |
 **clone** | **str**| The key of the feature flag to be cloned. The key identifies the flag in your code. For example, setting &#x60;clone&#x3D;flagKey&#x60; copies the full targeting configuration for all environments, including &#x60;on/off&#x60; state, from the original flag to the new flag. | [optional]

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Global flag response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

