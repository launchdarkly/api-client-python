# launchdarkly_api.UsageApi

All URIs are relative to *https://app.launchdarkly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_evaluations**](UsageApi.md#get_evaluations) | **GET** /usage/evaluations/{envId}/{flagKey} | [BETA] Get events usage by event id and the feature flag key.
[**get_event**](UsageApi.md#get_event) | **GET** /usage/events/{type} | [BETA] Get events usage by event type.
[**get_events**](UsageApi.md#get_events) | **GET** /usage/events | [BETA] Get events usage endpoints.
[**get_mau**](UsageApi.md#get_mau) | **GET** /usage/mau | [BETA] Get monthly active user data.
[**get_mau_by_category**](UsageApi.md#get_mau_by_category) | **GET** /usage/mau/bycategory | [BETA] Get monthly active user data by category.
[**get_stream**](UsageApi.md#get_stream) | **GET** /usage/streams/{source} | [BETA] Get a stream endpoint and return timeseries data.
[**get_stream_by_sdk**](UsageApi.md#get_stream_by_sdk) | **GET** /usage/streams/{source}/bysdkversion | [BETA] Get a stream timeseries data by source show sdk version metadata.
[**get_stream_sdk_version**](UsageApi.md#get_stream_sdk_version) | **GET** /usage/streams/{source}/sdkversions | [BETA] Get a stream timeseries data by source and show all sdk version associated.
[**get_streams**](UsageApi.md#get_streams) | **GET** /usage/streams | [BETA] Returns a list of all streams.
[**get_usage**](UsageApi.md#get_usage) | **GET** /usage | [BETA] Returns of the usage endpoints available.


# **get_evaluations**
> StreamSDKVersion get_evaluations(env_id, flag_key)

[BETA] Get events usage by event id and the feature flag key.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.UsageApi(launchdarkly_api.ApiClient(configuration))
env_id = 'env_id_example' # str | The environment id for the flag evaluations in question.
flag_key = 'flag_key_example' # str | The key of the flag we want metrics for.

try:
    # [BETA] Get events usage by event id and the feature flag key.
    api_response = api_instance.get_evaluations(env_id, flag_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_evaluations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_id** | **str**| The environment id for the flag evaluations in question. | 
 **flag_key** | **str**| The key of the flag we want metrics for. | 

### Return type

[**StreamSDKVersion**](StreamSDKVersion.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event**
> StreamSDKVersion get_event(type)

[BETA] Get events usage by event type.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.UsageApi(launchdarkly_api.ApiClient(configuration))
type = 'type_example' # str | The type of event we would like to track.

try:
    # [BETA] Get events usage by event type.
    api_response = api_instance.get_event(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of event we would like to track. | 

### Return type

[**StreamSDKVersion**](StreamSDKVersion.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events**
> Events get_events()

[BETA] Get events usage endpoints.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.UsageApi(launchdarkly_api.ApiClient(configuration))

try:
    # [BETA] Get events usage endpoints.
    api_response = api_instance.get_events()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_events: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Events**](Events.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mau**
> MAU get_mau()

[BETA] Get monthly active user data.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.UsageApi(launchdarkly_api.ApiClient(configuration))

try:
    # [BETA] Get monthly active user data.
    api_response = api_instance.get_mau()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_mau: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MAU**](MAU.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mau_by_category**
> MAUbyCategory get_mau_by_category()

[BETA] Get monthly active user data by category.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.UsageApi(launchdarkly_api.ApiClient(configuration))

try:
    # [BETA] Get monthly active user data by category.
    api_response = api_instance.get_mau_by_category()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_mau_by_category: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MAUbyCategory**](MAUbyCategory.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream**
> Stream get_stream(source)

[BETA] Get a stream endpoint and return timeseries data.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.UsageApi(launchdarkly_api.ApiClient(configuration))
source = 'source_example' # str | The source of where the stream comes from.

try:
    # [BETA] Get a stream endpoint and return timeseries data.
    api_response = api_instance.get_stream(source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source of where the stream comes from. | 

### Return type

[**Stream**](Stream.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream_by_sdk**
> StreamBySDK get_stream_by_sdk(source)

[BETA] Get a stream timeseries data by source show sdk version metadata.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.UsageApi(launchdarkly_api.ApiClient(configuration))
source = 'source_example' # str | The source of where the stream comes from.

try:
    # [BETA] Get a stream timeseries data by source show sdk version metadata.
    api_response = api_instance.get_stream_by_sdk(source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_stream_by_sdk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source of where the stream comes from. | 

### Return type

[**StreamBySDK**](StreamBySDK.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream_sdk_version**
> StreamSDKVersion get_stream_sdk_version(source)

[BETA] Get a stream timeseries data by source and show all sdk version associated.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.UsageApi(launchdarkly_api.ApiClient(configuration))
source = 'source_example' # str | The source of where the stream comes from.

try:
    # [BETA] Get a stream timeseries data by source and show all sdk version associated.
    api_response = api_instance.get_stream_sdk_version(source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_stream_sdk_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source of where the stream comes from. | 

### Return type

[**StreamSDKVersion**](StreamSDKVersion.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_streams**
> Streams get_streams()

[BETA] Returns a list of all streams.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.UsageApi(launchdarkly_api.ApiClient(configuration))

try:
    # [BETA] Returns a list of all streams.
    api_response = api_instance.get_streams()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_streams: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Streams**](Streams.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage**
> Usage get_usage()

[BETA] Returns of the usage endpoints available.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.UsageApi(launchdarkly_api.ApiClient(configuration))

try:
    # [BETA] Returns of the usage endpoints available.
    api_response = api_instance.get_usage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_usage: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Usage**](Usage.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

