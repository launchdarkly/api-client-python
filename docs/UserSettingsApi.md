# launchdarkly_api.UserSettingsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_expiring_flags_for_user**](UserSettingsApi.md#get_expiring_flags_for_user) | **GET** /api/v2/users/{projKey}/{userKey}/expiring-user-targets/{envKey} | Get expiring dates on flags for user
[**get_user_flag_setting**](UserSettingsApi.md#get_user_flag_setting) | **GET** /api/v2/users/{projKey}/{envKey}/{key}/flags/{featureKey} | Get flag setting for user
[**get_user_flag_settings**](UserSettingsApi.md#get_user_flag_settings) | **GET** /api/v2/users/{projKey}/{envKey}/{key}/flags | List flag settings for user
[**patch_expiring_flags_for_user**](UserSettingsApi.md#patch_expiring_flags_for_user) | **PATCH** /api/v2/users/{projKey}/{userKey}/expiring-user-targets/{envKey} | Update expiring user target for flags
[**put_flag_setting**](UserSettingsApi.md#put_flag_setting) | **PUT** /api/v2/users/{projKey}/{envKey}/{key}/flags/{featureKey} | Update flag settings for user


# **get_expiring_flags_for_user**
> ExpiringUserTargetGetResponse get_expiring_flags_for_user(proj_key, user_key, env_key)

Get expiring dates on flags for user

Get a list of flags for which the given user is scheduled for removal.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import user_settings_api
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
    api_instance = user_settings_api.UserSettingsApi(api_client)
    proj_key = "projKey_example" # str | The project key.
    user_key = "userKey_example" # str | The user key.
    env_key = "envKey_example" # str | The environment key.

    # example passing only required values which don't have defaults set
    try:
        # Get expiring dates on flags for user
        api_response = api_instance.get_expiring_flags_for_user(proj_key, user_key, env_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling UserSettingsApi->get_expiring_flags_for_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **user_key** | **str**| The user key. |
 **env_key** | **str**| The environment key. |

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

# **get_user_flag_setting**
> UserFlagSetting get_user_flag_setting(proj_key, env_key, key, feature_key)

Get flag setting for user

Get a single flag setting for a user by key. The most important attribute in the response is the `_value`. The `_value` is the current setting that the user sees. For a boolean feature toggle, this is `true`, `false`, or `null`. `null` returns if there is no defined fallback value. The example response indicates that the user `Abbie_Braun` has the `sort.order` flag enabled.<br /><br />The setting attribute indicates whether you've explicitly targeted a user to receive a particular variation. For example, if you have turned off a feature flag for a user, this setting will be `false`. A setting of `null` means that you haven't assigned that user to a specific variation.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import user_settings_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.user_flag_setting import UserFlagSetting
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
    api_instance = user_settings_api.UserSettingsApi(api_client)
    proj_key = "projKey_example" # str | The project key
    env_key = "envKey_example" # str | The environment key
    key = "key_example" # str | The user key
    feature_key = "featureKey_example" # str | The feature flag key

    # example passing only required values which don't have defaults set
    try:
        # Get flag setting for user
        api_response = api_instance.get_user_flag_setting(proj_key, env_key, key, feature_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling UserSettingsApi->get_user_flag_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **env_key** | **str**| The environment key |
 **key** | **str**| The user key |
 **feature_key** | **str**| The feature flag key |

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
> UserFlagSettings get_user_flag_settings(proj_key, env_key, key)

List flag settings for user

Get the current flag settings for a given user. The most important attribute in the response is the `_value`. The `_value` is the setting that the user sees. For a boolean feature toggle, this is `true`, `false`, or `null`. `null` returns if there is no defined fallthrough value. The example response indicates that the user `Abbie_Braun` has the `sort.order` flag enabled and the `alternate.page` flag disabled.<br /><br />The setting attribute indicates whether you've explicitly targeted a user to receive a particular variation. For example, if you have turned off a feature flag for a user, this setting will be `false`. A setting of `null` means that you haven't assigned that user to a specific variation.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import user_settings_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.user_flag_settings import UserFlagSettings
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
    api_instance = user_settings_api.UserSettingsApi(api_client)
    proj_key = "projKey_example" # str | The project key
    env_key = "envKey_example" # str | The environment key
    key = "key_example" # str | The user key

    # example passing only required values which don't have defaults set
    try:
        # List flag settings for user
        api_response = api_instance.get_user_flag_settings(proj_key, env_key, key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling UserSettingsApi->get_user_flag_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **env_key** | **str**| The environment key |
 **key** | **str**| The user key |

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
> ExpiringUserTargetPatchResponse patch_expiring_flags_for_user(proj_key, user_key, env_key, patch_with_comment)

Update expiring user target for flags

Schedule the specified user for removal from individual user targeting on one or more flags. You can only schedule a user for removal on a single variation per flag.  To learn more about semantic patches, read [Updates](/#section/Updates).  If you previously patched the flag, and the patch included the user's data, LaunchDarkly continues to use that data. If LaunchDarkly has never encountered the user's key before, it calculates the flag values based on the user key alone. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import user_settings_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.expiring_user_target_patch_response import ExpiringUserTargetPatchResponse
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.patch_with_comment import PatchWithComment
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
    api_instance = user_settings_api.UserSettingsApi(api_client)
    proj_key = "projKey_example" # str | The project key.
    user_key = "userKey_example" # str | The user key.
    env_key = "envKey_example" # str | The environment key.
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
        # Update expiring user target for flags
        api_response = api_instance.patch_expiring_flags_for_user(proj_key, user_key, env_key, patch_with_comment)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling UserSettingsApi->patch_expiring_flags_for_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **user_key** | **str**| The user key. |
 **env_key** | **str**| The environment key. |
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
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_flag_setting**
> put_flag_setting(proj_key, env_key, key, feature_key, value_put)

Update flag settings for user

Enable or disable a feature flag for a user based on their key.  To change the setting, send a `PUT` request to this URL with a request body containing the flag value. For example, to disable the sort.order flag for the user `test@test.com`, send a `PUT` to `https://app.launchdarkly.com/api/v2/users/default/production/test@test.com/flags/sort.order` with the following body:  ```json {   \"setting\": false } ```  Omitting the setting attribute, or a setting of null, in your `PUT` \"clears\" the current setting for a user.  If you previously patched the flag, and the patch included the user's data, LaunchDarkly continues to use that data. If LaunchDarkly has never encountered the user's key before, it calculates the flag values based on the user key alone. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import user_settings_api
from launchdarkly_api.model.value_put import ValuePut
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
    api_instance = user_settings_api.UserSettingsApi(api_client)
    proj_key = "projKey_example" # str | The project key
    env_key = "envKey_example" # str | The environment key
    key = "key_example" # str | The user key
    feature_key = "featureKey_example" # str | The feature flag key
    value_put = ValuePut(
        setting=None,
        comment="comment_example",
    ) # ValuePut | 

    # example passing only required values which don't have defaults set
    try:
        # Update flag settings for user
        api_instance.put_flag_setting(proj_key, env_key, key, feature_key, value_put)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling UserSettingsApi->put_flag_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **env_key** | **str**| The environment key |
 **key** | **str**| The user key |
 **feature_key** | **str**| The feature flag key |
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

