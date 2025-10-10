# launchdarkly_api.FlagTriggersApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_trigger_workflow**](FlagTriggersApi.md#create_trigger_workflow) | **POST** /api/v2/flags/{projectKey}/{featureFlagKey}/triggers/{environmentKey} | Create flag trigger
[**delete_trigger_workflow**](FlagTriggersApi.md#delete_trigger_workflow) | **DELETE** /api/v2/flags/{projectKey}/{featureFlagKey}/triggers/{environmentKey}/{id} | Delete flag trigger
[**get_trigger_workflow_by_id**](FlagTriggersApi.md#get_trigger_workflow_by_id) | **GET** /api/v2/flags/{projectKey}/{featureFlagKey}/triggers/{environmentKey}/{id} | Get flag trigger by ID
[**get_trigger_workflows**](FlagTriggersApi.md#get_trigger_workflows) | **GET** /api/v2/flags/{projectKey}/{featureFlagKey}/triggers/{environmentKey} | List flag triggers
[**patch_trigger_workflow**](FlagTriggersApi.md#patch_trigger_workflow) | **PATCH** /api/v2/flags/{projectKey}/{featureFlagKey}/triggers/{environmentKey}/{id} | Update flag trigger


# **create_trigger_workflow**
> TriggerWorkflowRep create_trigger_workflow(project_key, environment_key, feature_flag_key, trigger_post)

Create flag trigger

Create a new flag trigger.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.trigger_post import TriggerPost
from launchdarkly_api.models.trigger_workflow_rep import TriggerWorkflowRep
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
    api_instance = launchdarkly_api.FlagTriggersApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    trigger_post = launchdarkly_api.TriggerPost() # TriggerPost | 

    try:
        # Create flag trigger
        api_response = api_instance.create_trigger_workflow(project_key, environment_key, feature_flag_key, trigger_post)
        print("The response of FlagTriggersApi->create_trigger_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlagTriggersApi->create_trigger_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **trigger_post** | [**TriggerPost**](TriggerPost.md)|  | 

### Return type

[**TriggerWorkflowRep**](TriggerWorkflowRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Flag trigger response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_trigger_workflow**
> delete_trigger_workflow(project_key, environment_key, feature_flag_key, id)

Delete flag trigger

Delete a flag trigger by ID.

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
    api_instance = launchdarkly_api.FlagTriggersApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    id = 'id_example' # str | The flag trigger ID

    try:
        # Delete flag trigger
        api_instance.delete_trigger_workflow(project_key, environment_key, feature_flag_key, id)
    except Exception as e:
        print("Exception when calling FlagTriggersApi->delete_trigger_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **id** | **str**| The flag trigger ID | 

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

# **get_trigger_workflow_by_id**
> TriggerWorkflowRep get_trigger_workflow_by_id(project_key, feature_flag_key, environment_key, id)

Get flag trigger by ID

Get a flag trigger by ID.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.trigger_workflow_rep import TriggerWorkflowRep
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
    api_instance = launchdarkly_api.FlagTriggersApi(api_client)
    project_key = 'project_key_example' # str | The project key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    environment_key = 'environment_key_example' # str | The environment key
    id = 'id_example' # str | The flag trigger ID

    try:
        # Get flag trigger by ID
        api_response = api_instance.get_trigger_workflow_by_id(project_key, feature_flag_key, environment_key, id)
        print("The response of FlagTriggersApi->get_trigger_workflow_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlagTriggersApi->get_trigger_workflow_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **environment_key** | **str**| The environment key | 
 **id** | **str**| The flag trigger ID | 

### Return type

[**TriggerWorkflowRep**](TriggerWorkflowRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag trigger response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trigger_workflows**
> TriggerWorkflowCollectionRep get_trigger_workflows(project_key, environment_key, feature_flag_key)

List flag triggers

Get a list of all flag triggers.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.trigger_workflow_collection_rep import TriggerWorkflowCollectionRep
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
    api_instance = launchdarkly_api.FlagTriggersApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key

    try:
        # List flag triggers
        api_response = api_instance.get_trigger_workflows(project_key, environment_key, feature_flag_key)
        print("The response of FlagTriggersApi->get_trigger_workflows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlagTriggersApi->get_trigger_workflows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **feature_flag_key** | **str**| The feature flag key | 

### Return type

[**TriggerWorkflowCollectionRep**](TriggerWorkflowCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag trigger collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_trigger_workflow**
> TriggerWorkflowRep patch_trigger_workflow(project_key, environment_key, feature_flag_key, id, flag_trigger_input)

Update flag trigger

Update a flag trigger. Updating a flag trigger uses the semantic patch format.

To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](https://launchdarkly.com/docs/api#updates-using-semantic-patch).

### Instructions

Semantic patch requests support the following `kind` instructions for updating flag triggers.

<details>
<summary>Click to expand instructions for <strong>updating flag triggers</strong></summary>

#### replaceTriggerActionInstructions

Removes the existing trigger action and replaces it with the new instructions.

##### Parameters

- `value`: An array of the new `kind`s of actions to perform when triggering. Supported flag actions are `turnFlagOn` and `turnFlagOff`.

Here's an example that replaces the existing action with new instructions to turn flag targeting off:

```json
{
  "instructions": [
    {
      "kind": "replaceTriggerActionInstructions",
      "value": [ {"kind": "turnFlagOff"} ]
    }
  ]
}
```

#### cycleTriggerUrl

Generates a new URL for this trigger. You must update any clients using the trigger to use this new URL.

Here's an example:

```json
{
  "instructions": [{ "kind": "cycleTriggerUrl" }]
}
```

#### disableTrigger

Disables the trigger. This saves the trigger configuration, but the trigger stops running. To re-enable, use `enableTrigger`.

Here's an example:

```json
{
  "instructions": [{ "kind": "disableTrigger" }]
}
```

#### enableTrigger

Enables the trigger. If you previously disabled the trigger, it begins running again.

Here's an example:

```json
{
  "instructions": [{ "kind": "enableTrigger" }]
}
```

</details>


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.flag_trigger_input import FlagTriggerInput
from launchdarkly_api.models.trigger_workflow_rep import TriggerWorkflowRep
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
    api_instance = launchdarkly_api.FlagTriggersApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    id = 'id_example' # str | The flag trigger ID
    flag_trigger_input = launchdarkly_api.FlagTriggerInput() # FlagTriggerInput | 

    try:
        # Update flag trigger
        api_response = api_instance.patch_trigger_workflow(project_key, environment_key, feature_flag_key, id, flag_trigger_input)
        print("The response of FlagTriggersApi->patch_trigger_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlagTriggersApi->patch_trigger_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **id** | **str**| The flag trigger ID | 
 **flag_trigger_input** | [**FlagTriggerInput**](FlagTriggerInput.md)|  | 

### Return type

[**TriggerWorkflowRep**](TriggerWorkflowRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag trigger response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

