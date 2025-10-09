# launchdarkly_api.MetricsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_metric**](MetricsApi.md#delete_metric) | **DELETE** /api/v2/metrics/{projectKey}/{metricKey} | Delete metric
[**get_metric**](MetricsApi.md#get_metric) | **GET** /api/v2/metrics/{projectKey}/{metricKey} | Get metric
[**get_metrics**](MetricsApi.md#get_metrics) | **GET** /api/v2/metrics/{projectKey} | List metrics
[**patch_metric**](MetricsApi.md#patch_metric) | **PATCH** /api/v2/metrics/{projectKey}/{metricKey} | Update metric
[**post_metric**](MetricsApi.md#post_metric) | **POST** /api/v2/metrics/{projectKey} | Create metric


# **delete_metric**
> delete_metric(project_key, metric_key)

Delete metric

Delete a metric by key.

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
    api_instance = launchdarkly_api.MetricsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    metric_key = 'metric_key_example' # str | The metric key

    try:
        # Delete metric
        api_instance.delete_metric(project_key, metric_key)
    except Exception as e:
        print("Exception when calling MetricsApi->delete_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **metric_key** | **str**| The metric key | 

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

# **get_metric**
> MetricRep get_metric(project_key, metric_key, expand=expand, version_id=version_id)

Get metric

Get information for a single metric from the specific project.  ### Expanding the metric response LaunchDarkly supports four fields for expanding the \"Get metric\" response. By default, these fields are **not** included in the response.  To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:  - `experiments` includes all experiments from the specific project that use the metric - `experimentCount` includes the number of experiments from the specific project that use the metric - `metricGroups` includes all metric groups from the specific project that use the metric - `metricGroupCount` includes the number of metric groups from the specific project that use the metric  For example, `expand=experiments` includes the `experiments` field in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.metric_rep import MetricRep
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
    api_instance = launchdarkly_api.MetricsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    metric_key = 'metric_key_example' # str | The metric key
    expand = 'expand_example' # str | A comma-separated list of properties that can reveal additional information in the response. Supported fields are `experiments`, `experimentCount`, `metricGroups`, `metricGroupCount`, `eventSources`, `guardedRollouts`, `guardedRolloutCount`, and `lastUsedInEntity`. (optional)
    version_id = 'version_id_example' # str | The specific version ID of the metric (optional)

    try:
        # Get metric
        api_response = api_instance.get_metric(project_key, metric_key, expand=expand, version_id=version_id)
        print("The response of MetricsApi->get_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **metric_key** | **str**| The metric key | 
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. Supported fields are &#x60;experiments&#x60;, &#x60;experimentCount&#x60;, &#x60;metricGroups&#x60;, &#x60;metricGroupCount&#x60;, &#x60;eventSources&#x60;, &#x60;guardedRollouts&#x60;, &#x60;guardedRolloutCount&#x60;, and &#x60;lastUsedInEntity&#x60;. | [optional] 
 **version_id** | **str**| The specific version ID of the metric | [optional] 

### Return type

[**MetricRep**](MetricRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metric response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics**
> MetricCollectionRep get_metrics(project_key, expand=expand, limit=limit, offset=offset, sort=sort, filter=filter)

List metrics

Get a list of all metrics for the specified project.  ### Filtering metrics  The `filter` parameter supports the following operators: `contains`, `equals`, `anyOf`.  #### Supported fields and operators  You can only filter certain fields in metrics when using the `filter` parameter. Additionally, you can only filter some fields with certain operators.  When you search for metrics, the `filter` parameter supports the following fields and operators:  |<div style=\"width:120px\">Field</div> |Description |Supported operators | |---|---|---| | `eventKind` | The metric event kind. One of `custom`, `pageview`, `click`. | `equals` | | `hasConnections` | Whether the metric has connections to experiments or guarded rollouts. One of `true`, `false`. | `equals` | | `isNumeric` | Whether the metric is numeric. One of `true`, `false`. | `equals` | | `maintainerIds` | A comma-separated list of metric maintainer IDs. | `anyOf` | | `maintainerTeamKey` | The metric maintainer team key. | `equals` | | `query` | A \"fuzzy\" search across metric key and name. Supply a string or list of strings to the operator. | `equals` | | `tags` | The metric tags. | `contains` | | `unitAggregationType` | The metric's unit aggregation type. One of `sum`, `average`. | `equals` |  For example, the filter `?filter=tags contains [\"tag1\", \"tag2\", \"tag3\"]` matches metrics that have all three tags.  The documented values for `filter` query parameters are prior to URL encoding. For example, the `[` in `?filter=tags contains [\"tag1\", \"tag2\", \"tag3\"]` must be encoded to `%5B`.  ### Expanding the metric list response  LaunchDarkly supports expanding the \"List metrics\" response. By default, the expandable field is **not** included in the response.  To expand the response, append the `expand` query parameter and add the following supported field:  - `experimentCount` includes the number of experiments from the specific project that use the metric  For example, `expand=experimentCount` includes the `experimentCount` field for each metric in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.metric_collection_rep import MetricCollectionRep
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
    api_instance = launchdarkly_api.MetricsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    expand = 'expand_example' # str | A comma-separated list of properties that can reveal additional information in the response. (optional)
    limit = 56 # int | The number of metrics to return in the response. Defaults to 20. Maximum limit is 50. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and returns the next `limit` items. (optional)
    sort = 'sort_example' # str | A field to sort the items by. Prefix field by a dash ( - ) to sort in descending order. This endpoint supports sorting by `createdAt` or `name`. (optional)
    filter = 'filter_example' # str | A comma-separated list of filters. This endpoint accepts filtering by `query`, `tags`, 'eventKind', 'isNumeric', 'unitAggregationType`, `hasConnections`, `maintainerIds`, `maintainerTeamKey` and `view`. To learn more about the filter syntax, read the 'Filtering metrics' section above. (optional)

    try:
        # List metrics
        api_response = api_instance.get_metrics(project_key, expand=expand, limit=limit, offset=offset, sort=sort, filter=filter)
        print("The response of MetricsApi->get_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. | [optional] 
 **limit** | **int**| The number of metrics to return in the response. Defaults to 20. Maximum limit is 50. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and returns the next &#x60;limit&#x60; items. | [optional] 
 **sort** | **str**| A field to sort the items by. Prefix field by a dash ( - ) to sort in descending order. This endpoint supports sorting by &#x60;createdAt&#x60; or &#x60;name&#x60;. | [optional] 
 **filter** | **str**| A comma-separated list of filters. This endpoint accepts filtering by &#x60;query&#x60;, &#x60;tags&#x60;, &#39;eventKind&#39;, &#39;isNumeric&#39;, &#39;unitAggregationType&#x60;, &#x60;hasConnections&#x60;, &#x60;maintainerIds&#x60;, &#x60;maintainerTeamKey&#x60; and &#x60;view&#x60;. To learn more about the filter syntax, read the &#39;Filtering metrics&#39; section above. | [optional] 

### Return type

[**MetricCollectionRep**](MetricCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metrics collection response |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_metric**
> MetricRep patch_metric(project_key, metric_key, patch_operation)

Update metric

Patch a metric by key. Updating a metric uses a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.metric_rep import MetricRep
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
    api_instance = launchdarkly_api.MetricsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    metric_key = 'metric_key_example' # str | The metric key
    patch_operation = [{"op":"replace","path":"/name","value":"my-updated-metric"}] # List[PatchOperation] | 

    try:
        # Update metric
        api_response = api_instance.patch_metric(project_key, metric_key, patch_operation)
        print("The response of MetricsApi->patch_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->patch_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **metric_key** | **str**| The metric key | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**MetricRep**](MetricRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metric response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_metric**
> MetricRep post_metric(project_key, metric_post)

Create metric

Create a new metric in the specified project. The expected `POST` body differs depending on the specified `kind` property.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.metric_post import MetricPost
from launchdarkly_api.models.metric_rep import MetricRep
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
    api_instance = launchdarkly_api.MetricsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    metric_post = {"eventKey":"Order placed","isNumeric":false,"key":"metric-key-123abc","kind":"custom"} # MetricPost | 

    try:
        # Create metric
        api_response = api_instance.post_metric(project_key, metric_post)
        print("The response of MetricsApi->post_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->post_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **metric_post** | [**MetricPost**](MetricPost.md)|  | 

### Return type

[**MetricRep**](MetricRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metric response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

