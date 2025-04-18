# launchdarkly_api.ScheduledChangesApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_flag_config_scheduled_changes**](ScheduledChangesApi.md#delete_flag_config_scheduled_changes) | **DELETE** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes/{id} | Delete scheduled changes workflow
[**get_feature_flag_scheduled_change**](ScheduledChangesApi.md#get_feature_flag_scheduled_change) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes/{id} | Get a scheduled change
[**get_flag_config_scheduled_changes**](ScheduledChangesApi.md#get_flag_config_scheduled_changes) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes | List scheduled changes
[**patch_flag_config_scheduled_change**](ScheduledChangesApi.md#patch_flag_config_scheduled_change) | **PATCH** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes/{id} | Update scheduled changes workflow
[**post_flag_config_scheduled_changes**](ScheduledChangesApi.md#post_flag_config_scheduled_changes) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes | Create scheduled changes workflow


# **delete_flag_config_scheduled_changes**
> delete_flag_config_scheduled_changes(project_key, feature_flag_key, environment_key, id)

Delete scheduled changes workflow

Delete a scheduled changes workflow.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import scheduled_changes_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.status_conflict_error_rep import StatusConflictErrorRep
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
    api_instance = scheduled_changes_api.ScheduledChangesApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    id = "id_example" # str | The scheduled change id

    # example passing only required values which don't have defaults set
    try:
        # Delete scheduled changes workflow
        api_instance.delete_flag_config_scheduled_changes(project_key, feature_flag_key, environment_key, id)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ScheduledChangesApi->delete_flag_config_scheduled_changes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **environment_key** | **str**| The environment key |
 **id** | **str**| The scheduled change id |

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
**405** | Method not allowed |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flag_scheduled_change**
> FeatureFlagScheduledChange get_feature_flag_scheduled_change(project_key, feature_flag_key, environment_key, id)

Get a scheduled change

Get a scheduled change that will be applied to the feature flag by ID.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import scheduled_changes_api
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.feature_flag_scheduled_change import FeatureFlagScheduledChange
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
    api_instance = scheduled_changes_api.ScheduledChangesApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    id = "id_example" # str | The scheduled change id

    # example passing only required values which don't have defaults set
    try:
        # Get a scheduled change
        api_response = api_instance.get_feature_flag_scheduled_change(project_key, feature_flag_key, environment_key, id)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ScheduledChangesApi->get_feature_flag_scheduled_change: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **environment_key** | **str**| The environment key |
 **id** | **str**| The scheduled change id |

### Return type

[**FeatureFlagScheduledChange**](FeatureFlagScheduledChange.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scheduled changes response |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flag_config_scheduled_changes**
> FeatureFlagScheduledChanges get_flag_config_scheduled_changes(project_key, feature_flag_key, environment_key)

List scheduled changes

Get a list of scheduled changes that will be applied to the feature flag.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import scheduled_changes_api
from launchdarkly_api.model.feature_flag_scheduled_changes import FeatureFlagScheduledChanges
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
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
    api_instance = scheduled_changes_api.ScheduledChangesApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key

    # example passing only required values which don't have defaults set
    try:
        # List scheduled changes
        api_response = api_instance.get_flag_config_scheduled_changes(project_key, feature_flag_key, environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ScheduledChangesApi->get_flag_config_scheduled_changes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **environment_key** | **str**| The environment key |

### Return type

[**FeatureFlagScheduledChanges**](FeatureFlagScheduledChanges.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scheduled changes collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_flag_config_scheduled_change**
> FeatureFlagScheduledChange patch_flag_config_scheduled_change(project_key, feature_flag_key, environment_key, id, flag_scheduled_changes_input)

Update scheduled changes workflow

 Update a scheduled change, overriding existing instructions with the new ones. Updating a scheduled change uses the semantic patch format.  To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](https://launchdarkly.com/docs/api#updates-using-semantic-patch).  ### Instructions  Semantic patch requests support the following `kind` instructions for updating scheduled changes.  <details> <summary>Click to expand instructions for <strong>updating scheduled changes</strong></summary>  #### deleteScheduledChange  Removes the scheduled change.  Here's an example:  ```json {   \"instructions\": [{ \"kind\": \"deleteScheduledChange\" }] } ```  #### replaceScheduledChangesInstructions  Removes the existing scheduled changes and replaces them with the new instructions.  ##### Parameters  - `value`: An array of the new actions to perform when the execution date for these scheduled changes arrives. Supported scheduled actions are `turnFlagOn` and `turnFlagOff`.  Here's an example that replaces the scheduled changes with new instructions to turn flag targeting off:  ```json {   \"instructions\": [     {       \"kind\": \"replaceScheduledChangesInstructions\",       \"value\": [ {\"kind\": \"turnFlagOff\"} ]     }   ] } ```  #### updateScheduledChangesExecutionDate  Updates the execution date for the scheduled changes.  ##### Parameters  - `value`: the new execution date, in Unix milliseconds.  Here's an example:  ```json {   \"instructions\": [     {       \"kind\": \"updateScheduledChangesExecutionDate\",       \"value\": 1754092860000     }   ] } ```  </details> 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import scheduled_changes_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.flag_scheduled_changes_input import FlagScheduledChangesInput
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.feature_flag_scheduled_change import FeatureFlagScheduledChange
from launchdarkly_api.model.status_conflict_error_rep import StatusConflictErrorRep
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
    api_instance = scheduled_changes_api.ScheduledChangesApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    id = "id_example" # str | The scheduled change ID
    flag_scheduled_changes_input = FlagScheduledChangesInput(
        comment="optional comment",
        instructions=Instructions([
            Instruction(
                key=None,
            ),
        ]),
    ) # FlagScheduledChangesInput | 
    ignore_conflicts = True # bool | Whether to succeed (`true`) or fail (`false`) when these new instructions conflict with existing scheduled changes (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update scheduled changes workflow
        api_response = api_instance.patch_flag_config_scheduled_change(project_key, feature_flag_key, environment_key, id, flag_scheduled_changes_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ScheduledChangesApi->patch_flag_config_scheduled_change: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update scheduled changes workflow
        api_response = api_instance.patch_flag_config_scheduled_change(project_key, feature_flag_key, environment_key, id, flag_scheduled_changes_input, ignore_conflicts=ignore_conflicts)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ScheduledChangesApi->patch_flag_config_scheduled_change: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **environment_key** | **str**| The environment key |
 **id** | **str**| The scheduled change ID |
 **flag_scheduled_changes_input** | [**FlagScheduledChangesInput**](FlagScheduledChangesInput.md)|  |
 **ignore_conflicts** | **bool**| Whether to succeed (&#x60;true&#x60;) or fail (&#x60;false&#x60;) when these new instructions conflict with existing scheduled changes | [optional]

### Return type

[**FeatureFlagScheduledChange**](FeatureFlagScheduledChange.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scheduled changes response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_flag_config_scheduled_changes**
> FeatureFlagScheduledChange post_flag_config_scheduled_changes(project_key, feature_flag_key, environment_key, post_flag_scheduled_changes_input)

Create scheduled changes workflow

Create scheduled changes for a feature flag. If the `ignoreConficts` query parameter is false and there are conflicts between these instructions and existing scheduled changes, the request will fail. If the parameter is true and there are conflicts, the request will succeed.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import scheduled_changes_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.post_flag_scheduled_changes_input import PostFlagScheduledChangesInput
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.feature_flag_scheduled_change import FeatureFlagScheduledChange
from launchdarkly_api.model.status_conflict_error_rep import StatusConflictErrorRep
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
    api_instance = scheduled_changes_api.ScheduledChangesApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    post_flag_scheduled_changes_input = PostFlagScheduledChangesInput(
        comment="optional comment",
        execution_date=1,
        instructions=Instructions([
            Instruction(
                key=None,
            ),
        ]),
    ) # PostFlagScheduledChangesInput | 
    ignore_conflicts = True # bool | Whether to succeed (`true`) or fail (`false`) when these instructions conflict with existing scheduled changes (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create scheduled changes workflow
        api_response = api_instance.post_flag_config_scheduled_changes(project_key, feature_flag_key, environment_key, post_flag_scheduled_changes_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ScheduledChangesApi->post_flag_config_scheduled_changes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create scheduled changes workflow
        api_response = api_instance.post_flag_config_scheduled_changes(project_key, feature_flag_key, environment_key, post_flag_scheduled_changes_input, ignore_conflicts=ignore_conflicts)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ScheduledChangesApi->post_flag_config_scheduled_changes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **environment_key** | **str**| The environment key |
 **post_flag_scheduled_changes_input** | [**PostFlagScheduledChangesInput**](PostFlagScheduledChangesInput.md)|  |
 **ignore_conflicts** | **bool**| Whether to succeed (&#x60;true&#x60;) or fail (&#x60;false&#x60;) when these instructions conflict with existing scheduled changes | [optional]

### Return type

[**FeatureFlagScheduledChange**](FeatureFlagScheduledChange.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Scheduled changes response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

