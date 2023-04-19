# launchdarkly_api.ExperimentsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_experiment**](ExperimentsBetaApi.md#create_experiment) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments | Create experiment
[**create_iteration**](ExperimentsBetaApi.md#create_iteration) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey}/iterations | Create iteration
[**get_experiment**](ExperimentsBetaApi.md#get_experiment) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey} | Get experiment
[**get_experiment_results**](ExperimentsBetaApi.md#get_experiment_results) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey}/metrics/{metricKey}/results | Get experiment results
[**get_experimentation_settings**](ExperimentsBetaApi.md#get_experimentation_settings) | **GET** /api/v2/projects/{projectKey}/experimentation-settings | Get experimentation settings
[**get_experiments**](ExperimentsBetaApi.md#get_experiments) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments | Get experiments
[**get_legacy_experiment_results**](ExperimentsBetaApi.md#get_legacy_experiment_results) | **GET** /api/v2/flags/{projectKey}/{featureFlagKey}/experiments/{environmentKey}/{metricKey} | Get legacy experiment results (deprecated)
[**patch_experiment**](ExperimentsBetaApi.md#patch_experiment) | **PATCH** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey} | Patch experiment
[**put_experimentation_settings**](ExperimentsBetaApi.md#put_experimentation_settings) | **PUT** /api/v2/projects/{projectKey}/experimentation-settings | Update experimentation settings
[**reset_experiment**](ExperimentsBetaApi.md#reset_experiment) | **DELETE** /api/v2/flags/{projectKey}/{featureFlagKey}/experiments/{environmentKey}/{metricKey}/results | Reset experiment results


# **create_experiment**
> Experiment create_experiment(project_key, environment_key, experiment_post)

Create experiment

Create an experiment.  To run this experiment, you'll need to [create an iteration](/tag/Experiments-(beta)#operation/createIteration) and then [update the experiment](/tag/Experiments-(beta)#operation/patchExperiment) with the `startIteration` instruction.  To learn more, read [Creating experiments](https://docs.launchdarkly.com/home/creating-experiments). 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import experiments_beta_api
from launchdarkly_api.model.experiment import Experiment
from launchdarkly_api.model.experiment_post import ExperimentPost
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
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
    api_instance = experiments_beta_api.ExperimentsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    experiment_post = ExperimentPost(
        name="Example experiment",
        description="An example experiment, used in testing",
        maintainer_id="12ab3c45de678910fgh12345",
        key="experiment-key-123abc",
        iteration=IterationInput(
            hypothesis="Example hypothesis, the new button placement will increase conversion",
            can_reshuffle_traffic=True,
            metrics=MetricsInput([
                MetricInput(
                    key="metric-key-123abc",
                    primary=True,
                ),
            ]),
            treatments=TreatmentsInput([
                TreatmentInput(
                    name="Treatment 1",
                    baseline=True,
                    allocation_percent="10",
                    parameters=[
                        TreatmentParameterInput(
                            flag_key="example-flag-for-experiment",
                            variation_id="e432f62b-55f6-49dd-a02f-eb24acf39d05",
                        ),
                    ],
                ),
            ]),
            flags=FlagsInput(
                key=FlagInput(
                    rule_id="e432f62b-55f6-49dd-a02f-eb24acf39d05",
                    flag_config_version=12,
                ),
            ),
            randomization_unit="user",
        ),
    ) # ExperimentPost | 

    # example passing only required values which don't have defaults set
    try:
        # Create experiment
        api_response = api_instance.create_experiment(project_key, environment_key, experiment_post)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->create_experiment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **experiment_post** | [**ExperimentPost**](ExperimentPost.md)|  |

### Return type

[**Experiment**](Experiment.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Experiment response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iteration**
> IterationRep create_iteration(project_key, environment_key, experiment_key, iteration_input)

Create iteration

Create an experiment iteration.  Experiment iterations let you record experiments in individual blocks of time. Initially, iterations are created with a status of `not_started` and appear in the `draftIteration` field of an experiment. To start or stop an iteration, [update the experiment](/tag/Experiments-(beta)#operation/patchExperiment) with the `startIteration` or `stopIteration` instruction.   To learn more, read [Starting experiment iterations](https://docs.launchdarkly.com/home/creating-experiments#starting-experiment-iterations). 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import experiments_beta_api
from launchdarkly_api.model.iteration_rep import IterationRep
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.iteration_input import IterationInput
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
    api_instance = experiments_beta_api.ExperimentsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    experiment_key = "experimentKey_example" # str | The experiment key
    iteration_input = IterationInput(
        hypothesis="Example hypothesis, the new button placement will increase conversion",
        can_reshuffle_traffic=True,
        metrics=MetricsInput([
            MetricInput(
                key="metric-key-123abc",
                primary=True,
            ),
        ]),
        treatments=TreatmentsInput([
            TreatmentInput(
                name="Treatment 1",
                baseline=True,
                allocation_percent="10",
                parameters=[
                    TreatmentParameterInput(
                        flag_key="example-flag-for-experiment",
                        variation_id="e432f62b-55f6-49dd-a02f-eb24acf39d05",
                    ),
                ],
            ),
        ]),
        flags=FlagsInput(
            key=FlagInput(
                rule_id="e432f62b-55f6-49dd-a02f-eb24acf39d05",
                flag_config_version=12,
            ),
        ),
        randomization_unit="user",
    ) # IterationInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create iteration
        api_response = api_instance.create_iteration(project_key, environment_key, experiment_key, iteration_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->create_iteration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **experiment_key** | **str**| The experiment key |
 **iteration_input** | [**IterationInput**](IterationInput.md)|  |

### Return type

[**IterationRep**](IterationRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Iteration response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiment**
> Experiment get_experiment(project_key, environment_key, experiment_key)

Get experiment

Get details about an experiment.  ### Expanding the experiment response  LaunchDarkly supports four fields for expanding the \"Get experiment\" response. By default, these fields are **not** included in the response.  To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:  - `previousIterations` includes all iterations prior to the current iteration. By default only the current iteration is included in the response. - `draftIteration` includes the iteration which has not been started yet, if any. - `secondaryMetrics` includes secondary metrics. By default only the primary metric is included in the response. - `treatments` includes all treatment and parameter details. By default treatment data is not included in the response.  For example, `expand=draftIteration,treatments` includes the `draftIteration` and `treatments` fields in the response. If fields that you request with the `expand` query parameter are empty, they are not included in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import experiments_beta_api
from launchdarkly_api.model.experiment import Experiment
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
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
    api_instance = experiments_beta_api.ExperimentsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    experiment_key = "experimentKey_example" # str | The experiment key

    # example passing only required values which don't have defaults set
    try:
        # Get experiment
        api_response = api_instance.get_experiment(project_key, environment_key, experiment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->get_experiment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **experiment_key** | **str**| The experiment key |

### Return type

[**Experiment**](Experiment.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Experiment response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiment_results**
> ExperimentBayesianResultsRep get_experiment_results(project_key, environment_key, experiment_key, metric_key)

Get experiment results

Get results from an experiment for a particular metric.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import experiments_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.experiment_bayesian_results_rep import ExperimentBayesianResultsRep
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
    api_instance = experiments_beta_api.ExperimentsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    experiment_key = "experimentKey_example" # str | The experiment key
    metric_key = "metricKey_example" # str | The metric key

    # example passing only required values which don't have defaults set
    try:
        # Get experiment results
        api_response = api_instance.get_experiment_results(project_key, environment_key, experiment_key, metric_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->get_experiment_results: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **experiment_key** | **str**| The experiment key |
 **metric_key** | **str**| The metric key |

### Return type

[**ExperimentBayesianResultsRep**](ExperimentBayesianResultsRep.md)

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

# **get_experimentation_settings**
> ExperimentationSettingsRep get_experimentation_settings(project_key)

Get experimentation settings

Get current experimentation settings for the given project

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import experiments_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.experimentation_settings_rep import ExperimentationSettingsRep
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
    api_instance = experiments_beta_api.ExperimentsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key

    # example passing only required values which don't have defaults set
    try:
        # Get experimentation settings
        api_response = api_instance.get_experimentation_settings(project_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->get_experimentation_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |

### Return type

[**ExperimentationSettingsRep**](ExperimentationSettingsRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Experimentation settings response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiments**
> ExperimentCollectionRep get_experiments(project_key, environment_key)

Get experiments

Get details about all experiments in an environment.  ### Filtering experiments  LaunchDarkly supports the `filter` query param for filtering, with the following fields:  - `flagKey` filters for only experiments that use the flag with the given key. - `metricKey` filters for only experiments that use the metric with the given key. - `status` filters for only experiments with an iteration with the given status. An iteration can have the status `not_started`, `running` or `stopped`.  For example, `filter=flagKey:my-flag,status:running,metricKey:page-load-ms` filters for experiments for the given flag key and the given metric key which have a currently running iteration.  ### Expanding the experiments response  LaunchDarkly supports four fields for expanding the \"Get experiments\" response. By default, these fields are **not** included in the response.  To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:  - `previousIterations` includes all iterations prior to the current iteration. By default only the current iteration is included in the response. - `draftIteration` includes the iteration which has not been started yet, if any. - `secondaryMetrics` includes secondary metrics. By default only the primary metric is included in the response. - `treatments` includes all treatment and parameter details. By default treatment data is not included in the response.  For example, `expand=draftIteration,treatments` includes the `draftIteration` and `treatments` fields in the response. If fields that you request with the `expand` query parameter are empty, they are not included in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import experiments_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.experiment_collection_rep import ExperimentCollectionRep
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
    api_instance = experiments_beta_api.ExperimentsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    limit = 1 # int | The maximum number of experiments to return. Defaults to 20. (optional)
    offset = 1 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = "filter_example" # str | A comma-separated list of filters. Each filter is of the form `field:value`. Supported fields are explained above. (optional)
    expand = "expand_example" # str | A comma-separated list of properties that can reveal additional information in the response. Supported fields are explained above. (optional)
    lifecycle_state = "lifecycleState_example" # str | A comma-separated list of experiment archived states. Supports `archived`, `active`, or both. Defaults to `active` experiments. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get experiments
        api_response = api_instance.get_experiments(project_key, environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->get_experiments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get experiments
        api_response = api_instance.get_experiments(project_key, environment_key, limit=limit, offset=offset, filter=filter, expand=expand, lifecycle_state=lifecycle_state)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->get_experiments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **limit** | **int**| The maximum number of experiments to return. Defaults to 20. | [optional]
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional]
 **filter** | **str**| A comma-separated list of filters. Each filter is of the form &#x60;field:value&#x60;. Supported fields are explained above. | [optional]
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. Supported fields are explained above. | [optional]
 **lifecycle_state** | **str**| A comma-separated list of experiment archived states. Supports &#x60;archived&#x60;, &#x60;active&#x60;, or both. Defaults to &#x60;active&#x60; experiments. | [optional]

### Return type

[**ExperimentCollectionRep**](ExperimentCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Experiment collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legacy_experiment_results**
> ExperimentResults get_legacy_experiment_results(project_key, feature_flag_key, environment_key, metric_key)

Get legacy experiment results (deprecated)

Get detailed experiment result data for legacy experiments.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import experiments_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.experiment_results import ExperimentResults
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
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
    api_instance = experiments_beta_api.ExperimentsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    metric_key = "metricKey_example" # str | The metric key
    _from = 1 # int | A timestamp denoting the start of the data collection period, expressed as a Unix epoch time in milliseconds. (optional)
    to = 1 # int | A timestamp denoting the end of the data collection period, expressed as a Unix epoch time in milliseconds. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get legacy experiment results (deprecated)
        api_response = api_instance.get_legacy_experiment_results(project_key, feature_flag_key, environment_key, metric_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->get_legacy_experiment_results: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get legacy experiment results (deprecated)
        api_response = api_instance.get_legacy_experiment_results(project_key, feature_flag_key, environment_key, metric_key, _from=_from, to=to)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->get_legacy_experiment_results: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **environment_key** | **str**| The environment key |
 **metric_key** | **str**| The metric key |
 **_from** | **int**| A timestamp denoting the start of the data collection period, expressed as a Unix epoch time in milliseconds. | [optional]
 **to** | **int**| A timestamp denoting the end of the data collection period, expressed as a Unix epoch time in milliseconds. | [optional]

### Return type

[**ExperimentResults**](ExperimentResults.md)

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

# **patch_experiment**
> Experiment patch_experiment(project_key, environment_key, experiment_key, experiment_patch_input)

Patch experiment

Update an experiment. Updating an experiment uses the semantic patch format.  To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](/reference#updates-using-semantic-patch).  ### Instructions  Semantic patch requests support the following `kind` instructions for updating experiments.  #### updateName  Updates the experiment name.  ##### Parameters  - `value`: The new name.  #### updateDescription  Updates the experiment description.  ##### Parameters  - `value`: The new description.  #### startIteration  Starts a new iteration for this experiment. You must [create a new iteration](/tag/Experiments-(beta)#operation/createIteration) before calling this instruction.  An iteration may not be started until it meets the following criteria:  * Its associated flag is toggled on and is not archived * Its `randomizationUnit` is set * At least one of its `treatments` has a non-zero `allocationPercent`  ##### Parameters  - `changeJustification`: The reason for starting a new iteration. Required when you call `startIteration` on an already running experiment, otherwise optional.  #### stopIteration  Stops the current iteration for this experiment.  ##### Parameters  - `winningTreatmentId`: The ID of the winning treatment - `winningReason`: The reason for the winner  #### archiveExperiment  Archives this experiment. Archived experiments are hidden by default in the LaunchDarkly user interface. You cannot start new iterations for archived experiments.  #### restoreExperiment  Restores an archived experiment. After restoring an experiment, you can start new iterations for it again. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import experiments_beta_api
from launchdarkly_api.model.experiment import Experiment
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.experiment_patch_input import ExperimentPatchInput
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
    api_instance = experiments_beta_api.ExperimentsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    experiment_key = "experimentKey_example" # str | The experiment key
    experiment_patch_input = ExperimentPatchInput(
        comment="Optional comment",
        instructions=Instructions([
            Instruction(
                key=None,
            ),
        ]),
    ) # ExperimentPatchInput | 

    # example passing only required values which don't have defaults set
    try:
        # Patch experiment
        api_response = api_instance.patch_experiment(project_key, environment_key, experiment_key, experiment_patch_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->patch_experiment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **experiment_key** | **str**| The experiment key |
 **experiment_patch_input** | [**ExperimentPatchInput**](ExperimentPatchInput.md)|  |

### Return type

[**Experiment**](Experiment.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Experiment response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_experimentation_settings**
> ExperimentationSettingsRep put_experimentation_settings(project_key, experimentation_settings_put)

Update experimentation settings

Update experimentation settings for the given project

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import experiments_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.experimentation_settings_put import ExperimentationSettingsPut
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.experimentation_settings_rep import ExperimentationSettingsRep
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
    api_instance = experiments_beta_api.ExperimentsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    experimentation_settings_put = ExperimentationSettingsPut(
        randomization_units=[
            RandomizationUnitInput(
                randomization_unit="user",
                default=True,
                standard_randomization_unit="guest",
            ),
        ],
    ) # ExperimentationSettingsPut | 

    # example passing only required values which don't have defaults set
    try:
        # Update experimentation settings
        api_response = api_instance.put_experimentation_settings(project_key, experimentation_settings_put)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->put_experimentation_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **experimentation_settings_put** | [**ExperimentationSettingsPut**](ExperimentationSettingsPut.md)|  |

### Return type

[**ExperimentationSettingsRep**](ExperimentationSettingsRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Experimentation settings response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_experiment**
> reset_experiment(project_key, feature_flag_key, environment_key, metric_key)

Reset experiment results

Reset all experiment results by deleting all existing data for an experiment.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import experiments_beta_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
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
    api_instance = experiments_beta_api.ExperimentsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    metric_key = "metricKey_example" # str | The metric's key

    # example passing only required values which don't have defaults set
    try:
        # Reset experiment results
        api_instance.reset_experiment(project_key, feature_flag_key, environment_key, metric_key)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->reset_experiment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **environment_key** | **str**| The environment key |
 **metric_key** | **str**| The metric&#39;s key |

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
**204** | Experiment results reset successfully |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

