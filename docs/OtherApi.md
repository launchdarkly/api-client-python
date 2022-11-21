# launchdarkly_api.OtherApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ips**](OtherApi.md#get_ips) | **GET** /api/v2/public-ip-list | Gets the public IP list
[**get_openapi_spec**](OtherApi.md#get_openapi_spec) | **GET** /api/v2/openapi.json | Gets the OpenAPI spec in json
[**get_root**](OtherApi.md#get_root) | **GET** /api/v2 | Root resource
[**get_versions**](OtherApi.md#get_versions) | **GET** /api/v2/versions | Get version information


# **get_ips**
> IpList get_ips()

Gets the public IP list

Get a list of IP ranges the LaunchDarkly service uses. You can use this list to allow LaunchDarkly through your firewall. We post upcoming changes to this list in advance on our [status page](https://status.launchdarkly.com/). <br /><br />In the sandbox, click 'Try it' and enter any string in the 'Authorization' field to test this endpoint.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import other_api
from launchdarkly_api.model.ip_list import IpList
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
    api_instance = other_api.OtherApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Gets the public IP list
        api_response = api_instance.get_ips()
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling OtherApi->get_ips: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**IpList**](IpList.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public IP response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_openapi_spec**
> get_openapi_spec()

Gets the OpenAPI spec in json

Get the latest version of the OpenAPI specification for LaunchDarkly's API in JSON format. In the sandbox, click 'Try it' and enter any string in the 'Authorization' field to test this endpoint.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import other_api
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
    api_instance = other_api.OtherApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Gets the OpenAPI spec in json
        api_instance.get_openapi_spec()
    except launchdarkly_api.ApiException as e:
        print("Exception when calling OtherApi->get_openapi_spec: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | OpenAPI Spec |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root**
> RootResponse get_root()

Root resource

Get all of the resource categories the API supports. In the sandbox, click 'Try it' and enter any string in the 'Authorization' field to test this endpoint.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import other_api
from launchdarkly_api.model.root_response import RootResponse
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
    api_instance = other_api.OtherApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Root resource
        api_response = api_instance.get_root()
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling OtherApi->get_root: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RootResponse**](RootResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Root response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions**
> VersionsRep get_versions()

Get version information

Get the latest API version, the list of valid API versions in ascending order, and the version being used for this request. These are all in the external, date-based format.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import other_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.versions_rep import VersionsRep
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
    api_instance = other_api.OtherApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get version information
        api_response = api_instance.get_versions()
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling OtherApi->get_versions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionsRep**](VersionsRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Versions information response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

