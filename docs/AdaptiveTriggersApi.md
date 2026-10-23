# launchdarkly_api.AdaptiveTriggersApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_adaptive_trigger**](AdaptiveTriggersApi.md#delete_adaptive_trigger) | **DELETE** /api/v2/projects/{projectKey}/environments/{environmentKey}/adaptive-triggers/{triggerID} | Delete an adaptive trigger
[**get_adaptive_trigger**](AdaptiveTriggersApi.md#get_adaptive_trigger) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/adaptive-triggers/{triggerID} | Get an adaptive trigger
[**list_adaptive_triggers**](AdaptiveTriggersApi.md#list_adaptive_triggers) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/adaptive-triggers | List adaptive triggers
[**patch_adaptive_trigger**](AdaptiveTriggersApi.md#patch_adaptive_trigger) | **PATCH** /api/v2/projects/{projectKey}/environments/{environmentKey}/adaptive-triggers/{triggerID} | Update an adaptive trigger
[**post_adaptive_trigger**](AdaptiveTriggersApi.md#post_adaptive_trigger) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/adaptive-triggers | Create an adaptive trigger
[**post_disable_adaptive_trigger**](AdaptiveTriggersApi.md#post_disable_adaptive_trigger) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/adaptive-triggers/{triggerID}/disable | Disable an adaptive trigger
[**post_enable_adaptive_trigger**](AdaptiveTriggersApi.md#post_enable_adaptive_trigger) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/adaptive-triggers/{triggerID}/enable | Enable an adaptive trigger


# **delete_adaptive_trigger**
> delete_adaptive_trigger(project_key, environment_key, trigger_id)

Delete an adaptive trigger

Delete a single adaptive trigger.

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
    api_instance = launchdarkly_api.AdaptiveTriggersApi(api_client)
    project_key = 'project_key_example' # str | 
    environment_key = 'environment_key_example' # str | 
    trigger_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete an adaptive trigger
        api_instance.delete_adaptive_trigger(project_key, environment_key, trigger_id)
    except Exception as e:
        print("Exception when calling AdaptiveTriggersApi->delete_adaptive_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **trigger_id** | **UUID**|  | 

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
**204** | No content |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**429** | Rate Limited |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_adaptive_trigger**
> AdaptiveTrigger get_adaptive_trigger(project_key, environment_key, trigger_id)

Get an adaptive trigger

Get a single adaptive trigger.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.adaptive_trigger import AdaptiveTrigger
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
    api_instance = launchdarkly_api.AdaptiveTriggersApi(api_client)
    project_key = 'project_key_example' # str | 
    environment_key = 'environment_key_example' # str | 
    trigger_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get an adaptive trigger
        api_response = api_instance.get_adaptive_trigger(project_key, environment_key, trigger_id)
        print("The response of AdaptiveTriggersApi->get_adaptive_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdaptiveTriggersApi->get_adaptive_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **trigger_id** | **UUID**|  | 

### Return type

[**AdaptiveTrigger**](AdaptiveTrigger.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Trigger |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**429** | Rate Limited |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_adaptive_triggers**
> AdaptiveTriggers list_adaptive_triggers(project_key, environment_key, resource_kind, resource_key, limit=limit, offset=offset)

List adaptive triggers

List all adaptive triggers for a resource.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.adaptive_trigger_resource_kind import AdaptiveTriggerResourceKind
from launchdarkly_api.models.adaptive_triggers import AdaptiveTriggers
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
    api_instance = launchdarkly_api.AdaptiveTriggersApi(api_client)
    project_key = 'project_key_example' # str | 
    environment_key = 'environment_key_example' # str | 
    resource_kind = launchdarkly_api.AdaptiveTriggerResourceKind() # AdaptiveTriggerResourceKind | 
    resource_key = 'resource_key_example' # str | 
    limit = 25 # int | The number of items to return. (optional) (default to 25)
    offset = 0 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional) (default to 0)

    try:
        # List adaptive triggers
        api_response = api_instance.list_adaptive_triggers(project_key, environment_key, resource_kind, resource_key, limit=limit, offset=offset)
        print("The response of AdaptiveTriggersApi->list_adaptive_triggers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdaptiveTriggersApi->list_adaptive_triggers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **resource_kind** | [**AdaptiveTriggerResourceKind**](.md)|  | 
 **resource_key** | **str**|  | 
 **limit** | **int**| The number of items to return. | [optional] [default to 25]
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] [default to 0]

### Return type

[**AdaptiveTriggers**](AdaptiveTriggers.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Adaptive Triggers list |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**429** | Rate Limited |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_adaptive_trigger**
> AdaptiveTrigger patch_adaptive_trigger(project_key, environment_key, trigger_id, update_adaptive_trigger_request)

Update an adaptive trigger

Update a single adaptive trigger.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.adaptive_trigger import AdaptiveTrigger
from launchdarkly_api.models.update_adaptive_trigger_request import UpdateAdaptiveTriggerRequest
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
    api_instance = launchdarkly_api.AdaptiveTriggersApi(api_client)
    project_key = 'project_key_example' # str | 
    environment_key = 'environment_key_example' # str | 
    trigger_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    update_adaptive_trigger_request = launchdarkly_api.UpdateAdaptiveTriggerRequest() # UpdateAdaptiveTriggerRequest | 

    try:
        # Update an adaptive trigger
        api_response = api_instance.patch_adaptive_trigger(project_key, environment_key, trigger_id, update_adaptive_trigger_request)
        print("The response of AdaptiveTriggersApi->patch_adaptive_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdaptiveTriggersApi->patch_adaptive_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **trigger_id** | **UUID**|  | 
 **update_adaptive_trigger_request** | [**UpdateAdaptiveTriggerRequest**](UpdateAdaptiveTriggerRequest.md)|  | 

### Return type

[**AdaptiveTrigger**](AdaptiveTrigger.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Adaptive Trigger updated |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**429** | Rate Limited |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_adaptive_trigger**
> AdaptiveTrigger post_adaptive_trigger(project_key, environment_key, create_adaptive_trigger_request)

Create an adaptive trigger

Create a new adaptive trigger for a resource.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.adaptive_trigger import AdaptiveTrigger
from launchdarkly_api.models.create_adaptive_trigger_request import CreateAdaptiveTriggerRequest
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
    api_instance = launchdarkly_api.AdaptiveTriggersApi(api_client)
    project_key = 'project_key_example' # str | 
    environment_key = 'environment_key_example' # str | 
    create_adaptive_trigger_request = launchdarkly_api.CreateAdaptiveTriggerRequest() # CreateAdaptiveTriggerRequest | 

    try:
        # Create an adaptive trigger
        api_response = api_instance.post_adaptive_trigger(project_key, environment_key, create_adaptive_trigger_request)
        print("The response of AdaptiveTriggersApi->post_adaptive_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdaptiveTriggersApi->post_adaptive_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **create_adaptive_trigger_request** | [**CreateAdaptiveTriggerRequest**](CreateAdaptiveTriggerRequest.md)|  | 

### Return type

[**AdaptiveTrigger**](AdaptiveTrigger.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Adaptive Trigger created |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**429** | Rate Limited |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_disable_adaptive_trigger**
> post_disable_adaptive_trigger(project_key, environment_key, trigger_id)

Disable an adaptive trigger

Disable an adaptive trigger.

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
    api_instance = launchdarkly_api.AdaptiveTriggersApi(api_client)
    project_key = 'project_key_example' # str | 
    environment_key = 'environment_key_example' # str | 
    trigger_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Disable an adaptive trigger
        api_instance.post_disable_adaptive_trigger(project_key, environment_key, trigger_id)
    except Exception as e:
        print("Exception when calling AdaptiveTriggersApi->post_disable_adaptive_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **trigger_id** | **UUID**|  | 

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
**204** | No content |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**429** | Rate Limited |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_enable_adaptive_trigger**
> post_enable_adaptive_trigger(project_key, environment_key, trigger_id)

Enable an adaptive trigger

Enable an adaptive trigger.

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
    api_instance = launchdarkly_api.AdaptiveTriggersApi(api_client)
    project_key = 'project_key_example' # str | 
    environment_key = 'environment_key_example' # str | 
    trigger_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Enable an adaptive trigger
        api_instance.post_enable_adaptive_trigger(project_key, environment_key, trigger_id)
    except Exception as e:
        print("Exception when calling AdaptiveTriggersApi->post_enable_adaptive_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **environment_key** | **str**|  | 
 **trigger_id** | **UUID**|  | 

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
**204** | No content |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**429** | Rate Limited |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

