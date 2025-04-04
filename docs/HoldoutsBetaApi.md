# launchdarkly_api.HoldoutsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_holdouts**](HoldoutsBetaApi.md#get_all_holdouts) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/holdouts | Get all holdouts
[**get_holdout**](HoldoutsBetaApi.md#get_holdout) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/holdouts/{holdoutKey} | Get holdout
[**get_holdout_by_id**](HoldoutsBetaApi.md#get_holdout_by_id) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/holdouts/id/{holdoutId} | Get Holdout by Id
[**patch_holdout**](HoldoutsBetaApi.md#patch_holdout) | **PATCH** /api/v2/projects/{projectKey}/environments/{environmentKey}/holdouts/{holdoutKey} | Patch holdout
[**post_holdout**](HoldoutsBetaApi.md#post_holdout) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/holdouts | Create holdout


# **get_all_holdouts**
> HoldoutsCollectionRep get_all_holdouts(project_key, environment_key)

Get all holdouts

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import holdouts_beta_api
from launchdarkly_api.model.holdouts_collection_rep import HoldoutsCollectionRep
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
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
    api_instance = holdouts_beta_api.HoldoutsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    limit = 1 # int | The number of holdouts to return in the response. Defaults to 20 (optional)
    offset = 1 # int | Where to start in the list. Use this with pagination. For example, an `offset` of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all holdouts
        api_response = api_instance.get_all_holdouts(project_key, environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling HoldoutsBetaApi->get_all_holdouts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all holdouts
        api_response = api_instance.get_all_holdouts(project_key, environment_key, limit=limit, offset=offset)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling HoldoutsBetaApi->get_all_holdouts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **limit** | **int**| The number of holdouts to return in the response. Defaults to 20 | [optional]
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an &#x60;offset&#x60; of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional]

### Return type

[**HoldoutsCollectionRep**](HoldoutsCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All Holdouts response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_holdout**
> HoldoutDetailRep get_holdout(project_key, environment_key, holdout_key)

Get holdout

Get details about a holdout.  ### Expanding the holdout response  LaunchDarkly supports the following fields for expanding the \"Get holdout\" response. By default, these fields are **not** included in the response.  To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:  - `draftIteration` includes the iteration which has not been started yet, if any, for this holdout. - `previousIterations` includes all iterations prior to the current iteration, for this holdout. By default only the current iteration is included in the response. - `rel-draftIteration` includes the iteration which has not been started yet, if any, for the experiments related to this holdout. - `rel-metrics` includes metrics for experiments related to this holdout. - `rel-previousIterations` includes all iterations prior to the current iteration, for the experiments related to this holdout. - `rel-secondaryMetrics` includes secondary metrics for experiments related to this holdout. - `rel-treatments` includes all treatment and parameter details for experiments related to this holdout. - `secondaryMetrics` includes secondary metrics for this holdout. By default only the primary metric is included in the response. - `treatments` includes all treatment and parameter details for this holdout. By default treatment data is not included in the response.  For example, `expand=draftIteration,rel-draftIteration` includes the `draftIteration` and `rel-draftIteration` fields in the response. If fields that you request with the `expand` query parameter are empty, they are not included in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import holdouts_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.holdout_detail_rep import HoldoutDetailRep
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
    api_instance = holdouts_beta_api.HoldoutsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    holdout_key = "holdoutKey_example" # str | The holdout experiment key
    expand = "expand_example" # str | A comma-separated list of properties that can reveal additional information in the response. Supported fields are explained above. Holdout experiment expansion fields have no prefix. Related experiment expansion fields have `rel-` as a prefix. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get holdout
        api_response = api_instance.get_holdout(project_key, environment_key, holdout_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling HoldoutsBetaApi->get_holdout: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get holdout
        api_response = api_instance.get_holdout(project_key, environment_key, holdout_key, expand=expand)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling HoldoutsBetaApi->get_holdout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **holdout_key** | **str**| The holdout experiment key |
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. Supported fields are explained above. Holdout experiment expansion fields have no prefix. Related experiment expansion fields have &#x60;rel-&#x60; as a prefix. | [optional]

### Return type

[**HoldoutDetailRep**](HoldoutDetailRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HoldoutDetail response with full experiments |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_holdout_by_id**
> HoldoutRep get_holdout_by_id(project_key, environment_key, holdout_id)

Get Holdout by Id

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import holdouts_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.holdout_rep import HoldoutRep
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
    api_instance = holdouts_beta_api.HoldoutsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    holdout_id = "holdoutId_example" # str | The holdout experiment ID

    # example passing only required values which don't have defaults set
    try:
        # Get Holdout by Id
        api_response = api_instance.get_holdout_by_id(project_key, environment_key, holdout_id)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling HoldoutsBetaApi->get_holdout_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **holdout_id** | **str**| The holdout experiment ID |

### Return type

[**HoldoutRep**](HoldoutRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Holdout response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_holdout**
> HoldoutRep patch_holdout(project_key, environment_key, holdout_key, holdout_patch_input)

Patch holdout

Updates an existing holdout, and returns the updated holdout. Updating holdouts uses the semantic patch format.  To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](https://launchdarkly.com/docs/api#updates-using-semantic-patch).  ### Instructions  Semantic patch requests support the following `kind` instructions for updating holdouts.  <details> <summary>Click to expand instructions for <strong>updating holdouts</strong></summary>  #### endHoldout  Ends a holdout.  ##### Parameters  None.  Here's an example:  ```json {   \"comment\": \"Optional comment describing why the holdout is ending\",   \"instructions\": [{     \"kind\": \"endHoldout\"   }] } ```  #### removeExperiment  Removes an experiment from a holdout.  ##### Parameters  - `value`: The key of the experiment to remove  Here's an example:  ```json {   \"comment\": \"Optional comment describing the change\",   \"instructions\": [{     \"kind\": \"removeExperiment\",     \"value\": \"experiment-key\"   }] } ```  #### updateDescription  Updates the description of the holdout.  ##### Parameters  - `value`: The new description.  Here's an example:  ```json {   \"comment\": \"Optional comment describing the update\",   \"instructions\": [{     \"kind\": \"updateDescription\",     \"value\": \"Updated holdout description\"   }] } ```  #### updateName  Updates the name of the holdout.  ##### Parameters  - `value`: The new name.  Here's an example:  ```json {   \"comment\": \"Optional comment describing the update\",   \"instructions\": [{     \"kind\": \"updateName\",     \"value\": \"Updated holdout name\"   }] } ```  </details> 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import holdouts_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.holdout_rep import HoldoutRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.holdout_patch_input import HoldoutPatchInput
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
    api_instance = holdouts_beta_api.HoldoutsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    holdout_key = "holdoutKey_example" # str | The holdout key
    holdout_patch_input = HoldoutPatchInput(
        comment="Optional comment",
        instructions=Instructions([
            Instruction(
                key=None,
            ),
        ]),
    ) # HoldoutPatchInput | 

    # example passing only required values which don't have defaults set
    try:
        # Patch holdout
        api_response = api_instance.patch_holdout(project_key, environment_key, holdout_key, holdout_patch_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling HoldoutsBetaApi->patch_holdout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **holdout_key** | **str**| The holdout key |
 **holdout_patch_input** | [**HoldoutPatchInput**](HoldoutPatchInput.md)|  |

### Return type

[**HoldoutRep**](HoldoutRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Holdout response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_holdout**
> HoldoutRep post_holdout(project_key, environment_key, holdout_post_request)

Create holdout

Create a new holdout in the specified project.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import holdouts_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.holdout_post_request import HoldoutPostRequest
from launchdarkly_api.model.holdout_rep import HoldoutRep
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
    api_instance = holdouts_beta_api.HoldoutsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    holdout_post_request = HoldoutPostRequest(
        name="holdout-one-name",
        key="holdout-key",
        description="My holdout-one description",
        randomizationunit="user",
        attributes=["country","device","os"],
        holdoutamount="10",
        primarymetrickey="metric-key-123abc",
        metrics=[
            MetricInput(
                key="metric-key-123abc",
                is_group=True,
                primary=True,
            ),
        ],
        prerequisiteflagkey="flag-key-123abc",
        maintainer_id="maintainer_id_example",
    ) # HoldoutPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create holdout
        api_response = api_instance.post_holdout(project_key, environment_key, holdout_post_request)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling HoldoutsBetaApi->post_holdout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **holdout_post_request** | [**HoldoutPostRequest**](HoldoutPostRequest.md)|  |

### Return type

[**HoldoutRep**](HoldoutRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Holdout response |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

