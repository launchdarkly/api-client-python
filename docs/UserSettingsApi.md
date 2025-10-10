# launchdarkly_api.UserSettingsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_expiring_flags_for_user**](UserSettingsApi.md#get_expiring_flags_for_user) | **GET** /api/v2/users/{projectKey}/{userKey}/expiring-user-targets/{environmentKey} | Get expiring dates on flags for user
[**get_user_flag_setting**](UserSettingsApi.md#get_user_flag_setting) | **GET** /api/v2/users/{projectKey}/{environmentKey}/{userKey}/flags/{featureFlagKey} | Get flag setting for user
[**get_user_flag_settings**](UserSettingsApi.md#get_user_flag_settings) | **GET** /api/v2/users/{projectKey}/{environmentKey}/{userKey}/flags | List flag settings for user
[**patch_expiring_flags_for_user**](UserSettingsApi.md#patch_expiring_flags_for_user) | **PATCH** /api/v2/users/{projectKey}/{userKey}/expiring-user-targets/{environmentKey} | Update expiring user target for flags
[**put_flag_setting**](UserSettingsApi.md#put_flag_setting) | **PUT** /api/v2/users/{projectKey}/{environmentKey}/{userKey}/flags/{featureFlagKey} | Update flag settings for user


# **get_expiring_flags_for_user**
> ExpiringUserTargetGetResponse get_expiring_flags_for_user(project_key, user_key, environment_key)

Get expiring dates on flags for user

Get a list of flags for which the given user is scheduled for removal.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.expiring_user_target_get_response import ExpiringUserTargetGetResponse
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
    api_instance = launchdarkly_api.UserSettingsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    user_key = 'user_key_example' # str | The user key
    environment_key = 'environment_key_example' # str | The environment key

    try:
        # Get expiring dates on flags for user
        api_response = api_instance.get_expiring_flags_for_user(project_key, user_key, environment_key)
        print("The response of UserSettingsApi->get_expiring_flags_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSettingsApi->get_expiring_flags_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **user_key** | **str**| The user key | 
 **environment_key** | **str**| The environment key | 

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

# **get_user_flag_setting**
> UserFlagSetting get_user_flag_setting(project_key, environment_key, user_key, feature_flag_key)

Get flag setting for user

Get a single flag setting for a user by flag key. <br /><br />The `_value` is the flag variation that the user receives. The `setting` indicates whether you've explicitly targeted a user to receive a particular variation. For example, if you have turned off a feature flag for a user, this setting will be `false`. The example response indicates that the user `Abbie_Braun` has the `sort.order` flag enabled.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.user_flag_setting import UserFlagSetting
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
    api_instance = launchdarkly_api.UserSettingsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    user_key = 'user_key_example' # str | The user key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key

    try:
        # Get flag setting for user
        api_response = api_instance.get_user_flag_setting(project_key, environment_key, user_key, feature_flag_key)
        print("The response of UserSettingsApi->get_user_flag_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSettingsApi->get_user_flag_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **user_key** | **str**| The user key | 
 **feature_flag_key** | **str**| The feature flag key | 

### Return type

[**UserFlagSetting**](UserFlagSetting.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User flag settings response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_flag_settings**
> UserFlagSettings get_user_flag_settings(project_key, environment_key, user_key)

List flag settings for user

Get the current flag settings for a given user. <br /><br />The `_value` is the flag variation that the user receives. The `setting` indicates whether you've explicitly targeted a user to receive a particular variation. For example, if you have turned off a feature flag for a user, this setting will be `false`. The example response indicates that the user `Abbie_Braun` has the `sort.order` flag enabled and the `alternate.page` flag disabled, and that the user has not been explicitly targeted to receive a particular variation.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.user_flag_settings import UserFlagSettings
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
    api_instance = launchdarkly_api.UserSettingsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    user_key = 'user_key_example' # str | The user key

    try:
        # List flag settings for user
        api_response = api_instance.get_user_flag_settings(project_key, environment_key, user_key)
        print("The response of UserSettingsApi->get_user_flag_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSettingsApi->get_user_flag_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **user_key** | **str**| The user key | 

### Return type

[**UserFlagSettings**](UserFlagSettings.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User flag settings collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_expiring_flags_for_user**
> ExpiringUserTargetPatchResponse patch_expiring_flags_for_user(project_key, user_key, environment_key, patch_users_request)

Update expiring user target for flags

Schedule the specified user for removal from individual targeting on one or more flags. The user must already be individually targeted for each flag.

You can add, update, or remove a scheduled removal date. You can only schedule a user for removal on a single variation per flag.

Updating an expiring target uses the semantic patch format. To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](https://launchdarkly.com/docs/api#updates-using-semantic-patch).

### Instructions

Semantic patch requests support the following `kind` instructions for updating expiring user targets.

<details>
<summary>Click to expand instructions for <strong>updating expiring user targets</strong></summary>

#### addExpireUserTargetDate

Adds a date and time that LaunchDarkly will remove the user from the flag's individual targeting.

##### Parameters

* `flagKey`: The flag key
* `variationId`: ID of a variation on the flag
* `value`: The time, in Unix milliseconds, when LaunchDarkly should remove the user from individual targeting for this flag.

#### updateExpireUserTargetDate

Updates the date and time that LaunchDarkly will remove the user from the flag's individual targeting.

##### Parameters

* `flagKey`: The flag key
* `variationId`: ID of a variation on the flag
* `value`: The time, in Unix milliseconds, when LaunchDarkly should remove the user from individual targeting for this flag.
* `version`: The version of the expiring user target to update. If included, update will fail if version doesn't match current version of the expiring user target.

#### removeExpireUserTargetDate

Removes the scheduled removal of the user from the flag's individual targeting. The user will remain part of the flag's individual targeting until explicitly removed, or until another removal is scheduled.

##### Parameters

* `flagKey`: The flag key
* `variationId`: ID of a variation on the flag

</details>


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.expiring_user_target_patch_response import ExpiringUserTargetPatchResponse
from launchdarkly_api.models.patch_users_request import PatchUsersRequest
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
    api_instance = launchdarkly_api.UserSettingsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    user_key = 'user_key_example' # str | The user key
    environment_key = 'environment_key_example' # str | The environment key
    patch_users_request = launchdarkly_api.PatchUsersRequest() # PatchUsersRequest | 

    try:
        # Update expiring user target for flags
        api_response = api_instance.patch_expiring_flags_for_user(project_key, user_key, environment_key, patch_users_request)
        print("The response of UserSettingsApi->patch_expiring_flags_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserSettingsApi->patch_expiring_flags_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **user_key** | **str**| The user key | 
 **environment_key** | **str**| The environment key | 
 **patch_users_request** | [**PatchUsersRequest**](PatchUsersRequest.md)|  | 

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

# **put_flag_setting**
> put_flag_setting(project_key, environment_key, user_key, feature_flag_key, value_put)

Update flag settings for user

Enable or disable a feature flag for a user based on their key.

Omitting the `setting` attribute from the request body, or including a `setting` of `null`, erases the current setting for a user.

If you previously patched the flag, and the patch included the user's data, LaunchDarkly continues to use that data. If LaunchDarkly has never encountered the user's key before, it calculates the flag values based on the user key alone.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.value_put import ValuePut
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
    api_instance = launchdarkly_api.UserSettingsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    user_key = 'user_key_example' # str | The user key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    value_put = launchdarkly_api.ValuePut() # ValuePut | 

    try:
        # Update flag settings for user
        api_instance.put_flag_setting(project_key, environment_key, user_key, feature_flag_key, value_put)
    except Exception as e:
        print("Exception when calling UserSettingsApi->put_flag_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **user_key** | **str**| The user key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **value_put** | [**ValuePut**](ValuePut.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Action succeeded |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

