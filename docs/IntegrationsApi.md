# launchdarkly_api.IntegrationsApi

All URIs are relative to *https://app.launchdarkly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_integration_subscription**](IntegrationsApi.md#delete_integration_subscription) | **DELETE** /integrations/{integrationKey}/{integrationId} | Delete an integration subscription by ID.
[**get_integration_subscription**](IntegrationsApi.md#get_integration_subscription) | **GET** /integrations/{integrationKey}/{integrationId} | Get a single integration subscription by ID.
[**get_integration_subscriptions**](IntegrationsApi.md#get_integration_subscriptions) | **GET** /integrations/{integrationKey} | Get a list of all configured integrations of a given kind.
[**get_integrations**](IntegrationsApi.md#get_integrations) | **GET** /integrations | Get a list of all configured audit log event integrations associated with this account.
[**patch_integration_subscription**](IntegrationsApi.md#patch_integration_subscription) | **PATCH** /integrations/{integrationKey}/{integrationId} | Modify an integration subscription by ID.
[**post_integration_subscription**](IntegrationsApi.md#post_integration_subscription) | **POST** /integrations/{integrationKey} | Create a new integration subscription of a given kind.


# **delete_integration_subscription**
> delete_integration_subscription(integration_key, integration_id)

Delete an integration subscription by ID.

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
api_instance = launchdarkly_api.IntegrationsApi(launchdarkly_api.ApiClient(configuration))
integration_key = 'integration_key_example' # str | The key used to specify the integration kind.
integration_id = 'integration_id_example' # str | The integration ID.

try:
    # Delete an integration subscription by ID.
    api_instance.delete_integration_subscription(integration_key, integration_id)
except ApiException as e:
    print("Exception when calling IntegrationsApi->delete_integration_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_key** | **str**| The key used to specify the integration kind. | 
 **integration_id** | **str**| The integration ID. | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_subscription**
> IntegrationSubscription get_integration_subscription(integration_key, integration_id)

Get a single integration subscription by ID.

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
api_instance = launchdarkly_api.IntegrationsApi(launchdarkly_api.ApiClient(configuration))
integration_key = 'integration_key_example' # str | The key used to specify the integration kind.
integration_id = 'integration_id_example' # str | The integration ID.

try:
    # Get a single integration subscription by ID.
    api_response = api_instance.get_integration_subscription(integration_key, integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integration_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_key** | **str**| The key used to specify the integration kind. | 
 **integration_id** | **str**| The integration ID. | 

### Return type

[**IntegrationSubscription**](IntegrationSubscription.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_subscriptions**
> Integration get_integration_subscriptions(integration_key)

Get a list of all configured integrations of a given kind.

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
api_instance = launchdarkly_api.IntegrationsApi(launchdarkly_api.ApiClient(configuration))
integration_key = 'integration_key_example' # str | The key used to specify the integration kind.

try:
    # Get a list of all configured integrations of a given kind.
    api_response = api_instance.get_integration_subscriptions(integration_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integration_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_key** | **str**| The key used to specify the integration kind. | 

### Return type

[**Integration**](Integration.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integrations**
> Integrations get_integrations()

Get a list of all configured audit log event integrations associated with this account.

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
api_instance = launchdarkly_api.IntegrationsApi(launchdarkly_api.ApiClient(configuration))

try:
    # Get a list of all configured audit log event integrations associated with this account.
    api_response = api_instance.get_integrations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integrations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Integrations**](Integrations.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_integration_subscription**
> IntegrationSubscription patch_integration_subscription(integration_key, integration_id, patch_delta)

Modify an integration subscription by ID.

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
api_instance = launchdarkly_api.IntegrationsApi(launchdarkly_api.ApiClient(configuration))
integration_key = 'integration_key_example' # str | The key used to specify the integration kind.
integration_id = 'integration_id_example' # str | The integration ID.
patch_delta = [launchdarkly_api.PatchOperation()] # list[PatchOperation] | Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/'

try:
    # Modify an integration subscription by ID.
    api_response = api_instance.patch_integration_subscription(integration_key, integration_id, patch_delta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->patch_integration_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_key** | **str**| The key used to specify the integration kind. | 
 **integration_id** | **str**| The integration ID. | 
 **patch_delta** | [**list[PatchOperation]**](PatchOperation.md)| Requires a JSON Patch representation of the desired changes to the project. &#39;http://jsonpatch.com/&#39; | 

### Return type

[**IntegrationSubscription**](IntegrationSubscription.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_integration_subscription**
> IntegrationSubscription post_integration_subscription(integration_key, subscription_body)

Create a new integration subscription of a given kind.

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
api_instance = launchdarkly_api.IntegrationsApi(launchdarkly_api.ApiClient(configuration))
integration_key = 'integration_key_example' # str | The key used to specify the integration kind.
subscription_body = launchdarkly_api.SubscriptionBody() # SubscriptionBody | Create a new integration subscription.

try:
    # Create a new integration subscription of a given kind.
    api_response = api_instance.post_integration_subscription(integration_key, subscription_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->post_integration_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_key** | **str**| The key used to specify the integration kind. | 
 **subscription_body** | [**SubscriptionBody**](SubscriptionBody.md)| Create a new integration subscription. | 

### Return type

[**IntegrationSubscription**](IntegrationSubscription.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

