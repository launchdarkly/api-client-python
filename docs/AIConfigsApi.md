# launchdarkly_api.AIConfigsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_agent_optimization_runs**](AIConfigsApi.md#list_agent_optimization_runs) | **GET** /api/v2/projects/{projectKey}/agent-optimizations/{optimizationKey}/runs | List agent optimization runs
[**list_ai_tool_references**](AIConfigsApi.md#list_ai_tool_references) | **GET** /api/v2/projects/{projectKey}/ai-tools/{toolKey}/references | List AI tool references


# **list_agent_optimization_runs**
> AgentOptimizationRuns list_agent_optimization_runs(project_key, optimization_key, limit=limit, offset=offset)

List agent optimization runs

Get one run summary per distinct run_id across all versions of an agent optimization config, ordered by created_at DESC.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.agent_optimization_runs import AgentOptimizationRuns
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
    api_instance = launchdarkly_api.AIConfigsApi(api_client)
    project_key = 'project_key_example' # str | 
    optimization_key = 'optimization_key_example' # str | 
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # List agent optimization runs
        api_response = api_instance.list_agent_optimization_runs(project_key, optimization_key, limit=limit, offset=offset)
        print("The response of AIConfigsApi->list_agent_optimization_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsApi->list_agent_optimization_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **optimization_key** | **str**|  | 
 **limit** | **int**| The number of resources to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**AgentOptimizationRuns**](AgentOptimizationRuns.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent optimization run list |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ai_tool_references**
> ToolReferences list_ai_tool_references(project_key, tool_key, limit=limit, offset=offset)

List AI tool references

Get all AgentControl config variations that currently reference this tool.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.tool_references import ToolReferences
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
    api_instance = launchdarkly_api.AIConfigsApi(api_client)
    project_key = 'project_key_example' # str | 
    tool_key = 'tool_key_example' # str | 
    limit = 56 # int | The number of resources to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # List AI tool references
        api_response = api_instance.list_ai_tool_references(project_key, tool_key, limit=limit, offset=offset)
        print("The response of AIConfigsApi->list_ai_tool_references:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIConfigsApi->list_ai_tool_references: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**|  | 
 **tool_key** | **str**|  | 
 **limit** | **int**| The number of resources to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**ToolReferences**](ToolReferences.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AI tool references |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

