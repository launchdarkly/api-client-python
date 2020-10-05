# launchdarkly_api.RelayProxyConfigurationsApi

All URIs are relative to *https://app.launchdarkly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_relay_proxy_config**](RelayProxyConfigurationsApi.md#delete_relay_proxy_config) | **DELETE** /account/relay-auto-configs/{id} | Delete a relay proxy configuration by ID.
[**get_relay_proxy_config**](RelayProxyConfigurationsApi.md#get_relay_proxy_config) | **GET** /account/relay-auto-configs/{id} | Get a single relay proxy configuration by ID.
[**get_relay_proxy_configs**](RelayProxyConfigurationsApi.md#get_relay_proxy_configs) | **GET** /account/relay-auto-configs | Returns a list of relay proxy configurations in the account.
[**patch_relay_proxy_config**](RelayProxyConfigurationsApi.md#patch_relay_proxy_config) | **PATCH** /account/relay-auto-configs/{id} | Modify a relay proxy configuration by ID.
[**post_relay_auto_config**](RelayProxyConfigurationsApi.md#post_relay_auto_config) | **POST** /account/relay-auto-configs | Create a new relay proxy config.
[**reset_relay_proxy_config**](RelayProxyConfigurationsApi.md#reset_relay_proxy_config) | **POST** /account/relay-auto-configs/{id}/reset | Reset a relay proxy configuration&#39;s secret key with an optional expiry time for the old key.


# **delete_relay_proxy_config**
> delete_relay_proxy_config(id)

Delete a relay proxy configuration by ID.

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
api_instance = launchdarkly_api.RelayProxyConfigurationsApi(launchdarkly_api.ApiClient(configuration))
id = 'id_example' # str | The relay proxy configuration ID

try:
    # Delete a relay proxy configuration by ID.
    api_instance.delete_relay_proxy_config(id)
except ApiException as e:
    print("Exception when calling RelayProxyConfigurationsApi->delete_relay_proxy_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The relay proxy configuration ID | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relay_proxy_config**
> RelayProxyConfig get_relay_proxy_config(id)

Get a single relay proxy configuration by ID.

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
api_instance = launchdarkly_api.RelayProxyConfigurationsApi(launchdarkly_api.ApiClient(configuration))
id = 'id_example' # str | The relay proxy configuration ID

try:
    # Get a single relay proxy configuration by ID.
    api_response = api_instance.get_relay_proxy_config(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelayProxyConfigurationsApi->get_relay_proxy_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The relay proxy configuration ID | 

### Return type

[**RelayProxyConfig**](RelayProxyConfig.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relay_proxy_configs**
> RelayProxyConfigs get_relay_proxy_configs()

Returns a list of relay proxy configurations in the account.

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
api_instance = launchdarkly_api.RelayProxyConfigurationsApi(launchdarkly_api.ApiClient(configuration))

try:
    # Returns a list of relay proxy configurations in the account.
    api_response = api_instance.get_relay_proxy_configs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelayProxyConfigurationsApi->get_relay_proxy_configs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RelayProxyConfigs**](RelayProxyConfigs.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_relay_proxy_config**
> RelayProxyConfig patch_relay_proxy_config(id, patch_delta)

Modify a relay proxy configuration by ID.

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
api_instance = launchdarkly_api.RelayProxyConfigurationsApi(launchdarkly_api.ApiClient(configuration))
id = 'id_example' # str | The relay proxy configuration ID
patch_delta = [launchdarkly_api.PatchOperation()] # list[PatchOperation] | Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/'

try:
    # Modify a relay proxy configuration by ID.
    api_response = api_instance.patch_relay_proxy_config(id, patch_delta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelayProxyConfigurationsApi->patch_relay_proxy_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The relay proxy configuration ID | 
 **patch_delta** | [**list[PatchOperation]**](PatchOperation.md)| Requires a JSON Patch representation of the desired changes to the project. &#39;http://jsonpatch.com/&#39; | 

### Return type

[**RelayProxyConfig**](RelayProxyConfig.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_relay_auto_config**
> RelayProxyConfig post_relay_auto_config(relay_proxy_config_body)

Create a new relay proxy config.

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
api_instance = launchdarkly_api.RelayProxyConfigurationsApi(launchdarkly_api.ApiClient(configuration))
relay_proxy_config_body = launchdarkly_api.RelayProxyConfigBody() # RelayProxyConfigBody | Create a new relay proxy configuration

try:
    # Create a new relay proxy config.
    api_response = api_instance.post_relay_auto_config(relay_proxy_config_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelayProxyConfigurationsApi->post_relay_auto_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relay_proxy_config_body** | [**RelayProxyConfigBody**](RelayProxyConfigBody.md)| Create a new relay proxy configuration | 

### Return type

[**RelayProxyConfig**](RelayProxyConfig.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_relay_proxy_config**
> RelayProxyConfig reset_relay_proxy_config(id, expiry=expiry)

Reset a relay proxy configuration's secret key with an optional expiry time for the old key.

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
api_instance = launchdarkly_api.RelayProxyConfigurationsApi(launchdarkly_api.ApiClient(configuration))
id = 'id_example' # str | The relay proxy configuration ID
expiry = 789 # int | An expiration time for the old relay proxy configuration key, expressed as a Unix epoch time in milliseconds. By default, the relay proxy configuration will expire immediately (optional)

try:
    # Reset a relay proxy configuration's secret key with an optional expiry time for the old key.
    api_response = api_instance.reset_relay_proxy_config(id, expiry=expiry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelayProxyConfigurationsApi->reset_relay_proxy_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The relay proxy configuration ID | 
 **expiry** | **int**| An expiration time for the old relay proxy configuration key, expressed as a Unix epoch time in milliseconds. By default, the relay proxy configuration will expire immediately | [optional] 

### Return type

[**RelayProxyConfig**](RelayProxyConfig.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

