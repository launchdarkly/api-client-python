# launchdarkly_api.FeatureFlagsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_feature_flag**](FeatureFlagsApi.md#copy_feature_flag) | **POST** /api/v2/flags/{projKey}/{featureFlagKey}/copy | Copy feature flag
[**delete_feature_flag**](FeatureFlagsApi.md#delete_feature_flag) | **DELETE** /api/v2/flags/{projKey}/{key} | Delete feature flag
[**get_expiring_user_targets**](FeatureFlagsApi.md#get_expiring_user_targets) | **GET** /api/v2/flags/{projKey}/{flagKey}/expiring-user-targets/{envKey} | Get expiring user targets for feature flag
[**get_feature_flag**](FeatureFlagsApi.md#get_feature_flag) | **GET** /api/v2/flags/{projKey}/{key} | Get feature flag
[**get_feature_flag_status**](FeatureFlagsApi.md#get_feature_flag_status) | **GET** /api/v2/flag-statuses/{projKey}/{envKey}/{key} | Get feature flag status
[**get_feature_flag_status_across_environments**](FeatureFlagsApi.md#get_feature_flag_status_across_environments) | **GET** /api/v2/flag-status/{projKey}/{key} | Get flag status across environments
[**get_feature_flag_statuses**](FeatureFlagsApi.md#get_feature_flag_statuses) | **GET** /api/v2/flag-statuses/{projKey}/{envKey} | List feature flag statuses
[**get_feature_flags**](FeatureFlagsApi.md#get_feature_flags) | **GET** /api/v2/flags/{projKey} | List feature flags
[**patch_expiring_user_targets**](FeatureFlagsApi.md#patch_expiring_user_targets) | **PATCH** /api/v2/flags/{projKey}/{flagKey}/expiring-user-targets/{envKey} | Update expiring user targets on feature flag
[**patch_feature_flag**](FeatureFlagsApi.md#patch_feature_flag) | **PATCH** /api/v2/flags/{projKey}/{key} | Update feature flag
[**post_feature_flag**](FeatureFlagsApi.md#post_feature_flag) | **POST** /api/v2/flags/{projKey} | Create a feature flag


# **copy_feature_flag**
> FeatureFlag copy_feature_flag(proj_key, feature_flag_key, flag_copy_config_post)

Copy feature flag

The includedActions and excludedActions define the parts of the flag configuration that are copied or not copied. By default, the entire flag configuration is copied.  You can have either `includedActions` or `excludedActions` but not both.  Valid `includedActions` and `excludedActions` include:  - `updateOn` - `updatePrerequisites` - `updateTargets` - `updateRules` - `updateFallthrough` - `updateOffVariation`    The `source` and `target` must be JSON objects if using curl, specifying the environment key and (optional) current flag configuration version in that environment. For example:  ```json {   \"key\": \"production\",   \"currentVersion\": 3 } ```  If target is specified as above, the API will test to ensure that the current flag version in the `production` environment is `3`, and reject attempts to copy settings to `production` otherwise. You can use this to enforce optimistic locking on copy attempts. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.flag_copy_config_post import FlagCopyConfigPost
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
    proj_key = "projKey_example" # str | The project key.
    feature_flag_key = "featureFlagKey_example" # str | The feature flag's key. The key identifies the flag in your code.
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
        included_actions=[
            "updateOn",
        ],
        excluded_actions=[
            "updateOn",
        ],
    ) # FlagCopyConfigPost | 

    # example passing only required values which don't have defaults set
    try:
        # Copy feature flag
        api_response = api_instance.copy_feature_flag(proj_key, feature_flag_key, flag_copy_config_post)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->copy_feature_flag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. |
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
**400** | Invalid request body |  -  |
**401** | Invalid access token |  -  |
**405** | Method not allowed |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feature_flag**
> delete_feature_flag(proj_key, key)

Delete feature flag

Delete a feature flag in all environments. Use with caution: only delete feature flags your application no longer uses.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
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
    proj_key = "projKey_example" # str | The project key.
    key = "key_example" # str | The feature flag's key. The key identifies the flag in your code.

    # example passing only required values which don't have defaults set
    try:
        # Delete feature flag
        api_instance.delete_feature_flag(proj_key, key)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->delete_feature_flag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Action completed successfully |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expiring_user_targets**
> ExpiringUserTargetGetResponse get_expiring_user_targets(proj_key, env_key, flag_key)

Get expiring user targets for feature flag

Get a list of user targets on a feature flag that are scheduled for removal.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.expiring_user_target_get_response import ExpiringUserTargetGetResponse
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
    proj_key = "projKey_example" # str | The project key.
    env_key = "envKey_example" # str | The environment key.
    flag_key = "flagKey_example" # str | The feature flag key.

    # example passing only required values which don't have defaults set
    try:
        # Get expiring user targets for feature flag
        api_response = api_instance.get_expiring_user_targets(proj_key, env_key, flag_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_expiring_user_targets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **env_key** | **str**| The environment key. |
 **flag_key** | **str**| The feature flag key. |

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
**200** | User targeting expirations on feature flag response. |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flag**
> FeatureFlag get_feature_flag(proj_key, key)

Get feature flag

Get a single feature flag by key. By default, this returns the configurations for all environments. You can filter environments with the `env` query parameter. For example, setting `env=production` restricts the returned configurations to just the `production` environment.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
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
    proj_key = "projKey_example" # str | The project key
    key = "key_example" # str | The feature flag key
    env = "env_example" # str | Filter configurations by environment (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get feature flag
        api_response = api_instance.get_feature_flag(proj_key, key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get feature flag
        api_response = api_instance.get_feature_flag(proj_key, key, env=env)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **key** | **str**| The feature flag key |
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
> FlagStatusRep get_feature_flag_status(proj_key, env_key, key)

Get feature flag status

Get the status for a particular feature flag.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
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
    proj_key = "projKey_example" # str | The project key
    env_key = "envKey_example" # str | The environment key
    key = "key_example" # str | The feature flag key

    # example passing only required values which don't have defaults set
    try:
        # Get feature flag status
        api_response = api_instance.get_feature_flag_status(proj_key, env_key, key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flag_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **env_key** | **str**| The environment key |
 **key** | **str**| The feature flag key |

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
> FeatureFlagStatusAcrossEnvironments get_feature_flag_status_across_environments(proj_key, key)

Get flag status across environments

Get the status for a particular feature flag across environments.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
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
    proj_key = "projKey_example" # str | The project key
    key = "key_example" # str | The feature flag key
    env = "env_example" # str | Optional environment filter (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get flag status across environments
        api_response = api_instance.get_feature_flag_status_across_environments(proj_key, key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flag_status_across_environments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get flag status across environments
        api_response = api_instance.get_feature_flag_status_across_environments(proj_key, key, env=env)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flag_status_across_environments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **key** | **str**| The feature flag key |
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
> FeatureFlagStatuses get_feature_flag_statuses(proj_key, env_key)

List feature flag statuses

Get a list of statuses for all feature flags. The status includes the last time the feature flag was requested, as well as a state, which is one of the following:  - `new`: the feature flag was created within the last seven days, and has not been requested yet - `active`: the feature flag was requested by your servers or clients within the last seven days - `inactive`: the feature flag was created more than seven days ago, and hasn't been requested by your servers or clients within the past seven days - `launched`: one variation of the feature flag has been rolled out to all your users for at least 7 days 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.feature_flag_statuses import FeatureFlagStatuses
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
    proj_key = "projKey_example" # str | The project key
    env_key = "envKey_example" # str | Filter configurations by environment

    # example passing only required values which don't have defaults set
    try:
        # List feature flag statuses
        api_response = api_instance.get_feature_flag_statuses(proj_key, env_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flag_statuses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **env_key** | **str**| Filter configurations by environment |

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
> FeatureFlags get_feature_flags(proj_key)

List feature flags

Get a list of all features in the given project. By default, each feature includes configurations for each environment. You can filter environments with the env query parameter. For example, setting `env=production` restricts the returned configurations to just your production environment. You can also filter feature flags by tag with the tag query parameter.  We support the following fields for filters:  - `query` is a string that matches against the flags' keys and names. It is not case sensitive. - `archived` is a boolean to filter the list to archived flags. When this is absent, only unarchived flags are returned. - `type` is a string allowing filtering to `temporary` or `permanent` flags. - `status` is a string allowing filtering to `new`, `inactive`, `active`, or `launched` flags in the specified environment. This filter also requires a `filterEnv` field to be set to a valid environment. For example: `filter=status:active,filterEnv:production`. - `tags` is a + separated list of tags. It filters the list to members who have all of the tags in the list. - `hasExperiment` is a boolean with values of true or false and returns any flags that have an attached metric. - `hasDataExport` is a boolean with values of true or false and returns any flags that are currently exporting data in the specified environment. This includes flags that are exporting data via Experimentation. This filter also requires a `filterEnv` field to be set to a valid environment key. e.g. `filter=hasExperiment:true,filterEnv:production` - `evaluated` is an object that contains a key of `after` and a value in Unix time in milliseconds. This returns all flags that have been evaluated since the time you specify in the environment provided. This filter also requires a `filterEnv` field to be set to a valid environment. For example: `filter=evaluated:{\"after\": 1590768455282},filterEnv:production`. - `filterEnv` is a string with the key of a valid environment. The filterEnv field is used for filters that are environment specific. If there are multiple environment specific filters you should only declare this parameter once. For example: `filter=evaluated:{\"after\": 1590768455282},filterEnv:production,status:active`.  An example filter is `query:abc,tags:foo+bar`. This matches flags with the string `abc` in their key or name, ignoring case, which also have the tags `foo` and `bar`.  By default, this returns all flags. You can page through the list with the `limit` parameter and by following the `first`, `prev`, `next`, and `last` links in the returned `_links` field. These links will not be present if the pages they refer to don't exist. For example, the `first` and `prev` links will be missing from the response on the first page. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
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
    proj_key = "projKey_example" # str | The project key
    env = "env_example" # str | Filter configurations by environment (optional)
    tag = "tag_example" # str | Filter feature flags by tag (optional)
    limit = 1 # int | The number of feature flags to return. Defaults to -1, which returns all flags (optional)
    offset = 1 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next limit items (optional)
    query = "query_example" # str | A string that matches against the flags' keys and names. It is not case sensitive (optional)
    archived = True # bool | A boolean to filter the list to archived flags. When this is absent, only unarchived flags will be returned (optional)
    summary = True # bool | By default in API version >= 1, flags will _not_ include their list of prerequisites, targets or rules.  Set summary=0 to include these fields for each flag returned (optional)
    filter = "filter_example" # str | A comma-separated list of filters. Each filter is of the form field:value (optional)
    sort = "sort_example" # str | A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order (optional)

    # example passing only required values which don't have defaults set
    try:
        # List feature flags
        api_response = api_instance.get_feature_flags(proj_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List feature flags
        api_response = api_instance.get_feature_flags(proj_key, env=env, tag=tag, limit=limit, offset=offset, query=query, archived=archived, summary=summary, filter=filter, sort=sort)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->get_feature_flags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **env** | **str**| Filter configurations by environment | [optional]
 **tag** | **str**| Filter feature flags by tag | [optional]
 **limit** | **int**| The number of feature flags to return. Defaults to -1, which returns all flags | [optional]
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next limit items | [optional]
 **query** | **str**| A string that matches against the flags&#39; keys and names. It is not case sensitive | [optional]
 **archived** | **bool**| A boolean to filter the list to archived flags. When this is absent, only unarchived flags will be returned | [optional]
 **summary** | **bool**| By default in API version &gt;&#x3D; 1, flags will _not_ include their list of prerequisites, targets or rules.  Set summary&#x3D;0 to include these fields for each flag returned | [optional]
 **filter** | **str**| A comma-separated list of filters. Each filter is of the form field:value | [optional]
 **sort** | **str**| A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order | [optional]

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
**400** | Invalid request body |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_expiring_user_targets**
> ExpiringUserTargetPatchResponse patch_expiring_user_targets(proj_key, env_key, flag_key, patch_with_comment)

Update expiring user targets on feature flag

Update the list of user targets on a feature flag that are scheduled for removal.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.expiring_user_target_patch_response import ExpiringUserTargetPatchResponse
from launchdarkly_api.model.patch_with_comment import PatchWithComment
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
    proj_key = "projKey_example" # str | The project key.
    env_key = "envKey_example" # str | The environment key.
    flag_key = "flagKey_example" # str | The feature flag key.
    patch_with_comment = PatchWithComment(
        patch=JSONPatch([
            PatchOperation(
                op="replace",
                path="/biscuits",
                value=None,
            ),
        ]),
        comment="comment_example",
    ) # PatchWithComment | 

    # example passing only required values which don't have defaults set
    try:
        # Update expiring user targets on feature flag
        api_response = api_instance.patch_expiring_user_targets(proj_key, env_key, flag_key, patch_with_comment)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->patch_expiring_user_targets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **env_key** | **str**| The environment key. |
 **flag_key** | **str**| The feature flag key. |
 **patch_with_comment** | [**PatchWithComment**](PatchWithComment.md)|  |

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
**200** | User targeting expirations on feature flag response. |  -  |
**400** | Invalid request body |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_feature_flag**
> FeatureFlag patch_feature_flag(proj_key, key, patch_with_comment)

Update feature flag

Perform a partial update to a feature

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.patch_with_comment import PatchWithComment
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
    proj_key = "projKey_example" # str | The project key.
    key = "key_example" # str | The feature flag's key. The key identifies the flag in your code.
    patch_with_comment = PatchWithComment(
        patch=JSONPatch([
            PatchOperation(
                op="replace",
                path="/biscuits",
                value=None,
            ),
        ]),
        comment="comment_example",
    ) # PatchWithComment | 

    # example passing only required values which don't have defaults set
    try:
        # Update feature flag
        api_response = api_instance.patch_feature_flag(proj_key, key, patch_with_comment)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->patch_feature_flag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. |
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
**400** | Invalid request body |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_feature_flag**
> FeatureFlag post_feature_flag(proj_key, feature_flag_body)

Create a feature flag

Create a feature flag with the given name, key, and variations

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import feature_flags_api
from launchdarkly_api.model.feature_flag_body import FeatureFlagBody
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
    proj_key = "projKey_example" # str | The project key.
    feature_flag_body = FeatureFlagBody(
        name="name_example",
        key="key_example",
        description="description_example",
        include_in_snippet=True,
        client_side_availability=ClientSideAvailabilityPost(
            using_environment_id=True,
            using_mobile_key=True,
        ),
        variations=[
            Variate(
                id="id_example",
                value=None,
                description="description_example",
                name="name_example",
            ),
        ],
        variation_json_schema=None,
        temporary=True,
        tags=[
            "tags_example",
        ],
        custom_properties=CustomProperties(
            key=CustomProperty(
                name="name_example",
                value=[
                    "value_example",
                ],
            ),
        ),
        defaults=Defaults(
            on_variation=1,
            off_variation=1,
        ),
    ) # FeatureFlagBody | 
    clone = "clone_example" # str | The key of the feature flag to be cloned. The key identifies the flag in your code. For example, setting `clone=flagKey` copies the full targeting configuration for all environments, including `on/off` state, from the original flag to the new flag. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a feature flag
        api_response = api_instance.post_feature_flag(proj_key, feature_flag_body)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->post_feature_flag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a feature flag
        api_response = api_instance.post_feature_flag(proj_key, feature_flag_body, clone=clone)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FeatureFlagsApi->post_feature_flag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
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
**400** | Invalid request body |  -  |
**401** | Invalid access token |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

