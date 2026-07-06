# launchdarkly_api.SDKKeysBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sdk_key_by_key**](SDKKeysBetaApi.md#delete_sdk_key_by_key) | **DELETE** /api/v2/projects/{projectKey}/environments/{environmentKey}/sdk-keys/{sdkKeyKey} | Delete SDK key
[**get_sdk_key_by_key**](SDKKeysBetaApi.md#get_sdk_key_by_key) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/sdk-keys/{sdkKeyKey} | Get SDK key
[**patch_sdk_key_by_key**](SDKKeysBetaApi.md#patch_sdk_key_by_key) | **PATCH** /api/v2/projects/{projectKey}/environments/{environmentKey}/sdk-keys/{sdkKeyKey} | Update SDK key
[**post_sdk_key**](SDKKeysBetaApi.md#post_sdk_key) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/sdk-keys | Create SDK key


# **delete_sdk_key_by_key**
> delete_sdk_key_by_key(ld_api_version, project_key, environment_key, sdk_key_key)

Delete SDK key

Delete a specific SDK key by its key.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
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
    api_instance = launchdarkly_api.SDKKeysBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    environment_key = 'production' # str | 
    sdk_key_key = 'my-sdk-key' # str | The user-defined identifying key of the SDK key. This is used solely to identify an SDK key and is distinct from the value field, which is the actual SDK key value.

    try:
        # Delete SDK key
        api_instance.delete_sdk_key_by_key(ld_api_version, project_key, environment_key, sdk_key_key)
    except Exception as e:
        print("Exception when calling SDKKeysBetaApi->delete_sdk_key_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **sdk_key_key** | **str**| The user-defined identifying key of the SDK key. This is used solely to identify an SDK key and is distinct from the value field, which is the actual SDK key value. | 

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
**204** | SDK key deleted |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdk_key_by_key**
> SdkKey get_sdk_key_by_key(ld_api_version, project_key, environment_key, sdk_key_key)

Get SDK key

Get a specific SDK key by its key.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.sdk_key import SdkKey
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
    api_instance = launchdarkly_api.SDKKeysBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    environment_key = 'production' # str | 
    sdk_key_key = 'my-sdk-key' # str | The user-defined identifying key of the SDK key. This is used solely to identify an SDK key and is distinct from the value field, which is the actual SDK key value.

    try:
        # Get SDK key
        api_response = api_instance.get_sdk_key_by_key(ld_api_version, project_key, environment_key, sdk_key_key)
        print("The response of SDKKeysBetaApi->get_sdk_key_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKKeysBetaApi->get_sdk_key_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **sdk_key_key** | **str**| The user-defined identifying key of the SDK key. This is used solely to identify an SDK key and is distinct from the value field, which is the actual SDK key value. | 

### Return type

[**SdkKey**](SdkKey.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sdk_key_by_key**
> SdkKey patch_sdk_key_by_key(ld_api_version, project_key, environment_key, sdk_key_key, sdk_key_patch, version=version)

Update SDK key

Update a an existing SDK key by its identifying key.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.sdk_key import SdkKey
from launchdarkly_api.models.sdk_key_patch import SdkKeyPatch
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
    api_instance = launchdarkly_api.SDKKeysBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    environment_key = 'production' # str | 
    sdk_key_key = 'my-sdk-key' # str | The user-defined identifying key of the SDK key. This is used solely to identify an SDK key and is distinct from the value field, which is the actual SDK key value.
    sdk_key_patch = launchdarkly_api.SdkKeyPatch() # SdkKeyPatch | An array of patches for updating an existing SDK key. The following fields are supported: `name`, `description`, `expiry`.
    version = 56 # int | The version of the SDK key for optimistic locking. If provided, the update will only succeed if the current version matches. (optional)

    try:
        # Update SDK key
        api_response = api_instance.patch_sdk_key_by_key(ld_api_version, project_key, environment_key, sdk_key_key, sdk_key_patch, version=version)
        print("The response of SDKKeysBetaApi->patch_sdk_key_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKKeysBetaApi->patch_sdk_key_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **sdk_key_key** | **str**| The user-defined identifying key of the SDK key. This is used solely to identify an SDK key and is distinct from the value field, which is the actual SDK key value. | 
 **sdk_key_patch** | [**SdkKeyPatch**](SdkKeyPatch.md)| An array of patches for updating an existing SDK key. The following fields are supported: &#x60;name&#x60;, &#x60;description&#x60;, &#x60;expiry&#x60;. | 
 **version** | **int**| The version of the SDK key for optimistic locking. If provided, the update will only succeed if the current version matches. | [optional] 

### Return type

[**SdkKey**](SdkKey.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sdk_key**
> SdkKey post_sdk_key(ld_api_version, project_key, environment_key, sdk_key_post)

Create SDK key

Create a new server-side or mobile SDK key.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.sdk_key import SdkKey
from launchdarkly_api.models.sdk_key_post import SdkKeyPost
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
    api_instance = launchdarkly_api.SDKKeysBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    environment_key = 'production' # str | 
    sdk_key_post = launchdarkly_api.SdkKeyPost() # SdkKeyPost | Parameters for creating a new SDK key

    try:
        # Create SDK key
        api_response = api_instance.post_sdk_key(ld_api_version, project_key, environment_key, sdk_key_post)
        print("The response of SDKKeysBetaApi->post_sdk_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKKeysBetaApi->post_sdk_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **sdk_key_post** | [**SdkKeyPost**](SdkKeyPost.md)| Parameters for creating a new SDK key | 

### Return type

[**SdkKey**](SdkKey.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SDK key created |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

