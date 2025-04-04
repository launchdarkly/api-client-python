# launchdarkly_api.AccountUsageBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_export_events_usage**](AccountUsageBetaApi.md#get_data_export_events_usage) | **GET** /api/v2/usage/data-export-events | Get data export events usage
[**get_evaluations_usage**](AccountUsageBetaApi.md#get_evaluations_usage) | **GET** /api/v2/usage/evaluations/{projectKey}/{environmentKey}/{featureFlagKey} | Get evaluations usage
[**get_events_usage**](AccountUsageBetaApi.md#get_events_usage) | **GET** /api/v2/usage/events/{type} | Get events usage
[**get_experimentation_keys_usage**](AccountUsageBetaApi.md#get_experimentation_keys_usage) | **GET** /api/v2/usage/experimentation-keys | Get experimentation keys usage
[**get_experimentation_units_usage**](AccountUsageBetaApi.md#get_experimentation_units_usage) | **GET** /api/v2/usage/experimentation-units | Get experimentation units usage
[**get_mau_sdks_by_type**](AccountUsageBetaApi.md#get_mau_sdks_by_type) | **GET** /api/v2/usage/mau/sdks | Get MAU SDKs by type
[**get_mau_usage**](AccountUsageBetaApi.md#get_mau_usage) | **GET** /api/v2/usage/mau | Get MAU usage
[**get_mau_usage_by_category**](AccountUsageBetaApi.md#get_mau_usage_by_category) | **GET** /api/v2/usage/mau/bycategory | Get MAU usage by category
[**get_service_connection_usage**](AccountUsageBetaApi.md#get_service_connection_usage) | **GET** /api/v2/usage/service-connections | Get service connection usage
[**get_stream_usage**](AccountUsageBetaApi.md#get_stream_usage) | **GET** /api/v2/usage/streams/{source} | Get stream usage
[**get_stream_usage_by_sdk_version**](AccountUsageBetaApi.md#get_stream_usage_by_sdk_version) | **GET** /api/v2/usage/streams/{source}/bysdkversion | Get stream usage by SDK version
[**get_stream_usage_sdkversion**](AccountUsageBetaApi.md#get_stream_usage_sdkversion) | **GET** /api/v2/usage/streams/{source}/sdkversions | Get stream usage SDK versions


# **get_data_export_events_usage**
> SeriesIntervalsRep get_data_export_events_usage()

Get data export events usage

Get a time-series array of the number of monthly data export events from your account. The granularity is always daily, with a maximum of 31 days.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import account_usage_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.status_service_unavailable import StatusServiceUnavailable
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.series_intervals_rep import SeriesIntervalsRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = account_usage_beta_api.AccountUsageBetaApi(api_client)
    _from = "from_example" # str | The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. (optional)
    to = "to_example" # str | The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. (optional)
    project_key = "projectKey_example" # str | A project key. If specified, `environmentKey` is required and results apply to the corresponding environment in this project. (optional)
    environment_key = "environmentKey_example" # str | An environment key. If specified, `projectKey` is required and results apply to the corresponding environment in this project. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data export events usage
        api_response = api_instance.get_data_export_events_usage(_from=_from, to=to, project_key=project_key, environment_key=environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountUsageBetaApi->get_data_export_events_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. | [optional]
 **to** | **str**| The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. | [optional]
 **project_key** | **str**| A project key. If specified, &#x60;environmentKey&#x60; is required and results apply to the corresponding environment in this project. | [optional]
 **environment_key** | **str**| An environment key. If specified, &#x60;projectKey&#x60; is required and results apply to the corresponding environment in this project. | [optional]

### Return type

[**SeriesIntervalsRep**](SeriesIntervalsRep.md)

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
> SeriesListRep get_evaluations_usage(project_key, environment_key, feature_flag_key)

Get evaluations usage

Get time-series arrays of the number of times a flag is evaluated, broken down by the variation that resulted from that evaluation. The granularity of the data depends on the age of the data requested. If the requested range is within the past two hours, minutely data is returned. If it is within the last two days, hourly data is returned. Otherwise, daily data is returned.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import account_usage_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.series_list_rep import SeriesListRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = account_usage_beta_api.AccountUsageBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    _from = "from_example" # str | The series of data returned starts from this timestamp. Defaults to 30 days ago. (optional)
    to = "to_example" # str | The series of data returned ends at this timestamp. Defaults to the current time. (optional)
    tz = "tz_example" # str | The timezone to use for breaks between days when returning daily data. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get evaluations usage
        api_response = api_instance.get_evaluations_usage(project_key, environment_key, feature_flag_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountUsageBetaApi->get_evaluations_usage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get evaluations usage
        api_response = api_instance.get_evaluations_usage(project_key, environment_key, feature_flag_key, _from=_from, to=to, tz=tz)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountUsageBetaApi->get_evaluations_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **feature_flag_key** | **str**| The feature flag key |
 **_from** | **str**| The series of data returned starts from this timestamp. Defaults to 30 days ago. | [optional]
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
> SeriesListRep get_events_usage(type)

Get events usage

Get time-series arrays of the number of times a flag is evaluated, broken down by the variation that resulted from that evaluation. The granularity of the data depends on the age of the data requested. If the requested range is within the past two hours, minutely data is returned. If it is within the last two days, hourly data is returned. Otherwise, daily data is returned.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import account_usage_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.series_list_rep import SeriesListRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = account_usage_beta_api.AccountUsageBetaApi(api_client)
    type = "type_example" # str | The type of event to retrieve. Must be either `received` or `published`.
    _from = "from_example" # str | The series of data returned starts from this timestamp. Defaults to 24 hours ago. (optional)
    to = "to_example" # str | The series of data returned ends at this timestamp. Defaults to the current time. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get events usage
        api_response = api_instance.get_events_usage(type)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountUsageBetaApi->get_events_usage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get events usage
        api_response = api_instance.get_events_usage(type, _from=_from, to=to)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountUsageBetaApi->get_events_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of event to retrieve. Must be either &#x60;received&#x60; or &#x60;published&#x60;. |
 **_from** | **str**| The series of data returned starts from this timestamp. Defaults to 24 hours ago. | [optional]
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

# **get_experimentation_keys_usage**
> SeriesIntervalsRep get_experimentation_keys_usage()

Get experimentation keys usage

Get a time-series array of the number of monthly experimentation keys from your account. The granularity is always daily, with a maximum of 31 days.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import account_usage_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.status_service_unavailable import StatusServiceUnavailable
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.series_intervals_rep import SeriesIntervalsRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = account_usage_beta_api.AccountUsageBetaApi(api_client)
    _from = "from_example" # str | The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. (optional)
    to = "to_example" # str | The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. (optional)
    project_key = "projectKey_example" # str | A project key. If specified, `environmentKey` is required and results apply to the corresponding environment in this project. (optional)
    environment_key = "environmentKey_example" # str | An environment key. If specified, `projectKey` is required and results apply to the corresponding environment in this project. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get experimentation keys usage
        api_response = api_instance.get_experimentation_keys_usage(_from=_from, to=to, project_key=project_key, environment_key=environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountUsageBetaApi->get_experimentation_keys_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. | [optional]
 **to** | **str**| The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. | [optional]
 **project_key** | **str**| A project key. If specified, &#x60;environmentKey&#x60; is required and results apply to the corresponding environment in this project. | [optional]
 **environment_key** | **str**| An environment key. If specified, &#x60;projectKey&#x60; is required and results apply to the corresponding environment in this project. | [optional]

### Return type

[**SeriesIntervalsRep**](SeriesIntervalsRep.md)

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

# **get_experimentation_units_usage**
> SeriesIntervalsRep get_experimentation_units_usage()

Get experimentation units usage

Get a time-series array of the number of monthly experimentation units from your account. The granularity is always daily, with a maximum of 31 days.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import account_usage_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.status_service_unavailable import StatusServiceUnavailable
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.series_intervals_rep import SeriesIntervalsRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = account_usage_beta_api.AccountUsageBetaApi(api_client)
    _from = "from_example" # str | The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. (optional)
    to = "to_example" # str | The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. (optional)
    project_key = "projectKey_example" # str | A project key. If specified, `environmentKey` is required and results apply to the corresponding environment in this project. (optional)
    environment_key = "environmentKey_example" # str | An environment key. If specified, `projectKey` is required and results apply to the corresponding environment in this project. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get experimentation units usage
        api_response = api_instance.get_experimentation_units_usage(_from=_from, to=to, project_key=project_key, environment_key=environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountUsageBetaApi->get_experimentation_units_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. | [optional]
 **to** | **str**| The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. | [optional]
 **project_key** | **str**| A project key. If specified, &#x60;environmentKey&#x60; is required and results apply to the corresponding environment in this project. | [optional]
 **environment_key** | **str**| An environment key. If specified, &#x60;projectKey&#x60; is required and results apply to the corresponding environment in this project. | [optional]

### Return type

[**SeriesIntervalsRep**](SeriesIntervalsRep.md)

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
> SdkListRep get_mau_sdks_by_type()

Get MAU SDKs by type

Get a list of SDKs. These are all of the SDKs that have connected to LaunchDarkly by monthly active users (MAU) in the requested time period.<br/><br/>Endpoints for retrieving monthly active users (MAU) do not return information about active context instances. After you have upgraded your LaunchDarkly SDK to use contexts instead of users, you should not rely on this endpoint. To learn more, read [Account usage metrics](https://launchdarkly.com/docs/home/account/metrics).

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import account_usage_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.sdk_list_rep import SdkListRep
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
    api_instance = account_usage_beta_api.AccountUsageBetaApi(api_client)
    _from = "from_example" # str | The data returned starts from this timestamp. Defaults to seven days ago. The timestamp is in Unix milliseconds, for example, 1656694800000. (optional)
    to = "to_example" # str | The data returned ends at this timestamp. Defaults to the current time. The timestamp is in Unix milliseconds, for example, 1657904400000. (optional)
    sdktype = "sdktype_example" # str | The type of SDK with monthly active users (MAU) to list. Must be either `client` or `server`. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get MAU SDKs by type
        api_response = api_instance.get_mau_sdks_by_type(_from=_from, to=to, sdktype=sdktype)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountUsageBetaApi->get_mau_sdks_by_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| The data returned starts from this timestamp. Defaults to seven days ago. The timestamp is in Unix milliseconds, for example, 1656694800000. | [optional]
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

# **get_mau_usage**
> SeriesListRep get_mau_usage()

Get MAU usage

Get a time-series array of the number of monthly active users (MAU) seen by LaunchDarkly from your account. The granularity is always daily.<br/><br/>Endpoints for retrieving monthly active users (MAU) do not return information about active context instances. After you have upgraded your LaunchDarkly SDK to use contexts instead of users, you should not rely on this endpoint. To learn more, read [Account usage metrics](https://launchdarkly.com/docs/home/account/metrics).

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import account_usage_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.series_list_rep import SeriesListRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = account_usage_beta_api.AccountUsageBetaApi(api_client)
    _from = "from_example" # str | The series of data returned starts from this timestamp. Defaults to 30 days ago. (optional)
    to = "to_example" # str | The series of data returned ends at this timestamp. Defaults to the current time. (optional)
    project = "project_example" # str | A project key to filter results to. Can be specified multiple times, one query parameter per project key, to view data for multiple projects. (optional)
    environment = "environment_example" # str | An environment key to filter results to. When using this parameter, exactly one project key must also be set. Can be specified multiple times as separate query parameters to view data for multiple environments within a single project. (optional)
    sdktype = "sdktype_example" # str | An SDK type to filter results to. Can be specified multiple times, one query parameter per SDK type. Valid values: client, server (optional)
    sdk = "sdk_example" # str | An SDK name to filter results to. Can be specified multiple times, one query parameter per SDK. (optional)
    anonymous = "anonymous_example" # str | If specified, filters results to either anonymous or nonanonymous users. (optional)
    groupby = "groupby_example" # str | If specified, returns data for each distinct value of the given field. Can be specified multiple times to group data by multiple dimensions (for example, to group by both project and SDK). Valid values: project, environment, sdktype, sdk, anonymous, contextKind, sdkAppId (optional)
    aggregation_type = "aggregationType_example" # str | If specified, queries for rolling 30-day, month-to-date, or daily incremental counts. Default is rolling 30-day. Valid values: rolling_30d, month_to_date, daily_incremental (optional)
    context_kind = "contextKind_example" # str | Filters results to the specified context kinds. Can be specified multiple times, one query parameter per context kind. If not set, queries for the user context kind. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get MAU usage
        api_response = api_instance.get_mau_usage(_from=_from, to=to, project=project, environment=environment, sdktype=sdktype, sdk=sdk, anonymous=anonymous, groupby=groupby, aggregation_type=aggregation_type, context_kind=context_kind)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountUsageBetaApi->get_mau_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| The series of data returned starts from this timestamp. Defaults to 30 days ago. | [optional]
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
> SeriesListRep get_mau_usage_by_category()

Get MAU usage by category

Get time-series arrays of the number of monthly active users (MAU) seen by LaunchDarkly from your account, broken down by the category of users. The category is either `browser`, `mobile`, or `backend`.<br/><br/>Endpoints for retrieving monthly active users (MAU) do not return information about active context instances. After you have upgraded your LaunchDarkly SDK to use contexts instead of users, you should not rely on this endpoint. To learn more, read [Account usage metrics](https://launchdarkly.com/docs/home/account/metrics).

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import account_usage_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.series_list_rep import SeriesListRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = account_usage_beta_api.AccountUsageBetaApi(api_client)
    _from = "from_example" # str | The series of data returned starts from this timestamp. Defaults to 30 days ago. (optional)
    to = "to_example" # str | The series of data returned ends at this timestamp. Defaults to the current time. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get MAU usage by category
        api_response = api_instance.get_mau_usage_by_category(_from=_from, to=to)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountUsageBetaApi->get_mau_usage_by_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| The series of data returned starts from this timestamp. Defaults to 30 days ago. | [optional]
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

# **get_service_connection_usage**
> SeriesIntervalsRep get_service_connection_usage()

Get service connection usage

Get a time-series array of the number of monthly service connections from your account. The granularity is always daily, with a maximum of 31 days.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import account_usage_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.status_service_unavailable import StatusServiceUnavailable
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.series_intervals_rep import SeriesIntervalsRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = account_usage_beta_api.AccountUsageBetaApi(api_client)
    _from = "from_example" # str | The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. (optional)
    to = "to_example" # str | The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. (optional)
    project_key = "projectKey_example" # str | A project key. If specified, `environmentKey` is required and results apply to the corresponding environment in this project. (optional)
    environment_key = "environmentKey_example" # str | An environment key. If specified, `projectKey` is required and results apply to the corresponding environment in this project. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get service connection usage
        api_response = api_instance.get_service_connection_usage(_from=_from, to=to, project_key=project_key, environment_key=environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountUsageBetaApi->get_service_connection_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| The series of data returned starts from this timestamp (Unix seconds). Defaults to the beginning of the current month. | [optional]
 **to** | **str**| The series of data returned ends at this timestamp (Unix seconds). Defaults to the current time. | [optional]
 **project_key** | **str**| A project key. If specified, &#x60;environmentKey&#x60; is required and results apply to the corresponding environment in this project. | [optional]
 **environment_key** | **str**| An environment key. If specified, &#x60;projectKey&#x60; is required and results apply to the corresponding environment in this project. | [optional]

### Return type

[**SeriesIntervalsRep**](SeriesIntervalsRep.md)

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
> SeriesListRep get_stream_usage(source)

Get stream usage

Get a time-series array of the number of streaming connections to LaunchDarkly in each time period. The granularity of the data depends on the age of the data requested. If the requested range is within the past two hours, minutely data is returned. If it is within the last two days, hourly data is returned. Otherwise, daily data is returned.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import account_usage_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.series_list_rep import SeriesListRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = account_usage_beta_api.AccountUsageBetaApi(api_client)
    source = "source_example" # str | The source of streaming connections to describe. Must be either `client` or `server`.
    _from = "from_example" # str | The series of data returned starts from this timestamp. Defaults to 30 days ago. (optional)
    to = "to_example" # str | The series of data returned ends at this timestamp. Defaults to the current time. (optional)
    tz = "tz_example" # str | The timezone to use for breaks between days when returning daily data. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get stream usage
        api_response = api_instance.get_stream_usage(source)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountUsageBetaApi->get_stream_usage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get stream usage
        api_response = api_instance.get_stream_usage(source, _from=_from, to=to, tz=tz)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountUsageBetaApi->get_stream_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source of streaming connections to describe. Must be either &#x60;client&#x60; or &#x60;server&#x60;. |
 **_from** | **str**| The series of data returned starts from this timestamp. Defaults to 30 days ago. | [optional]
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
> SeriesListRep get_stream_usage_by_sdk_version(source)

Get stream usage by SDK version

Get multiple series of the number of streaming connections to LaunchDarkly in each time period, separated by SDK type and version. Information about each series is in the metadata array. The granularity of the data depends on the age of the data requested. If the requested range is within the past 2 hours, minutely data is returned. If it is within the last two days, hourly data is returned. Otherwise, daily data is returned.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import account_usage_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.series_list_rep import SeriesListRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = account_usage_beta_api.AccountUsageBetaApi(api_client)
    source = "source_example" # str | The source of streaming connections to describe. Must be either `client` or `server`.
    _from = "from_example" # str | The series of data returned starts from this timestamp. Defaults to 24 hours ago. (optional)
    to = "to_example" # str | The series of data returned ends at this timestamp. Defaults to the current time. (optional)
    tz = "tz_example" # str | The timezone to use for breaks between days when returning daily data. (optional)
    sdk = "sdk_example" # str | If included, this filters the returned series to only those that match this SDK name. (optional)
    version = "version_example" # str | If included, this filters the returned series to only those that match this SDK version. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get stream usage by SDK version
        api_response = api_instance.get_stream_usage_by_sdk_version(source)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountUsageBetaApi->get_stream_usage_by_sdk_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get stream usage by SDK version
        api_response = api_instance.get_stream_usage_by_sdk_version(source, _from=_from, to=to, tz=tz, sdk=sdk, version=version)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling AccountUsageBetaApi->get_stream_usage_by_sdk_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source of streaming connections to describe. Must be either &#x60;client&#x60; or &#x60;server&#x60;. |
 **_from** | **str**| The series of data returned starts from this timestamp. Defaults to 24 hours ago. | [optional]
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
import time
import launchdarkly_api
from launchdarkly_api.api import account_usage_beta_api
from launchdarkly_api.model.sdk_version_list_rep import SdkVersionListRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = account_usage_beta_api.AccountUsageBetaApi(api_client)
    source = "source_example" # str | The source of streaming connections to describe. Must be either `client` or `server`.

    # example passing only required values which don't have defaults set
    try:
        # Get stream usage SDK versions
        api_response = api_instance.get_stream_usage_sdkversion(source)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
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

