# launchdarkly_api.ExperimentsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_experiment**](ExperimentsBetaApi.md#create_experiment) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments | Create experiment
[**create_iteration**](ExperimentsBetaApi.md#create_iteration) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey}/iterations | Create iteration
[**get_experiment**](ExperimentsBetaApi.md#get_experiment) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey} | Get experiment
[**get_experiment_results**](ExperimentsBetaApi.md#get_experiment_results) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey}/metrics/{metricKey}/results | Get experiment results
[**get_experiments**](ExperimentsBetaApi.md#get_experiments) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments | Get experiments
[**get_legacy_experiment_results**](ExperimentsBetaApi.md#get_legacy_experiment_results) | **GET** /api/v2/flags/{projectKey}/{featureFlagKey}/experiments/{environmentKey}/{metricKey} | Get legacy experiment results (deprecated)
[**patch_experiment**](ExperimentsBetaApi.md#patch_experiment) | **PATCH** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey} | Patch experiment
[**reset_experiment**](ExperimentsBetaApi.md#reset_experiment) | **DELETE** /api/v2/flags/{projectKey}/{featureFlagKey}/experiments/{environmentKey}/{metricKey}/results | Reset experiment results


# **create_experiment**
> Experiment create_experiment(project_key, environment_key, experiment_post)

Create experiment

Create an experiment. To learn more, read [Creating experiments](https://docs.launchdarkly.com/home/experimentation/create).

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
        name="name_example",
        description="description_example",
        maintainer_id="maintainer_id_example",
        key="key_example",
        iteration=IterationInput(
            hypothesis="hypothesis_example",
            can_reshuffle_traffic=True,
            metrics=MetricsInput([
                MetricInput(
                    key="key_example",
                    primary=True,
                ),
            ]),
            treatments=TreatmentsInput([
                TreatmentInput(
                    name="name_example",
                    baseline=True,
                    allocation_percent="allocation_percent_example",
                    parameters=[
                        TreatmentParameterInput(
                            flag_key="flag_key_example",
                            variation_id="variation_id_example",
                        ),
                    ],
                ),
            ]),
            flags=FlagsInput(
                key=FlagInput(
                    rule_id="rule_id_example",
                    flag_config_version=1,
                ),
            ),
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
**201** | Experiment response JSON |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_iteration**
> IterationRep create_iteration(project_key, environment_key, experiment_key, iteration_input)

Create iteration

Create an experiment iteration. Experiment iterations let you record experiments in discrete blocks of time. To learn more, read [Starting experiment iterations](https://docs.launchdarkly.com/home/experimentation/create#starting-experiment-iterations).

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
        hypothesis="hypothesis_example",
        can_reshuffle_traffic=True,
        metrics=MetricsInput([
            MetricInput(
                key="key_example",
                primary=True,
            ),
        ]),
        treatments=TreatmentsInput([
            TreatmentInput(
                name="name_example",
                baseline=True,
                allocation_percent="allocation_percent_example",
                parameters=[
                    TreatmentParameterInput(
                        flag_key="flag_key_example",
                        variation_id="variation_id_example",
                    ),
                ],
            ),
        ]),
        flags=FlagsInput(
            key=FlagInput(
                rule_id="rule_id_example",
                flag_config_version=1,
            ),
        ),
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
**200** | Iteration response JSON |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiment**
> Experiment get_experiment(project_key, environment_key, experiment_key)

Get experiment

Get details about an experiment.

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
**200** | Experiment response JSON |  -  |
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
**200** | Experiment results response JSON |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiments**
> ExperimentCollectionRep get_experiments(project_key, environment_key)

Get experiments

Get details about all experiments in an environment.  ### Filtering experiments  LaunchDarkly supports the `filter` query param for filtering, with the following fields:  - `flagKey` filters for only experiments which use the flag with the given key. - `status` filters for only experiments with an iteration with the given status. An iteration can have the status `not_started`, `running` or `stopped`.  For example, `filter=flagKey:my-flag,status=running` filters for experiments for the given flag key which have a currently running iteration.  ### Expanding the experiments response LaunchDarkly supports four fields for expanding the \"List experiments\" response. By default, these fields are **not** included in the response.  To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:  - `previousIterations` includes all iterations prior to the current iteration.  By default only the current iteration will be included in the response. - `draftIteration` includes a draft of an iteration which has not been started yet, if any. - `secondaryMetrics` includes secondary metrics.  By default only the primary metric is included in the response. - `treatments` includes all treatment and parameter details.  By default treatment data will not be included in the response.  For example, `expand=draftIteration,treatments` includes the `draftIteration` and `treatments` fields in the response. 

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
    limit = 1 # int | The maximum number of experiments to return. Defaults to 20 (optional)
    offset = 1 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = "filter_example" # str | A comma-separated list of filters. Each filter is of the form `field:value`. Supported fields are explained above. (optional)
    expand = "expand_example" # str | A comma-separated list of properties that can reveal additional information in the response. Supported fields are explained above. (optional)

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
        api_response = api_instance.get_experiments(project_key, environment_key, limit=limit, offset=offset, filter=filter, expand=expand)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ExperimentsBetaApi->get_experiments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **limit** | **int**| The maximum number of experiments to return. Defaults to 20 | [optional]
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional]
 **filter** | **str**| A comma-separated list of filters. Each filter is of the form &#x60;field:value&#x60;. Supported fields are explained above. | [optional]
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. Supported fields are explained above. | [optional]

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
**200** | Experiment response JSON |  -  |
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

Update an experiment. Updating an experiment uses the semantic patch format.  To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](/reference#updates-using-semantic-patch).  ### Instructions  Semantic patch requests support the following `kind` instructions for updating experiments.  #### updateName  Updates the experiment name.  ##### Parameters  - `value`: The new name.  #### updateDescription  Updates the experiment description.  ##### Parameters  - `value`: The new description.  #### startIteration  Starts a new iteration for this experiment.  #### stopIteration  Stops the current iteration for this experiment. 

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
        comment="comment_example",
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
**200** | Experiment response JSON |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
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

