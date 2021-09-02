# launchdarkly_api.DataExportDestinationsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_destination**](DataExportDestinationsApi.md#delete_destination) | **DELETE** /api/v2/destinations/{projKey}/{envKey}/{id} | Delete Data Export destination
[**get_destination**](DataExportDestinationsApi.md#get_destination) | **GET** /api/v2/destinations/{projKey}/{envKey}/{id} | Get destination
[**get_destinations**](DataExportDestinationsApi.md#get_destinations) | **GET** /api/v2/destinations | List destinations
[**patch_destination**](DataExportDestinationsApi.md#patch_destination) | **PATCH** /api/v2/destinations/{projKey}/{envKey}/{id} | Update Data Export destination
[**post_destination**](DataExportDestinationsApi.md#post_destination) | **POST** /api/v2/destinations/{projKey}/{envKey} | Create data export destination


# **delete_destination**
> delete_destination(proj_key, env_key, id)

Delete Data Export destination

Delete Data Export destination by ID

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import data_export_destinations_api
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
    api_instance = data_export_destinations_api.DataExportDestinationsApi(api_client)
    proj_key = "projKey_example" # str | The project key
    env_key = "envKey_example" # str | The environment key
    id = "id_example" # str | The Data Export destination ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Data Export destination
        api_instance.delete_destination(proj_key, env_key, id)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling DataExportDestinationsApi->delete_destination: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **env_key** | **str**| The environment key |
 **id** | **str**| The Data Export destination ID |

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
**204** | Destination response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource specifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destination**
> Destination get_destination(proj_key, env_key, id)

Get destination

Get a single Data Export destination by ID

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import data_export_destinations_api
from launchdarkly_api.model.destination import Destination
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
    api_instance = data_export_destinations_api.DataExportDestinationsApi(api_client)
    proj_key = "projKey_example" # str | The project key
    env_key = "envKey_example" # str | The environment key
    id = "id_example" # str | The Data Export destination ID

    # example passing only required values which don't have defaults set
    try:
        # Get destination
        api_response = api_instance.get_destination(proj_key, env_key, id)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling DataExportDestinationsApi->get_destination: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **env_key** | **str**| The environment key |
 **id** | **str**| The Data Export destination ID |

### Return type

[**Destination**](Destination.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Destination response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource specifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destinations**
> Destinations get_destinations()

List destinations

Get a list of Data Export destinations configured across all projects and environments.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import data_export_destinations_api
from launchdarkly_api.model.destinations import Destinations
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
    api_instance = data_export_destinations_api.DataExportDestinationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List destinations
        api_response = api_instance.get_destinations()
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling DataExportDestinationsApi->get_destinations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Destinations**](Destinations.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Destination collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_destination**
> Destination patch_destination(proj_key, env_key, id, json_patch)

Update Data Export destination

Update a Data Export destination. This requires a JSON Patch representation of the modified destination.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import data_export_destinations_api
from launchdarkly_api.model.json_patch import JSONPatch
from launchdarkly_api.model.destination import Destination
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
    api_instance = data_export_destinations_api.DataExportDestinationsApi(api_client)
    proj_key = "projKey_example" # str | The project key
    env_key = "envKey_example" # str | The environment key
    id = "id_example" # str | The Data Export destination ID
    json_patch = JSONPatch([
        PatchOperation(
            op="replace",
            path="/biscuits",
            value=None,
        ),
    ]) # JSONPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update Data Export destination
        api_response = api_instance.patch_destination(proj_key, env_key, id, json_patch)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling DataExportDestinationsApi->patch_destination: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **env_key** | **str**| The environment key |
 **id** | **str**| The Data Export destination ID |
 **json_patch** | [**JSONPatch**](JSONPatch.md)|  |

### Return type

[**Destination**](Destination.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Destination response |  -  |
**400** | Invalid request body |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource specifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_destination**
> Destination post_destination(proj_key, env_key, destination_post)

Create data export destination

Create a new destination. The `config` body parameter represents the configuration parameters required for a destination type.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import data_export_destinations_api
from launchdarkly_api.model.destination_post import DestinationPost
from launchdarkly_api.model.destination import Destination
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
    api_instance = data_export_destinations_api.DataExportDestinationsApi(api_client)
    proj_key = "projKey_example" # str | The project key
    env_key = "envKey_example" # str | The environment key
    destination_post = DestinationPost(
        name="name_example",
        kind="google-pubsub",
        config=None,
        on=True,
    ) # DestinationPost | 

    # example passing only required values which don't have defaults set
    try:
        # Create data export destination
        api_response = api_instance.post_destination(proj_key, env_key, destination_post)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling DataExportDestinationsApi->post_destination: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **env_key** | **str**| The environment key |
 **destination_post** | [**DestinationPost**](DestinationPost.md)|  |

### Return type

[**Destination**](Destination.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Destination response |  -  |
**400** | Invalid request body |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

