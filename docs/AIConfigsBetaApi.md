# launchdarkly_api.AIConfigsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ai_config**](AIConfigsBetaApi.md#delete_ai_config) | **DELETE** /api/v2/projects/{projectKey}/ai-configs/{configKey} | Delete AI Config
[**delete_ai_config_variation**](AIConfigsBetaApi.md#delete_ai_config_variation) | **DELETE** /api/v2/projects/{projectKey}/ai-configs/{configKey}/variations/{variationKey} | Delete AI Config variation
[**delete_ai_tool**](AIConfigsBetaApi.md#delete_ai_tool) | **DELETE** /api/v2/projects/{projectKey}/ai-tools/{toolKey} | Delete AI tool
[**delete_model_config**](AIConfigsBetaApi.md#delete_model_config) | **DELETE** /api/v2/projects/{projectKey}/ai-configs/model-configs/{modelConfigKey} | Delete an AI model config
[**delete_restricted_models**](AIConfigsBetaApi.md#delete_restricted_models) | **DELETE** /api/v2/projects/{projectKey}/ai-configs/model-configs/restricted | Remove AI models from the restricted list
[**get_ai_config**](AIConfigsBetaApi.md#get_ai_config) | **GET** /api/v2/projects/{projectKey}/ai-configs/{configKey} | Get AI Config
[**get_ai_config_metrics**](AIConfigsBetaApi.md#get_ai_config_metrics) | **GET** /api/v2/projects/{projectKey}/ai-configs/{configKey}/metrics | Get AI Config metrics
[**get_ai_config_metrics_by_variation**](AIConfigsBetaApi.md#get_ai_config_metrics_by_variation) | **GET** /api/v2/projects/{projectKey}/ai-configs/{configKey}/metrics-by-variation | Get AI Config metrics by variation
[**get_ai_config_targeting**](AIConfigsBetaApi.md#get_ai_config_targeting) | **GET** /api/v2/projects/{projectKey}/ai-configs/{configKey}/targeting | Show an AI Config&#39;s targeting
[**get_ai_config_variation**](AIConfigsBetaApi.md#get_ai_config_variation) | **GET** /api/v2/projects/{projectKey}/ai-configs/{configKey}/variations/{variationKey} | Get AI Config variation
[**get_ai_configs**](AIConfigsBetaApi.md#get_ai_configs) | **GET** /api/v2/projects/{projectKey}/ai-configs | List AI Configs
[**get_ai_tool**](AIConfigsBetaApi.md#get_ai_tool) | **GET** /api/v2/projects/{projectKey}/ai-tools/{toolKey} | Get AI tool
[**get_model_config**](AIConfigsBetaApi.md#get_model_config) | **GET** /api/v2/projects/{projectKey}/ai-configs/model-configs/{modelConfigKey} | Get AI model config
[**list_agent_graphs**](AIConfigsBetaApi.md#list_agent_graphs) | **GET** /api/v2/projects/{projectKey}/agent-graphs | List agent graphs
[**list_ai_tool_versions**](AIConfigsBetaApi.md#list_ai_tool_versions) | **GET** /api/v2/projects/{projectKey}/ai-tools/{toolKey}/versions | List AI tool versions
[**list_ai_tools**](AIConfigsBetaApi.md#list_ai_tools) | **GET** /api/v2/projects/{projectKey}/ai-tools | List AI tools
[**list_model_configs**](AIConfigsBetaApi.md#list_model_configs) | **GET** /api/v2/projects/{projectKey}/ai-configs/model-configs | List AI model configs
[**patch_ai_config**](AIConfigsBetaApi.md#patch_ai_config) | **PATCH** /api/v2/projects/{projectKey}/ai-configs/{configKey} | Update AI Config
[**patch_ai_config_targeting**](AIConfigsBetaApi.md#patch_ai_config_targeting) | **PATCH** /api/v2/projects/{projectKey}/ai-configs/{configKey}/targeting | Update AI Config targeting
[**patch_ai_config_variation**](AIConfigsBetaApi.md#patch_ai_config_variation) | **PATCH** /api/v2/projects/{projectKey}/ai-configs/{configKey}/variations/{variationKey} | Update AI Config variation
[**patch_ai_tool**](AIConfigsBetaApi.md#patch_ai_tool) | **PATCH** /api/v2/projects/{projectKey}/ai-tools/{toolKey} | Update AI tool
[**post_agent_graph**](AIConfigsBetaApi.md#post_agent_graph) | **POST** /api/v2/projects/{projectKey}/agent-graphs | Create new agent graph
[**post_ai_config**](AIConfigsBetaApi.md#post_ai_config) | **POST** /api/v2/projects/{projectKey}/ai-configs | Create new AI Config
[**post_ai_config_variation**](AIConfigsBetaApi.md#post_ai_config_variation) | **POST** /api/v2/projects/{projectKey}/ai-configs/{configKey}/variations | Create AI Config variation
[**post_ai_tool**](AIConfigsBetaApi.md#post_ai_tool) | **POST** /api/v2/projects/{projectKey}/ai-tools | Create an AI tool
[**post_model_config**](AIConfigsBetaApi.md#post_model_config) | **POST** /api/v2/projects/{projectKey}/ai-configs/model-configs | Create an AI model config
[**post_restricted_models**](AIConfigsBetaApi.md#post_restricted_models) | **POST** /api/v2/projects/{projectKey}/ai-configs/model-configs/restricted | Add AI models to the restricted list


# **delete_ai_config**
> delete_ai_config(ld_api_version, project_key, config_key)

Delete AI Config

Delete an existing AI Config.

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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    config_key = 'config_key_example' # str | 

    try:
        # Delete AI Config
        api_instance.delete_ai_config(ld_api_version, project_key, config_key)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->delete_ai_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **config_key** | **str**|  | 

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ai_config_variation**
> delete_ai_config_variation(ld_api_version, project_key, config_key, variation_key)

Delete AI Config variation

Delete a specific variation of an AI Config by config key and variation key.

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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 
    variation_key = 'variation_key_example' # str | 

    try:
        # Delete AI Config variation
        api_instance.delete_ai_config_variation(ld_api_version, project_key, config_key, variation_key)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->delete_ai_config_variation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **config_key** | **str**|  | 
 **variation_key** | **str**|  | 

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ai_tool**
> delete_ai_tool(ld_api_version, project_key, tool_key)

Delete AI tool

Delete an existing AI tool.

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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    tool_key = 'tool_key_example' # str | 

    try:
        # Delete AI tool
        api_instance.delete_ai_tool(ld_api_version, project_key, tool_key)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->delete_ai_tool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **tool_key** | **str**|  | 

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_config**
> delete_model_config(ld_api_version, project_key, model_config_key)

Delete an AI model config

Delete an AI model config.

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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    model_config_key = 'model_config_key_example' # str | 

    try:
        # Delete an AI model config
        api_instance.delete_model_config(ld_api_version, project_key, model_config_key)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->delete_model_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **model_config_key** | **str**|  | 

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_restricted_models**
> delete_restricted_models(ld_api_version, project_key, restricted_models_request)

Remove AI models from the restricted list

Remove AI models, by key, from the restricted list.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.restricted_models_request import RestrictedModelsRequest
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    restricted_models_request = launchdarkly_api.RestrictedModelsRequest() # RestrictedModelsRequest | List of AI model keys to remove from the restricted list

    try:
        # Remove AI models from the restricted list
        api_instance.delete_restricted_models(ld_api_version, project_key, restricted_models_request)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->delete_restricted_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **restricted_models_request** | [**RestrictedModelsRequest**](RestrictedModelsRequest.md)| List of AI model keys to remove from the restricted list | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_config**
> AIConfig get_ai_config(ld_api_version, project_key, config_key)

Get AI Config

Retrieve a specific AI Config by its key.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ai_config import AIConfig
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 

    try:
        # Get AI Config
        api_response = api_instance.get_ai_config(ld_api_version, project_key, config_key)
        print("The response of AIConfigsBetaApi->get_ai_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->get_ai_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **config_key** | **str**|  | 

### Return type

[**AIConfig**](AIConfig.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AI Config found |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_config_metrics**
> Metrics get_ai_config_metrics(ld_api_version, project_key, config_key, var_from, to, env)

Get AI Config metrics

Retrieve usage metrics for an AI Config by config key.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.metrics import Metrics
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 
    var_from = 56 # int | The starting time, as milliseconds since epoch (inclusive).
    to = 56 # int | The ending time, as milliseconds since epoch (exclusive). May not be more than 100 days after `from`.
    env = 'env_example' # str | An environment key. Only metrics from this environment will be included.

    try:
        # Get AI Config metrics
        api_response = api_instance.get_ai_config_metrics(ld_api_version, project_key, config_key, var_from, to, env)
        print("The response of AIConfigsBetaApi->get_ai_config_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->get_ai_config_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **config_key** | **str**|  | 
 **var_from** | **int**| The starting time, as milliseconds since epoch (inclusive). | 
 **to** | **int**| The ending time, as milliseconds since epoch (exclusive). May not be more than 100 days after &#x60;from&#x60;. | 
 **env** | **str**| An environment key. Only metrics from this environment will be included. | 

### Return type

[**Metrics**](Metrics.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metrics computed |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_config_metrics_by_variation**
> List[MetricByVariation] get_ai_config_metrics_by_variation(ld_api_version, project_key, config_key, var_from, to, env)

Get AI Config metrics by variation

Retrieve usage metrics for an AI Config by config key, with results split by variation.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.metric_by_variation import MetricByVariation
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 
    var_from = 56 # int | The starting time, as milliseconds since epoch (inclusive).
    to = 56 # int | The ending time, as milliseconds since epoch (exclusive). May not be more than 100 days after `from`.
    env = 'env_example' # str | An environment key. Only metrics from this environment will be included.

    try:
        # Get AI Config metrics by variation
        api_response = api_instance.get_ai_config_metrics_by_variation(ld_api_version, project_key, config_key, var_from, to, env)
        print("The response of AIConfigsBetaApi->get_ai_config_metrics_by_variation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->get_ai_config_metrics_by_variation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **config_key** | **str**|  | 
 **var_from** | **int**| The starting time, as milliseconds since epoch (inclusive). | 
 **to** | **int**| The ending time, as milliseconds since epoch (exclusive). May not be more than 100 days after &#x60;from&#x60;. | 
 **env** | **str**| An environment key. Only metrics from this environment will be included. | 

### Return type

[**List[MetricByVariation]**](MetricByVariation.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metrics computed |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_config_targeting**
> AIConfigTargeting get_ai_config_targeting(ld_api_version, project_key, config_key)

Show an AI Config's targeting

Retrieves a specific AI Config's targeting by its key

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ai_config_targeting import AIConfigTargeting
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 

    try:
        # Show an AI Config's targeting
        api_response = api_instance.get_ai_config_targeting(ld_api_version, project_key, config_key)
        print("The response of AIConfigsBetaApi->get_ai_config_targeting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->get_ai_config_targeting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **config_key** | **str**|  | 

### Return type

[**AIConfigTargeting**](AIConfigTargeting.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_config_variation**
> AIConfigVariationsResponse get_ai_config_variation(ld_api_version, project_key, config_key, variation_key)

Get AI Config variation

Get an AI Config variation by key. The response includes all variation versions for the given variation key.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ai_config_variations_response import AIConfigVariationsResponse
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    config_key = 'default' # str | 
    variation_key = 'default' # str | 

    try:
        # Get AI Config variation
        api_response = api_instance.get_ai_config_variation(ld_api_version, project_key, config_key, variation_key)
        print("The response of AIConfigsBetaApi->get_ai_config_variation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->get_ai_config_variation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **config_key** | **str**|  | 
 **variation_key** | **str**|  | 

### Return type

[**AIConfigVariationsResponse**](AIConfigVariationsResponse.md)

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

# **get_ai_configs**
> AIConfigs get_ai_configs(ld_api_version, project_key, sort=sort, limit=limit, offset=offset, filter=filter)

List AI Configs

Get a list of all AI Configs in the given project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ai_configs import AIConfigs
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    sort = 'sort_example' # str | A sort to apply to the list of AI Configs. (optional)
    limit = 56 # int | The number of AI Configs to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = 'filter_example' # str | A filter to apply to the list of AI Configs. (optional)

    try:
        # List AI Configs
        api_response = api_instance.get_ai_configs(ld_api_version, project_key, sort=sort, limit=limit, offset=offset, filter=filter)
        print("The response of AIConfigsBetaApi->get_ai_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->get_ai_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **sort** | **str**| A sort to apply to the list of AI Configs. | [optional] 
 **limit** | **int**| The number of AI Configs to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 
 **filter** | **str**| A filter to apply to the list of AI Configs. | [optional] 

### Return type

[**AIConfigs**](AIConfigs.md)

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

# **get_ai_tool**
> AITool get_ai_tool(ld_api_version, project_key, tool_key)

Get AI tool

Retrieve a specific AI tool by its key.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ai_tool import AITool
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    tool_key = 'tool_key_example' # str | 

    try:
        # Get AI tool
        api_response = api_instance.get_ai_tool(ld_api_version, project_key, tool_key)
        print("The response of AIConfigsBetaApi->get_ai_tool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->get_ai_tool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **tool_key** | **str**|  | 

### Return type

[**AITool**](AITool.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AI tool found |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_config**
> ModelConfig get_model_config(ld_api_version, project_key, model_config_key)

Get AI model config

Get an AI model config by key.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.model_config import ModelConfig
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    model_config_key = 'default' # str | 

    try:
        # Get AI model config
        api_response = api_instance.get_model_config(ld_api_version, project_key, model_config_key)
        print("The response of AIConfigsBetaApi->get_model_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->get_model_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **model_config_key** | **str**|  | 

### Return type

[**ModelConfig**](ModelConfig.md)

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

# **list_agent_graphs**
> AgentGraphs list_agent_graphs(ld_api_version, project_key, limit=limit, offset=offset)

List agent graphs

Get a list of all agent graphs in the given project. Returns metadata only, without edge data.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_graphs import AgentGraphs
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    limit = 56 # int | The number of AI Configs to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # List agent graphs
        api_response = api_instance.list_agent_graphs(ld_api_version, project_key, limit=limit, offset=offset)
        print("The response of AIConfigsBetaApi->list_agent_graphs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->list_agent_graphs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **limit** | **int**| The number of AI Configs to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**AgentGraphs**](AgentGraphs.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ai_tool_versions**
> AITools list_ai_tool_versions(ld_api_version, project_key, tool_key, sort=sort, limit=limit, offset=offset)

List AI tool versions

Get a list of all versions of an AI tool in the given project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ai_tools import AITools
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    tool_key = 'tool_key_example' # str | 
    sort = 'sort_example' # str | A sort to apply to the list of AI Configs. (optional)
    limit = 56 # int | The number of AI Configs to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # List AI tool versions
        api_response = api_instance.list_ai_tool_versions(ld_api_version, project_key, tool_key, sort=sort, limit=limit, offset=offset)
        print("The response of AIConfigsBetaApi->list_ai_tool_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->list_ai_tool_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **tool_key** | **str**|  | 
 **sort** | **str**| A sort to apply to the list of AI Configs. | [optional] 
 **limit** | **int**| The number of AI Configs to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**AITools**](AITools.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ai_tools**
> AITools list_ai_tools(ld_api_version, project_key, sort=sort, limit=limit, offset=offset, filter=filter)

List AI tools

Get a list of all AI tools in the given project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ai_tools import AITools
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    sort = 'sort_example' # str | A sort to apply to the list of AI Configs. (optional)
    limit = 56 # int | The number of AI Configs to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = 'filter_example' # str | A filter to apply to the list of AI Configs. (optional)

    try:
        # List AI tools
        api_response = api_instance.list_ai_tools(ld_api_version, project_key, sort=sort, limit=limit, offset=offset, filter=filter)
        print("The response of AIConfigsBetaApi->list_ai_tools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->list_ai_tools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **sort** | **str**| A sort to apply to the list of AI Configs. | [optional] 
 **limit** | **int**| The number of AI Configs to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 
 **filter** | **str**| A filter to apply to the list of AI Configs. | [optional] 

### Return type

[**AITools**](AITools.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_model_configs**
> List[ModelConfig] list_model_configs(ld_api_version, project_key, restricted=restricted)

List AI model configs

Get all AI model configs for a project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.model_config import ModelConfig
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    restricted = True # bool | Whether to return only restricted models (optional)

    try:
        # List AI model configs
        api_response = api_instance.list_model_configs(ld_api_version, project_key, restricted=restricted)
        print("The response of AIConfigsBetaApi->list_model_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->list_model_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **restricted** | **bool**| Whether to return only restricted models | [optional] 

### Return type

[**List[ModelConfig]**](ModelConfig.md)

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

# **patch_ai_config**
> AIConfig patch_ai_config(ld_api_version, project_key, config_key, ai_config_patch=ai_config_patch)

Update AI Config

Edit an existing AI Config.

The request body must be a JSON object of the fields to update. The values you include replace the existing values for the fields.

Here's an example:
  ```
    {
      "description": "Example updated description",
      "tags": ["new-tag"]
    }
  ```


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ai_config import AIConfig
from launchdarkly_api.models.ai_config_patch import AIConfigPatch
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 
    ai_config_patch = launchdarkly_api.AIConfigPatch() # AIConfigPatch | AI Config object to update (optional)

    try:
        # Update AI Config
        api_response = api_instance.patch_ai_config(ld_api_version, project_key, config_key, ai_config_patch=ai_config_patch)
        print("The response of AIConfigsBetaApi->patch_ai_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->patch_ai_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **config_key** | **str**|  | 
 **ai_config_patch** | [**AIConfigPatch**](AIConfigPatch.md)| AI Config object to update | [optional] 

### Return type

[**AIConfig**](AIConfig.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AI Config updated |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_ai_config_targeting**
> AIConfigTargeting patch_ai_config_targeting(ld_api_version, project_key, config_key, ai_config_targeting_patch=ai_config_targeting_patch)

Update AI Config targeting

Perform a partial update to an AI Config's targeting. The request body must be a valid semantic patch.

### Using semantic patches on an AI Config

To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](https://launchdarkly.com/docs/api#updates-using-semantic-patch).

The body of a semantic patch request for updating an AI Config's targeting takes the following properties:

* `comment` (string): (Optional) A description of the update.
* `environmentKey` (string): The key of the LaunchDarkly environment.
* `instructions` (array): (Required) A list of actions the update should perform. Each action in the list must be an object with a `kind` property that indicates the instruction. If the action requires parameters, you must include those parameters as additional fields in the object. The body of a single semantic patch can contain many different instructions.

### Instructions

Semantic patch requests support the following `kind` instructions for updating AI Configs.

<details>
<summary>Click to expand instructions for <strong>working with targeting and variations</strong> for AI Configs</summary>

#### addClauses

Adds the given clauses to the rule indicated by `ruleId`.

##### Parameters

- `ruleId`: ID of a rule in the AI Config.
- `clauses`: Array of clause objects, with `contextKind` (string), `attribute` (string), `op` (string), `negate` (boolean), and `values` (array of strings, numbers, or dates) properties. The `contextKind`, `attribute`, and `values` are case sensitive. The `op` must be lower-case.

Here's an example:

```json
{
  "environmentKey": "environment-key-123abc",
  "instructions": [{
    "kind": "addClauses",
    "ruleId": "a902ef4a-2faf-4eaf-88e1-ecc356708a29",
    "clauses": [{
      "contextKind": "user",
      "attribute": "country",
      "op": "in",
      "negate": false,
      "values": ["USA", "Canada"]
    }]
  }]
}
```

#### addRule

Adds a new targeting rule to the AI Config. The rule may contain `clauses` and serve the variation that `variationId` indicates, or serve a percentage rollout that `rolloutWeights`, `rolloutBucketBy`, and `rolloutContextKind` indicate.

If you set `beforeRuleId`, this adds the new rule before the indicated rule. Otherwise, adds the new rule to the end of the list.

##### Parameters

- `clauses`: Array of clause objects, with `contextKind` (string), `attribute` (string), `op` (string), `negate` (boolean), and `values` (array of strings, numbers, or dates) properties. The `contextKind`, `attribute`, and `values` are case sensitive. The `op` must be lower-case.
- `beforeRuleId`: (Optional) ID of a rule.
- Either
- `variationId`: ID of a variation.

or

- `rolloutWeights`: (Optional) Map of `variationId` to weight, in thousandths of a percent (0-100000).
- `rolloutBucketBy`: (Optional) Context attribute available in the specified `rolloutContextKind`.
- `rolloutContextKind`: (Optional) Context kind, defaults to `user`

Here's an example that uses a `variationId`:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [{
  "kind": "addRule",
  "variationId": "2f43f67c-3e4e-4945-a18a-26559378ca00",
  "clauses": [{
    "contextKind": "organization",
    "attribute": "located_in",
    "op": "in",
    "negate": false,
    "values": ["Sweden", "Norway"]
  }]
}]
}
```

Here's an example that uses a percentage rollout:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [{
  "kind": "addRule",
  "clauses": [{
    "contextKind": "organization",
    "attribute": "located_in",
    "op": "in",
    "negate": false,
    "values": ["Sweden", "Norway"]
  }],
  "rolloutContextKind": "organization",
  "rolloutWeights": {
    "2f43f67c-3e4e-4945-a18a-26559378ca00": 15000, // serve 15% this variation
    "e5830889-1ec5-4b0c-9cc9-c48790090c43": 85000  // serve 85% this variation
  }
}]
}
```

#### addTargets

Adds context keys to the individual context targets for the context kind that `contextKind` specifies and the variation that `variationId` specifies. Returns an error if this causes the AI Config to target the same context key in multiple variations.

##### Parameters

- `values`: List of context keys.
- `contextKind`: (Optional) Context kind to target, defaults to `user`
- `variationId`: ID of a variation.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [{
  "kind": "addTargets",
  "values": ["context-key-123abc", "context-key-456def"],
  "variationId": "2f43f67c-3e4e-4945-a18a-26559378ca00"
}]
}
```

#### addValuesToClause

Adds `values` to the values of the clause that `ruleId` and `clauseId` indicate. Does not update the context kind, attribute, or operator.

##### Parameters

- `ruleId`: ID of a rule in the AI Config.
- `clauseId`: ID of a clause in that rule.
- `values`: Array of strings, case sensitive.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [{
  "kind": "addValuesToClause",
  "ruleId": "a902ef4a-2faf-4eaf-88e1-ecc356708a29",
  "clauseId": "10a58772-3121-400f-846b-b8a04e8944ed",
  "values": ["beta_testers"]
}]
}
```

#### clearTargets

Removes all individual targets from the variation that `variationId` specifies. This includes both user and non-user targets.

##### Parameters

- `variationId`: ID of a variation.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [ { "kind": "clearTargets", "variationId": "2f43f67c-3e4e-4945-a18a-26559378ca00" } ]
}
```

#### removeClauses

Removes the clauses specified by `clauseIds` from the rule indicated by `ruleId`.

##### Parameters

- `ruleId`: ID of a rule.
- `clauseIds`: Array of IDs of clauses in the rule.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [{
  "kind": "removeClauses",
  "ruleId": "a902ef4a-2faf-4eaf-88e1-ecc356708a29",
  "clauseIds": ["10a58772-3121-400f-846b-b8a04e8944ed", "36a461dc-235e-4b08-97b9-73ce9365873e"]
}]
}
```

#### removeRule

Removes the targeting rule specified by `ruleId`. Does nothing if the rule does not exist.

##### Parameters

- `ruleId`: ID of a rule.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [ { "kind": "removeRule", "ruleId": "a902ef4a-2faf-4eaf-88e1-ecc356708a29" } ]
}
```

#### removeTargets

Removes context keys from the individual context targets for the context kind that `contextKind` specifies and the variation that `variationId` specifies. Does nothing if the flag does not target the context keys.

##### Parameters

- `values`: List of context keys.
- `contextKind`: (Optional) Context kind to target, defaults to `user`
- `variationId`: ID of a variation.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [{
  "kind": "removeTargets",
  "values": ["context-key-123abc", "context-key-456def"],
  "variationId": "2f43f67c-3e4e-4945-a18a-26559378ca00"
}]
}
```

#### removeValuesFromClause

Removes `values` from the values of the clause indicated by `ruleId` and `clauseId`. Does not update the context kind, attribute, or operator.

##### Parameters

- `ruleId`: ID of a rule.
- `clauseId`: ID of a clause in that rule.
- `values`: Array of strings, case sensitive.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [{
  "kind": "removeValuesFromClause",
  "ruleId": "a902ef4a-2faf-4eaf-88e1-ecc356708a29",
  "clauseId": "10a58772-3121-400f-846b-b8a04e8944ed",
  "values": ["beta_testers"]
}]
}
```

#### reorderRules

Rearranges the rules to match the order given in `ruleIds`. Returns an error if `ruleIds` does not match the current set of rules on the AI Config.

##### Parameters

- `ruleIds`: Array of IDs of all rules.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [{
  "kind": "reorderRules",
  "ruleIds": ["a902ef4a-2faf-4eaf-88e1-ecc356708a29", "63c238d1-835d-435e-8f21-c8d5e40b2a3d"]
}]
}
```

#### replaceRules

Removes all targeting rules for the AI Config and replaces them with the list you provide.

##### Parameters

- `rules`: A list of rules.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [
  {
    "kind": "replaceRules",
    "rules": [
      {
        "variationId": "2f43f67c-3e4e-4945-a18a-26559378ca00",
        "description": "My new rule",
        "clauses": [
          {
            "contextKind": "user",
            "attribute": "segmentMatch",
            "op": "segmentMatch",
            "values": ["test"]
          }
        ]
      }
    ]
  }
]
}
```

#### replaceTargets

Removes all existing targeting and replaces it with the list of targets you provide.

##### Parameters

- `targets`: A list of context targeting. Each item in the list includes an optional `contextKind` that defaults to `user`, a required `variationId`, and a required list of `values`.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [
  {
    "kind": "replaceTargets",
    "targets": [
      {
        "contextKind": "user",
        "variationId": "2f43f67c-3e4e-4945-a18a-26559378ca00",
        "values": ["user-key-123abc"]
      },
      {
        "contextKind": "device",
        "variationId": "e5830889-1ec5-4b0c-9cc9-c48790090c43",
        "values": ["device-key-456def"]
      }
    ]
  }
]
}
```

#### updateClause

Replaces the clause indicated by `ruleId` and `clauseId` with `clause`.

##### Parameters

- `ruleId`: ID of a rule.
- `clauseId`: ID of a clause in that rule.
- `clause`: New `clause` object, with `contextKind` (string), `attribute` (string), `op` (string), `negate` (boolean), and `values` (array of strings, numbers, or dates) properties. The `contextKind`, `attribute`, and `values` are case sensitive. The `op` must be lower-case.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [{
  "kind": "updateClause",
  "ruleId": "a902ef4a-2faf-4eaf-88e1-ecc356708a29",
  "clauseId": "10c7462a-2062-45ba-a8bb-dfb3de0f8af5",
  "clause": {
    "contextKind": "user",
    "attribute": "country",
    "op": "in",
    "negate": false,
    "values": ["Mexico", "Canada"]
  }
}]
}
```

#### updateDefaultVariation

Updates the default on or off variation of the AI Config.

##### Parameters

- `onVariationValue`: (Optional) The value of the variation of the new on variation.
- `offVariationValue`: (Optional) The value of the variation of the new off variation

Here's an example:

```json
{
"instructions": [ { "kind": "updateDefaultVariation", "OnVariationValue": true, "OffVariationValue": false } ]
}
```

#### updateFallthroughVariationOrRollout

Updates the default or "fallthrough" rule for the AI Config, which the AI Config serves when a context matches none of the targeting rules. The rule can serve either the variation that `variationId` indicates, or a percentage rollout that `rolloutWeights` and `rolloutBucketBy` indicate.

##### Parameters

- `variationId`: ID of a variation.

or

- `rolloutWeights`: Map of `variationId` to weight, in thousandths of a percent (0-100000).
- `rolloutBucketBy`: (Optional) Context attribute available in the specified `rolloutContextKind`.
- `rolloutContextKind`: (Optional) Context kind, defaults to `user`

Here's an example that uses a `variationId`:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [{
  "kind": "updateFallthroughVariationOrRollout",
  "variationId": "2f43f67c-3e4e-4945-a18a-26559378ca00"
}]
}
```

Here's an example that uses a percentage rollout:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [{
  "kind": "updateFallthroughVariationOrRollout",
  "rolloutContextKind": "user",
  "rolloutWeights": {
    "2f43f67c-3e4e-4945-a18a-26559378ca00": 15000, // serve 15% this variation
    "e5830889-1ec5-4b0c-9cc9-c48790090c43": 85000  // serve 85% this variation
  }
}]
}
```

#### updateOffVariation

Updates the default off variation to `variationId`. The AI Config serves the default off variation when the AI Config's targeting is **Off**.

##### Parameters

- `variationId`: ID of a variation.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [ { "kind": "updateOffVariation", "variationId": "2f43f67c-3e4e-4945-a18a-26559378ca00" } ]
}
```

#### updateRuleDescription

Updates the description of the targeting rule.

##### Parameters

- `description`: The new human-readable description for this rule.
- `ruleId`: The ID of the rule. You can retrieve this by making a GET request for the AI Config.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [{
  "kind": "updateRuleDescription",
  "description": "New rule description",
  "ruleId": "a902ef4a-2faf-4eaf-88e1-ecc356708a29"
}]
}
```

#### updateRuleTrackEvents

Updates whether or not LaunchDarkly tracks events for the AI Config associated with this rule.

##### Parameters

- `ruleId`: The ID of the rule. You can retrieve this by making a GET request for the AI Config.
- `trackEvents`: Whether or not events are tracked.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [{
  "kind": "updateRuleTrackEvents",
  "ruleId": "a902ef4a-2faf-4eaf-88e1-ecc356708a29",
  "trackEvents": true
}]
}
```

#### updateRuleVariationOrRollout

Updates what `ruleId` serves when its clauses evaluate to true. The rule can serve either the variation that `variationId` indicates, or a percent rollout that `rolloutWeights` and `rolloutBucketBy` indicate.

##### Parameters

- `ruleId`: ID of a rule.
- `variationId`: ID of a variation.

or

- `rolloutWeights`: Map of `variationId` to weight, in thousandths of a percent (0-100000).
- `rolloutBucketBy`: (Optional) Context attribute available in the specified `rolloutContextKind`.
- `rolloutContextKind`: (Optional) Context kind, defaults to `user`

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [{
  "kind": "updateRuleVariationOrRollout",
  "ruleId": "a902ef4a-2faf-4eaf-88e1-ecc356708a29",
  "variationId": "2f43f67c-3e4e-4945-a18a-26559378ca00"
}]
}
```

#### updateTrackEvents

Updates whether or not LaunchDarkly tracks events for the AI Config, for all rules.

##### Parameters

- `trackEvents`: Whether or not events are tracked.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [ { "kind": "updateTrackEvents", "trackEvents": true } ]
}
```

#### updateTrackEventsFallthrough

Updates whether or not LaunchDarkly tracks events for the AI Config, for the default rule.

##### Parameters

- `trackEvents`: Whether or not events are tracked.

Here's an example:

```json
{
"environmentKey": "environment-key-123abc",
"instructions": [ { "kind": "updateTrackEventsFallthrough", "trackEvents": true } ]
}
```
</details>


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ai_config_targeting import AIConfigTargeting
from launchdarkly_api.models.ai_config_targeting_patch import AIConfigTargetingPatch
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 
    ai_config_targeting_patch = launchdarkly_api.AIConfigTargetingPatch() # AIConfigTargetingPatch | AI Config targeting semantic patch instructions (optional)

    try:
        # Update AI Config targeting
        api_response = api_instance.patch_ai_config_targeting(ld_api_version, project_key, config_key, ai_config_targeting_patch=ai_config_targeting_patch)
        print("The response of AIConfigsBetaApi->patch_ai_config_targeting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->patch_ai_config_targeting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **config_key** | **str**|  | 
 **ai_config_targeting_patch** | [**AIConfigTargetingPatch**](AIConfigTargetingPatch.md)| AI Config targeting semantic patch instructions | [optional] 

### Return type

[**AIConfigTargeting**](AIConfigTargeting.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AI Config targeting updated |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_ai_config_variation**
> AIConfigVariation patch_ai_config_variation(ld_api_version, project_key, config_key, variation_key, ai_config_variation_patch=ai_config_variation_patch)

Update AI Config variation

Edit an existing variation of an AI Config. This creates a new version of the variation.

The request body must be a JSON object of the fields to update. The values you include replace the existing values for the fields.

Here's an example:
```
  {
    "messages": [
      {
        "role": "system",
        "content": "The new message"
      }
    ]
  }
```


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ai_config_variation import AIConfigVariation
from launchdarkly_api.models.ai_config_variation_patch import AIConfigVariationPatch
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 
    variation_key = 'variation_key_example' # str | 
    ai_config_variation_patch = launchdarkly_api.AIConfigVariationPatch() # AIConfigVariationPatch | AI Config variation object to update (optional)

    try:
        # Update AI Config variation
        api_response = api_instance.patch_ai_config_variation(ld_api_version, project_key, config_key, variation_key, ai_config_variation_patch=ai_config_variation_patch)
        print("The response of AIConfigsBetaApi->patch_ai_config_variation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->patch_ai_config_variation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **config_key** | **str**|  | 
 **variation_key** | **str**|  | 
 **ai_config_variation_patch** | [**AIConfigVariationPatch**](AIConfigVariationPatch.md)| AI Config variation object to update | [optional] 

### Return type

[**AIConfigVariation**](AIConfigVariation.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AI Config variation updated |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_ai_tool**
> AITool patch_ai_tool(ld_api_version, project_key, tool_key, ai_tool_patch=ai_tool_patch)

Update AI tool

Edit an existing AI tool.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ai_tool import AITool
from launchdarkly_api.models.ai_tool_patch import AIToolPatch
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    tool_key = 'tool_key_example' # str | 
    ai_tool_patch = launchdarkly_api.AIToolPatch() # AIToolPatch | AI tool object to update (optional)

    try:
        # Update AI tool
        api_response = api_instance.patch_ai_tool(ld_api_version, project_key, tool_key, ai_tool_patch=ai_tool_patch)
        print("The response of AIConfigsBetaApi->patch_ai_tool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->patch_ai_tool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **tool_key** | **str**|  | 
 **ai_tool_patch** | [**AIToolPatch**](AIToolPatch.md)| AI tool object to update | [optional] 

### Return type

[**AITool**](AITool.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AI tool updated |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_agent_graph**
> AgentGraph post_agent_graph(ld_api_version, project_key, agent_graph_post)

Create new agent graph

Create a new agent graph within the given project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_graph import AgentGraph
from launchdarkly_api.models.agent_graph_post import AgentGraphPost
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    agent_graph_post = launchdarkly_api.AgentGraphPost() # AgentGraphPost | Agent graph object to create

    try:
        # Create new agent graph
        api_response = api_instance.post_agent_graph(ld_api_version, project_key, agent_graph_post)
        print("The response of AIConfigsBetaApi->post_agent_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->post_agent_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **agent_graph_post** | [**AgentGraphPost**](AgentGraphPost.md)| Agent graph object to create | 

### Return type

[**AgentGraph**](AgentGraph.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Agent graph created |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**413** | Payload too large |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_config**
> AIConfig post_ai_config(ld_api_version, project_key, ai_config_post)

Create new AI Config

Create a new AI Config within the given project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ai_config import AIConfig
from launchdarkly_api.models.ai_config_post import AIConfigPost
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    ai_config_post = launchdarkly_api.AIConfigPost() # AIConfigPost | AI Config object to create

    try:
        # Create new AI Config
        api_response = api_instance.post_ai_config(ld_api_version, project_key, ai_config_post)
        print("The response of AIConfigsBetaApi->post_ai_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->post_ai_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **ai_config_post** | [**AIConfigPost**](AIConfigPost.md)| AI Config object to create | 

### Return type

[**AIConfig**](AIConfig.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | AI Config created |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_config_variation**
> AIConfigVariation post_ai_config_variation(ld_api_version, project_key, config_key, ai_config_variation_post)

Create AI Config variation

Create a new variation for a given AI Config.

The <code>model</code> in the request body requires a <code>modelName</code> and <code>parameters</code>, for example:

```
  "model": {
    "modelName": "claude-3-opus-20240229",
    "parameters": {
      "max_tokens": 1024
    }
  }
```


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ai_config_variation import AIConfigVariation
from launchdarkly_api.models.ai_config_variation_post import AIConfigVariationPost
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 
    ai_config_variation_post = launchdarkly_api.AIConfigVariationPost() # AIConfigVariationPost | AI Config variation object to create

    try:
        # Create AI Config variation
        api_response = api_instance.post_ai_config_variation(ld_api_version, project_key, config_key, ai_config_variation_post)
        print("The response of AIConfigsBetaApi->post_ai_config_variation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->post_ai_config_variation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **config_key** | **str**|  | 
 **ai_config_variation_post** | [**AIConfigVariationPost**](AIConfigVariationPost.md)| AI Config variation object to create | 

### Return type

[**AIConfigVariation**](AIConfigVariation.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | AI Config variation created |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_tool**
> AITool post_ai_tool(ld_api_version, project_key, ai_tool_post)

Create an AI tool

Create an AI tool

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.ai_tool import AITool
from launchdarkly_api.models.ai_tool_post import AIToolPost
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    ai_tool_post = launchdarkly_api.AIToolPost() # AIToolPost | AI tool object to create

    try:
        # Create an AI tool
        api_response = api_instance.post_ai_tool(ld_api_version, project_key, ai_tool_post)
        print("The response of AIConfigsBetaApi->post_ai_tool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->post_ai_tool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **ai_tool_post** | [**AIToolPost**](AIToolPost.md)| AI tool object to create | 

### Return type

[**AITool**](AITool.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | AI tool created |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_model_config**
> ModelConfig post_model_config(ld_api_version, project_key, model_config_post)

Create an AI model config

Create an AI model config. You can use this in any variation for any AI Config in your project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.model_config import ModelConfig
from launchdarkly_api.models.model_config_post import ModelConfigPost
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    model_config_post = launchdarkly_api.ModelConfigPost() # ModelConfigPost | AI model config object to create

    try:
        # Create an AI model config
        api_response = api_instance.post_model_config(ld_api_version, project_key, model_config_post)
        print("The response of AIConfigsBetaApi->post_model_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->post_model_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **model_config_post** | [**ModelConfigPost**](ModelConfigPost.md)| AI model config object to create | 

### Return type

[**ModelConfig**](ModelConfig.md)

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

# **post_restricted_models**
> RestrictedModelsResponse post_restricted_models(ld_api_version, project_key, restricted_models_request)

Add AI models to the restricted list

Add AI models, by key, to the restricted list. Keys are included in the response from the [List AI model configs](https://launchdarkly.com/docs/api/ai-configs-beta/list-model-configs) endpoint.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.restricted_models_request import RestrictedModelsRequest
from launchdarkly_api.models.restricted_models_response import RestrictedModelsResponse
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
    api_instance = launchdarkly_api.AIConfigsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    restricted_models_request = launchdarkly_api.RestrictedModelsRequest() # RestrictedModelsRequest | List of AI model keys to add to the restricted list.

    try:
        # Add AI models to the restricted list
        api_response = api_instance.post_restricted_models(ld_api_version, project_key, restricted_models_request)
        print("The response of AIConfigsBetaApi->post_restricted_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsBetaApi->post_restricted_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **restricted_models_request** | [**RestrictedModelsRequest**](RestrictedModelsRequest.md)| List of AI model keys to add to the restricted list. | 

### Return type

[**RestrictedModelsResponse**](RestrictedModelsResponse.md)

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

