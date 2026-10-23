# launchdarkly_api.SDKKeysBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sdk_key_by_key**](SDKKeysBetaApi.md#delete_sdk_key_by_key) | **DELETE** /api/v2/projects/{projectKey}/environments/{environmentKey}/sdk-keys/{sdkKeyKey} | Delete SDK key
[**get_project_sdk_keys**](SDKKeysBetaApi.md#get_project_sdk_keys) | **GET** /api/v2/projects/{projectKey}/sdk-keys | Get all project SDK keys
[**get_sdk_key_by_key**](SDKKeysBetaApi.md#get_sdk_key_by_key) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/sdk-keys/{sdkKeyKey} | Get SDK key
[**get_sdk_keys**](SDKKeysBetaApi.md#get_sdk_keys) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/sdk-keys | Get all environment SDK keys
[**patch_sdk_key_by_key**](SDKKeysBetaApi.md#patch_sdk_key_by_key) | **PATCH** /api/v2/projects/{projectKey}/environments/{environmentKey}/sdk-keys/{sdkKeyKey} | Update SDK key
[**post_sdk_key**](SDKKeysBetaApi.md#post_sdk_key) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/sdk-keys | Create SDK key
[**put_sdk_key_views**](SDKKeysBetaApi.md#put_sdk_key_views) | **PUT** /api/v2/projects/{projectKey}/environments/{environmentKey}/sdk-keys/{sdkKeyKey}/views | Replace SDK key views


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

# **get_project_sdk_keys**
> SdkKeys get_project_sdk_keys(ld_api_version, project_key, filter=filter, limit=limit, offset=offset, expand=expand, sort=sort)

Get all project SDK keys

Get all SDK keys for a given project across environments.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.sdk_keys import SdkKeys
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
    filter = 'filter_example' # str | A queryfilter expression to apply to the list of SDK keys. Supports the following fields and operators: `kind` (`equals`, `anyOf`; values: \"sdk\", \"mobile\"), `active` (`equals`, `anyOf`; values: `true`, `false`), `environmentKey` (`equals`, `anyOf`; values: environment keys), `viewKey` (`equals`, `anyOf`; values: view key strings — returns only SDK keys linked to the specified view(s)), `name` (`equals` only; returns SDK keys whose name or key contains the value, matched case-insensitively). Example: `kind anyOf [\"sdk\",\"mobile\"], environmentKey anyOf [\"production\",\"test\"], viewKey equals my-view, name equals \"production\"`. (optional)
    limit = 56 # int | The number of SDK keys to return. Defaults to 20. Maximum is 100. (optional)
    offset = 56 # int | The number of SDK keys to skip. Used for pagination. (optional)
    expand = 'expand_example' # str | A comma-separated list of fields to expand in the response. Supported fields: `environmentSummary`, `viewSummaries`. (optional)
    sort = 'sort_example' # str | A sort to apply to the list of SDK keys. Supported fields: `createdAt` and `environmentKey`. Prefix `createdAt` with `-` to sort in descending order (for example, `-createdAt`). `environmentKey` orders keys by environment key ascending, then by creation time ascending within each environment, so each page is environment-contiguous. (optional)

    try:
        # Get all project SDK keys
        api_response = api_instance.get_project_sdk_keys(ld_api_version, project_key, filter=filter, limit=limit, offset=offset, expand=expand, sort=sort)
        print("The response of SDKKeysBetaApi->get_project_sdk_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKKeysBetaApi->get_project_sdk_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **filter** | **str**| A queryfilter expression to apply to the list of SDK keys. Supports the following fields and operators: &#x60;kind&#x60; (&#x60;equals&#x60;, &#x60;anyOf&#x60;; values: \&quot;sdk\&quot;, \&quot;mobile\&quot;), &#x60;active&#x60; (&#x60;equals&#x60;, &#x60;anyOf&#x60;; values: &#x60;true&#x60;, &#x60;false&#x60;), &#x60;environmentKey&#x60; (&#x60;equals&#x60;, &#x60;anyOf&#x60;; values: environment keys), &#x60;viewKey&#x60; (&#x60;equals&#x60;, &#x60;anyOf&#x60;; values: view key strings — returns only SDK keys linked to the specified view(s)), &#x60;name&#x60; (&#x60;equals&#x60; only; returns SDK keys whose name or key contains the value, matched case-insensitively). Example: &#x60;kind anyOf [\&quot;sdk\&quot;,\&quot;mobile\&quot;], environmentKey anyOf [\&quot;production\&quot;,\&quot;test\&quot;], viewKey equals my-view, name equals \&quot;production\&quot;&#x60;. | [optional] 
 **limit** | **int**| The number of SDK keys to return. Defaults to 20. Maximum is 100. | [optional] 
 **offset** | **int**| The number of SDK keys to skip. Used for pagination. | [optional] 
 **expand** | **str**| A comma-separated list of fields to expand in the response. Supported fields: &#x60;environmentSummary&#x60;, &#x60;viewSummaries&#x60;. | [optional] 
 **sort** | **str**| A sort to apply to the list of SDK keys. Supported fields: &#x60;createdAt&#x60; and &#x60;environmentKey&#x60;. Prefix &#x60;createdAt&#x60; with &#x60;-&#x60; to sort in descending order (for example, &#x60;-createdAt&#x60;). &#x60;environmentKey&#x60; orders keys by environment key ascending, then by creation time ascending within each environment, so each page is environment-contiguous. | [optional] 

### Return type

[**SdkKeys**](SdkKeys.md)

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

# **get_sdk_keys**
> SdkKeysForGetSdkKeys get_sdk_keys(ld_api_version, project_key, environment_key, filter=filter, limit=limit, offset=offset, sort=sort)

Get all environment SDK keys

Get all SDK keys for a given project and environment. Can filter by kind.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.sdk_keys_for_get_sdk_keys import SdkKeysForGetSdkKeys
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
    filter = 'filter_example' # str | A filter to apply to the list of SDK keys. Supports the following fields and operators: `kind` (equals \"sdk\" or \"mobile\"), `active` (equals true or false). Format: `field:value`. Example: `kind:sdk`. (optional)
    limit = 56 # int | The number of SDK keys to return. Defaults to 20. Maximum is 100. (optional)
    offset = 56 # int | The number of SDK keys to skip. Used for pagination. (optional)
    sort = 'sort_example' # str | A sort to apply to the list of SDK keys. Supported field: `createdAt`. Prefix the field with `-` to sort in descending order (for example, `-createdAt`). (optional)

    try:
        # Get all environment SDK keys
        api_response = api_instance.get_sdk_keys(ld_api_version, project_key, environment_key, filter=filter, limit=limit, offset=offset, sort=sort)
        print("The response of SDKKeysBetaApi->get_sdk_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKKeysBetaApi->get_sdk_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **filter** | **str**| A filter to apply to the list of SDK keys. Supports the following fields and operators: &#x60;kind&#x60; (equals \&quot;sdk\&quot; or \&quot;mobile\&quot;), &#x60;active&#x60; (equals true or false). Format: &#x60;field:value&#x60;. Example: &#x60;kind:sdk&#x60;. | [optional] 
 **limit** | **int**| The number of SDK keys to return. Defaults to 20. Maximum is 100. | [optional] 
 **offset** | **int**| The number of SDK keys to skip. Used for pagination. | [optional] 
 **sort** | **str**| A sort to apply to the list of SDK keys. Supported field: &#x60;createdAt&#x60;. Prefix the field with &#x60;-&#x60; to sort in descending order (for example, &#x60;-createdAt&#x60;). | [optional] 

### Return type

[**SdkKeysForGetSdkKeys**](SdkKeysForGetSdkKeys.md)

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

Deleted SDK keys are retained for 180 days. During that period you cannot reuse the `key` of a deleted SDK key, even though the deleted key no longer appears in the list of SDK keys for the environment.

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

# **put_sdk_key_views**
> SdkKeyForPutSdkKeyViews put_sdk_key_views(ld_api_version, project_key, environment_key, sdk_key_key, sdk_key_views_put, expand=expand)

Replace SDK key views

Replace the set of views associated with an SDK key. The `viewKeys` field is required. To remove all views from the SDK key, pass an empty `viewKeys` array.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.sdk_key_for_put_sdk_key_views import SdkKeyForPutSdkKeyViews
from launchdarkly_api.models.sdk_key_views_put import SdkKeyViewsPut
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
    project_key = 'project_key_example' # str | 
    environment_key = 'environment_key_example' # str | 
    sdk_key_key = 'sdk_key_key_example' # str | 
    sdk_key_views_put = launchdarkly_api.SdkKeyViewsPut() # SdkKeyViewsPut | 
    expand = 'expand_example' # str | A comma-separated list of fields to expand in the response. Supported fields: `viewSummaries`. (optional)

    try:
        # Replace SDK key views
        api_response = api_instance.put_sdk_key_views(ld_api_version, project_key, environment_key, sdk_key_key, sdk_key_views_put, expand=expand)
        print("The response of SDKKeysBetaApi->put_sdk_key_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKKeysBetaApi->put_sdk_key_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **sdk_key_key** | **str**|  | 
 **sdk_key_views_put** | [**SdkKeyViewsPut**](SdkKeyViewsPut.md)|  | 
 **expand** | **str**| A comma-separated list of fields to expand in the response. Supported fields: &#x60;viewSummaries&#x60;. | [optional] 

### Return type

[**SdkKeyForPutSdkKeyViews**](SdkKeyForPutSdkKeyViews.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

