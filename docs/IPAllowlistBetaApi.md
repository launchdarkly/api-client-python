# launchdarkly_api.IPAllowlistBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ip_allowlist_entry**](IPAllowlistBetaApi.md#create_ip_allowlist_entry) | **POST** /api/v2/account/ip-allowlist | Create IP Allowlist Entry
[**delete_ip_allowlist_entry**](IPAllowlistBetaApi.md#delete_ip_allowlist_entry) | **DELETE** /api/v2/account/ip-allowlist/{id} | Delete IP Allowlist Entry
[**get_ip_allowlist**](IPAllowlistBetaApi.md#get_ip_allowlist) | **GET** /api/v2/account/ip-allowlist | Get IP Allowlist
[**patch_ip_allowlist_config**](IPAllowlistBetaApi.md#patch_ip_allowlist_config) | **PATCH** /api/v2/account/ip-allowlist | Update IP Allowlist Configuration
[**patch_ip_allowlist_entry**](IPAllowlistBetaApi.md#patch_ip_allowlist_entry) | **PATCH** /api/v2/account/ip-allowlist/{id} | Update IP Allowlist Entry Description


# **create_ip_allowlist_entry**
> IpAllowlistEntryResponse create_ip_allowlist_entry(create_ip_allowlist_entry_request)

Create IP Allowlist Entry

Create a new IP allowlist entry.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.create_ip_allowlist_entry_request import CreateIpAllowlistEntryRequest
from launchdarkly_api.models.ip_allowlist_entry_response import IpAllowlistEntryResponse
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
    api_instance = launchdarkly_api.IPAllowlistBetaApi(api_client)
    create_ip_allowlist_entry_request = launchdarkly_api.CreateIpAllowlistEntryRequest() # CreateIpAllowlistEntryRequest | 

    try:
        # Create IP Allowlist Entry
        api_response = api_instance.create_ip_allowlist_entry(create_ip_allowlist_entry_request)
        print("The response of IPAllowlistBetaApi->create_ip_allowlist_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAllowlistBetaApi->create_ip_allowlist_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_ip_allowlist_entry_request** | [**CreateIpAllowlistEntryRequest**](CreateIpAllowlistEntryRequest.md)|  | 

### Return type

[**IpAllowlistEntryResponse**](IpAllowlistEntryResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | IP allowlist entry created |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_allowlist_entry**
> delete_ip_allowlist_entry(id)

Delete IP Allowlist Entry

Delete an IP allowlist entry by id.

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
    api_instance = launchdarkly_api.IPAllowlistBetaApi(api_client)
    id = 'id_example' # str | Unique identifier for the allowlist entry

    try:
        # Delete IP Allowlist Entry
        api_instance.delete_ip_allowlist_entry(id)
    except Exception as e:
        print("Exception when calling IPAllowlistBetaApi->delete_ip_allowlist_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the allowlist entry | 

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
**204** | IP allowlist entry deleted successfully |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_allowlist**
> IpAllowlistResponse get_ip_allowlist()

Get IP Allowlist

Get the current IP allowlist configuration and entries.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ip_allowlist_response import IpAllowlistResponse
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
    api_instance = launchdarkly_api.IPAllowlistBetaApi(api_client)

    try:
        # Get IP Allowlist
        api_response = api_instance.get_ip_allowlist()
        print("The response of IPAllowlistBetaApi->get_ip_allowlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAllowlistBetaApi->get_ip_allowlist: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IpAllowlistResponse**](IpAllowlistResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP allowlist configuration and entries |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_ip_allowlist_config**
> IpAllowlistResponse patch_ip_allowlist_config(patch_ip_allowlist_config_request)

Update IP Allowlist Configuration

Update sessionAllowlistEnabled and apiTokenAllowlistEnabled settings.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ip_allowlist_response import IpAllowlistResponse
from launchdarkly_api.models.patch_ip_allowlist_config_request import PatchIpAllowlistConfigRequest
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
    api_instance = launchdarkly_api.IPAllowlistBetaApi(api_client)
    patch_ip_allowlist_config_request = launchdarkly_api.PatchIpAllowlistConfigRequest() # PatchIpAllowlistConfigRequest | 

    try:
        # Update IP Allowlist Configuration
        api_response = api_instance.patch_ip_allowlist_config(patch_ip_allowlist_config_request)
        print("The response of IPAllowlistBetaApi->patch_ip_allowlist_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAllowlistBetaApi->patch_ip_allowlist_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_ip_allowlist_config_request** | [**PatchIpAllowlistConfigRequest**](PatchIpAllowlistConfigRequest.md)|  | 

### Return type

[**IpAllowlistResponse**](IpAllowlistResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated IP allowlist configuration and entries |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_ip_allowlist_entry**
> IpAllowlistEntryResponse patch_ip_allowlist_entry(id, patch_ip_allowlist_entry_request)

Update IP Allowlist Entry Description

Update the description of an IP allowlist entry.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ip_allowlist_entry_response import IpAllowlistEntryResponse
from launchdarkly_api.models.patch_ip_allowlist_entry_request import PatchIpAllowlistEntryRequest
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
    api_instance = launchdarkly_api.IPAllowlistBetaApi(api_client)
    id = 'id_example' # str | Unique identifier for the allowlist entry
    patch_ip_allowlist_entry_request = launchdarkly_api.PatchIpAllowlistEntryRequest() # PatchIpAllowlistEntryRequest | 

    try:
        # Update IP Allowlist Entry Description
        api_response = api_instance.patch_ip_allowlist_entry(id, patch_ip_allowlist_entry_request)
        print("The response of IPAllowlistBetaApi->patch_ip_allowlist_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAllowlistBetaApi->patch_ip_allowlist_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the allowlist entry | 
 **patch_ip_allowlist_entry_request** | [**PatchIpAllowlistEntryRequest**](PatchIpAllowlistEntryRequest.md)|  | 

### Return type

[**IpAllowlistEntryResponse**](IpAllowlistEntryResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated IP allowlist entry |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

