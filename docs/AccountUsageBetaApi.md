# launchdarkly_api.AccountUsageBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contexts_clientside_usage**](AccountUsageBetaApi.md#get_contexts_clientside_usage) | **GET** /api/v2/usage/clientside-contexts | Get contexts clientside usage
[**get_contexts_serverside_usage**](AccountUsageBetaApi.md#get_contexts_serverside_usage) | **GET** /api/v2/usage/serverside-contexts | Get contexts serverside usage
[**get_contexts_total_usage**](AccountUsageBetaApi.md#get_contexts_total_usage) | **GET** /api/v2/usage/total-contexts | Get contexts total usage
[**get_data_export_events_usage**](AccountUsageBetaApi.md#get_data_export_events_usage) | **GET** /api/v2/usage/data-export-events | Get data export events usage
[**get_evaluations_usage**](AccountUsageBetaApi.md#get_evaluations_usage) | **GET** /api/v2/usage/evaluations/{projectKey}/{environmentKey}/{featureFlagKey} | Get evaluations usage
[**get_events_usage**](AccountUsageBetaApi.md#get_events_usage) | **GET** /api/v2/usage/events/{type} | Get events usage
[**get_experimentation_events_usage**](AccountUsageBetaApi.md#get_experimentation_events_usage) | **GET** /api/v2/usage/experimentation-events | Get experimentation events usage
[**get_experimentation_keys_usage**](AccountUsageBetaApi.md#get_experimentation_keys_usage) | **GET** /api/v2/usage/experimentation-keys | Get experimentation keys usage
[**get_mau_clientside_usage**](AccountUsageBetaApi.md#get_mau_clientside_usage) | **GET** /api/v2/usage/clientside-mau | Get MAU clientside usage
[**get_mau_sdks_by_type**](AccountUsageBetaApi.md#get_mau_sdks_by_type) | **GET** /api/v2/usage/mau/sdks | Get MAU SDKs by type
[**get_mau_total_usage**](AccountUsageBetaApi.md#get_mau_total_usage) | **GET** /api/v2/usage/total-mau | Get MAU total usage
[**get_mau_usage**](AccountUsageBetaApi.md#get_mau_usage) | **GET** /api/v2/usage/mau | Get MAU usage
[**get_mau_usage_by_category**](AccountUsageBetaApi.md#get_mau_usage_by_category) | **GET** /api/v2/usage/mau/bycategory | Get MAU usage by category
[**get_observability_errors_usage**](AccountUsageBetaApi.md#get_observability_errors_usage) | **GET** /api/v2/usage/observability/errors | Get observability errors usage
[**get_observability_logs_usage**](AccountUsageBetaApi.md#get_observability_logs_usage) | **GET** /api/v2/usage/observability/logs | Get observability logs usage
[**get_observability_sessions_usage**](AccountUsageBetaApi.md#get_observability_sessions_usage) | **GET** /api/v2/usage/observability/sessions | Get observability sessions usage
[**get_observability_traces_usage**](AccountUsageBetaApi.md#get_observability_traces_usage) | **GET** /api/v2/usage/observability/traces | Get observability traces usage
[**get_service_connections_usage**](AccountUsageBetaApi.md#get_service_connections_usage) | **GET** /api/v2/usage/service-connections | Get service connections usage
[**get_stream_usage**](AccountUsageBetaApi.md#get_stream_usage) | **GET** /api/v2/usage/streams/{source} | Get stream usage
[**get_stream_usage_by_sdk_version**](AccountUsageBetaApi.md#get_stream_usage_by_sdk_version) | **GET** /api/v2/usage/streams/{source}/bysdkversion | Get stream usage by SDK version
[**get_stream_usage_sdkversion**](AccountUsageBetaApi.md#get_stream_usage_sdkversion) | **GET** /api/v2/usage/streams/{source}/sdkversions | Get stream usage SDK versions


# **get_contexts_clientside_usage**
> SeriesListRep get_contexts_clientside_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, context_kind=context_kind, sdk_name=sdk_name, anonymous=anonymous, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)

Get contexts clientside usage

Get a detailed time series of the number of context key usages observed by LaunchDarkly in your account, including non-primary context kinds. Use this for breakdowns that go beyond the primary-only aggregation of MAU endpoints. The counts reflect data reported by client-side SDKs.<br/><br/>The supported granularity varies by aggregation type. The maximum time range is 365 days.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. (optional)
    project_key = 'project_key_example' # str | A project key to filter results by. Can be specified multiple times, one query parameter per project key. (optional)
    environment_key = 'environment_key_example' # str | An environment key to filter results by. If specified, exactly one `projectKey` must be provided. Can be specified multiple times, one query parameter per environment key. (optional)
    context_kind = 'context_kind_example' # str | A context kind to filter results by. Can be specified multiple times, one query parameter per context kind. (optional)
    sdk_name = 'sdk_name_example' # str | An SDK name to filter results by. Can be specified multiple times, one query parameter per SDK name. (optional)
    anonymous = 'anonymous_example' # str | An anonymous value to filter results by. Can be specified multiple times, one query parameter per anonymous value.<br/>Valid values: `true`, `false`. (optional)
    group_by = 'group_by_example' # str | If specified, returns data for each distinct value of the given field. `contextKind` is always included as a grouping dimension. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.<br/>Valid values: `projectId`, `environmentId`, `sdkName`, `sdkAppId`, `anonymousV2`. (optional)
    aggregation_type = 'aggregation_type_example' # str | Specifies the aggregation method. Defaults to `month_to_date`.<br/>Valid values: `month_to_date`, `incremental`, `rolling_30d`. (optional)
    granularity = 'granularity_example' # str | Specifies the data granularity. Defaults to `daily`. Valid values depend on `aggregationType`: **month_to_date** supports `daily` and `monthly`; **incremental** and **rolling_30d** support `daily` only. (optional)

    try:
        # Get contexts clientside usage
        api_response = api_instance.get_contexts_clientside_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, context_kind=context_kind, sdk_name=sdk_name, anonymous=anonymous, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)
        print("The response of AccountUsageBetaApi->get_contexts_clientside_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_contexts_clientside_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. | [optional] 
 **project_key** | **str**| A project key to filter results by. Can be specified multiple times, one query parameter per project key. | [optional] 
 **environment_key** | **str**| An environment key to filter results by. If specified, exactly one &#x60;projectKey&#x60; must be provided. Can be specified multiple times, one query parameter per environment key. | [optional] 
 **context_kind** | **str**| A context kind to filter results by. Can be specified multiple times, one query parameter per context kind. | [optional] 
 **sdk_name** | **str**| An SDK name to filter results by. Can be specified multiple times, one query parameter per SDK name. | [optional] 
 **anonymous** | **str**| An anonymous value to filter results by. Can be specified multiple times, one query parameter per anonymous value.&lt;br/&gt;Valid values: &#x60;true&#x60;, &#x60;false&#x60;. | [optional] 
 **group_by** | **str**| If specified, returns data for each distinct value of the given field. &#x60;contextKind&#x60; is always included as a grouping dimension. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.&lt;br/&gt;Valid values: &#x60;projectId&#x60;, &#x60;environmentId&#x60;, &#x60;sdkName&#x60;, &#x60;sdkAppId&#x60;, &#x60;anonymousV2&#x60;. | [optional] 
 **aggregation_type** | **str**| Specifies the aggregation method. Defaults to &#x60;month_to_date&#x60;.&lt;br/&gt;Valid values: &#x60;month_to_date&#x60;, &#x60;incremental&#x60;, &#x60;rolling_30d&#x60;. | [optional] 
 **granularity** | **str**| Specifies the data granularity. Defaults to &#x60;daily&#x60;. Valid values depend on &#x60;aggregationType&#x60;: **month_to_date** supports &#x60;daily&#x60; and &#x60;monthly&#x60;; **incremental** and **rolling_30d** support &#x60;daily&#x60; only. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contexts_serverside_usage**
> SeriesListRep get_contexts_serverside_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, context_kind=context_kind, sdk_name=sdk_name, anonymous=anonymous, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)

Get contexts serverside usage

Get a detailed time series of the number of context key usages observed by LaunchDarkly in your account, including non-primary context kinds. Use this for breakdowns that go beyond the primary-only aggregation of MAU endpoints. The counts reflect data reported by server-side SDKs.<br/><br/>The supported granularity varies by aggregation type. The maximum time range is 365 days.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. (optional)
    project_key = 'project_key_example' # str | A project key to filter results by. Can be specified multiple times, one query parameter per project key. (optional)
    environment_key = 'environment_key_example' # str | An environment key to filter results by. If specified, exactly one `projectKey` must be provided. Can be specified multiple times, one query parameter per environment key. (optional)
    context_kind = 'context_kind_example' # str | A context kind to filter results by. Can be specified multiple times, one query parameter per context kind. (optional)
    sdk_name = 'sdk_name_example' # str | An SDK name to filter results by. Can be specified multiple times, one query parameter per SDK name. (optional)
    anonymous = 'anonymous_example' # str | An anonymous value to filter results by. Can be specified multiple times, one query parameter per anonymous value.<br/>Valid values: `true`, `false`. (optional)
    group_by = 'group_by_example' # str | If specified, returns data for each distinct value of the given field. `contextKind` is always included as a grouping dimension. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.<br/>Valid values: `projectId`, `environmentId`, `sdkName`, `sdkAppId`, `anonymousV2`. (optional)
    aggregation_type = 'aggregation_type_example' # str | Specifies the aggregation method. Defaults to `month_to_date`.<br/>Valid values: `month_to_date`, `incremental`, `rolling_30d`. (optional)
    granularity = 'granularity_example' # str | Specifies the data granularity. Defaults to `daily`. Valid values depend on `aggregationType`: **month_to_date** supports `daily` and `monthly`; **incremental** and **rolling_30d** support `daily` only. (optional)

    try:
        # Get contexts serverside usage
        api_response = api_instance.get_contexts_serverside_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, context_kind=context_kind, sdk_name=sdk_name, anonymous=anonymous, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)
        print("The response of AccountUsageBetaApi->get_contexts_serverside_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_contexts_serverside_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. | [optional] 
 **project_key** | **str**| A project key to filter results by. Can be specified multiple times, one query parameter per project key. | [optional] 
 **environment_key** | **str**| An environment key to filter results by. If specified, exactly one &#x60;projectKey&#x60; must be provided. Can be specified multiple times, one query parameter per environment key. | [optional] 
 **context_kind** | **str**| A context kind to filter results by. Can be specified multiple times, one query parameter per context kind. | [optional] 
 **sdk_name** | **str**| An SDK name to filter results by. Can be specified multiple times, one query parameter per SDK name. | [optional] 
 **anonymous** | **str**| An anonymous value to filter results by. Can be specified multiple times, one query parameter per anonymous value.&lt;br/&gt;Valid values: &#x60;true&#x60;, &#x60;false&#x60;. | [optional] 
 **group_by** | **str**| If specified, returns data for each distinct value of the given field. &#x60;contextKind&#x60; is always included as a grouping dimension. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.&lt;br/&gt;Valid values: &#x60;projectId&#x60;, &#x60;environmentId&#x60;, &#x60;sdkName&#x60;, &#x60;sdkAppId&#x60;, &#x60;anonymousV2&#x60;. | [optional] 
 **aggregation_type** | **str**| Specifies the aggregation method. Defaults to &#x60;month_to_date&#x60;.&lt;br/&gt;Valid values: &#x60;month_to_date&#x60;, &#x60;incremental&#x60;, &#x60;rolling_30d&#x60;. | [optional] 
 **granularity** | **str**| Specifies the data granularity. Defaults to &#x60;daily&#x60;. Valid values depend on &#x60;aggregationType&#x60;: **month_to_date** supports &#x60;daily&#x60; and &#x60;monthly&#x60;; **incremental** and **rolling_30d** support &#x60;daily&#x60; only. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contexts_total_usage**
> SeriesListRep get_contexts_total_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, context_kind=context_kind, sdk_name=sdk_name, sdk_type=sdk_type, anonymous=anonymous, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)

Get contexts total usage

Get a detailed time series of the number of context key usages observed by LaunchDarkly in your account, including non-primary context kinds. Use this for breakdowns that go beyond the primary-only aggregation of MAU endpoints.<br/><br/>The supported granularity varies by aggregation type. The maximum time range is 365 days.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. (optional)
    project_key = 'project_key_example' # str | A project key to filter results by. Can be specified multiple times, one query parameter per project key. (optional)
    environment_key = 'environment_key_example' # str | An environment key to filter results by. If specified, exactly one `projectKey` must be provided. Can be specified multiple times, one query parameter per environment key. (optional)
    context_kind = 'context_kind_example' # str | A context kind to filter results by. Can be specified multiple times, one query parameter per context kind. (optional)
    sdk_name = 'sdk_name_example' # str | An SDK name to filter results by. Can be specified multiple times, one query parameter per SDK name. (optional)
    sdk_type = 'sdk_type_example' # str | An SDK type to filter results by. Can be specified multiple times, one query parameter per SDK type. (optional)
    anonymous = 'anonymous_example' # str | An anonymous value to filter results by. Can be specified multiple times, one query parameter per anonymous value.<br/>Valid values: `true`, `false`. (optional)
    group_by = 'group_by_example' # str | If specified, returns data for each distinct value of the given field. `contextKind` is always included as a grouping dimension. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.<br/>Valid values: `projectId`, `environmentId`, `sdkName`, `sdkType`, `sdkAppId`, `anonymousV2`. (optional)
    aggregation_type = 'aggregation_type_example' # str | Specifies the aggregation method. Defaults to `month_to_date`.<br/>Valid values: `month_to_date`, `incremental`, `rolling_30d`. (optional)
    granularity = 'granularity_example' # str | Specifies the data granularity. Defaults to `daily`. Valid values depend on `aggregationType`: **month_to_date** supports `daily` and `monthly`; **incremental** and **rolling_30d** support `daily` only. (optional)

    try:
        # Get contexts total usage
        api_response = api_instance.get_contexts_total_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, context_kind=context_kind, sdk_name=sdk_name, sdk_type=sdk_type, anonymous=anonymous, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)
        print("The response of AccountUsageBetaApi->get_contexts_total_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_contexts_total_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. | [optional] 
 **project_key** | **str**| A project key to filter results by. Can be specified multiple times, one query parameter per project key. | [optional] 
 **environment_key** | **str**| An environment key to filter results by. If specified, exactly one &#x60;projectKey&#x60; must be provided. Can be specified multiple times, one query parameter per environment key. | [optional] 
 **context_kind** | **str**| A context kind to filter results by. Can be specified multiple times, one query parameter per context kind. | [optional] 
 **sdk_name** | **str**| An SDK name to filter results by. Can be specified multiple times, one query parameter per SDK name. | [optional] 
 **sdk_type** | **str**| An SDK type to filter results by. Can be specified multiple times, one query parameter per SDK type. | [optional] 
 **anonymous** | **str**| An anonymous value to filter results by. Can be specified multiple times, one query parameter per anonymous value.&lt;br/&gt;Valid values: &#x60;true&#x60;, &#x60;false&#x60;. | [optional] 
 **group_by** | **str**| If specified, returns data for each distinct value of the given field. &#x60;contextKind&#x60; is always included as a grouping dimension. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.&lt;br/&gt;Valid values: &#x60;projectId&#x60;, &#x60;environmentId&#x60;, &#x60;sdkName&#x60;, &#x60;sdkType&#x60;, &#x60;sdkAppId&#x60;, &#x60;anonymousV2&#x60;. | [optional] 
 **aggregation_type** | **str**| Specifies the aggregation method. Defaults to &#x60;month_to_date&#x60;.&lt;br/&gt;Valid values: &#x60;month_to_date&#x60;, &#x60;incremental&#x60;, &#x60;rolling_30d&#x60;. | [optional] 
 **granularity** | **str**| Specifies the data granularity. Defaults to &#x60;daily&#x60;. Valid values depend on &#x60;aggregationType&#x60;: **month_to_date** supports &#x60;daily&#x60; and &#x60;monthly&#x60;; **incremental** and **rolling_30d** support &#x60;daily&#x60; only. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_export_events_usage**
> SeriesListRep get_data_export_events_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, event_kind=event_kind, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)

Get data export events usage

Get a time series array showing the number of data export events from your account. The supported granularity varies by aggregation type. The maximum time range is 365 days.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. (optional)
    project_key = 'project_key_example' # str | A project key to filter results by. Can be specified multiple times, one query parameter per project key. (optional)
    environment_key = 'environment_key_example' # str | An environment key to filter results by. If specified, exactly one `projectKey` must be provided. Can be specified multiple times, one query parameter per environment key. (optional)
    event_kind = 'event_kind_example' # str | An event kind to filter results by. Can be specified multiple times, one query parameter per event kind. (optional)
    group_by = 'group_by_example' # str | If specified, returns data for each distinct value of the given field. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.<br/>Valid values: `environmentId`, `eventKind`. (optional)
    aggregation_type = 'aggregation_type_example' # str | Specifies the aggregation method. Defaults to `month_to_date`.<br/>Valid values: `month_to_date`, `incremental`. (optional)
    granularity = 'granularity_example' # str | Specifies the data granularity. Defaults to `daily`. `monthly` granularity is only supported with the **month_to_date** aggregation type.<br/>Valid values: `daily`, `hourly`, `monthly`. (optional)

    try:
        # Get data export events usage
        api_response = api_instance.get_data_export_events_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, event_kind=event_kind, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)
        print("The response of AccountUsageBetaApi->get_data_export_events_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_data_export_events_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. | [optional] 
 **project_key** | **str**| A project key to filter results by. Can be specified multiple times, one query parameter per project key. | [optional] 
 **environment_key** | **str**| An environment key to filter results by. If specified, exactly one &#x60;projectKey&#x60; must be provided. Can be specified multiple times, one query parameter per environment key. | [optional] 
 **event_kind** | **str**| An event kind to filter results by. Can be specified multiple times, one query parameter per event kind. | [optional] 
 **group_by** | **str**| If specified, returns data for each distinct value of the given field. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.&lt;br/&gt;Valid values: &#x60;environmentId&#x60;, &#x60;eventKind&#x60;. | [optional] 
 **aggregation_type** | **str**| Specifies the aggregation method. Defaults to &#x60;month_to_date&#x60;.&lt;br/&gt;Valid values: &#x60;month_to_date&#x60;, &#x60;incremental&#x60;. | [optional] 
 **granularity** | **str**| Specifies the data granularity. Defaults to &#x60;daily&#x60;. &#x60;monthly&#x60; granularity is only supported with the **month_to_date** aggregation type.&lt;br/&gt;Valid values: &#x60;daily&#x60;, &#x60;hourly&#x60;, &#x60;monthly&#x60;. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluations_usage**
> SeriesListRep get_evaluations_usage(project_key, environment_key, feature_flag_key, var_from=var_from, to=to, tz=tz)

Get evaluations usage

Get time-series arrays of the number of times a flag is evaluated, broken down by the variation that resulted from that evaluation. The granularity of the data depends on the age of the data requested. If the requested range is within the past two hours, minutely data is returned. If it is within the last two days, hourly data is returned. Otherwise, daily data is returned.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp. Defaults to 30 days ago. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp. Defaults to the current time. (optional)
    tz = 'tz_example' # str | The timezone to use for breaks between days when returning daily data. (optional)

    try:
        # Get evaluations usage
        api_response = api_instance.get_evaluations_usage(project_key, environment_key, feature_flag_key, var_from=var_from, to=to, tz=tz)
        print("The response of AccountUsageBetaApi->get_evaluations_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_evaluations_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **var_from** | **str**| The series of data returned starts from this timestamp. Defaults to 30 days ago. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp. Defaults to the current time. | [optional] 
 **tz** | **str**| The timezone to use for breaks between days when returning daily data. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_usage**
> SeriesListRep get_events_usage(type, var_from=var_from, to=to)

Get events usage

Get time-series arrays of the number of times a flag is evaluated, broken down by the variation that resulted from that evaluation. The granularity of the data depends on the age of the data requested. If the requested range is within the past two hours, minutely data is returned. If it is within the last two days, hourly data is returned. Otherwise, daily data is returned.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    type = 'type_example' # str | The type of event to retrieve. Must be either `received` or `published`.
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp. Defaults to 24 hours ago. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp. Defaults to the current time. (optional)

    try:
        # Get events usage
        api_response = api_instance.get_events_usage(type, var_from=var_from, to=to)
        print("The response of AccountUsageBetaApi->get_events_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_events_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of event to retrieve. Must be either &#x60;received&#x60; or &#x60;published&#x60;. | 
 **var_from** | **str**| The series of data returned starts from this timestamp. Defaults to 24 hours ago. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp. Defaults to the current time. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experimentation_events_usage**
> SeriesListRep get_experimentation_events_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, event_key=event_key, event_kind=event_kind, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)

Get experimentation events usage

Get a time series array showing the number of experimentation events from your account. The supported granularity varies by aggregation type. The maximum time range is 365 days.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. (optional)
    project_key = 'project_key_example' # str | A project key to filter results by. Can be specified multiple times, one query parameter per project key. (optional)
    environment_key = 'environment_key_example' # str | An environment key to filter results by. If specified, exactly one `projectKey` must be provided. Can be specified multiple times, one query parameter per environment key. (optional)
    event_key = 'event_key_example' # str | An event key to filter results by. Can be specified multiple times, one query parameter per event key. (optional)
    event_kind = 'event_kind_example' # str | An event kind to filter results by. Can be specified multiple times, one query parameter per event kind. (optional)
    group_by = 'group_by_example' # str | If specified, returns data for each distinct value of the given field. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.<br/>Valid values: `environmentId`, `eventKey`, `eventKind`. (optional)
    aggregation_type = 'aggregation_type_example' # str | Specifies the aggregation method. Defaults to `month_to_date`.<br/>Valid values: `month_to_date`, `incremental`. (optional)
    granularity = 'granularity_example' # str | Specifies the data granularity. Defaults to `daily`. `monthly` granularity is only supported with the **month_to_date** aggregation type.<br/>Valid values: `daily`, `hourly`, `monthly`. (optional)

    try:
        # Get experimentation events usage
        api_response = api_instance.get_experimentation_events_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, event_key=event_key, event_kind=event_kind, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)
        print("The response of AccountUsageBetaApi->get_experimentation_events_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_experimentation_events_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. | [optional] 
 **project_key** | **str**| A project key to filter results by. Can be specified multiple times, one query parameter per project key. | [optional] 
 **environment_key** | **str**| An environment key to filter results by. If specified, exactly one &#x60;projectKey&#x60; must be provided. Can be specified multiple times, one query parameter per environment key. | [optional] 
 **event_key** | **str**| An event key to filter results by. Can be specified multiple times, one query parameter per event key. | [optional] 
 **event_kind** | **str**| An event kind to filter results by. Can be specified multiple times, one query parameter per event kind. | [optional] 
 **group_by** | **str**| If specified, returns data for each distinct value of the given field. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.&lt;br/&gt;Valid values: &#x60;environmentId&#x60;, &#x60;eventKey&#x60;, &#x60;eventKind&#x60;. | [optional] 
 **aggregation_type** | **str**| Specifies the aggregation method. Defaults to &#x60;month_to_date&#x60;.&lt;br/&gt;Valid values: &#x60;month_to_date&#x60;, &#x60;incremental&#x60;. | [optional] 
 **granularity** | **str**| Specifies the data granularity. Defaults to &#x60;daily&#x60;. &#x60;monthly&#x60; granularity is only supported with the **month_to_date** aggregation type.&lt;br/&gt;Valid values: &#x60;daily&#x60;, &#x60;hourly&#x60;, &#x60;monthly&#x60;. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experimentation_keys_usage**
> SeriesListRep get_experimentation_keys_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, experiment_id=experiment_id, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)

Get experimentation keys usage

Get a time series array showing the number of experimentation keys from your account. The supported granularity varies by aggregation type. The maximum time range is 365 days.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. (optional)
    project_key = 'project_key_example' # str | A project key to filter results by. Can be specified multiple times, one query parameter per project key. (optional)
    environment_key = 'environment_key_example' # str | An environment key to filter results by. If specified, exactly one `projectKey` must be provided. Can be specified multiple times, one query parameter per environment key. (optional)
    experiment_id = 'experiment_id_example' # str | An experiment ID to filter results by. Can be specified multiple times, one query parameter per experiment ID. (optional)
    group_by = 'group_by_example' # str | If specified, returns data for each distinct value of the given field. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.<br/>Valid values: `projectId`, `environmentId`, `experimentId`. (optional)
    aggregation_type = 'aggregation_type_example' # str | Specifies the aggregation method. Defaults to `month_to_date`.<br/>Valid values: `month_to_date`, `incremental`. (optional)
    granularity = 'granularity_example' # str | Specifies the data granularity. Defaults to `daily`. `monthly` granularity is only supported with the **month_to_date** aggregation type.<br/>Valid values: `daily`, `hourly`, `monthly`. (optional)

    try:
        # Get experimentation keys usage
        api_response = api_instance.get_experimentation_keys_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, experiment_id=experiment_id, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)
        print("The response of AccountUsageBetaApi->get_experimentation_keys_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_experimentation_keys_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. | [optional] 
 **project_key** | **str**| A project key to filter results by. Can be specified multiple times, one query parameter per project key. | [optional] 
 **environment_key** | **str**| An environment key to filter results by. If specified, exactly one &#x60;projectKey&#x60; must be provided. Can be specified multiple times, one query parameter per environment key. | [optional] 
 **experiment_id** | **str**| An experiment ID to filter results by. Can be specified multiple times, one query parameter per experiment ID. | [optional] 
 **group_by** | **str**| If specified, returns data for each distinct value of the given field. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.&lt;br/&gt;Valid values: &#x60;projectId&#x60;, &#x60;environmentId&#x60;, &#x60;experimentId&#x60;. | [optional] 
 **aggregation_type** | **str**| Specifies the aggregation method. Defaults to &#x60;month_to_date&#x60;.&lt;br/&gt;Valid values: &#x60;month_to_date&#x60;, &#x60;incremental&#x60;. | [optional] 
 **granularity** | **str**| Specifies the data granularity. Defaults to &#x60;daily&#x60;. &#x60;monthly&#x60; granularity is only supported with the **month_to_date** aggregation type.&lt;br/&gt;Valid values: &#x60;daily&#x60;, &#x60;hourly&#x60;, &#x60;monthly&#x60;. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mau_clientside_usage**
> SeriesListRep get_mau_clientside_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, sdk_name=sdk_name, anonymous=anonymous, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)

Get MAU clientside usage

Get a time series of the number of context key usages observed by LaunchDarkly in your account, for the primary context kind only. The counts reflect data reported from client-side SDKs.<br/><br/>For past months, the primary context kind is fixed and reflects the last known primary kind for that month. For the current month, it may vary as new primary context kinds are observed.<br/><br/>The supported granularity varies by aggregation type. The maximum time range is 365 days.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. (optional)
    project_key = 'project_key_example' # str | A project key to filter results by. Can be specified multiple times, one query parameter per project key. (optional)
    environment_key = 'environment_key_example' # str | An environment key to filter results by. If specified, exactly one `projectKey` must be provided. Can be specified multiple times, one query parameter per environment key. (optional)
    sdk_name = 'sdk_name_example' # str | An SDK name to filter results by. Can be specified multiple times, one query parameter per SDK name. (optional)
    anonymous = 'anonymous_example' # str | An anonymous value to filter results by. Can be specified multiple times, one query parameter per anonymous value.<br/>Valid values: `true`, `false`. (optional)
    group_by = 'group_by_example' # str | If specified, returns data for each distinct value of the given field. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.<br/>Valid values: `projectId`, `environmentId`, `sdkName`, `sdkAppId`, `anonymousV2`. (optional)
    aggregation_type = 'aggregation_type_example' # str | Specifies the aggregation method. Defaults to `month_to_date`.<br/>Valid values: `month_to_date`, `incremental`, `rolling_30d`. (optional)
    granularity = 'granularity_example' # str | Specifies the data granularity. Defaults to `daily`. Valid values depend on `aggregationType`: **month_to_date** supports `daily` and `monthly`; **incremental** and **rolling_30d** support `daily` only. (optional)

    try:
        # Get MAU clientside usage
        api_response = api_instance.get_mau_clientside_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, sdk_name=sdk_name, anonymous=anonymous, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)
        print("The response of AccountUsageBetaApi->get_mau_clientside_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_mau_clientside_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. | [optional] 
 **project_key** | **str**| A project key to filter results by. Can be specified multiple times, one query parameter per project key. | [optional] 
 **environment_key** | **str**| An environment key to filter results by. If specified, exactly one &#x60;projectKey&#x60; must be provided. Can be specified multiple times, one query parameter per environment key. | [optional] 
 **sdk_name** | **str**| An SDK name to filter results by. Can be specified multiple times, one query parameter per SDK name. | [optional] 
 **anonymous** | **str**| An anonymous value to filter results by. Can be specified multiple times, one query parameter per anonymous value.&lt;br/&gt;Valid values: &#x60;true&#x60;, &#x60;false&#x60;. | [optional] 
 **group_by** | **str**| If specified, returns data for each distinct value of the given field. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.&lt;br/&gt;Valid values: &#x60;projectId&#x60;, &#x60;environmentId&#x60;, &#x60;sdkName&#x60;, &#x60;sdkAppId&#x60;, &#x60;anonymousV2&#x60;. | [optional] 
 **aggregation_type** | **str**| Specifies the aggregation method. Defaults to &#x60;month_to_date&#x60;.&lt;br/&gt;Valid values: &#x60;month_to_date&#x60;, &#x60;incremental&#x60;, &#x60;rolling_30d&#x60;. | [optional] 
 **granularity** | **str**| Specifies the data granularity. Defaults to &#x60;daily&#x60;. Valid values depend on &#x60;aggregationType&#x60;: **month_to_date** supports &#x60;daily&#x60; and &#x60;monthly&#x60;; **incremental** and **rolling_30d** support &#x60;daily&#x60; only. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mau_sdks_by_type**
> SdkListRep get_mau_sdks_by_type(var_from=var_from, to=to, sdktype=sdktype)

Get MAU SDKs by type

Get a list of SDKs. These are all of the SDKs that have connected to LaunchDarkly by monthly active users (MAU) in the requested time period.<br/><br/>Endpoints for retrieving monthly active users (MAU) do not return information about active context instances. After you have upgraded your LaunchDarkly SDK to use contexts instead of users, you should not rely on this endpoint. To learn more, read [Account usage metrics](https://launchdarkly.com/docs/home/account/metrics).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.sdk_list_rep import SdkListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The data returned starts from this timestamp. Defaults to seven days ago. The timestamp is in Unix milliseconds, for example, 1656694800000. (optional)
    to = 'to_example' # str | The data returned ends at this timestamp. Defaults to the current time. The timestamp is in Unix milliseconds, for example, 1657904400000. (optional)
    sdktype = 'sdktype_example' # str | The type of SDK with monthly active users (MAU) to list. Must be either `client` or `server`. (optional)

    try:
        # Get MAU SDKs by type
        api_response = api_instance.get_mau_sdks_by_type(var_from=var_from, to=to, sdktype=sdktype)
        print("The response of AccountUsageBetaApi->get_mau_sdks_by_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_mau_sdks_by_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The data returned starts from this timestamp. Defaults to seven days ago. The timestamp is in Unix milliseconds, for example, 1656694800000. | [optional] 
 **to** | **str**| The data returned ends at this timestamp. Defaults to the current time. The timestamp is in Unix milliseconds, for example, 1657904400000. | [optional] 
 **sdktype** | **str**| The type of SDK with monthly active users (MAU) to list. Must be either &#x60;client&#x60; or &#x60;server&#x60;. | [optional] 

### Return type

[**SdkListRep**](SdkListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MAU SDKs response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mau_total_usage**
> SeriesListRep get_mau_total_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, sdk_name=sdk_name, sdk_type=sdk_type, anonymous=anonymous, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)

Get MAU total usage

Get a time series of the number of context key usages observed by LaunchDarkly in your account, for the primary context kind only.<br/><br/>For past months, this reflects the context kind that was most recently marked as primary for that month. For the current month, the context kind may vary as new primary kinds are observed.<br/><br/>The supported granularity varies by aggregation type. The maximum time range is 365 days.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. (optional)
    project_key = 'project_key_example' # str | A project key to filter results by. Can be specified multiple times, one query parameter per project key. (optional)
    environment_key = 'environment_key_example' # str | An environment key to filter results by. If specified, exactly one `projectKey` must be provided. Can be specified multiple times, one query parameter per environment key. (optional)
    sdk_name = 'sdk_name_example' # str | An SDK name to filter results by. Can be specified multiple times, one query parameter per SDK name. (optional)
    sdk_type = 'sdk_type_example' # str | An SDK type to filter results by. Can be specified multiple times, one query parameter per SDK type. (optional)
    anonymous = 'anonymous_example' # str | An anonymous value to filter results by. Can be specified multiple times, one query parameter per anonymous value.<br/>Valid values: `true`, `false`. (optional)
    group_by = 'group_by_example' # str | If specified, returns data for each distinct value of the given field. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.<br/>Valid values: `projectId`, `environmentId`, `sdkName`, `sdkType`, `sdkAppId`, `anonymousV2`. (optional)
    aggregation_type = 'aggregation_type_example' # str | Specifies the aggregation method. Defaults to `month_to_date`.<br/>Valid values: `month_to_date`, `incremental`, `rolling_30d`. (optional)
    granularity = 'granularity_example' # str | Specifies the data granularity. Defaults to `daily`. Valid values depend on `aggregationType`: **month_to_date** supports `daily` and `monthly`; **incremental** and **rolling_30d** support `daily` only. (optional)

    try:
        # Get MAU total usage
        api_response = api_instance.get_mau_total_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, sdk_name=sdk_name, sdk_type=sdk_type, anonymous=anonymous, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)
        print("The response of AccountUsageBetaApi->get_mau_total_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_mau_total_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. | [optional] 
 **project_key** | **str**| A project key to filter results by. Can be specified multiple times, one query parameter per project key. | [optional] 
 **environment_key** | **str**| An environment key to filter results by. If specified, exactly one &#x60;projectKey&#x60; must be provided. Can be specified multiple times, one query parameter per environment key. | [optional] 
 **sdk_name** | **str**| An SDK name to filter results by. Can be specified multiple times, one query parameter per SDK name. | [optional] 
 **sdk_type** | **str**| An SDK type to filter results by. Can be specified multiple times, one query parameter per SDK type. | [optional] 
 **anonymous** | **str**| An anonymous value to filter results by. Can be specified multiple times, one query parameter per anonymous value.&lt;br/&gt;Valid values: &#x60;true&#x60;, &#x60;false&#x60;. | [optional] 
 **group_by** | **str**| If specified, returns data for each distinct value of the given field. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.&lt;br/&gt;Valid values: &#x60;projectId&#x60;, &#x60;environmentId&#x60;, &#x60;sdkName&#x60;, &#x60;sdkType&#x60;, &#x60;sdkAppId&#x60;, &#x60;anonymousV2&#x60;. | [optional] 
 **aggregation_type** | **str**| Specifies the aggregation method. Defaults to &#x60;month_to_date&#x60;.&lt;br/&gt;Valid values: &#x60;month_to_date&#x60;, &#x60;incremental&#x60;, &#x60;rolling_30d&#x60;. | [optional] 
 **granularity** | **str**| Specifies the data granularity. Defaults to &#x60;daily&#x60;. Valid values depend on &#x60;aggregationType&#x60;: **month_to_date** supports &#x60;daily&#x60; and &#x60;monthly&#x60;; **incremental** and **rolling_30d** support &#x60;daily&#x60; only. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mau_usage**
> SeriesListRep get_mau_usage(var_from=var_from, to=to, project=project, environment=environment, sdktype=sdktype, sdk=sdk, anonymous=anonymous, groupby=groupby, aggregation_type=aggregation_type, context_kind=context_kind)

Get MAU usage

Get a time-series array of the number of monthly active users (MAU) seen by LaunchDarkly from your account. The granularity is always daily.<br/><br/>Endpoints for retrieving monthly active users (MAU) do not return information about active context instances. After you have upgraded your LaunchDarkly SDK to use contexts instead of users, you should not rely on this endpoint. To learn more, read [Account usage metrics](https://launchdarkly.com/docs/home/account/metrics).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp. Defaults to 30 days ago. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp. Defaults to the current time. (optional)
    project = 'project_example' # str | A project key to filter results to. Can be specified multiple times, one query parameter per project key, to view data for multiple projects. (optional)
    environment = 'environment_example' # str | An environment key to filter results to. When using this parameter, exactly one project key must also be set. Can be specified multiple times as separate query parameters to view data for multiple environments within a single project. (optional)
    sdktype = 'sdktype_example' # str | An SDK type to filter results to. Can be specified multiple times, one query parameter per SDK type. Valid values: client, server (optional)
    sdk = 'sdk_example' # str | An SDK name to filter results to. Can be specified multiple times, one query parameter per SDK. (optional)
    anonymous = 'anonymous_example' # str | If specified, filters results to either anonymous or nonanonymous users. (optional)
    groupby = 'groupby_example' # str | If specified, returns data for each distinct value of the given field. Can be specified multiple times to group data by multiple dimensions (for example, to group by both project and SDK). Valid values: project, environment, sdktype, sdk, anonymous, contextKind, sdkAppId (optional)
    aggregation_type = 'aggregation_type_example' # str | If specified, queries for rolling 30-day, month-to-date, or daily incremental counts. Default is rolling 30-day. Valid values: rolling_30d, month_to_date, daily_incremental (optional)
    context_kind = 'context_kind_example' # str | Filters results to the specified context kinds. Can be specified multiple times, one query parameter per context kind. If not set, queries for the user context kind. (optional)

    try:
        # Get MAU usage
        api_response = api_instance.get_mau_usage(var_from=var_from, to=to, project=project, environment=environment, sdktype=sdktype, sdk=sdk, anonymous=anonymous, groupby=groupby, aggregation_type=aggregation_type, context_kind=context_kind)
        print("The response of AccountUsageBetaApi->get_mau_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_mau_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The series of data returned starts from this timestamp. Defaults to 30 days ago. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp. Defaults to the current time. | [optional] 
 **project** | **str**| A project key to filter results to. Can be specified multiple times, one query parameter per project key, to view data for multiple projects. | [optional] 
 **environment** | **str**| An environment key to filter results to. When using this parameter, exactly one project key must also be set. Can be specified multiple times as separate query parameters to view data for multiple environments within a single project. | [optional] 
 **sdktype** | **str**| An SDK type to filter results to. Can be specified multiple times, one query parameter per SDK type. Valid values: client, server | [optional] 
 **sdk** | **str**| An SDK name to filter results to. Can be specified multiple times, one query parameter per SDK. | [optional] 
 **anonymous** | **str**| If specified, filters results to either anonymous or nonanonymous users. | [optional] 
 **groupby** | **str**| If specified, returns data for each distinct value of the given field. Can be specified multiple times to group data by multiple dimensions (for example, to group by both project and SDK). Valid values: project, environment, sdktype, sdk, anonymous, contextKind, sdkAppId | [optional] 
 **aggregation_type** | **str**| If specified, queries for rolling 30-day, month-to-date, or daily incremental counts. Default is rolling 30-day. Valid values: rolling_30d, month_to_date, daily_incremental | [optional] 
 **context_kind** | **str**| Filters results to the specified context kinds. Can be specified multiple times, one query parameter per context kind. If not set, queries for the user context kind. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mau_usage_by_category**
> SeriesListRep get_mau_usage_by_category(var_from=var_from, to=to)

Get MAU usage by category

Get time-series arrays of the number of monthly active users (MAU) seen by LaunchDarkly from your account, broken down by the category of users. The category is either `browser`, `mobile`, or `backend`.<br/><br/>Endpoints for retrieving monthly active users (MAU) do not return information about active context instances. After you have upgraded your LaunchDarkly SDK to use contexts instead of users, you should not rely on this endpoint. To learn more, read [Account usage metrics](https://launchdarkly.com/docs/home/account/metrics).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp. Defaults to 30 days ago. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp. Defaults to the current time. (optional)

    try:
        # Get MAU usage by category
        api_response = api_instance.get_mau_usage_by_category(var_from=var_from, to=to)
        print("The response of AccountUsageBetaApi->get_mau_usage_by_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_mau_usage_by_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The series of data returned starts from this timestamp. Defaults to 30 days ago. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp. Defaults to the current time. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observability_errors_usage**
> SeriesListRep get_observability_errors_usage(var_from=var_from, to=to, project_key=project_key, granularity=granularity, aggregation_type=aggregation_type)

Get observability errors usage

Get time-series arrays of the number of observability errors. Supports `daily` and `monthly` granularity.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. (optional)
    project_key = 'project_key_example' # str | A project key to filter results by. Can be specified multiple times, one query parameter per project key. (optional)
    granularity = 'granularity_example' # str | Specifies the data granularity. Defaults to `daily`. Valid values depend on `aggregationType`: **month_to_date** supports `daily` and `monthly`; **incremental** and **rolling_30d** support `daily` only. (optional)
    aggregation_type = 'aggregation_type_example' # str | Specifies the aggregation method. Defaults to `month_to_date`.<br/>Valid values: `month_to_date`, `incremental`, `rolling_30d`. (optional)

    try:
        # Get observability errors usage
        api_response = api_instance.get_observability_errors_usage(var_from=var_from, to=to, project_key=project_key, granularity=granularity, aggregation_type=aggregation_type)
        print("The response of AccountUsageBetaApi->get_observability_errors_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_observability_errors_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. | [optional] 
 **project_key** | **str**| A project key to filter results by. Can be specified multiple times, one query parameter per project key. | [optional] 
 **granularity** | **str**| Specifies the data granularity. Defaults to &#x60;daily&#x60;. Valid values depend on &#x60;aggregationType&#x60;: **month_to_date** supports &#x60;daily&#x60; and &#x60;monthly&#x60;; **incremental** and **rolling_30d** support &#x60;daily&#x60; only. | [optional] 
 **aggregation_type** | **str**| Specifies the aggregation method. Defaults to &#x60;month_to_date&#x60;.&lt;br/&gt;Valid values: &#x60;month_to_date&#x60;, &#x60;incremental&#x60;, &#x60;rolling_30d&#x60;. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observability_logs_usage**
> SeriesListRep get_observability_logs_usage(var_from=var_from, to=to, project_key=project_key, granularity=granularity, aggregation_type=aggregation_type)

Get observability logs usage

Get time-series arrays of the number of observability logs. Supports `daily` and `monthly` granularity.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. (optional)
    project_key = 'project_key_example' # str | A project key to filter results by. Can be specified multiple times, one query parameter per project key. (optional)
    granularity = 'granularity_example' # str | Specifies the data granularity. Defaults to `daily`. Valid values depend on `aggregationType`: **month_to_date** supports `daily` and `monthly`; **incremental** and **rolling_30d** support `daily` only. (optional)
    aggregation_type = 'aggregation_type_example' # str | Specifies the aggregation method. Defaults to `month_to_date`.<br/>Valid values: `month_to_date`, `incremental`, `rolling_30d`. (optional)

    try:
        # Get observability logs usage
        api_response = api_instance.get_observability_logs_usage(var_from=var_from, to=to, project_key=project_key, granularity=granularity, aggregation_type=aggregation_type)
        print("The response of AccountUsageBetaApi->get_observability_logs_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_observability_logs_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. | [optional] 
 **project_key** | **str**| A project key to filter results by. Can be specified multiple times, one query parameter per project key. | [optional] 
 **granularity** | **str**| Specifies the data granularity. Defaults to &#x60;daily&#x60;. Valid values depend on &#x60;aggregationType&#x60;: **month_to_date** supports &#x60;daily&#x60; and &#x60;monthly&#x60;; **incremental** and **rolling_30d** support &#x60;daily&#x60; only. | [optional] 
 **aggregation_type** | **str**| Specifies the aggregation method. Defaults to &#x60;month_to_date&#x60;.&lt;br/&gt;Valid values: &#x60;month_to_date&#x60;, &#x60;incremental&#x60;, &#x60;rolling_30d&#x60;. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observability_sessions_usage**
> SeriesListRep get_observability_sessions_usage(var_from=var_from, to=to, project_key=project_key, granularity=granularity, aggregation_type=aggregation_type)

Get observability sessions usage

Get time-series arrays of the number of observability sessions. Supports `daily` and `monthly` granularity.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. (optional)
    project_key = 'project_key_example' # str | A project key to filter results by. Can be specified multiple times, one query parameter per project key. (optional)
    granularity = 'granularity_example' # str | Specifies the data granularity. Defaults to `daily`. Valid values depend on `aggregationType`: **month_to_date** supports `daily` and `monthly`; **incremental** and **rolling_30d** support `daily` only. (optional)
    aggregation_type = 'aggregation_type_example' # str | Specifies the aggregation method. Defaults to `month_to_date`.<br/>Valid values: `month_to_date`, `incremental`, `rolling_30d`. (optional)

    try:
        # Get observability sessions usage
        api_response = api_instance.get_observability_sessions_usage(var_from=var_from, to=to, project_key=project_key, granularity=granularity, aggregation_type=aggregation_type)
        print("The response of AccountUsageBetaApi->get_observability_sessions_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_observability_sessions_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. | [optional] 
 **project_key** | **str**| A project key to filter results by. Can be specified multiple times, one query parameter per project key. | [optional] 
 **granularity** | **str**| Specifies the data granularity. Defaults to &#x60;daily&#x60;. Valid values depend on &#x60;aggregationType&#x60;: **month_to_date** supports &#x60;daily&#x60; and &#x60;monthly&#x60;; **incremental** and **rolling_30d** support &#x60;daily&#x60; only. | [optional] 
 **aggregation_type** | **str**| Specifies the aggregation method. Defaults to &#x60;month_to_date&#x60;.&lt;br/&gt;Valid values: &#x60;month_to_date&#x60;, &#x60;incremental&#x60;, &#x60;rolling_30d&#x60;. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observability_traces_usage**
> SeriesListRep get_observability_traces_usage(var_from=var_from, to=to, project_key=project_key, granularity=granularity, aggregation_type=aggregation_type)

Get observability traces usage

Get time-series arrays of the number of observability traces. Supports `daily` and `monthly` granularity.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. (optional)
    project_key = 'project_key_example' # str | A project key to filter results by. Can be specified multiple times, one query parameter per project key. (optional)
    granularity = 'granularity_example' # str | Specifies the data granularity. Defaults to `daily`. Valid values depend on `aggregationType`: **month_to_date** supports `daily` and `monthly`; **incremental** and **rolling_30d** support `daily` only. (optional)
    aggregation_type = 'aggregation_type_example' # str | Specifies the aggregation method. Defaults to `month_to_date`.<br/>Valid values: `month_to_date`, `incremental`, `rolling_30d`. (optional)

    try:
        # Get observability traces usage
        api_response = api_instance.get_observability_traces_usage(var_from=var_from, to=to, project_key=project_key, granularity=granularity, aggregation_type=aggregation_type)
        print("The response of AccountUsageBetaApi->get_observability_traces_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_observability_traces_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. | [optional] 
 **project_key** | **str**| A project key to filter results by. Can be specified multiple times, one query parameter per project key. | [optional] 
 **granularity** | **str**| Specifies the data granularity. Defaults to &#x60;daily&#x60;. Valid values depend on &#x60;aggregationType&#x60;: **month_to_date** supports &#x60;daily&#x60; and &#x60;monthly&#x60;; **incremental** and **rolling_30d** support &#x60;daily&#x60; only. | [optional] 
 **aggregation_type** | **str**| Specifies the aggregation method. Defaults to &#x60;month_to_date&#x60;.&lt;br/&gt;Valid values: &#x60;month_to_date&#x60;, &#x60;incremental&#x60;, &#x60;rolling_30d&#x60;. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_connections_usage**
> SeriesListRepFloat get_service_connections_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, connection_type=connection_type, relay_version=relay_version, sdk_name=sdk_name, sdk_version=sdk_version, sdk_type=sdk_type, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)

Get service connections usage

Get a time series array showing the number of service connection minutes from your account. The supported granularity varies by aggregation type. The maximum time range is 365 days.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep_float import SeriesListRepFloat
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. (optional)
    project_key = 'project_key_example' # str | A project key to filter results by. Can be specified multiple times, one query parameter per project key. (optional)
    environment_key = 'environment_key_example' # str | An environment key to filter results by. If specified, exactly one `projectKey` must be provided. Can be specified multiple times, one query parameter per environment key. (optional)
    connection_type = 'connection_type_example' # str | A connection type to filter results by. Can be specified multiple times, one query parameter per connection type. (optional)
    relay_version = 'relay_version_example' # str | A relay version to filter results by. Can be specified multiple times, one query parameter per relay version. (optional)
    sdk_name = 'sdk_name_example' # str | An SDK name to filter results by. Can be specified multiple times, one query parameter per SDK name. (optional)
    sdk_version = 'sdk_version_example' # str | An SDK version to filter results by. Can be specified multiple times, one query parameter per SDK version. (optional)
    sdk_type = 'sdk_type_example' # str | An SDK type to filter results by. Can be specified multiple times, one query parameter per SDK type. (optional)
    group_by = 'group_by_example' # str | If specified, returns data for each distinct value of the given field. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.<br/>Valid values: `projectId`, `environmentId`, `connectionType`, `relayVersion`, `sdkName`, `sdkVersion`, `sdkType`. (optional)
    aggregation_type = 'aggregation_type_example' # str | Specifies the aggregation method. Defaults to `month_to_date`.<br/>Valid values: `month_to_date`, `incremental`. (optional)
    granularity = 'granularity_example' # str | Specifies the data granularity. Defaults to `daily`. `monthly` granularity is only supported with the **month_to_date** aggregation type.<br/>Valid values: `daily`, `hourly`, `monthly`. (optional)

    try:
        # Get service connections usage
        api_response = api_instance.get_service_connections_usage(var_from=var_from, to=to, project_key=project_key, environment_key=environment_key, connection_type=connection_type, relay_version=relay_version, sdk_name=sdk_name, sdk_version=sdk_version, sdk_type=sdk_type, group_by=group_by, aggregation_type=aggregation_type, granularity=granularity)
        print("The response of AccountUsageBetaApi->get_service_connections_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_service_connections_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**| The series of data returned starts from this timestamp (Unix milliseconds). Defaults to the beginning of the current month. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp (Unix milliseconds). Defaults to the current time. | [optional] 
 **project_key** | **str**| A project key to filter results by. Can be specified multiple times, one query parameter per project key. | [optional] 
 **environment_key** | **str**| An environment key to filter results by. If specified, exactly one &#x60;projectKey&#x60; must be provided. Can be specified multiple times, one query parameter per environment key. | [optional] 
 **connection_type** | **str**| A connection type to filter results by. Can be specified multiple times, one query parameter per connection type. | [optional] 
 **relay_version** | **str**| A relay version to filter results by. Can be specified multiple times, one query parameter per relay version. | [optional] 
 **sdk_name** | **str**| An SDK name to filter results by. Can be specified multiple times, one query parameter per SDK name. | [optional] 
 **sdk_version** | **str**| An SDK version to filter results by. Can be specified multiple times, one query parameter per SDK version. | [optional] 
 **sdk_type** | **str**| An SDK type to filter results by. Can be specified multiple times, one query parameter per SDK type. | [optional] 
 **group_by** | **str**| If specified, returns data for each distinct value of the given field. Can be specified multiple times to group data by multiple dimensions, one query parameter per dimension.&lt;br/&gt;Valid values: &#x60;projectId&#x60;, &#x60;environmentId&#x60;, &#x60;connectionType&#x60;, &#x60;relayVersion&#x60;, &#x60;sdkName&#x60;, &#x60;sdkVersion&#x60;, &#x60;sdkType&#x60;. | [optional] 
 **aggregation_type** | **str**| Specifies the aggregation method. Defaults to &#x60;month_to_date&#x60;.&lt;br/&gt;Valid values: &#x60;month_to_date&#x60;, &#x60;incremental&#x60;. | [optional] 
 **granularity** | **str**| Specifies the data granularity. Defaults to &#x60;daily&#x60;. &#x60;monthly&#x60; granularity is only supported with the **month_to_date** aggregation type.&lt;br/&gt;Valid values: &#x60;daily&#x60;, &#x60;hourly&#x60;, &#x60;monthly&#x60;. | [optional] 

### Return type

[**SeriesListRepFloat**](SeriesListRepFloat.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream_usage**
> SeriesListRep get_stream_usage(source, var_from=var_from, to=to, tz=tz)

Get stream usage

Get a time-series array of the number of streaming connections to LaunchDarkly in each time period. The granularity of the data depends on the age of the data requested. If the requested range is within the past two hours, minutely data is returned. If it is within the last two days, hourly data is returned. Otherwise, daily data is returned.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    source = 'source_example' # str | The source of streaming connections to describe. Must be either `client` or `server`.
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp. Defaults to 30 days ago. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp. Defaults to the current time. (optional)
    tz = 'tz_example' # str | The timezone to use for breaks between days when returning daily data. (optional)

    try:
        # Get stream usage
        api_response = api_instance.get_stream_usage(source, var_from=var_from, to=to, tz=tz)
        print("The response of AccountUsageBetaApi->get_stream_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_stream_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source of streaming connections to describe. Must be either &#x60;client&#x60; or &#x60;server&#x60;. | 
 **var_from** | **str**| The series of data returned starts from this timestamp. Defaults to 30 days ago. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp. Defaults to the current time. | [optional] 
 **tz** | **str**| The timezone to use for breaks between days when returning daily data. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream_usage_by_sdk_version**
> SeriesListRep get_stream_usage_by_sdk_version(source, var_from=var_from, to=to, tz=tz, sdk=sdk, version=version)

Get stream usage by SDK version

Get multiple series of the number of streaming connections to LaunchDarkly in each time period, separated by SDK type and version. Information about each series is in the metadata array. The granularity of the data depends on the age of the data requested. If the requested range is within the past 2 hours, minutely data is returned. If it is within the last two days, hourly data is returned. Otherwise, daily data is returned.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.series_list_rep import SeriesListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    source = 'source_example' # str | The source of streaming connections to describe. Must be either `client` or `server`.
    var_from = 'var_from_example' # str | The series of data returned starts from this timestamp. Defaults to 24 hours ago. (optional)
    to = 'to_example' # str | The series of data returned ends at this timestamp. Defaults to the current time. (optional)
    tz = 'tz_example' # str | The timezone to use for breaks between days when returning daily data. (optional)
    sdk = 'sdk_example' # str | If included, this filters the returned series to only those that match this SDK name. (optional)
    version = 'version_example' # str | If included, this filters the returned series to only those that match this SDK version. (optional)

    try:
        # Get stream usage by SDK version
        api_response = api_instance.get_stream_usage_by_sdk_version(source, var_from=var_from, to=to, tz=tz, sdk=sdk, version=version)
        print("The response of AccountUsageBetaApi->get_stream_usage_by_sdk_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_stream_usage_by_sdk_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source of streaming connections to describe. Must be either &#x60;client&#x60; or &#x60;server&#x60;. | 
 **var_from** | **str**| The series of data returned starts from this timestamp. Defaults to 24 hours ago. | [optional] 
 **to** | **str**| The series of data returned ends at this timestamp. Defaults to the current time. | [optional] 
 **tz** | **str**| The timezone to use for breaks between days when returning daily data. | [optional] 
 **sdk** | **str**| If included, this filters the returned series to only those that match this SDK name. | [optional] 
 **version** | **str**| If included, this filters the returned series to only those that match this SDK version. | [optional] 

### Return type

[**SeriesListRep**](SeriesListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream_usage_sdkversion**
> SdkVersionListRep get_stream_usage_sdkversion(source)

Get stream usage SDK versions

Get a list of SDK version objects, which contain an SDK name and version. These are all of the SDKs that have connected to LaunchDarkly from your account in the past 60 days.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.sdk_version_list_rep import SdkVersionListRep
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
    api_instance = launchdarkly_api.AccountUsageBetaApi(api_client)
    source = 'source_example' # str | The source of streaming connections to describe. Must be either `client` or `server`.

    try:
        # Get stream usage SDK versions
        api_response = api_instance.get_stream_usage_sdkversion(source)
        print("The response of AccountUsageBetaApi->get_stream_usage_sdkversion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountUsageBetaApi->get_stream_usage_sdkversion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source of streaming connections to describe. Must be either &#x60;client&#x60; or &#x60;server&#x60;. | 

### Return type

[**SdkVersionListRep**](SdkVersionListRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SDK Versions response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

