# launchdarkly_api.AgentControlApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_agent_graph**](AgentControlApi.md#delete_agent_graph) | **DELETE** /api/v2/projects/{projectKey}/agent-graphs/{graphKey} | Delete agent graph
[**delete_agent_optimization**](AgentControlApi.md#delete_agent_optimization) | **DELETE** /api/v2/projects/{projectKey}/agent-optimizations/{optimizationKey} | Delete an agent optimization
[**delete_agent_optimization_run**](AgentControlApi.md#delete_agent_optimization_run) | **DELETE** /api/v2/projects/{projectKey}/agent-optimizations/{optimizationKey}/runs/{runId} | Delete an agent optimization run
[**delete_agent_skill**](AgentControlApi.md#delete_agent_skill) | **DELETE** /api/v2/projects/{projectKey}/ai-configs/skills/{skillKey} | Delete an agent skill
[**delete_ai_config**](AgentControlApi.md#delete_ai_config) | **DELETE** /api/v2/projects/{projectKey}/ai-configs/{configKey} | Delete AI Config
[**delete_ai_config_variation**](AgentControlApi.md#delete_ai_config_variation) | **DELETE** /api/v2/projects/{projectKey}/ai-configs/{configKey}/variations/{variationKey} | Delete AI Config variation
[**delete_ai_tool**](AgentControlApi.md#delete_ai_tool) | **DELETE** /api/v2/projects/{projectKey}/ai-tools/{toolKey} | Delete AI tool
[**delete_model_config**](AgentControlApi.md#delete_model_config) | **DELETE** /api/v2/projects/{projectKey}/ai-configs/model-configs/{modelConfigKey} | Delete an AI model config
[**delete_prompt_snippet**](AgentControlApi.md#delete_prompt_snippet) | **DELETE** /api/v2/projects/{projectKey}/ai-configs/prompt-snippets/{snippetKey} | Delete a prompt snippet
[**delete_restricted_models**](AgentControlApi.md#delete_restricted_models) | **DELETE** /api/v2/projects/{projectKey}/ai-configs/model-configs/restricted | Remove AI models from the restricted list
[**get_agent_graph**](AgentControlApi.md#get_agent_graph) | **GET** /api/v2/projects/{projectKey}/agent-graphs/{graphKey} | Get agent graph
[**get_agent_optimization**](AgentControlApi.md#get_agent_optimization) | **GET** /api/v2/projects/{projectKey}/agent-optimizations/{optimizationKey} | Get an agent optimization
[**get_agent_skill**](AgentControlApi.md#get_agent_skill) | **GET** /api/v2/projects/{projectKey}/ai-configs/skills/{skillKey} | Get an agent skill
[**get_ai_config**](AgentControlApi.md#get_ai_config) | **GET** /api/v2/projects/{projectKey}/ai-configs/{configKey} | Get AI Config
[**get_ai_config_metrics**](AgentControlApi.md#get_ai_config_metrics) | **GET** /api/v2/projects/{projectKey}/ai-configs/{configKey}/metrics | Get AI Config metrics
[**get_ai_config_metrics_by_variation**](AgentControlApi.md#get_ai_config_metrics_by_variation) | **GET** /api/v2/projects/{projectKey}/ai-configs/{configKey}/metrics-by-variation | Get AI Config metrics by variation
[**get_ai_config_quick_stats**](AgentControlApi.md#get_ai_config_quick_stats) | **GET** /api/v2/projects/{projectKey}/ai-configs/quick-stats | Get AI Config quick stats
[**get_ai_config_targeting**](AgentControlApi.md#get_ai_config_targeting) | **GET** /api/v2/projects/{projectKey}/ai-configs/{configKey}/targeting | Show an AI Config&#39;s targeting
[**get_ai_config_variation**](AgentControlApi.md#get_ai_config_variation) | **GET** /api/v2/projects/{projectKey}/ai-configs/{configKey}/variations/{variationKey} | Get AI Config variation
[**get_ai_configs**](AgentControlApi.md#get_ai_configs) | **GET** /api/v2/projects/{projectKey}/ai-configs | List AI Configs
[**get_ai_tool**](AgentControlApi.md#get_ai_tool) | **GET** /api/v2/projects/{projectKey}/ai-tools/{toolKey} | Get AI tool
[**get_model_config**](AgentControlApi.md#get_model_config) | **GET** /api/v2/projects/{projectKey}/ai-configs/model-configs/{modelConfigKey} | Get AI model config
[**get_prompt_snippet**](AgentControlApi.md#get_prompt_snippet) | **GET** /api/v2/projects/{projectKey}/ai-configs/prompt-snippets/{snippetKey} | Get a prompt snippet
[**list_agent_graphs**](AgentControlApi.md#list_agent_graphs) | **GET** /api/v2/projects/{projectKey}/agent-graphs | List agent graphs
[**list_agent_optimization_results**](AgentControlApi.md#list_agent_optimization_results) | **GET** /api/v2/projects/{projectKey}/agent-optimizations/{optimizationKey}/results | List agent optimization runs
[**list_agent_optimization_results_by_run_id**](AgentControlApi.md#list_agent_optimization_results_by_run_id) | **GET** /api/v2/projects/{projectKey}/agent-optimizations/{optimizationKey}/runs/{runId}/results | List agent optimization results for a run
[**list_agent_optimizations**](AgentControlApi.md#list_agent_optimizations) | **GET** /api/v2/projects/{projectKey}/agent-optimizations | List agent optimizations
[**list_agent_skill_references**](AgentControlApi.md#list_agent_skill_references) | **GET** /api/v2/projects/{projectKey}/ai-configs/skills/{skillKey}/references | List agent skill references
[**list_agent_skill_versions**](AgentControlApi.md#list_agent_skill_versions) | **GET** /api/v2/projects/{projectKey}/ai-configs/skills/{skillKey}/versions | List agent skill versions
[**list_agent_skills**](AgentControlApi.md#list_agent_skills) | **GET** /api/v2/projects/{projectKey}/ai-configs/skills | List agent skills
[**list_ai_tool_versions**](AgentControlApi.md#list_ai_tool_versions) | **GET** /api/v2/projects/{projectKey}/ai-tools/{toolKey}/versions | List AI tool versions
[**list_ai_tools**](AgentControlApi.md#list_ai_tools) | **GET** /api/v2/projects/{projectKey}/ai-tools | List AI tools
[**list_all_agent_optimization_results**](AgentControlApi.md#list_all_agent_optimization_results) | **GET** /api/v2/projects/{projectKey}/agent-optimizations/{optimizationKey}/all-results | List all agent optimization results across versions
[**list_model_config_versions**](AgentControlApi.md#list_model_config_versions) | **GET** /api/v2/projects/{projectKey}/ai-configs/model-configs/{modelConfigKey}/versions | List AI model config versions
[**list_model_configs**](AgentControlApi.md#list_model_configs) | **GET** /api/v2/projects/{projectKey}/ai-configs/model-configs | List AI model configs
[**list_prompt_snippet_references**](AgentControlApi.md#list_prompt_snippet_references) | **GET** /api/v2/projects/{projectKey}/ai-configs/prompt-snippets/{snippetKey}/references | List prompt snippet references
[**list_prompt_snippet_versions**](AgentControlApi.md#list_prompt_snippet_versions) | **GET** /api/v2/projects/{projectKey}/ai-configs/prompt-snippets/{snippetKey}/versions | List prompt snippet versions
[**list_prompt_snippets**](AgentControlApi.md#list_prompt_snippets) | **GET** /api/v2/projects/{projectKey}/ai-configs/prompt-snippets | List prompt snippets
[**patch_agent_graph**](AgentControlApi.md#patch_agent_graph) | **PATCH** /api/v2/projects/{projectKey}/agent-graphs/{graphKey} | Update agent graph
[**patch_agent_optimization**](AgentControlApi.md#patch_agent_optimization) | **PATCH** /api/v2/projects/{projectKey}/agent-optimizations/{optimizationKey} | Update an agent optimization
[**patch_agent_optimization_result**](AgentControlApi.md#patch_agent_optimization_result) | **PATCH** /api/v2/projects/{projectKey}/agent-optimizations/{optimizationKey}/results/{resultId} | Update an agent optimization result
[**patch_agent_skill**](AgentControlApi.md#patch_agent_skill) | **PATCH** /api/v2/projects/{projectKey}/ai-configs/skills/{skillKey} | Update an agent skill
[**patch_ai_config**](AgentControlApi.md#patch_ai_config) | **PATCH** /api/v2/projects/{projectKey}/ai-configs/{configKey} | Update AI Config
[**patch_ai_config_targeting**](AgentControlApi.md#patch_ai_config_targeting) | **PATCH** /api/v2/projects/{projectKey}/ai-configs/{configKey}/targeting | Update AI Config targeting
[**patch_ai_config_variation**](AgentControlApi.md#patch_ai_config_variation) | **PATCH** /api/v2/projects/{projectKey}/ai-configs/{configKey}/variations/{variationKey} | Update AI Config variation
[**patch_ai_tool**](AgentControlApi.md#patch_ai_tool) | **PATCH** /api/v2/projects/{projectKey}/ai-tools/{toolKey} | Update AI tool
[**patch_model_config**](AgentControlApi.md#patch_model_config) | **PATCH** /api/v2/projects/{projectKey}/ai-configs/model-configs/{modelConfigKey} | Update an AI model config
[**patch_prompt_snippet**](AgentControlApi.md#patch_prompt_snippet) | **PATCH** /api/v2/projects/{projectKey}/ai-configs/prompt-snippets/{snippetKey} | Update a prompt snippet
[**post_agent_graph**](AgentControlApi.md#post_agent_graph) | **POST** /api/v2/projects/{projectKey}/agent-graphs | Create new agent graph
[**post_agent_optimization**](AgentControlApi.md#post_agent_optimization) | **POST** /api/v2/projects/{projectKey}/agent-optimizations | Create agent optimization
[**post_agent_optimization_result**](AgentControlApi.md#post_agent_optimization_result) | **POST** /api/v2/projects/{projectKey}/agent-optimizations/{optimizationKey}/results | Create agent optimization result
[**post_agent_skill**](AgentControlApi.md#post_agent_skill) | **POST** /api/v2/projects/{projectKey}/ai-configs/skills | Create an agent skill
[**post_ai_config**](AgentControlApi.md#post_ai_config) | **POST** /api/v2/projects/{projectKey}/ai-configs | Create new AI Config
[**post_ai_config_variation**](AgentControlApi.md#post_ai_config_variation) | **POST** /api/v2/projects/{projectKey}/ai-configs/{configKey}/variations | Create AI Config variation
[**post_ai_tool**](AgentControlApi.md#post_ai_tool) | **POST** /api/v2/projects/{projectKey}/ai-tools | Create an AI tool
[**post_model_config**](AgentControlApi.md#post_model_config) | **POST** /api/v2/projects/{projectKey}/ai-configs/model-configs | Create an AI model config
[**post_prompt_snippet**](AgentControlApi.md#post_prompt_snippet) | **POST** /api/v2/projects/{projectKey}/ai-configs/prompt-snippets | Create a prompt snippet
[**post_restricted_models**](AgentControlApi.md#post_restricted_models) | **POST** /api/v2/projects/{projectKey}/ai-configs/model-configs/restricted | Add AI models to the restricted list


# **delete_agent_graph**
> delete_agent_graph(ld_api_version, project_key, graph_key)

Delete agent graph

Delete an existing agent graph and all of its edges.

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    graph_key = 'graph_key_example' # str | 

    try:
        # Delete agent graph
        api_instance.delete_agent_graph(ld_api_version, project_key, graph_key)
    except Exception as e:
        print("Exception when calling AgentControlApi->delete_agent_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **graph_key** | **str**|  | 

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

# **delete_agent_optimization**
> delete_agent_optimization(project_key, optimization_key)

Delete an agent optimization

Delete an existing agent optimization.

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    optimization_key = 'optimization_key_example' # str | 

    try:
        # Delete an agent optimization
        api_instance.delete_agent_optimization(project_key, optimization_key)
    except Exception as e:
        print("Exception when calling AgentControlApi->delete_agent_optimization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **optimization_key** | **str**|  | 

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
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_optimization_run**
> delete_agent_optimization_run(ld_api_version, project_key, optimization_key, run_id)

Delete an agent optimization run

Delete all results for a specific run of an agent optimization. Returns a 404 if the optimization does not exist or if the run has no results. A run whose results have already been deleted is indistinguishable from a run that never existed, so repeating this request also returns a 404.

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    optimization_key = 'optimization_key_example' # str | 
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete an agent optimization run
        api_instance.delete_agent_optimization_run(ld_api_version, project_key, optimization_key, run_id)
    except Exception as e:
        print("Exception when calling AgentControlApi->delete_agent_optimization_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **optimization_key** | **str**|  | 
 **run_id** | **UUID**|  | 

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
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_skill**
> delete_agent_skill(project_key, skill_key)

Delete an agent skill

Delete an agent skill, including all of its versions.

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    skill_key = 'skill_key_example' # str | 

    try:
        # Delete an agent skill
        api_instance.delete_agent_skill(project_key, skill_key)
    except Exception as e:
        print("Exception when calling AgentControlApi->delete_agent_skill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **skill_key** | **str**|  | 

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
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ai_config**
> delete_ai_config(project_key, config_key)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'default' # str | 
    config_key = 'config_key_example' # str | 

    try:
        # Delete AI Config
        api_instance.delete_ai_config(project_key, config_key)
    except Exception as e:
        print("Exception when calling AgentControlApi->delete_ai_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> delete_ai_config_variation(project_key, config_key, variation_key)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 
    variation_key = 'variation_key_example' # str | 

    try:
        # Delete AI Config variation
        api_instance.delete_ai_config_variation(project_key, config_key, variation_key)
    except Exception as e:
        print("Exception when calling AgentControlApi->delete_ai_config_variation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> delete_ai_tool(project_key, tool_key)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    tool_key = 'tool_key_example' # str | 

    try:
        # Delete AI tool
        api_instance.delete_ai_tool(project_key, tool_key)
    except Exception as e:
        print("Exception when calling AgentControlApi->delete_ai_tool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> delete_model_config(project_key, model_config_key)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'default' # str | 
    model_config_key = 'model_config_key_example' # str | 

    try:
        # Delete an AI model config
        api_instance.delete_model_config(project_key, model_config_key)
    except Exception as e:
        print("Exception when calling AgentControlApi->delete_model_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_prompt_snippet**
> delete_prompt_snippet(project_key, snippet_key)

Delete a prompt snippet

Delete an existing prompt snippet.

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    snippet_key = 'snippet_key_example' # str | 

    try:
        # Delete a prompt snippet
        api_instance.delete_prompt_snippet(project_key, snippet_key)
    except Exception as e:
        print("Exception when calling AgentControlApi->delete_prompt_snippet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **snippet_key** | **str**|  | 

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
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_restricted_models**
> delete_restricted_models(project_key, restricted_models_request)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'default' # str | 
    restricted_models_request = launchdarkly_api.RestrictedModelsRequest() # RestrictedModelsRequest | List of AI model keys to remove from the restricted list

    try:
        # Remove AI models from the restricted list
        api_instance.delete_restricted_models(project_key, restricted_models_request)
    except Exception as e:
        print("Exception when calling AgentControlApi->delete_restricted_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_agent_graph**
> AgentGraph get_agent_graph(ld_api_version, project_key, graph_key)

Get agent graph

Retrieve a specific agent graph by its key, including its edges.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_graph import AgentGraph
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    graph_key = 'graph_key_example' # str | 

    try:
        # Get agent graph
        api_response = api_instance.get_agent_graph(ld_api_version, project_key, graph_key)
        print("The response of AgentControlApi->get_agent_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->get_agent_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **graph_key** | **str**|  | 

### Return type

[**AgentGraph**](AgentGraph.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent graph found |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_optimization**
> AgentOptimization get_agent_optimization(project_key, optimization_key)

Get an agent optimization

Retrieve a specific agent optimization by its key.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_optimization import AgentOptimization
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    optimization_key = 'optimization_key_example' # str | 

    try:
        # Get an agent optimization
        api_response = api_instance.get_agent_optimization(project_key, optimization_key)
        print("The response of AgentControlApi->get_agent_optimization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->get_agent_optimization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **optimization_key** | **str**|  | 

### Return type

[**AgentOptimization**](AgentOptimization.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent optimization found |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_skill**
> AgentSkill get_agent_skill(project_key, skill_key)

Get an agent skill

Retrieve a specific agent skill by its key.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_skill import AgentSkill
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    skill_key = 'skill_key_example' # str | 

    try:
        # Get an agent skill
        api_response = api_instance.get_agent_skill(project_key, skill_key)
        print("The response of AgentControlApi->get_agent_skill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->get_agent_skill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **skill_key** | **str**|  | 

### Return type

[**AgentSkill**](AgentSkill.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent skill found |  -  |
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 

    try:
        # Get AI Config
        api_response = api_instance.get_ai_config(project_key, config_key)
        print("The response of AgentControlApi->get_ai_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->get_ai_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> Metrics get_ai_config_metrics(project_key, config_key, var_from, to, env, context_kind=context_kind, context_key=context_key)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 
    var_from = 56 # int | The starting time, as milliseconds since epoch (inclusive).
    to = 56 # int | The ending time, as milliseconds since epoch (exclusive). May not be more than 100 days after `from`.
    env = 'env_example' # str | An environment key. Only metrics from this environment will be included.
    context_kind = 'context_kind_example' # str | A context kind. Only metrics from events that include a context of this kind are included. Required if `contextKey` is provided. (optional)
    context_key = 'context_key_example' # str | A context key. Only metrics from events whose context of the `contextKind` kind has this key are included. Requires `contextKind`. (optional)

    try:
        # Get AI Config metrics
        api_response = api_instance.get_ai_config_metrics(project_key, config_key, var_from, to, env, context_kind=context_kind, context_key=context_key)
        print("The response of AgentControlApi->get_ai_config_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->get_ai_config_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **config_key** | **str**|  | 
 **var_from** | **int**| The starting time, as milliseconds since epoch (inclusive). | 
 **to** | **int**| The ending time, as milliseconds since epoch (exclusive). May not be more than 100 days after &#x60;from&#x60;. | 
 **env** | **str**| An environment key. Only metrics from this environment will be included. | 
 **context_kind** | **str**| A context kind. Only metrics from events that include a context of this kind are included. Required if &#x60;contextKey&#x60; is provided. | [optional] 
 **context_key** | **str**| A context key. Only metrics from events whose context of the &#x60;contextKind&#x60; kind has this key are included. Requires &#x60;contextKind&#x60;. | [optional] 

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
> List[MetricByVariation] get_ai_config_metrics_by_variation(project_key, config_key, var_from, to, env, context_kind=context_kind, context_key=context_key)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 
    var_from = 56 # int | The starting time, as milliseconds since epoch (inclusive).
    to = 56 # int | The ending time, as milliseconds since epoch (exclusive). May not be more than 100 days after `from`.
    env = 'env_example' # str | An environment key. Only metrics from this environment will be included.
    context_kind = 'context_kind_example' # str | A context kind. Only metrics from events that include a context of this kind are included. Required if `contextKey` is provided. (optional)
    context_key = 'context_key_example' # str | A context key. Only metrics from events whose context of the `contextKind` kind has this key are included. Requires `contextKind`. (optional)

    try:
        # Get AI Config metrics by variation
        api_response = api_instance.get_ai_config_metrics_by_variation(project_key, config_key, var_from, to, env, context_kind=context_kind, context_key=context_key)
        print("The response of AgentControlApi->get_ai_config_metrics_by_variation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->get_ai_config_metrics_by_variation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **config_key** | **str**|  | 
 **var_from** | **int**| The starting time, as milliseconds since epoch (inclusive). | 
 **to** | **int**| The ending time, as milliseconds since epoch (exclusive). May not be more than 100 days after &#x60;from&#x60;. | 
 **env** | **str**| An environment key. Only metrics from this environment will be included. | 
 **context_kind** | **str**| A context kind. Only metrics from events that include a context of this kind are included. Required if &#x60;contextKey&#x60; is provided. | [optional] 
 **context_key** | **str**| A context key. Only metrics from events whose context of the &#x60;contextKind&#x60; kind has this key are included. Requires &#x60;contextKind&#x60;. | [optional] 

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

# **get_ai_config_quick_stats**
> QuickStats get_ai_config_quick_stats(project_key, env)

Get AI Config quick stats

Retrieve aggregate quick stats for AI Configs in a project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.quick_stats import QuickStats
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    env = 'env_example' # str | An environment key. Only metrics from this environment will be included.

    try:
        # Get AI Config quick stats
        api_response = api_instance.get_ai_config_quick_stats(project_key, env)
        print("The response of AgentControlApi->get_ai_config_quick_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->get_ai_config_quick_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **env** | **str**| An environment key. Only metrics from this environment will be included. | 

### Return type

[**QuickStats**](QuickStats.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quick stats computed |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_config_targeting**
> AIConfigTargeting get_ai_config_targeting(project_key, config_key)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 

    try:
        # Show an AI Config's targeting
        api_response = api_instance.get_ai_config_targeting(project_key, config_key)
        print("The response of AgentControlApi->get_ai_config_targeting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->get_ai_config_targeting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> AIConfigVariationsResponse get_ai_config_variation(project_key, config_key, variation_key)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'default' # str | 
    config_key = 'default' # str | 
    variation_key = 'default' # str | 

    try:
        # Get AI Config variation
        api_response = api_instance.get_ai_config_variation(project_key, config_key, variation_key)
        print("The response of AgentControlApi->get_ai_config_variation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->get_ai_config_variation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> AIConfigs get_ai_configs(project_key, sort=sort, limit=limit, offset=offset, filter=filter)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'default' # str | 
    sort = 'sort_example' # str | A sort to apply to the list of AgentControl configs. (optional)
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = 'filter_example' # str | A filter to apply to the list. (optional)

    try:
        # List AI Configs
        api_response = api_instance.get_ai_configs(project_key, sort=sort, limit=limit, offset=offset, filter=filter)
        print("The response of AgentControlApi->get_ai_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->get_ai_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **sort** | **str**| A sort to apply to the list of AgentControl configs. | [optional] 
 **limit** | **int**| The number of resources to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 
 **filter** | **str**| A filter to apply to the list. | [optional] 

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
> AITool get_ai_tool(project_key, tool_key)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    tool_key = 'tool_key_example' # str | 

    try:
        # Get AI tool
        api_response = api_instance.get_ai_tool(project_key, tool_key)
        print("The response of AgentControlApi->get_ai_tool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->get_ai_tool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> ModelConfig get_model_config(project_key, model_config_key, version=version)

Get AI model config

Get an AI model config by key. Specify a version to retrieve a historical custom model config version. Global model configs accept version 0 or 1 and return their current representation.

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'default' # str | 
    model_config_key = 'default' # str | 
    version = 56 # int | Specific model config version to return. Omit to return the latest version. (optional)

    try:
        # Get AI model config
        api_response = api_instance.get_model_config(project_key, model_config_key, version=version)
        print("The response of AgentControlApi->get_model_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->get_model_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **model_config_key** | **str**|  | 
 **version** | **int**| Specific model config version to return. Omit to return the latest version. | [optional] 

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

# **get_prompt_snippet**
> PromptSnippet get_prompt_snippet(project_key, snippet_key)

Get a prompt snippet

Retrieve a specific prompt snippet by its key.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.prompt_snippet import PromptSnippet
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    snippet_key = 'snippet_key_example' # str | 

    try:
        # Get a prompt snippet
        api_response = api_instance.get_prompt_snippet(project_key, snippet_key)
        print("The response of AgentControlApi->get_prompt_snippet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->get_prompt_snippet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **snippet_key** | **str**|  | 

### Return type

[**PromptSnippet**](PromptSnippet.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prompt snippet found |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agent_graphs**
> AgentGraphs list_agent_graphs(ld_api_version, project_key, limit=limit, offset=offset, filter=filter)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = 'filter_example' # str | A filter to apply to the list. (optional)

    try:
        # List agent graphs
        api_response = api_instance.list_agent_graphs(ld_api_version, project_key, limit=limit, offset=offset, filter=filter)
        print("The response of AgentControlApi->list_agent_graphs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->list_agent_graphs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **limit** | **int**| The number of resources to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 
 **filter** | **str**| A filter to apply to the list. | [optional] 

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

# **list_agent_optimization_results**
> AgentOptimizationResults list_agent_optimization_results(project_key, optimization_key, limit=limit, offset=offset)

List agent optimization runs

Get the most recent result for each unique run of an agent optimization.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_optimization_results import AgentOptimizationResults
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    optimization_key = 'optimization_key_example' # str | 
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # List agent optimization runs
        api_response = api_instance.list_agent_optimization_results(project_key, optimization_key, limit=limit, offset=offset)
        print("The response of AgentControlApi->list_agent_optimization_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->list_agent_optimization_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **optimization_key** | **str**|  | 
 **limit** | **int**| The number of resources to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**AgentOptimizationResults**](AgentOptimizationResults.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent optimization results list |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agent_optimization_results_by_run_id**
> AgentOptimizationResults list_agent_optimization_results_by_run_id(project_key, optimization_key, run_id)

List agent optimization results for a run

Get all results for a specific run of an agent optimization, sorted by iteration descending.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_optimization_results import AgentOptimizationResults
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    optimization_key = 'optimization_key_example' # str | 
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # List agent optimization results for a run
        api_response = api_instance.list_agent_optimization_results_by_run_id(project_key, optimization_key, run_id)
        print("The response of AgentControlApi->list_agent_optimization_results_by_run_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->list_agent_optimization_results_by_run_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **optimization_key** | **str**|  | 
 **run_id** | **UUID**|  | 

### Return type

[**AgentOptimizationResults**](AgentOptimizationResults.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent optimization results for run |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agent_optimizations**
> AgentOptimizations list_agent_optimizations(project_key, limit=limit, offset=offset, filter=filter)

List agent optimizations

Get a list of all agent optimizations in the given project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_optimizations import AgentOptimizations
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = 'filter_example' # str | A filter to apply to the list. (optional)

    try:
        # List agent optimizations
        api_response = api_instance.list_agent_optimizations(project_key, limit=limit, offset=offset, filter=filter)
        print("The response of AgentControlApi->list_agent_optimizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->list_agent_optimizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **limit** | **int**| The number of resources to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 
 **filter** | **str**| A filter to apply to the list. | [optional] 

### Return type

[**AgentOptimizations**](AgentOptimizations.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent optimizations list |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agent_skill_references**
> AgentSkillReferences list_agent_skill_references(project_key, skill_key, limit=limit, offset=offset)

List agent skill references

Get all config variations that currently reference this agent skill.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_skill_references import AgentSkillReferences
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    skill_key = 'skill_key_example' # str | 
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # List agent skill references
        api_response = api_instance.list_agent_skill_references(project_key, skill_key, limit=limit, offset=offset)
        print("The response of AgentControlApi->list_agent_skill_references:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->list_agent_skill_references: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **skill_key** | **str**|  | 
 **limit** | **int**| The number of resources to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**AgentSkillReferences**](AgentSkillReferences.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent skill references |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agent_skill_versions**
> AgentSkills list_agent_skill_versions(project_key, skill_key, limit=limit, offset=offset)

List agent skill versions

Get all versions of an agent skill in the given project, ordered by version descending.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_skills import AgentSkills
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    skill_key = 'skill_key_example' # str | 
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # List agent skill versions
        api_response = api_instance.list_agent_skill_versions(project_key, skill_key, limit=limit, offset=offset)
        print("The response of AgentControlApi->list_agent_skill_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->list_agent_skill_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **skill_key** | **str**|  | 
 **limit** | **int**| The number of resources to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**AgentSkills**](AgentSkills.md)

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

# **list_agent_skills**
> AgentSkills list_agent_skills(project_key, limit=limit, offset=offset, filter=filter)

List agent skills

Get a list of all agent skills in the given project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_skills import AgentSkills
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = 'filter_example' # str | A filter to apply to the list. (optional)

    try:
        # List agent skills
        api_response = api_instance.list_agent_skills(project_key, limit=limit, offset=offset, filter=filter)
        print("The response of AgentControlApi->list_agent_skills:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->list_agent_skills: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **limit** | **int**| The number of resources to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 
 **filter** | **str**| A filter to apply to the list. | [optional] 

### Return type

[**AgentSkills**](AgentSkills.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent skills list |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ai_tool_versions**
> AITools list_ai_tool_versions(project_key, tool_key, sort=sort, limit=limit, offset=offset)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    tool_key = 'tool_key_example' # str | 
    sort = 'sort_example' # str | A sort to apply to the list of AgentControl configs. (optional)
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # List AI tool versions
        api_response = api_instance.list_ai_tool_versions(project_key, tool_key, sort=sort, limit=limit, offset=offset)
        print("The response of AgentControlApi->list_ai_tool_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->list_ai_tool_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **tool_key** | **str**|  | 
 **sort** | **str**| A sort to apply to the list of AgentControl configs. | [optional] 
 **limit** | **int**| The number of resources to return. | [optional] 
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
> AITools list_ai_tools(project_key, sort=sort, limit=limit, offset=offset, filter=filter)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    sort = 'sort_example' # str | A sort to apply to the list of AgentControl configs. (optional)
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = 'filter_example' # str | A filter to apply to the list. (optional)

    try:
        # List AI tools
        api_response = api_instance.list_ai_tools(project_key, sort=sort, limit=limit, offset=offset, filter=filter)
        print("The response of AgentControlApi->list_ai_tools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->list_ai_tools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **sort** | **str**| A sort to apply to the list of AgentControl configs. | [optional] 
 **limit** | **int**| The number of resources to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 
 **filter** | **str**| A filter to apply to the list. | [optional] 

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

# **list_all_agent_optimization_results**
> AgentOptimizationResults list_all_agent_optimization_results(project_key, optimization_key, limit=limit, offset=offset)

List all agent optimization results across versions

Get all results across all versions of an agent optimization.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_optimization_results import AgentOptimizationResults
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    optimization_key = 'optimization_key_example' # str | 
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # List all agent optimization results across versions
        api_response = api_instance.list_all_agent_optimization_results(project_key, optimization_key, limit=limit, offset=offset)
        print("The response of AgentControlApi->list_all_agent_optimization_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->list_all_agent_optimization_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **optimization_key** | **str**|  | 
 **limit** | **int**| The number of resources to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**AgentOptimizationResults**](AgentOptimizationResults.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent optimization results list |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_model_config_versions**
> ModelConfigs list_model_config_versions(project_key, model_config_key, limit=limit, offset=offset)

List AI model config versions

Get a paginated list of all available versions of an AI model config, ordered from newest to oldest. Global model configs return their single current representation.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.model_configs import ModelConfigs
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'default' # str | 
    model_config_key = 'default' # str | 
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # List AI model config versions
        api_response = api_instance.list_model_config_versions(project_key, model_config_key, limit=limit, offset=offset)
        print("The response of AgentControlApi->list_model_config_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->list_model_config_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **model_config_key** | **str**|  | 
 **limit** | **int**| The number of resources to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**ModelConfigs**](ModelConfigs.md)

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
> List[ModelConfig] list_model_configs(project_key, restricted=restricted)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'default' # str | 
    restricted = True # bool | Whether to return only restricted models (optional)

    try:
        # List AI model configs
        api_response = api_instance.list_model_configs(project_key, restricted=restricted)
        print("The response of AgentControlApi->list_model_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->list_model_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **list_prompt_snippet_references**
> SnippetReferences list_prompt_snippet_references(project_key, snippet_key, limit=limit, offset=offset)

List prompt snippet references

Get all config variations that currently reference this prompt snippet.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.snippet_references import SnippetReferences
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    snippet_key = 'snippet_key_example' # str | 
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # List prompt snippet references
        api_response = api_instance.list_prompt_snippet_references(project_key, snippet_key, limit=limit, offset=offset)
        print("The response of AgentControlApi->list_prompt_snippet_references:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->list_prompt_snippet_references: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **snippet_key** | **str**|  | 
 **limit** | **int**| The number of resources to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**SnippetReferences**](SnippetReferences.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prompt snippet references |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_prompt_snippet_versions**
> PromptSnippets list_prompt_snippet_versions(project_key, snippet_key, limit=limit, offset=offset)

List prompt snippet versions

Get all versions of a prompt snippet in the given project, ordered by version descending.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.prompt_snippets import PromptSnippets
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    snippet_key = 'snippet_key_example' # str | 
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # List prompt snippet versions
        api_response = api_instance.list_prompt_snippet_versions(project_key, snippet_key, limit=limit, offset=offset)
        print("The response of AgentControlApi->list_prompt_snippet_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->list_prompt_snippet_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **snippet_key** | **str**|  | 
 **limit** | **int**| The number of resources to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**PromptSnippets**](PromptSnippets.md)

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

# **list_prompt_snippets**
> PromptSnippets list_prompt_snippets(project_key, limit=limit, offset=offset, filter=filter)

List prompt snippets

Get a list of all prompt snippets in the given project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.prompt_snippets import PromptSnippets
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = 'filter_example' # str | A filter to apply to the list. (optional)

    try:
        # List prompt snippets
        api_response = api_instance.list_prompt_snippets(project_key, limit=limit, offset=offset, filter=filter)
        print("The response of AgentControlApi->list_prompt_snippets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->list_prompt_snippets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **limit** | **int**| The number of resources to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 
 **filter** | **str**| A filter to apply to the list. | [optional] 

### Return type

[**PromptSnippets**](PromptSnippets.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prompt snippets list |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_agent_graph**
> AgentGraph patch_agent_graph(ld_api_version, project_key, graph_key, agent_graph_patch=agent_graph_patch)

Update agent graph

Edit an existing agent graph.

The request body must be a JSON object of the fields to update. The values you include replace the existing values for the fields.

If the update includes `rootConfigKey` or `edges`, both must be present and will be treated as full replacements.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_graph import AgentGraph
from launchdarkly_api.models.agent_graph_patch import AgentGraphPatch
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    graph_key = 'graph_key_example' # str | 
    agent_graph_patch = launchdarkly_api.AgentGraphPatch() # AgentGraphPatch | Agent graph object to update (optional)

    try:
        # Update agent graph
        api_response = api_instance.patch_agent_graph(ld_api_version, project_key, graph_key, agent_graph_patch=agent_graph_patch)
        print("The response of AgentControlApi->patch_agent_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->patch_agent_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **graph_key** | **str**|  | 
 **agent_graph_patch** | [**AgentGraphPatch**](AgentGraphPatch.md)| Agent graph object to update | [optional] 

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
**200** | Agent graph updated |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_agent_optimization**
> AgentOptimization patch_agent_optimization(project_key, optimization_key, agent_optimization_patch)

Update an agent optimization

Update an existing agent optimization. Creates a new version of the optimization.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_optimization import AgentOptimization
from launchdarkly_api.models.agent_optimization_patch import AgentOptimizationPatch
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    optimization_key = 'optimization_key_example' # str | 
    agent_optimization_patch = launchdarkly_api.AgentOptimizationPatch() # AgentOptimizationPatch | Agent optimization fields to update

    try:
        # Update an agent optimization
        api_response = api_instance.patch_agent_optimization(project_key, optimization_key, agent_optimization_patch)
        print("The response of AgentControlApi->patch_agent_optimization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->patch_agent_optimization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **optimization_key** | **str**|  | 
 **agent_optimization_patch** | [**AgentOptimizationPatch**](AgentOptimizationPatch.md)| Agent optimization fields to update | 

### Return type

[**AgentOptimization**](AgentOptimization.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent optimization updated |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_agent_optimization_result**
> AgentOptimizationResult patch_agent_optimization_result(project_key, optimization_key, result_id, agent_optimization_result_patch)

Update an agent optimization result

Update status, activity, and AI request metadata fields on an agent optimization result.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_optimization_result import AgentOptimizationResult
from launchdarkly_api.models.agent_optimization_result_patch import AgentOptimizationResultPatch
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    optimization_key = 'optimization_key_example' # str | 
    result_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    agent_optimization_result_patch = launchdarkly_api.AgentOptimizationResultPatch() # AgentOptimizationResultPatch | Agent optimization result fields to update

    try:
        # Update an agent optimization result
        api_response = api_instance.patch_agent_optimization_result(project_key, optimization_key, result_id, agent_optimization_result_patch)
        print("The response of AgentControlApi->patch_agent_optimization_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->patch_agent_optimization_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **optimization_key** | **str**|  | 
 **result_id** | **UUID**|  | 
 **agent_optimization_result_patch** | [**AgentOptimizationResultPatch**](AgentOptimizationResultPatch.md)| Agent optimization result fields to update | 

### Return type

[**AgentOptimizationResult**](AgentOptimizationResult.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent optimization result updated |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_agent_skill**
> AgentSkill patch_agent_skill(project_key, skill_key, agent_skill_patch)

Update an agent skill

Update an existing agent skill. Creates a new version of the skill.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_skill import AgentSkill
from launchdarkly_api.models.agent_skill_patch import AgentSkillPatch
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    skill_key = 'skill_key_example' # str | 
    agent_skill_patch = launchdarkly_api.AgentSkillPatch() # AgentSkillPatch | Agent skill fields to update

    try:
        # Update an agent skill
        api_response = api_instance.patch_agent_skill(project_key, skill_key, agent_skill_patch)
        print("The response of AgentControlApi->patch_agent_skill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->patch_agent_skill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **skill_key** | **str**|  | 
 **agent_skill_patch** | [**AgentSkillPatch**](AgentSkillPatch.md)| Agent skill fields to update | 

### Return type

[**AgentSkill**](AgentSkill.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent skill updated |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_ai_config**
> AIConfig patch_ai_config(project_key, config_key, ai_config_patch=ai_config_patch)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 
    ai_config_patch = launchdarkly_api.AIConfigPatch() # AIConfigPatch | AI Config object to update (optional)

    try:
        # Update AI Config
        api_response = api_instance.patch_ai_config(project_key, config_key, ai_config_patch=ai_config_patch)
        print("The response of AgentControlApi->patch_ai_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->patch_ai_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> AIConfigTargeting patch_ai_config_targeting(project_key, config_key, ai_config_targeting_patch=ai_config_targeting_patch)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 
    ai_config_targeting_patch = launchdarkly_api.AIConfigTargetingPatch() # AIConfigTargetingPatch | AI Config targeting semantic patch instructions (optional)

    try:
        # Update AI Config targeting
        api_response = api_instance.patch_ai_config_targeting(project_key, config_key, ai_config_targeting_patch=ai_config_targeting_patch)
        print("The response of AgentControlApi->patch_ai_config_targeting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->patch_ai_config_targeting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> AIConfigVariation patch_ai_config_variation(project_key, config_key, variation_key, ai_config_variation_patch=ai_config_variation_patch)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 
    variation_key = 'variation_key_example' # str | 
    ai_config_variation_patch = launchdarkly_api.AIConfigVariationPatch() # AIConfigVariationPatch | AI Config variation object to update (optional)

    try:
        # Update AI Config variation
        api_response = api_instance.patch_ai_config_variation(project_key, config_key, variation_key, ai_config_variation_patch=ai_config_variation_patch)
        print("The response of AgentControlApi->patch_ai_config_variation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->patch_ai_config_variation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> AITool patch_ai_tool(project_key, tool_key, ai_tool_patch=ai_tool_patch)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    tool_key = 'tool_key_example' # str | 
    ai_tool_patch = launchdarkly_api.AIToolPatch() # AIToolPatch | AI tool object to update (optional)

    try:
        # Update AI tool
        api_response = api_instance.patch_ai_tool(project_key, tool_key, ai_tool_patch=ai_tool_patch)
        print("The response of AgentControlApi->patch_ai_tool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->patch_ai_tool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **patch_model_config**
> ModelConfig patch_model_config(project_key, model_config_key, model_config_patch)

Update an AI model config

Update an AI model config.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.model_config import ModelConfig
from launchdarkly_api.models.model_config_patch import ModelConfigPatch
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'default' # str | 
    model_config_key = 'model_config_key_example' # str | 
    model_config_patch = launchdarkly_api.ModelConfigPatch() # ModelConfigPatch | AI model config object to update

    try:
        # Update an AI model config
        api_response = api_instance.patch_model_config(project_key, model_config_key, model_config_patch)
        print("The response of AgentControlApi->patch_model_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->patch_model_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **model_config_key** | **str**|  | 
 **model_config_patch** | [**ModelConfigPatch**](ModelConfigPatch.md)| AI model config object to update | 

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

# **patch_prompt_snippet**
> PromptSnippet patch_prompt_snippet(project_key, snippet_key, prompt_snippet_patch)

Update a prompt snippet

Update an existing prompt snippet. Creates a new version of the snippet.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.prompt_snippet import PromptSnippet
from launchdarkly_api.models.prompt_snippet_patch import PromptSnippetPatch
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    snippet_key = 'snippet_key_example' # str | 
    prompt_snippet_patch = launchdarkly_api.PromptSnippetPatch() # PromptSnippetPatch | Prompt snippet fields to update

    try:
        # Update a prompt snippet
        api_response = api_instance.patch_prompt_snippet(project_key, snippet_key, prompt_snippet_patch)
        print("The response of AgentControlApi->patch_prompt_snippet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->patch_prompt_snippet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **snippet_key** | **str**|  | 
 **prompt_snippet_patch** | [**PromptSnippetPatch**](PromptSnippetPatch.md)| Prompt snippet fields to update | 

### Return type

[**PromptSnippet**](PromptSnippet.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prompt snippet updated |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'project_key_example' # str | 
    agent_graph_post = launchdarkly_api.AgentGraphPost() # AgentGraphPost | Agent graph object to create

    try:
        # Create new agent graph
        api_response = api_instance.post_agent_graph(ld_api_version, project_key, agent_graph_post)
        print("The response of AgentControlApi->post_agent_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->post_agent_graph: %s\n" % e)
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

# **post_agent_optimization**
> AgentOptimization post_agent_optimization(project_key, agent_optimization_post)

Create agent optimization

Create a new agent optimization within the given project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_optimization import AgentOptimization
from launchdarkly_api.models.agent_optimization_post import AgentOptimizationPost
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    agent_optimization_post = launchdarkly_api.AgentOptimizationPost() # AgentOptimizationPost | Agent optimization object to create

    try:
        # Create agent optimization
        api_response = api_instance.post_agent_optimization(project_key, agent_optimization_post)
        print("The response of AgentControlApi->post_agent_optimization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->post_agent_optimization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **agent_optimization_post** | [**AgentOptimizationPost**](AgentOptimizationPost.md)| Agent optimization object to create | 

### Return type

[**AgentOptimization**](AgentOptimization.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Agent optimization created |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_agent_optimization_result**
> AgentOptimizationResult post_agent_optimization_result(project_key, optimization_key, agent_optimization_result_post)

Create agent optimization result

Create a new result for an agent optimization run.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_optimization_result import AgentOptimizationResult
from launchdarkly_api.models.agent_optimization_result_post import AgentOptimizationResultPost
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    optimization_key = 'optimization_key_example' # str | 
    agent_optimization_result_post = launchdarkly_api.AgentOptimizationResultPost() # AgentOptimizationResultPost | Agent optimization result to create

    try:
        # Create agent optimization result
        api_response = api_instance.post_agent_optimization_result(project_key, optimization_key, agent_optimization_result_post)
        print("The response of AgentControlApi->post_agent_optimization_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->post_agent_optimization_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **optimization_key** | **str**|  | 
 **agent_optimization_result_post** | [**AgentOptimizationResultPost**](AgentOptimizationResultPost.md)| Agent optimization result to create | 

### Return type

[**AgentOptimizationResult**](AgentOptimizationResult.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Agent optimization result created |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**429** | Rate Limited |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_agent_skill**
> AgentSkill post_agent_skill(project_key, agent_skill_post)

Create an agent skill

Create a new agent skill within the given project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_skill import AgentSkill
from launchdarkly_api.models.agent_skill_post import AgentSkillPost
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    agent_skill_post = launchdarkly_api.AgentSkillPost() # AgentSkillPost | Agent skill object to create

    try:
        # Create an agent skill
        api_response = api_instance.post_agent_skill(project_key, agent_skill_post)
        print("The response of AgentControlApi->post_agent_skill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->post_agent_skill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **agent_skill_post** | [**AgentSkillPost**](AgentSkillPost.md)| Agent skill object to create | 

### Return type

[**AgentSkill**](AgentSkill.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Agent skill created |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_config**
> AIConfig post_ai_config(project_key, ai_config_post)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    ai_config_post = launchdarkly_api.AIConfigPost() # AIConfigPost | AI Config object to create

    try:
        # Create new AI Config
        api_response = api_instance.post_ai_config(project_key, ai_config_post)
        print("The response of AgentControlApi->post_ai_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->post_ai_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**429** | Rate Limited |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_config_variation**
> AIConfigVariation post_ai_config_variation(project_key, config_key, ai_config_variation_post)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    config_key = 'config_key_example' # str | 
    ai_config_variation_post = launchdarkly_api.AIConfigVariationPost() # AIConfigVariationPost | AI Config variation object to create

    try:
        # Create AI Config variation
        api_response = api_instance.post_ai_config_variation(project_key, config_key, ai_config_variation_post)
        print("The response of AgentControlApi->post_ai_config_variation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->post_ai_config_variation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**429** | Rate Limited |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_tool**
> AITool post_ai_tool(project_key, ai_tool_post)

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    ai_tool_post = launchdarkly_api.AIToolPost() # AIToolPost | AI tool object to create

    try:
        # Create an AI tool
        api_response = api_instance.post_ai_tool(project_key, ai_tool_post)
        print("The response of AgentControlApi->post_ai_tool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->post_ai_tool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_model_config**
> ModelConfig post_model_config(project_key, model_config_post)

Create an AI model config

Create an AI model config. You can use this in any variation for any config in your project.

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'default' # str | 
    model_config_post = launchdarkly_api.ModelConfigPost() # ModelConfigPost | AI model config object to create

    try:
        # Create an AI model config
        api_response = api_instance.post_model_config(project_key, model_config_post)
        print("The response of AgentControlApi->post_model_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->post_model_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **post_prompt_snippet**
> PromptSnippet post_prompt_snippet(project_key, prompt_snippet_post)

Create a prompt snippet

Create a new prompt snippet within the given project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.prompt_snippet import PromptSnippet
from launchdarkly_api.models.prompt_snippet_post import PromptSnippetPost
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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'project_key_example' # str | 
    prompt_snippet_post = launchdarkly_api.PromptSnippetPost() # PromptSnippetPost | Prompt snippet object to create

    try:
        # Create a prompt snippet
        api_response = api_instance.post_prompt_snippet(project_key, prompt_snippet_post)
        print("The response of AgentControlApi->post_prompt_snippet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->post_prompt_snippet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **prompt_snippet_post** | [**PromptSnippetPost**](PromptSnippetPost.md)| Prompt snippet object to create | 

### Return type

[**PromptSnippet**](PromptSnippet.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Prompt snippet created |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_restricted_models**
> RestrictedModelsResponse post_restricted_models(project_key, restricted_models_request)

Add AI models to the restricted list

Add AI models, by key, to the restricted list. Keys are included in the response from the [List AI model configs](https://launchdarkly.com/docs/api/agent-control/list-model-configs) endpoint.

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
    api_instance = launchdarkly_api.AgentControlApi(api_client)
    project_key = 'default' # str | 
    restricted_models_request = launchdarkly_api.RestrictedModelsRequest() # RestrictedModelsRequest | List of AI model keys to add to the restricted list.

    try:
        # Add AI models to the restricted list
        api_response = api_instance.post_restricted_models(project_key, restricted_models_request)
        print("The response of AgentControlApi->post_restricted_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentControlApi->post_restricted_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

