# launchdarkly_api.AIConfigsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ai_config**](AIConfigsBetaApi.md#delete_ai_config) | **DELETE** /api/v2/projects/{projectKey}/ai-configs/{configKey} | Delete AI Config
[**delete_ai_config_variation**](AIConfigsBetaApi.md#delete_ai_config_variation) | **DELETE** /api/v2/projects/{projectKey}/ai-configs/{configKey}/variations/{variationKey} | Delete AI Config variation
[**delete_model_config**](AIConfigsBetaApi.md#delete_model_config) | **DELETE** /api/v2/projects/{projectKey}/ai-configs/model-configs/{modelConfigKey} | Delete an AI model config
[**get_ai_config**](AIConfigsBetaApi.md#get_ai_config) | **GET** /api/v2/projects/{projectKey}/ai-configs/{configKey} | Get AI Config
[**get_ai_config_metrics**](AIConfigsBetaApi.md#get_ai_config_metrics) | **GET** /api/v2/projects/{projectKey}/ai-configs/{configKey}/metrics | Get AI Config metrics
[**get_ai_config_metrics_by_variation**](AIConfigsBetaApi.md#get_ai_config_metrics_by_variation) | **GET** /api/v2/projects/{projectKey}/ai-configs/{configKey}/metrics-by-variation | Get AI Config metrics by variation
[**get_ai_config_variation**](AIConfigsBetaApi.md#get_ai_config_variation) | **GET** /api/v2/projects/{projectKey}/ai-configs/{configKey}/variations/{variationKey} | Get AI Config variation
[**get_ai_configs**](AIConfigsBetaApi.md#get_ai_configs) | **GET** /api/v2/projects/{projectKey}/ai-configs | List AI Configs
[**get_model_config**](AIConfigsBetaApi.md#get_model_config) | **GET** /api/v2/projects/{projectKey}/ai-configs/model-configs/{modelConfigKey} | Get AI model config
[**list_model_configs**](AIConfigsBetaApi.md#list_model_configs) | **GET** /api/v2/projects/{projectKey}/ai-configs/model-configs | List AI model configs
[**patch_ai_config**](AIConfigsBetaApi.md#patch_ai_config) | **PATCH** /api/v2/projects/{projectKey}/ai-configs/{configKey} | Update AI Config
[**patch_ai_config_variation**](AIConfigsBetaApi.md#patch_ai_config_variation) | **PATCH** /api/v2/projects/{projectKey}/ai-configs/{configKey}/variations/{variationKey} | Update AI Config variation
[**post_ai_config**](AIConfigsBetaApi.md#post_ai_config) | **POST** /api/v2/projects/{projectKey}/ai-configs | Create new AI Config
[**post_ai_config_variation**](AIConfigsBetaApi.md#post_ai_config_variation) | **POST** /api/v2/projects/{projectKey}/ai-configs/{configKey}/variations | Create AI Config variation
[**post_model_config**](AIConfigsBetaApi.md#post_model_config) | **POST** /api/v2/projects/{projectKey}/ai-configs/model-configs | Create an AI model config


# **delete_ai_config**
> delete_ai_config(project_key, config_key)

Delete AI Config

Delete an existing AI Config.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import ai_configs_beta_api
from launchdarkly_api.model.error import Error
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
    api_instance = ai_configs_beta_api.AIConfigsBetaApi(api_client)
    project_key = "default" # str | 
    config_key = "configKey_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete AI Config
        api_instance.delete_ai_config(project_key, config_key)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->delete_ai_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  |
 **config_key** | **str**|  |
 **ld_api_version** | **str**| Version of the endpoint. | defaults to "beta"

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
> delete_ai_config_variation(project_key, config_key, variation_key)

Delete AI Config variation

Delete a specific variation of an AI Config by config key and variation key.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import ai_configs_beta_api
from launchdarkly_api.model.error import Error
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
    api_instance = ai_configs_beta_api.AIConfigsBetaApi(api_client)
    project_key = "projectKey_example" # str | 
    config_key = "configKey_example" # str | 
    variation_key = "variationKey_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete AI Config variation
        api_instance.delete_ai_config_variation(project_key, config_key, variation_key)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->delete_ai_config_variation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  |
 **config_key** | **str**|  |
 **variation_key** | **str**|  |
 **ld_api_version** | **str**| Version of the endpoint. | defaults to "beta"

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
> delete_model_config(project_key, model_config_key)

Delete an AI model config

Delete an AI model config.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import ai_configs_beta_api
from launchdarkly_api.model.error import Error
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
    api_instance = ai_configs_beta_api.AIConfigsBetaApi(api_client)
    project_key = "default" # str | 
    model_config_key = "modelConfigKey_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an AI model config
        api_instance.delete_model_config(project_key, model_config_key)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->delete_model_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  |
 **model_config_key** | **str**|  |
 **ld_api_version** | **str**| Version of the endpoint. | defaults to "beta"

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

# **get_ai_config**
> AIConfig get_ai_config(project_key, config_key)

Get AI Config

Retrieve a specific AI Config by its key.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import ai_configs_beta_api
from launchdarkly_api.model.error import Error
from launchdarkly_api.model.ai_config import AIConfig
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
    api_instance = ai_configs_beta_api.AIConfigsBetaApi(api_client)
    project_key = "projectKey_example" # str | 
    config_key = "configKey_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get AI Config
        api_response = api_instance.get_ai_config(project_key, config_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->get_ai_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  |
 **config_key** | **str**|  |
 **ld_api_version** | **str**| Version of the endpoint. | defaults to "beta"

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
> Metrics get_ai_config_metrics(project_key, config_key, _from, to, env)

Get AI Config metrics

Retrieve usage metrics for an AI Config by config key.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import ai_configs_beta_api
from launchdarkly_api.model.error import Error
from launchdarkly_api.model.metrics import Metrics
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
    api_instance = ai_configs_beta_api.AIConfigsBetaApi(api_client)
    project_key = "projectKey_example" # str | 
    config_key = "configKey_example" # str | 
    _from = 1 # int | The starting time, as milliseconds since epoch (inclusive).
    to = 1 # int | The ending time, as milliseconds since epoch (exclusive). May not be more than 100 days after `from`.
    env = "env_example" # str | An environment key. Only metrics from this environment will be included.

    # example passing only required values which don't have defaults set
    try:
        # Get AI Config metrics
        api_response = api_instance.get_ai_config_metrics(project_key, config_key, _from, to, env)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->get_ai_config_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  |
 **config_key** | **str**|  |
 **_from** | **int**| The starting time, as milliseconds since epoch (inclusive). |
 **to** | **int**| The ending time, as milliseconds since epoch (exclusive). May not be more than 100 days after &#x60;from&#x60;. |
 **env** | **str**| An environment key. Only metrics from this environment will be included. |
 **ld_api_version** | **str**| Version of the endpoint. | defaults to "beta"

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
> MetricsByVariation get_ai_config_metrics_by_variation(project_key, config_key, _from, to, env)

Get AI Config metrics by variation

Retrieve usage metrics for an AI Config by config key, with results split by variation.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import ai_configs_beta_api
from launchdarkly_api.model.metrics_by_variation import MetricsByVariation
from launchdarkly_api.model.error import Error
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
    api_instance = ai_configs_beta_api.AIConfigsBetaApi(api_client)
    project_key = "projectKey_example" # str | 
    config_key = "configKey_example" # str | 
    _from = 1 # int | The starting time, as milliseconds since epoch (inclusive).
    to = 1 # int | The ending time, as milliseconds since epoch (exclusive). May not be more than 100 days after `from`.
    env = "env_example" # str | An environment key. Only metrics from this environment will be included.

    # example passing only required values which don't have defaults set
    try:
        # Get AI Config metrics by variation
        api_response = api_instance.get_ai_config_metrics_by_variation(project_key, config_key, _from, to, env)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->get_ai_config_metrics_by_variation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  |
 **config_key** | **str**|  |
 **_from** | **int**| The starting time, as milliseconds since epoch (inclusive). |
 **to** | **int**| The ending time, as milliseconds since epoch (exclusive). May not be more than 100 days after &#x60;from&#x60;. |
 **env** | **str**| An environment key. Only metrics from this environment will be included. |
 **ld_api_version** | **str**| Version of the endpoint. | defaults to "beta"

### Return type

[**MetricsByVariation**](MetricsByVariation.md)

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

# **get_ai_config_variation**
> AIConfigVariationsResponse get_ai_config_variation(project_key, config_key, variation_key)

Get AI Config variation

Get an AI Config variation by key. The response includes all variation versions for the given variation key.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import ai_configs_beta_api
from launchdarkly_api.model.ai_config_variations_response import AIConfigVariationsResponse
from launchdarkly_api.model.error import Error
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
    api_instance = ai_configs_beta_api.AIConfigsBetaApi(api_client)
    project_key = "default" # str | 
    config_key = "default" # str | 
    variation_key = "default" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get AI Config variation
        api_response = api_instance.get_ai_config_variation(project_key, config_key, variation_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->get_ai_config_variation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  |
 **config_key** | **str**|  |
 **variation_key** | **str**|  |
 **ld_api_version** | **str**| Version of the endpoint. | defaults to "beta"

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
> AIConfigs get_ai_configs(project_key)

List AI Configs

Get a list of all AI Configs in the given project.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import ai_configs_beta_api
from launchdarkly_api.model.ai_configs import AIConfigs
from launchdarkly_api.model.error import Error
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
    api_instance = ai_configs_beta_api.AIConfigsBetaApi(api_client)
    project_key = "default" # str | 
    sort = "sort_example" # str | A sort to apply to the list of AI Configs. (optional)
    limit = 1 # int | The number of AI Configs to return. (optional)
    offset = 1 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = "filter_example" # str | A filter to apply to the list of AI Configs. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List AI Configs
        api_response = api_instance.get_ai_configs(project_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->get_ai_configs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List AI Configs
        api_response = api_instance.get_ai_configs(project_key, sort=sort, limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->get_ai_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  |
 **ld_api_version** | **str**| Version of the endpoint. | defaults to "beta"
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

# **get_model_config**
> ModelConfig get_model_config(project_key, model_config_key)

Get AI model config

Get an AI model config by key.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import ai_configs_beta_api
from launchdarkly_api.model.error import Error
from launchdarkly_api.model.model_config import ModelConfig
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
    api_instance = ai_configs_beta_api.AIConfigsBetaApi(api_client)
    project_key = "default" # str | 
    model_config_key = "default" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get AI model config
        api_response = api_instance.get_model_config(project_key, model_config_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->get_model_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  |
 **model_config_key** | **str**|  |
 **ld_api_version** | **str**| Version of the endpoint. | defaults to "beta"

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

# **list_model_configs**
> [ModelConfig] list_model_configs(project_key)

List AI model configs

Get all AI model configs for a project.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import ai_configs_beta_api
from launchdarkly_api.model.error import Error
from launchdarkly_api.model.model_config import ModelConfig
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
    api_instance = ai_configs_beta_api.AIConfigsBetaApi(api_client)
    project_key = "default" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List AI model configs
        api_response = api_instance.list_model_configs(project_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->list_model_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  |
 **ld_api_version** | **str**| Version of the endpoint. | defaults to "beta"

### Return type

[**[ModelConfig]**](ModelConfig.md)

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
> AIConfig patch_ai_config(project_key, config_key)

Update AI Config

Edit an existing AI Config.  The request body must be a JSON object of the fields to update. The values you include replace the existing values for the fields.  Here's an example:   ```     {       \"description\": \"Example updated description\",       \"tags\": [\"new-tag\"]     }   ``` 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import ai_configs_beta_api
from launchdarkly_api.model.error import Error
from launchdarkly_api.model.ai_config import AIConfig
from launchdarkly_api.model.ai_config_patch import AIConfigPatch
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
    api_instance = ai_configs_beta_api.AIConfigsBetaApi(api_client)
    project_key = "projectKey_example" # str | 
    config_key = "configKey_example" # str | 
    ai_config_patch = AIConfigPatch(
        description="description_example",
        maintainer_id="maintainer_id_example",
        maintainer_team_key="maintainer_team_key_example",
        name="name_example",
        tags=[
            "tags_example",
        ],
    ) # AIConfigPatch | AI Config object to update (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update AI Config
        api_response = api_instance.patch_ai_config(project_key, config_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->patch_ai_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update AI Config
        api_response = api_instance.patch_ai_config(project_key, config_key, ai_config_patch=ai_config_patch)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->patch_ai_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  |
 **config_key** | **str**|  |
 **ld_api_version** | **str**| Version of the endpoint. | defaults to "beta"
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

# **patch_ai_config_variation**
> AIConfigVariation patch_ai_config_variation(project_key, config_key, variation_key)

Update AI Config variation

Edit an existing variation of an AI Config. This creates a new version of the variation.  The request body must be a JSON object of the fields to update. The values you include replace the existing values for the fields.  Here's an example: ```   {     \"messages\": [       {         \"role\": \"system\",         \"content\": \"The new message\"       }     ]   } ``` 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import ai_configs_beta_api
from launchdarkly_api.model.ai_config_variation import AIConfigVariation
from launchdarkly_api.model.error import Error
from launchdarkly_api.model.ai_config_variation_patch import AIConfigVariationPatch
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
    api_instance = ai_configs_beta_api.AIConfigsBetaApi(api_client)
    project_key = "projectKey_example" # str | 
    config_key = "configKey_example" # str | 
    variation_key = "variationKey_example" # str | 
    ai_config_variation_patch = AIConfigVariationPatch(
        messages=[
            Message(
                content="content_example",
                role="role_example",
            ),
        ],
        model={},
        model_config_key="model_config_key_example",
        name="name_example",
        published=True,
        state="state_example",
    ) # AIConfigVariationPatch | AI Config variation object to update (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update AI Config variation
        api_response = api_instance.patch_ai_config_variation(project_key, config_key, variation_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->patch_ai_config_variation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update AI Config variation
        api_response = api_instance.patch_ai_config_variation(project_key, config_key, variation_key, ai_config_variation_patch=ai_config_variation_patch)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->patch_ai_config_variation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  |
 **config_key** | **str**|  |
 **variation_key** | **str**|  |
 **ld_api_version** | **str**| Version of the endpoint. | defaults to "beta"
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

# **post_ai_config**
> AIConfig post_ai_config(project_key, ai_config_post)

Create new AI Config

Create a new AI Config within the given project.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import ai_configs_beta_api
from launchdarkly_api.model.ai_config_post import AIConfigPost
from launchdarkly_api.model.error import Error
from launchdarkly_api.model.ai_config import AIConfig
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
    api_instance = ai_configs_beta_api.AIConfigsBetaApi(api_client)
    project_key = "projectKey_example" # str | 
    ai_config_post = AIConfigPost(
        description="",
        key="key_example",
        maintainer_id="maintainer_id_example",
        maintainer_team_key="maintainer_team_key_example",
        name="name_example",
        tags=[
            "tags_example",
        ],
    ) # AIConfigPost | AI Config object to create

    # example passing only required values which don't have defaults set
    try:
        # Create new AI Config
        api_response = api_instance.post_ai_config(project_key, ai_config_post)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->post_ai_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  |
 **ai_config_post** | [**AIConfigPost**](AIConfigPost.md)| AI Config object to create |
 **ld_api_version** | **str**| Version of the endpoint. | defaults to "beta"

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
> AIConfigVariation post_ai_config_variation(project_key, config_key, ai_config_variation_post)

Create AI Config variation

Create a new variation for a given AI Config.  The <code>model</code> in the request body requires a <code>modelName</code> and <code>parameters</code>, for example:  ```   \"model\": {     \"modelName\": \"claude-3-opus-20240229\",     \"parameters\": {       \"max_tokens\": 1024     }   } ``` 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import ai_configs_beta_api
from launchdarkly_api.model.ai_config_variation import AIConfigVariation
from launchdarkly_api.model.ai_config_variation_post import AIConfigVariationPost
from launchdarkly_api.model.error import Error
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
    api_instance = ai_configs_beta_api.AIConfigsBetaApi(api_client)
    project_key = "projectKey_example" # str | 
    config_key = "configKey_example" # str | 
    ai_config_variation_post = AIConfigVariationPost(
        key="key_example",
        messages=[
            Message(
                content="content_example",
                role="role_example",
            ),
        ],
        model={},
        name="name_example",
        model_config_key="model_config_key_example",
    ) # AIConfigVariationPost | AI Config variation object to create

    # example passing only required values which don't have defaults set
    try:
        # Create AI Config variation
        api_response = api_instance.post_ai_config_variation(project_key, config_key, ai_config_variation_post)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->post_ai_config_variation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  |
 **config_key** | **str**|  |
 **ai_config_variation_post** | [**AIConfigVariationPost**](AIConfigVariationPost.md)| AI Config variation object to create |
 **ld_api_version** | **str**| Version of the endpoint. | defaults to "beta"

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

# **post_model_config**
> ModelConfig post_model_config(project_key, model_config_post)

Create an AI model config

Create an AI model config. You can use this in any variation for any AI Config in your project.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import ai_configs_beta_api
from launchdarkly_api.model.error import Error
from launchdarkly_api.model.model_config import ModelConfig
from launchdarkly_api.model.model_config_post import ModelConfigPost
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
    api_instance = ai_configs_beta_api.AIConfigsBetaApi(api_client)
    project_key = "default" # str | 
    model_config_post = ModelConfigPost(
        name="name_example",
        key="key_example",
        id="id_example",
        icon="icon_example",
        provider="provider_example",
        params={},
        custom_params={},
        tags=[
            "tags_example",
        ],
        cost_per_input_token=3.14,
        cost_per_output_token=3.14,
    ) # ModelConfigPost | AI model config object to create

    # example passing only required values which don't have defaults set
    try:
        # Create an AI model config
        api_response = api_instance.post_model_config(project_key, model_config_post)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AIConfigsBetaApi->post_model_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  |
 **model_config_post** | [**ModelConfigPost**](ModelConfigPost.md)| AI model config object to create |
 **ld_api_version** | **str**| Version of the endpoint. | defaults to "beta"

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

