# launchdarkly_api.ExperimentsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_experiment**](ExperimentsBetaApi.md#get_experiment) | **GET** /api/v2/flags/{projKey}/{flagKey}/experiments/{envKey}/{metricKey} | Get experiment results
[**reset_experiment**](ExperimentsBetaApi.md#reset_experiment) | **DELETE** /api/v2/flags/{projKey}/{flagKey}/experiments/{envKey}/{metricKey}/results | Reset experiment results


# **get_experiment**
> ExperimentResultsRep get_experiment(proj_key, flag_key, env_key, metric_key)

Get experiment results

Get detailed experiment result data

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import experiments__beta_api
from launchdarkly_api.model.experiment_results_rep import ExperimentResultsRep
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
    api_instance = experiments__beta_api.ExperimentsBetaApi(api_client)
    proj_key = "projKey_example" # str | The project key
    flag_key = "flagKey_example" # str | The flag key
    env_key = "envKey_example" # str | The environment key
    metric_key = "metricKey_example" # str | The metric key
    _from = 1 # int | A timestamp denoting the start of the data collection period, expressed as a Unix epoch time in milliseconds. (optional)
    to = 1 # int | A timestamp denoting the end of the data collection period, expressed as a Unix epoch time in milliseconds. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get experiment results
        api_response = api_instance.get_experiment(proj_key, flag_key, env_key, metric_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->get_experiment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get experiment results
        api_response = api_instance.get_experiment(proj_key, flag_key, env_key, metric_key, _from=_from, to=to)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->get_experiment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **flag_key** | **str**| The flag key |
 **env_key** | **str**| The environment key |
 **metric_key** | **str**| The metric key |
 **_from** | **int**| A timestamp denoting the start of the data collection period, expressed as a Unix epoch time in milliseconds. | [optional]
 **to** | **int**| A timestamp denoting the end of the data collection period, expressed as a Unix epoch time in milliseconds. | [optional]

### Return type

[**ExperimentResultsRep**](ExperimentResultsRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Experiment results response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_experiment**
> reset_experiment(proj_key, flag_key, env_key, metric_key)

Reset experiment results

Reset all experiment results by deleting all existing data for an experiment

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import experiments__beta_api
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
    api_instance = experiments__beta_api.ExperimentsBetaApi(api_client)
    proj_key = "projKey_example" # str | The project key
    flag_key = "flagKey_example" # str | The feature flag's key
    env_key = "envKey_example" # str | The environment key
    metric_key = "metricKey_example" # str | The metric's key

    # example passing only required values which don't have defaults set
    try:
        # Reset experiment results
        api_instance.reset_experiment(proj_key, flag_key, env_key, metric_key)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->reset_experiment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **flag_key** | **str**| The feature flag&#39;s key |
 **env_key** | **str**| The environment key |
 **metric_key** | **str**| The metric&#39;s key |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Experiment results reset successfully |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Unknown project, flag, environment or metric key |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

