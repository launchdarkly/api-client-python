# launchdarkly_api.InsightsRepositoriesBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associate_repositories_and_projects**](InsightsRepositoriesBetaApi.md#associate_repositories_and_projects) | **PUT** /api/v2/engineering-insights/repositories/projects | Associate repositories with projects
[**delete_repository_project**](InsightsRepositoriesBetaApi.md#delete_repository_project) | **DELETE** /api/v2/engineering-insights/repositories/{repositoryKey}/projects/{projectKey} | Remove repository project association
[**get_insights_repositories**](InsightsRepositoriesBetaApi.md#get_insights_repositories) | **GET** /api/v2/engineering-insights/repositories | List repositories


# **associate_repositories_and_projects**
> InsightsRepositoryProjectCollection associate_repositories_and_projects(insights_repository_project_mappings)

Associate repositories with projects

Associate repositories with projects

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.insights_repository_project_collection import InsightsRepositoryProjectCollection
from launchdarkly_api.models.insights_repository_project_mappings import InsightsRepositoryProjectMappings
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
    api_instance = launchdarkly_api.InsightsRepositoriesBetaApi(api_client)
    insights_repository_project_mappings = launchdarkly_api.InsightsRepositoryProjectMappings() # InsightsRepositoryProjectMappings | 

    try:
        # Associate repositories with projects
        api_response = api_instance.associate_repositories_and_projects(insights_repository_project_mappings)
        print("The response of InsightsRepositoriesBetaApi->associate_repositories_and_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsRepositoriesBetaApi->associate_repositories_and_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insights_repository_project_mappings** | [**InsightsRepositoryProjectMappings**](InsightsRepositoryProjectMappings.md)|  | 

### Return type

[**InsightsRepositoryProjectCollection**](InsightsRepositoryProjectCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repositories projects response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repository_project**
> delete_repository_project(repository_key, project_key)

Remove repository project association

Remove repository project association

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
    api_instance = launchdarkly_api.InsightsRepositoriesBetaApi(api_client)
    repository_key = 'repository_key_example' # str | The repository key
    project_key = 'project_key_example' # str | The project key

    try:
        # Remove repository project association
        api_instance.delete_repository_project(repository_key, project_key)
    except Exception as e:
        print("Exception when calling InsightsRepositoriesBetaApi->delete_repository_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_key** | **str**| The repository key | 
 **project_key** | **str**| The project key | 

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
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_insights_repositories**
> InsightsRepositoryCollection get_insights_repositories(expand=expand)

List repositories

Get a list of repositories  ### Expanding the repository collection response  LaunchDarkly supports expanding the repository collection response to include additional fields.  To expand the response, append the `expand` query parameter and include the following:  * `projects` includes details on all of the LaunchDarkly projects associated with each repository  For example, use `?expand=projects` to include the `projects` field in the response. By default, this field is **not** included in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.insights_repository_collection import InsightsRepositoryCollection
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
    api_instance = launchdarkly_api.InsightsRepositoriesBetaApi(api_client)
    expand = 'expand_example' # str | Expand properties in response. Options: `projects` (optional)

    try:
        # List repositories
        api_response = api_instance.get_insights_repositories(expand=expand)
        print("The response of InsightsRepositoriesBetaApi->get_insights_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsRepositoriesBetaApi->get_insights_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand properties in response. Options: &#x60;projects&#x60; | [optional] 

### Return type

[**InsightsRepositoryCollection**](InsightsRepositoryCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repository collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

