# swagger_client.WebhooksApi

All URIs are relative to *https://app.launchdarkly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{webhookId} | Delete a webhook by ID
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /webhooks/{webhookId} | Get a webhook by ID
[**get_webhooks**](WebhooksApi.md#get_webhooks) | **GET** /webhooks | Fetch a list of all webhooks
[**patch_webhook**](WebhooksApi.md#patch_webhook) | **PATCH** /webhooks/{webhookId} | Modify a webhook by ID
[**post_webhook**](WebhooksApi.md#post_webhook) | **POST** /webhooks | Create a webhook


# **delete_webhook**
> delete_webhook(webhook_id)

Delete a webhook by ID

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebhooksApi()
webhook_id = 'webhook_id_example' # str | The webhook ID

try: 
    # Delete a webhook by ID
    api_instance.delete_webhook(webhook_id)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The webhook ID | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> Webhook get_webhook(webhook_id)

Get a webhook by ID

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebhooksApi()
webhook_id = 'webhook_id_example' # str | The webhook ID

try: 
    # Get a webhook by ID
    api_response = api_instance.get_webhook(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The webhook ID | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> Webhooks get_webhooks()

Fetch a list of all webhooks

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebhooksApi()

try: 
    # Fetch a list of all webhooks
    api_response = api_instance.get_webhooks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhooks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Webhooks**](Webhooks.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_webhook**
> patch_webhook(webhook_id, patch_delta)

Modify a webhook by ID

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebhooksApi()
webhook_id = 'webhook_id_example' # str | The webhook ID
patch_delta = [swagger_client.PatchDelta()] # list[PatchDelta] | http://jsonpatch.com/

try: 
    # Modify a webhook by ID
    api_instance.patch_webhook(webhook_id, patch_delta)
except ApiException as e:
    print("Exception when calling WebhooksApi->patch_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The webhook ID | 
 **patch_delta** | [**list[PatchDelta]**](PatchDelta.md)| http://jsonpatch.com/ | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_webhook**
> post_webhook(webhook_post)

Create a webhook

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebhooksApi()
webhook_post = swagger_client.WebhookPost() # WebhookPost | New webhook

try: 
    # Create a webhook
    api_instance.post_webhook(webhook_post)
except ApiException as e:
    print("Exception when calling WebhooksApi->post_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_post** | [**WebhookPost**](WebhookPost.md)| New webhook | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

