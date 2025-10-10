# launchdarkly_api.InsightsScoresBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_insight_group**](InsightsScoresBetaApi.md#create_insight_group) | **POST** /api/v2/engineering-insights/insights/group | Create insight group
[**delete_insight_group**](InsightsScoresBetaApi.md#delete_insight_group) | **DELETE** /api/v2/engineering-insights/insights/groups/{insightGroupKey} | Delete insight group
[**get_insight_group**](InsightsScoresBetaApi.md#get_insight_group) | **GET** /api/v2/engineering-insights/insights/groups/{insightGroupKey} | Get insight group
[**get_insight_groups**](InsightsScoresBetaApi.md#get_insight_groups) | **GET** /api/v2/engineering-insights/insights/groups | List insight groups
[**get_insights_scores**](InsightsScoresBetaApi.md#get_insights_scores) | **GET** /api/v2/engineering-insights/insights/scores | Get insight scores
[**patch_insight_group**](InsightsScoresBetaApi.md#patch_insight_group) | **PATCH** /api/v2/engineering-insights/insights/groups/{insightGroupKey} | Patch insight group


# **create_insight_group**
> InsightGroup create_insight_group(post_insight_group_params)

Create insight group

Create insight group

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.insight_group import InsightGroup
from launchdarkly_api.models.post_insight_group_params import PostInsightGroupParams
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
    api_instance = launchdarkly_api.InsightsScoresBetaApi(api_client)
    post_insight_group_params = launchdarkly_api.PostInsightGroupParams() # PostInsightGroupParams | 

    try:
        # Create insight group
        api_response = api_instance.create_insight_group(post_insight_group_params)
        print("The response of InsightsScoresBetaApi->create_insight_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsScoresBetaApi->create_insight_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_insight_group_params** | [**PostInsightGroupParams**](PostInsightGroupParams.md)|  | 

### Return type

[**InsightGroup**](InsightGroup.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_insight_group**
> delete_insight_group(insight_group_key)

Delete insight group

Delete insight group

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
    api_instance = launchdarkly_api.InsightsScoresBetaApi(api_client)
    insight_group_key = 'insight_group_key_example' # str | The insight group key

    try:
        # Delete insight group
        api_instance.delete_insight_group(insight_group_key)
    except Exception as e:
        print("Exception when calling InsightsScoresBetaApi->delete_insight_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insight_group_key** | **str**| The insight group key | 

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

# **get_insight_group**
> InsightGroup get_insight_group(insight_group_key, expand=expand)

Get insight group

Get insight group

### Expanding the insight group response

LaunchDarkly supports expanding the insight group response to include additional fields.

To expand the response, append the `expand` query parameter and include the following:

* `scores` includes details on all of the scores used in the engineering insights metrics views for this group
* `environment` includes details on each environment associated with this group

For example, use `?expand=scores` to include the `scores` field in the response. By default, this field is **not** included in the response.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.insight_group import InsightGroup
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
    api_instance = launchdarkly_api.InsightsScoresBetaApi(api_client)
    insight_group_key = 'insight_group_key_example' # str | The insight group key
    expand = 'expand_example' # str | Options: `scores`, `environment` (optional)

    try:
        # Get insight group
        api_response = api_instance.get_insight_group(insight_group_key, expand=expand)
        print("The response of InsightsScoresBetaApi->get_insight_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsScoresBetaApi->get_insight_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insight_group_key** | **str**| The insight group key | 
 **expand** | **str**| Options: &#x60;scores&#x60;, &#x60;environment&#x60; | [optional] 

### Return type

[**InsightGroup**](InsightGroup.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Insight group response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_insight_groups**
> InsightGroupCollection get_insight_groups(limit=limit, offset=offset, sort=sort, query=query, expand=expand)

List insight groups

List groups for which you are collecting insights

### Expanding the insight groups collection response

LaunchDarkly supports expanding the insight groups collection response to include additional fields.

To expand the response, append the `expand` query parameter and include the following:

* `scores` includes details on all of the scores used in the engineering insights metrics views for each group
* `environment` includes details on each environment associated with each group
* `metadata` includes counts of the number of insight groups with particular indicators, such as "excellent," "good," "fair," and so on.

For example, use `?expand=scores` to include the `scores` field in the response. By default, this field is **not** included in the response.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.insight_group_collection import InsightGroupCollection
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
    api_instance = launchdarkly_api.InsightsScoresBetaApi(api_client)
    limit = 56 # int | The number of insight groups to return. Default is 20. Must be between 1 and 20 inclusive. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    sort = 'sort_example' # str | Sort flag list by field. Prefix field with <code>-</code> to sort in descending order. Allowed fields: name (optional)
    query = 'query_example' # str | Filter list of insights groups by name. (optional)
    expand = 'expand_example' # str | Options: `scores`, `environment`, `metadata` (optional)

    try:
        # List insight groups
        api_response = api_instance.get_insight_groups(limit=limit, offset=offset, sort=sort, query=query, expand=expand)
        print("The response of InsightsScoresBetaApi->get_insight_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsScoresBetaApi->get_insight_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of insight groups to return. Default is 20. Must be between 1 and 20 inclusive. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 
 **sort** | **str**| Sort flag list by field. Prefix field with &lt;code&gt;-&lt;/code&gt; to sort in descending order. Allowed fields: name | [optional] 
 **query** | **str**| Filter list of insights groups by name. | [optional] 
 **expand** | **str**| Options: &#x60;scores&#x60;, &#x60;environment&#x60;, &#x60;metadata&#x60; | [optional] 

### Return type

[**InsightGroupCollection**](InsightGroupCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Insight groups collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_insights_scores**
> InsightScores get_insights_scores(project_key, environment_key, application_key=application_key)

Get insight scores

Return insights scores, based on the given parameters. This data is also used in engineering insights metrics views.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.insight_scores import InsightScores
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
    api_instance = launchdarkly_api.InsightsScoresBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    application_key = 'application_key_example' # str | Comma separated list of application keys (optional)

    try:
        # Get insight scores
        api_response = api_instance.get_insights_scores(project_key, environment_key, application_key=application_key)
        print("The response of InsightsScoresBetaApi->get_insights_scores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsScoresBetaApi->get_insights_scores: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **application_key** | **str**| Comma separated list of application keys | [optional] 

### Return type

[**InsightScores**](InsightScores.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Insight score response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_insight_group**
> InsightGroup patch_insight_group(insight_group_key, patch_operation)

Patch insight group

Update an insight group. Updating an insight group uses a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.insight_group import InsightGroup
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
    api_instance = launchdarkly_api.InsightsScoresBetaApi(api_client)
    insight_group_key = 'insight_group_key_example' # str | The insight group key
    patch_operation = [{"op":"replace","path":"/name","value":"Prod group"}] # List[PatchOperation] | 

    try:
        # Patch insight group
        api_response = api_instance.patch_insight_group(insight_group_key, patch_operation)
        print("The response of InsightsScoresBetaApi->patch_insight_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsScoresBetaApi->patch_insight_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insight_group_key** | **str**| The insight group key | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**InsightGroup**](InsightGroup.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Insight group response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**422** | Invalid patch content |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

