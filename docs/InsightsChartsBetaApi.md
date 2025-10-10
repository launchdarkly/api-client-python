# launchdarkly_api.InsightsChartsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_deployment_frequency_chart**](InsightsChartsBetaApi.md#get_deployment_frequency_chart) | **GET** /api/v2/engineering-insights/charts/deployments/frequency | Get deployment frequency chart data
[**get_flag_status_chart**](InsightsChartsBetaApi.md#get_flag_status_chart) | **GET** /api/v2/engineering-insights/charts/flags/status | Get flag status chart data
[**get_lead_time_chart**](InsightsChartsBetaApi.md#get_lead_time_chart) | **GET** /api/v2/engineering-insights/charts/lead-time | Get lead time chart data
[**get_release_frequency_chart**](InsightsChartsBetaApi.md#get_release_frequency_chart) | **GET** /api/v2/engineering-insights/charts/releases/frequency | Get release frequency chart data
[**get_stale_flags_chart**](InsightsChartsBetaApi.md#get_stale_flags_chart) | **GET** /api/v2/engineering-insights/charts/flags/stale | Get stale flags chart data


# **get_deployment_frequency_chart**
> InsightsChart get_deployment_frequency_chart(project_key=project_key, environment_key=environment_key, application_key=application_key, var_from=var_from, to=to, bucket_type=bucket_type, bucket_ms=bucket_ms, group_by=group_by, expand=expand)

Get deployment frequency chart data

Get deployment frequency chart data. Engineering insights displays deployment frequency data in the [deployment frequency metric view](https://launchdarkly.com/docs/home/observability/deployments).

### Expanding the chart response

LaunchDarkly supports expanding the chart response to include additional fields.

To expand the response, append the `expand` query parameter and include the following:

* `metrics` includes details on the metrics related to deployment frequency

For example, use `?expand=metrics` to include the `metrics` field in the response. By default, this field is **not** included in the response.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.insights_chart import InsightsChart
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
    api_instance = launchdarkly_api.InsightsChartsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key (optional)
    environment_key = 'environment_key_example' # str | The environment key (optional)
    application_key = 'application_key_example' # str | Comma separated list of application keys (optional)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Unix timestamp in milliseconds. Default value is 7 days ago. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Unix timestamp in milliseconds. Default value is now. (optional)
    bucket_type = 'bucket_type_example' # str | Specify type of bucket. Options: `rolling`, `hour`, `day`. Default: `rolling`. (optional)
    bucket_ms = 56 # int | Duration of intervals for x-axis in milliseconds. Default value is one day (`86400000` milliseconds). (optional)
    group_by = 'group_by_example' # str | Options: `application`, `kind` (optional)
    expand = 'expand_example' # str | Options: `metrics` (optional)

    try:
        # Get deployment frequency chart data
        api_response = api_instance.get_deployment_frequency_chart(project_key=project_key, environment_key=environment_key, application_key=application_key, var_from=var_from, to=to, bucket_type=bucket_type, bucket_ms=bucket_ms, group_by=group_by, expand=expand)
        print("The response of InsightsChartsBetaApi->get_deployment_frequency_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsChartsBetaApi->get_deployment_frequency_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | [optional] 
 **environment_key** | **str**| The environment key | [optional] 
 **application_key** | **str**| Comma separated list of application keys | [optional] 
 **var_from** | **datetime**| Unix timestamp in milliseconds. Default value is 7 days ago. | [optional] 
 **to** | **datetime**| Unix timestamp in milliseconds. Default value is now. | [optional] 
 **bucket_type** | **str**| Specify type of bucket. Options: &#x60;rolling&#x60;, &#x60;hour&#x60;, &#x60;day&#x60;. Default: &#x60;rolling&#x60;. | [optional] 
 **bucket_ms** | **int**| Duration of intervals for x-axis in milliseconds. Default value is one day (&#x60;86400000&#x60; milliseconds). | [optional] 
 **group_by** | **str**| Options: &#x60;application&#x60;, &#x60;kind&#x60; | [optional] 
 **expand** | **str**| Options: &#x60;metrics&#x60; | [optional] 

### Return type

[**InsightsChart**](InsightsChart.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chart response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flag_status_chart**
> InsightsChart get_flag_status_chart(project_key, environment_key, application_key=application_key)

Get flag status chart data

Get flag status chart data. To learn more, read [Flag statuses](https://launchdarkly.com/docs/home/observability/flag-health#flag-statuses).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.insights_chart import InsightsChart
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
    api_instance = launchdarkly_api.InsightsChartsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    application_key = 'application_key_example' # str | Comma separated list of application keys (optional)

    try:
        # Get flag status chart data
        api_response = api_instance.get_flag_status_chart(project_key, environment_key, application_key=application_key)
        print("The response of InsightsChartsBetaApi->get_flag_status_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsChartsBetaApi->get_flag_status_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **application_key** | **str**| Comma separated list of application keys | [optional] 

### Return type

[**InsightsChart**](InsightsChart.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chart response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lead_time_chart**
> InsightsChart get_lead_time_chart(project_key, environment_key=environment_key, application_key=application_key, var_from=var_from, to=to, bucket_type=bucket_type, bucket_ms=bucket_ms, group_by=group_by, expand=expand)

Get lead time chart data

Get lead time chart data. The engineering insights UI displays lead time data in the [lead time metric view](https://launchdarkly.com/docs/home/observability/lead-time).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.insights_chart import InsightsChart
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
    api_instance = launchdarkly_api.InsightsChartsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key (optional)
    application_key = 'application_key_example' # str | Comma separated list of application keys (optional)
    var_from = 56 # int | Unix timestamp in milliseconds. Default value is 7 days ago. (optional)
    to = 56 # int | Unix timestamp in milliseconds. Default value is now. (optional)
    bucket_type = 'bucket_type_example' # str | Specify type of bucket. Options: `rolling`, `hour`, `day`. Default: `rolling`. (optional)
    bucket_ms = 56 # int | Duration of intervals for x-axis in milliseconds. Default value is one day (`86400000` milliseconds). (optional)
    group_by = 'group_by_example' # str | Options: `application`, `stage`. Default: `stage`. (optional)
    expand = 'expand_example' # str | Options: `metrics`, `percentiles`. (optional)

    try:
        # Get lead time chart data
        api_response = api_instance.get_lead_time_chart(project_key, environment_key=environment_key, application_key=application_key, var_from=var_from, to=to, bucket_type=bucket_type, bucket_ms=bucket_ms, group_by=group_by, expand=expand)
        print("The response of InsightsChartsBetaApi->get_lead_time_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsChartsBetaApi->get_lead_time_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | [optional] 
 **application_key** | **str**| Comma separated list of application keys | [optional] 
 **var_from** | **int**| Unix timestamp in milliseconds. Default value is 7 days ago. | [optional] 
 **to** | **int**| Unix timestamp in milliseconds. Default value is now. | [optional] 
 **bucket_type** | **str**| Specify type of bucket. Options: &#x60;rolling&#x60;, &#x60;hour&#x60;, &#x60;day&#x60;. Default: &#x60;rolling&#x60;. | [optional] 
 **bucket_ms** | **int**| Duration of intervals for x-axis in milliseconds. Default value is one day (&#x60;86400000&#x60; milliseconds). | [optional] 
 **group_by** | **str**| Options: &#x60;application&#x60;, &#x60;stage&#x60;. Default: &#x60;stage&#x60;. | [optional] 
 **expand** | **str**| Options: &#x60;metrics&#x60;, &#x60;percentiles&#x60;. | [optional] 

### Return type

[**InsightsChart**](InsightsChart.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chart response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_frequency_chart**
> InsightsChart get_release_frequency_chart(project_key, environment_key, application_key=application_key, has_experiments=has_experiments, var_global=var_global, group_by=group_by, var_from=var_from, to=to, bucket_type=bucket_type, bucket_ms=bucket_ms, expand=expand)

Get release frequency chart data

Get release frequency chart data. Engineering insights displays release frequency data in the [release frequency metric view](https://launchdarkly.com/docs/home/observability/releases).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.insights_chart import InsightsChart
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
    api_instance = launchdarkly_api.InsightsChartsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    application_key = 'application_key_example' # str | Comma separated list of application keys (optional)
    has_experiments = True # bool | Filter events to those associated with an experiment (`true`) or without an experiment (`false`) (optional)
    var_global = 'var_global_example' # str | Filter to include or exclude global events. Default value is `include`. Options: `include`, `exclude` (optional)
    group_by = 'group_by_example' # str | Property to group results by. Options: `impact` (optional)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Unix timestamp in milliseconds. Default value is 7 days ago. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Unix timestamp in milliseconds. Default value is now. (optional)
    bucket_type = 'bucket_type_example' # str | Specify type of bucket. Options: `rolling`, `hour`, `day`. Default: `rolling`. (optional)
    bucket_ms = 56 # int | Duration of intervals for x-axis in milliseconds. Default value is one day (`86400000` milliseconds). (optional)
    expand = 'expand_example' # str | Options: `metrics` (optional)

    try:
        # Get release frequency chart data
        api_response = api_instance.get_release_frequency_chart(project_key, environment_key, application_key=application_key, has_experiments=has_experiments, var_global=var_global, group_by=group_by, var_from=var_from, to=to, bucket_type=bucket_type, bucket_ms=bucket_ms, expand=expand)
        print("The response of InsightsChartsBetaApi->get_release_frequency_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsChartsBetaApi->get_release_frequency_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **application_key** | **str**| Comma separated list of application keys | [optional] 
 **has_experiments** | **bool**| Filter events to those associated with an experiment (&#x60;true&#x60;) or without an experiment (&#x60;false&#x60;) | [optional] 
 **var_global** | **str**| Filter to include or exclude global events. Default value is &#x60;include&#x60;. Options: &#x60;include&#x60;, &#x60;exclude&#x60; | [optional] 
 **group_by** | **str**| Property to group results by. Options: &#x60;impact&#x60; | [optional] 
 **var_from** | **datetime**| Unix timestamp in milliseconds. Default value is 7 days ago. | [optional] 
 **to** | **datetime**| Unix timestamp in milliseconds. Default value is now. | [optional] 
 **bucket_type** | **str**| Specify type of bucket. Options: &#x60;rolling&#x60;, &#x60;hour&#x60;, &#x60;day&#x60;. Default: &#x60;rolling&#x60;. | [optional] 
 **bucket_ms** | **int**| Duration of intervals for x-axis in milliseconds. Default value is one day (&#x60;86400000&#x60; milliseconds). | [optional] 
 **expand** | **str**| Options: &#x60;metrics&#x60; | [optional] 

### Return type

[**InsightsChart**](InsightsChart.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chart response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stale_flags_chart**
> InsightsChart get_stale_flags_chart(project_key, environment_key, application_key=application_key, group_by=group_by, maintainer_id=maintainer_id, maintainer_team_key=maintainer_team_key, expand=expand)

Get stale flags chart data

Get stale flags chart data. Engineering insights displays stale flags data in the [flag health metric view](https://launchdarkly.com/docs/home/observability/flag-health).

### Expanding the chart response

LaunchDarkly supports expanding the chart response to include additional fields.

To expand the response, append the `expand` query parameter and include the following:

* `metrics` includes details on the metrics related to stale flags

For example, use `?expand=metrics` to include the `metrics` field in the response. By default, this field is **not** included in the response.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.insights_chart import InsightsChart
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
    api_instance = launchdarkly_api.InsightsChartsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    application_key = 'application_key_example' # str | Comma separated list of application keys (optional)
    group_by = 'group_by_example' # str | Property to group results by. Options: `maintainer` (optional)
    maintainer_id = 'maintainer_id_example' # str | Comma-separated list of individual maintainers to filter results. (optional)
    maintainer_team_key = 'maintainer_team_key_example' # str | Comma-separated list of team maintainer keys to filter results. (optional)
    expand = 'expand_example' # str | Options: `metrics` (optional)

    try:
        # Get stale flags chart data
        api_response = api_instance.get_stale_flags_chart(project_key, environment_key, application_key=application_key, group_by=group_by, maintainer_id=maintainer_id, maintainer_team_key=maintainer_team_key, expand=expand)
        print("The response of InsightsChartsBetaApi->get_stale_flags_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsChartsBetaApi->get_stale_flags_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **application_key** | **str**| Comma separated list of application keys | [optional] 
 **group_by** | **str**| Property to group results by. Options: &#x60;maintainer&#x60; | [optional] 
 **maintainer_id** | **str**| Comma-separated list of individual maintainers to filter results. | [optional] 
 **maintainer_team_key** | **str**| Comma-separated list of team maintainer keys to filter results. | [optional] 
 **expand** | **str**| Options: &#x60;metrics&#x60; | [optional] 

### Return type

[**InsightsChart**](InsightsChart.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chart response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

