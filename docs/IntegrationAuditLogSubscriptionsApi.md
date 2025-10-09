# launchdarkly_api.IntegrationAuditLogSubscriptionsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](IntegrationAuditLogSubscriptionsApi.md#create_subscription) | **POST** /api/v2/integrations/{integrationKey} | Create audit log subscription
[**delete_subscription**](IntegrationAuditLogSubscriptionsApi.md#delete_subscription) | **DELETE** /api/v2/integrations/{integrationKey}/{id} | Delete audit log subscription
[**get_subscription_by_id**](IntegrationAuditLogSubscriptionsApi.md#get_subscription_by_id) | **GET** /api/v2/integrations/{integrationKey}/{id} | Get audit log subscription by ID
[**get_subscriptions**](IntegrationAuditLogSubscriptionsApi.md#get_subscriptions) | **GET** /api/v2/integrations/{integrationKey} | Get audit log subscriptions by integration
[**update_subscription**](IntegrationAuditLogSubscriptionsApi.md#update_subscription) | **PATCH** /api/v2/integrations/{integrationKey}/{id} | Update audit log subscription


# **create_subscription**
> Integration create_subscription(integration_key, subscription_post)

Create audit log subscription

Create an audit log subscription.<br /><br />For each subscription, you must specify the set of resources you wish to subscribe to audit log notifications for. You can describe these resources using a custom role policy. To learn more, read [Custom role concepts](https://launchdarkly.com/docs/home/account/role-concepts).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.integration import Integration
from launchdarkly_api.models.subscription_post import SubscriptionPost
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
    api_instance = launchdarkly_api.IntegrationAuditLogSubscriptionsApi(api_client)
    integration_key = 'integration_key_example' # str | The integration key
    subscription_post = {"config":{"optional":"an optional property","required":"the required property","url":"https://example.com"},"name":"Example audit log subscription.","on":false,"statements":[{"actions":["*"],"effect":"allow","resources":["proj/*:env/*:flag/*;testing-tag"]}],"tags":["testing-tag"]} # SubscriptionPost | 

    try:
        # Create audit log subscription
        api_response = api_instance.create_subscription(integration_key, subscription_post)
        print("The response of IntegrationAuditLogSubscriptionsApi->create_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationAuditLogSubscriptionsApi->create_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_key** | **str**| The integration key | 
 **subscription_post** | [**SubscriptionPost**](SubscriptionPost.md)|  | 

### Return type

[**Integration**](Integration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Integration response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(integration_key, id)

Delete audit log subscription

Delete an audit log subscription.

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
    api_instance = launchdarkly_api.IntegrationAuditLogSubscriptionsApi(api_client)
    integration_key = 'integration_key_example' # str | The integration key
    id = 'id_example' # str | The subscription ID

    try:
        # Delete audit log subscription
        api_instance.delete_subscription(integration_key, id)
    except Exception as e:
        print("Exception when calling IntegrationAuditLogSubscriptionsApi->delete_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_key** | **str**| The integration key | 
 **id** | **str**| The subscription ID | 

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
**204** | Action succeeded |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_by_id**
> Integration get_subscription_by_id(integration_key, id)

Get audit log subscription by ID

Get an audit log subscription by ID.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.integration import Integration
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
    api_instance = launchdarkly_api.IntegrationAuditLogSubscriptionsApi(api_client)
    integration_key = 'integration_key_example' # str | The integration key
    id = 'id_example' # str | The subscription ID

    try:
        # Get audit log subscription by ID
        api_response = api_instance.get_subscription_by_id(integration_key, id)
        print("The response of IntegrationAuditLogSubscriptionsApi->get_subscription_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationAuditLogSubscriptionsApi->get_subscription_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_key** | **str**| The integration key | 
 **id** | **str**| The subscription ID | 

### Return type

[**Integration**](Integration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions**
> Integrations get_subscriptions(integration_key)

Get audit log subscriptions by integration

Get all audit log subscriptions associated with a given integration.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.integrations import Integrations
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
    api_instance = launchdarkly_api.IntegrationAuditLogSubscriptionsApi(api_client)
    integration_key = 'integration_key_example' # str | The integration key

    try:
        # Get audit log subscriptions by integration
        api_response = api_instance.get_subscriptions(integration_key)
        print("The response of IntegrationAuditLogSubscriptionsApi->get_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationAuditLogSubscriptionsApi->get_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_key** | **str**| The integration key | 

### Return type

[**Integrations**](Integrations.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integrations collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription**
> Integration update_subscription(integration_key, id, patch_operation)

Update audit log subscription

Update an audit log subscription configuration. Updating an audit log subscription uses a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.integration import Integration
from launchdarkly_api.models.patch_operation import PatchOperation
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
    api_instance = launchdarkly_api.IntegrationAuditLogSubscriptionsApi(api_client)
    integration_key = 'integration_key_example' # str | The integration key
    id = 'id_example' # str | The ID of the audit log subscription
    patch_operation = [{"op":"replace","path":"/on","value":false}] # List[PatchOperation] | 

    try:
        # Update audit log subscription
        api_response = api_instance.update_subscription(integration_key, id, patch_operation)
        print("The response of IntegrationAuditLogSubscriptionsApi->update_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationAuditLogSubscriptionsApi->update_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_key** | **str**| The integration key | 
 **id** | **str**| The ID of the audit log subscription | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**Integration**](Integration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration response |  -  |
**400** | Invalid request |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

