# launchdarkly_api.ReleasesBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_release_for_flag**](ReleasesBetaApi.md#create_release_for_flag) | **PUT** /api/v2/projects/{projectKey}/flags/{flagKey}/release | Create a new release for flag
[**delete_release_by_flag_key**](ReleasesBetaApi.md#delete_release_by_flag_key) | **DELETE** /api/v2/flags/{projectKey}/{flagKey}/release | Delete a release for flag
[**get_release_by_flag_key**](ReleasesBetaApi.md#get_release_by_flag_key) | **GET** /api/v2/flags/{projectKey}/{flagKey}/release | Get release for flag
[**patch_release_by_flag_key**](ReleasesBetaApi.md#patch_release_by_flag_key) | **PATCH** /api/v2/flags/{projectKey}/{flagKey}/release | Patch release for flag
[**update_phase_status**](ReleasesBetaApi.md#update_phase_status) | **PUT** /api/v2/projects/{projectKey}/flags/{flagKey}/release/phases/{phaseId} | Update phase status for release


# **create_release_for_flag**
> Release create_release_for_flag(project_key, flag_key, create_release_input)

Create a new release for flag

Creates a release by adding a flag to a release pipeline

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import releases_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.release import Release
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.create_release_input import CreateReleaseInput
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
    api_instance = releases_beta_api.ReleasesBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    flag_key = "flagKey_example" # str | The flag key
    create_release_input = CreateReleaseInput(
        release_variation_id="release_variation_id_example",
        release_pipeline_key="release_pipeline_key_example",
    ) # CreateReleaseInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new release for flag
        api_response = api_instance.create_release_for_flag(project_key, flag_key, create_release_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ReleasesBetaApi->create_release_for_flag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **flag_key** | **str**| The flag key |
 **create_release_input** | [**CreateReleaseInput**](CreateReleaseInput.md)|  |

### Return type

[**Release**](Release.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_release_by_flag_key**
> delete_release_by_flag_key(project_key, flag_key)

Delete a release for flag

Deletes a release from a flag

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import releases_beta_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
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
    api_instance = releases_beta_api.ReleasesBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    flag_key = "flagKey_example" # str | The flag key

    # example passing only required values which don't have defaults set
    try:
        # Delete a release for flag
        api_instance.delete_release_by_flag_key(project_key, flag_key)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ReleasesBetaApi->delete_release_by_flag_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **flag_key** | **str**| The flag key |

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
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_by_flag_key**
> Release get_release_by_flag_key(project_key, flag_key)

Get release for flag

Get currently active release for a flag

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import releases_beta_api
from launchdarkly_api.model.release import Release
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
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
    api_instance = releases_beta_api.ReleasesBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    flag_key = "flagKey_example" # str | The flag key

    # example passing only required values which don't have defaults set
    try:
        # Get release for flag
        api_response = api_instance.get_release_by_flag_key(project_key, flag_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ReleasesBetaApi->get_release_by_flag_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **flag_key** | **str**| The flag key |

### Return type

[**Release**](Release.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release response |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_release_by_flag_key**
> Release patch_release_by_flag_key(project_key, flag_key, json_patch)

Patch release for flag

This endpoint is only available for releases that are part of a legacy release pipeline. Releases for new release pipelines should use the [Update phase status for release](/tag/Releases-(beta)#operation/updatePhaseStatus) endpoint. To learn more about migrating from legacy release pipelines to fully automated release pipelines, read the [Release pipeline migration guide](https://docs.launchdarkly.com/guides/flags/release-pipeline-migration).  Update currently active release for a flag. Updating releases requires the [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) format. To learn more, read [Updates](/#section/Overview/Updates).  You can only use this endpoint to mark a release phase complete or incomplete. To indicate which phase to update, use the array index in the `path`. For example, to mark the first phase of a release as complete, use the following request body:  ```   [     {       \"op\": \"replace\",       \"path\": \"/phase/0/complete\",       \"value\": true     }   ] ``` 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import releases_beta_api
from launchdarkly_api.model.json_patch import JSONPatch
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.release import Release
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
    api_instance = releases_beta_api.ReleasesBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    flag_key = "flagKey_example" # str | The flag key
    json_patch = JSONPatch([
        PatchOperation(
            op="replace",
            path="/exampleField",
            value=None,
        ),
    ]) # JSONPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Patch release for flag
        api_response = api_instance.patch_release_by_flag_key(project_key, flag_key, json_patch)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ReleasesBetaApi->patch_release_by_flag_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **flag_key** | **str**| The flag key |
 **json_patch** | [**JSONPatch**](JSONPatch.md)|  |

### Return type

[**Release**](Release.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_phase_status**
> Release update_phase_status(project_key, flag_key, phase_id, update_phase_status_input)

Update phase status for release

Updates the execution status of a phase of a release

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import releases_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.release import Release
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.update_phase_status_input import UpdatePhaseStatusInput
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
    api_instance = releases_beta_api.ReleasesBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    flag_key = "flagKey_example" # str | The flag key
    phase_id = "phaseId_example" # str | The phase ID
    update_phase_status_input = UpdatePhaseStatusInput(
        status="status_example",
        audiences=[
            ReleaserAudienceConfigInput(
                audience_id="audience_id_example",
                release_guardian_configuration=ReleaseGuardianConfigurationInput(
                    monitoring_window_milliseconds=60000,
                    rollout_weight=50,
                    rollback_on_regression=True,
                    randomization_unit="user",
                ),
                notify_member_ids=["1234a56b7c89d012345e678f"],
                notify_team_keys=["example-reviewer-team"],
            ),
        ],
    ) # UpdatePhaseStatusInput | 

    # example passing only required values which don't have defaults set
    try:
        # Update phase status for release
        api_response = api_instance.update_phase_status(project_key, flag_key, phase_id, update_phase_status_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ReleasesBetaApi->update_phase_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **flag_key** | **str**| The flag key |
 **phase_id** | **str**| The phase ID |
 **update_phase_status_input** | [**UpdatePhaseStatusInput**](UpdatePhaseStatusInput.md)|  |

### Return type

[**Release**](Release.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Action succeeded |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**404** | release or phase not found |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

