# launchdarkly_api.ExperimentsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_experiment**](ExperimentsApi.md#create_experiment) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments | Create experiment
[**create_iteration**](ExperimentsApi.md#create_iteration) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey}/iterations | Create iteration
[**get_experiment**](ExperimentsApi.md#get_experiment) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey} | Get experiment
[**get_experimentation_settings**](ExperimentsApi.md#get_experimentation_settings) | **GET** /api/v2/projects/{projectKey}/experimentation-settings | Get experimentation settings
[**get_experiments**](ExperimentsApi.md#get_experiments) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments | Get experiments
[**patch_experiment**](ExperimentsApi.md#patch_experiment) | **PATCH** /api/v2/projects/{projectKey}/environments/{environmentKey}/experiments/{experimentKey} | Patch experiment
[**put_experimentation_settings**](ExperimentsApi.md#put_experimentation_settings) | **PUT** /api/v2/projects/{projectKey}/experimentation-settings | Update experimentation settings


# **create_experiment**
> Experiment create_experiment(project_key, environment_key, experiment_post)

Create experiment

Create an experiment.

To run this experiment, you'll need to [create an iteration](https://launchdarkly.com/docs/api/experiments/create-iteration) and then [update the experiment](https://launchdarkly.com/docs/api/experiments/patch-experiment) with the `startIteration` instruction.

To learn more, read [Creating experiments](https://launchdarkly.com/docs/home/experimentation/create).


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.experiment import Experiment
from launchdarkly_api.models.experiment_post import ExperimentPost
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
    api_instance = launchdarkly_api.ExperimentsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    experiment_post = launchdarkly_api.ExperimentPost() # ExperimentPost | 

    try:
        # Create experiment
        api_response = api_instance.create_experiment(project_key, environment_key, experiment_post)
        print("The response of ExperimentsApi->create_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentsApi->create_experiment: %s\n" % e)
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

Create an experiment iteration.

Experiment iterations let you record experiments in individual blocks of time. Initially, iterations are created with a status of `not_started` and appear in the `draftIteration` field of an experiment. To start or stop an iteration, [update the experiment](https://launchdarkly.com/docs/api/experiments/patch-experiment) with the `startIteration` or `stopIteration` instruction. 

To learn more, read [Start experiment iterations](https://launchdarkly.com/docs/home/experimentation/feature#start-experiment-iterations).


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.iteration_input import IterationInput
from launchdarkly_api.models.iteration_rep import IterationRep
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
    api_instance = launchdarkly_api.ExperimentsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    experiment_key = 'experiment_key_example' # str | The experiment key
    iteration_input = launchdarkly_api.IterationInput() # IterationInput | 

    try:
        # Create iteration
        api_response = api_instance.create_iteration(project_key, environment_key, experiment_key, iteration_input)
        print("The response of ExperimentsApi->create_iteration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentsApi->create_iteration: %s\n" % e)
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
> Experiment get_experiment(project_key, environment_key, experiment_key, expand=expand)

Get experiment

Get details about an experiment.

### Expanding the experiment response

LaunchDarkly supports four fields for expanding the "Get experiment" response. By default, these fields are **not** included in the response.

To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:

- `previousIterations` includes all iterations prior to the current iteration. By default only the current iteration is included in the response.
- `draftIteration` includes the iteration which has not been started yet, if any.
- `secondaryMetrics` includes secondary metrics. By default only the primary metric is included in the response.
- `treatments` includes all treatment and parameter details. By default treatment data is not included in the response.

For example, `expand=draftIteration,treatments` includes the `draftIteration` and `treatments` fields in the response. If fields that you request with the `expand` query parameter are empty, they are not included in the response.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.experiment import Experiment
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
    api_instance = launchdarkly_api.ExperimentsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    experiment_key = 'experiment_key_example' # str | The experiment key
    expand = 'expand_example' # str | A comma-separated list of properties that can reveal additional information in the response. Supported fields are explained above. (optional)

    try:
        # Get experiment
        api_response = api_instance.get_experiment(project_key, environment_key, experiment_key, expand=expand)
        print("The response of ExperimentsApi->get_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentsApi->get_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **experiment_key** | **str**| The experiment key | 
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. Supported fields are explained above. | [optional] 

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

# **get_experimentation_settings**
> RandomizationSettingsRep get_experimentation_settings(project_key)

Get experimentation settings

Get current experimentation settings for the given project

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.randomization_settings_rep import RandomizationSettingsRep
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
    api_instance = launchdarkly_api.ExperimentsApi(api_client)
    project_key = 'project_key_example' # str | The project key

    try:
        # Get experimentation settings
        api_response = api_instance.get_experimentation_settings(project_key)
        print("The response of ExperimentsApi->get_experimentation_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentsApi->get_experimentation_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 

### Return type

[**RandomizationSettingsRep**](RandomizationSettingsRep.md)

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
> ExperimentCollectionRep get_experiments(project_key, environment_key, limit=limit, offset=offset, filter=filter, expand=expand, lifecycle_state=lifecycle_state)

Get experiments

Get details about all experiments in an environment.

### Filtering experiments

LaunchDarkly supports the `filter` query param for filtering, with the following fields:

- `flagKey` filters for only experiments that use the flag with the given key.
- `metricKey` filters for only experiments that use the metric with the given key.
- `status` filters for only experiments with an iteration with the given status. An iteration can have the status `not_started`, `running` or `stopped`.

For example, `filter=flagKey:my-flag,status:running,metricKey:page-load-ms` filters for experiments for the given flag key and the given metric key which have a currently running iteration.

### Expanding the experiments response

LaunchDarkly supports four fields for expanding the "Get experiments" response. By default, these fields are **not** included in the response.

To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:

- `previousIterations` includes all iterations prior to the current iteration. By default only the current iteration is included in the response.
- `draftIteration` includes the iteration which has not been started yet, if any.
- `secondaryMetrics` includes secondary metrics. By default only the primary metric is included in the response.
- `treatments` includes all treatment and parameter details. By default treatment data is not included in the response.

For example, `expand=draftIteration,treatments` includes the `draftIteration` and `treatments` fields in the response. If fields that you request with the `expand` query parameter are empty, they are not included in the response.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.experiment_collection_rep import ExperimentCollectionRep
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
    api_instance = launchdarkly_api.ExperimentsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    limit = 56 # int | The maximum number of experiments to return. Defaults to 20. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = 'filter_example' # str | A comma-separated list of filters. Each filter is of the form `field:value`. Supported fields are explained above. (optional)
    expand = 'expand_example' # str | A comma-separated list of properties that can reveal additional information in the response. Supported fields are explained above. (optional)
    lifecycle_state = 'lifecycle_state_example' # str | A comma-separated list of experiment archived states. Supports `archived`, `active`, or both. Defaults to `active` experiments. (optional)

    try:
        # Get experiments
        api_response = api_instance.get_experiments(project_key, environment_key, limit=limit, offset=offset, filter=filter, expand=expand, lifecycle_state=lifecycle_state)
        print("The response of ExperimentsApi->get_experiments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentsApi->get_experiments: %s\n" % e)
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

# **patch_experiment**
> Experiment patch_experiment(project_key, environment_key, experiment_key, experiment_patch_input)

Patch experiment

Update an experiment. Updating an experiment uses the semantic patch format.

To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](https://launchdarkly.com/docs/api#updates-using-semantic-patch).

### Instructions

Semantic patch requests support the following `kind` instructions for updating experiments.

#### updateName

Updates the experiment name.

##### Parameters

- `value`: The new name.

Here's an example:

```json
{
  "instructions": [{
    "kind": "updateName",
    "value": "Example updated experiment name"
  }]
}
```

#### updateDescription

Updates the experiment description.

##### Parameters

- `value`: The new description.

Here's an example:

```json
{
  "instructions": [{
    "kind": "updateDescription",
    "value": "Example updated description"
  }]
}
```

#### startIteration

Starts a new iteration for this experiment. You must [create a new iteration](https://launchdarkly.com/docs/api/experiments/create-iteration) before calling this instruction.

An iteration may not be started until it meets the following criteria:

* Its associated flag is toggled on and is not archived
* Its `randomizationUnit` is set
* At least one of its `treatments` has a non-zero `allocationPercent`

##### Parameters

- `changeJustification`: The reason for starting a new iteration. Required when you call `startIteration` on an already running experiment, otherwise optional.

Here's an example:

```json
{
  "instructions": [{
    "kind": "startIteration",
    "changeJustification": "It's time to start a new iteration"
  }]
}
```

#### stopIteration

Stops the current iteration for this experiment.

##### Parameters

- `winningTreatmentId`: The ID of the winning treatment. Treatment IDs are returned as part of the [Get experiment](https://launchdarkly.com/docs/api/experiments/get-experiment) response. They are the `_id` of each element in the `treatments` array.
- `winningReason`: The reason for the winner

Here's an example:

```json
{
  "instructions": [{
    "kind": "stopIteration",
    "winningTreatmentId": "3a548ec2-72ac-4e59-8518-5c24f5609ccf",
    "winningReason": "Example reason to stop the iteration"
  }]
}
```

#### archiveExperiment

Archives this experiment. Archived experiments are hidden by default in the LaunchDarkly user interface. You cannot start new iterations for archived experiments.

Here's an example:

```json
{
  "instructions": [{ "kind": "archiveExperiment" }]
}
```

#### restoreExperiment

Restores an archived experiment. After restoring an experiment, you can start new iterations for it again.

Here's an example:

```json
{
  "instructions": [{ "kind": "restoreExperiment" }]
}
```


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.experiment import Experiment
from launchdarkly_api.models.experiment_patch_input import ExperimentPatchInput
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
    api_instance = launchdarkly_api.ExperimentsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    experiment_key = 'experiment_key_example' # str | The experiment key
    experiment_patch_input = {"comment":"Example comment describing the update","instructions":[{"kind":"updateName","value":"Updated experiment name"}]} # ExperimentPatchInput | 

    try:
        # Patch experiment
        api_response = api_instance.patch_experiment(project_key, environment_key, experiment_key, experiment_patch_input)
        print("The response of ExperimentsApi->patch_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentsApi->patch_experiment: %s\n" % e)
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
**409** | Conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_experimentation_settings**
> RandomizationSettingsRep put_experimentation_settings(project_key, randomization_settings_put)

Update experimentation settings

Update experimentation settings for the given project

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.randomization_settings_put import RandomizationSettingsPut
from launchdarkly_api.models.randomization_settings_rep import RandomizationSettingsRep
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
    api_instance = launchdarkly_api.ExperimentsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    randomization_settings_put = launchdarkly_api.RandomizationSettingsPut() # RandomizationSettingsPut | 

    try:
        # Update experimentation settings
        api_response = api_instance.put_experimentation_settings(project_key, randomization_settings_put)
        print("The response of ExperimentsApi->put_experimentation_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimentsApi->put_experimentation_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **randomization_settings_put** | [**RandomizationSettingsPut**](RandomizationSettingsPut.md)|  | 

### Return type

[**RandomizationSettingsRep**](RandomizationSettingsRep.md)

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

