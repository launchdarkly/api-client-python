# launchdarkly_api.ReleasePipelinesDeprecatedApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_release_for_flag**](ReleasePipelinesDeprecatedApi.md#create_release_for_flag) | **PUT** /api/v2/projects/{projectKey}/flags/{flagKey}/release | Create a new release for flag
[**delete_release_by_flag_key**](ReleasePipelinesDeprecatedApi.md#delete_release_by_flag_key) | **DELETE** /api/v2/flags/{projectKey}/{flagKey}/release | Delete a release for flag
[**delete_release_pipeline**](ReleasePipelinesDeprecatedApi.md#delete_release_pipeline) | **DELETE** /api/v2/projects/{projectKey}/release-pipelines/{pipelineKey} | Delete release pipeline
[**get_all_release_pipelines**](ReleasePipelinesDeprecatedApi.md#get_all_release_pipelines) | **GET** /api/v2/projects/{projectKey}/release-pipelines | Get all release pipelines
[**get_all_release_progressions_for_release_pipeline**](ReleasePipelinesDeprecatedApi.md#get_all_release_progressions_for_release_pipeline) | **GET** /api/v2/projects/{projectKey}/release-pipelines/{pipelineKey}/releases | Get release progressions for release pipeline
[**get_release_by_flag_key**](ReleasePipelinesDeprecatedApi.md#get_release_by_flag_key) | **GET** /api/v2/flags/{projectKey}/{flagKey}/release | Get release for flag
[**get_release_pipeline_by_key**](ReleasePipelinesDeprecatedApi.md#get_release_pipeline_by_key) | **GET** /api/v2/projects/{projectKey}/release-pipelines/{pipelineKey} | Get release pipeline by key
[**patch_release_by_flag_key**](ReleasePipelinesDeprecatedApi.md#patch_release_by_flag_key) | **PATCH** /api/v2/flags/{projectKey}/{flagKey}/release | Patch release for flag
[**post_release_pipeline**](ReleasePipelinesDeprecatedApi.md#post_release_pipeline) | **POST** /api/v2/projects/{projectKey}/release-pipelines | Create a release pipeline
[**put_release_pipeline**](ReleasePipelinesDeprecatedApi.md#put_release_pipeline) | **PUT** /api/v2/projects/{projectKey}/release-pipelines/{pipelineKey} | Update a release pipeline
[**update_phase_status**](ReleasePipelinesDeprecatedApi.md#update_phase_status) | **PUT** /api/v2/projects/{projectKey}/flags/{flagKey}/release/phases/{phaseId} | Update phase status for release


# **create_release_for_flag**
> PipelineRelease create_release_for_flag(project_key, flag_key, create_pipeline_release_input)

Create a new release for flag

Creates a release by adding a flag to a release pipeline

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.create_pipeline_release_input import CreatePipelineReleaseInput
from launchdarkly_api.models.pipeline_release import PipelineRelease
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
    api_instance = launchdarkly_api.ReleasePipelinesDeprecatedApi(api_client)
    project_key = 'project_key_example' # str | The project key
    flag_key = 'flag_key_example' # str | The flag key
    create_pipeline_release_input = launchdarkly_api.CreatePipelineReleaseInput() # CreatePipelineReleaseInput | 

    try:
        # Create a new release for flag
        api_response = api_instance.create_release_for_flag(project_key, flag_key, create_pipeline_release_input)
        print("The response of ReleasePipelinesDeprecatedApi->create_release_for_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePipelinesDeprecatedApi->create_release_for_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **flag_key** | **str**| The flag key | 
 **create_pipeline_release_input** | [**CreatePipelineReleaseInput**](CreatePipelineReleaseInput.md)|  | 

### Return type

[**PipelineRelease**](PipelineRelease.md)

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
    api_instance = launchdarkly_api.ReleasePipelinesDeprecatedApi(api_client)
    project_key = 'project_key_example' # str | The project key
    flag_key = 'flag_key_example' # str | The flag key

    try:
        # Delete a release for flag
        api_instance.delete_release_by_flag_key(project_key, flag_key)
    except Exception as e:
        print("Exception when calling ReleasePipelinesDeprecatedApi->delete_release_by_flag_key: %s\n" % e)
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

# **delete_release_pipeline**
> delete_release_pipeline(project_key, pipeline_key)

Delete release pipeline

Deletes a release pipeline.

You cannot delete the default release pipeline.

If you want to delete a release pipeline that is currently the default, create a second release pipeline and set it as the default. Then delete the first release pipeline. To change the default release pipeline, use the [Update project](https://launchdarkly.com/docs/api/projects/patch-project) API to set the `defaultReleasePipelineKey`.


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
    api_instance = launchdarkly_api.ReleasePipelinesDeprecatedApi(api_client)
    project_key = 'project_key_example' # str | The project key
    pipeline_key = 'pipeline_key_example' # str | The release pipeline key

    try:
        # Delete release pipeline
        api_instance.delete_release_pipeline(project_key, pipeline_key)
    except Exception as e:
        print("Exception when calling ReleasePipelinesDeprecatedApi->delete_release_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **pipeline_key** | **str**| The release pipeline key | 

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

# **get_all_release_pipelines**
> ReleasePipelineCollection get_all_release_pipelines(project_key, filter=filter, limit=limit, offset=offset)

Get all release pipelines

Get all release pipelines for a project.

### Filtering release pipelines

LaunchDarkly supports the following fields for filters:

- `query` is a string that matches against the release pipeline `key`, `name`, and `description`. It is not case sensitive. For example: `?filter=query:examplePipeline`.

- `env` is a string that matches an environment key. For example: `?filter=env:production`.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.release_pipeline_collection import ReleasePipelineCollection
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
    api_instance = launchdarkly_api.ReleasePipelinesDeprecatedApi(api_client)
    project_key = 'project_key_example' # str | The project key
    filter = 'filter_example' # str | A comma-separated list of filters. Each filter is of the form field:value. Read the endpoint description for a full list of available filter fields. (optional)
    limit = 56 # int | The maximum number of items to return. Defaults to 20. (optional)
    offset = 56 # int | Where to start in the list. Defaults to 0. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # Get all release pipelines
        api_response = api_instance.get_all_release_pipelines(project_key, filter=filter, limit=limit, offset=offset)
        print("The response of ReleasePipelinesDeprecatedApi->get_all_release_pipelines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePipelinesDeprecatedApi->get_all_release_pipelines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **filter** | **str**| A comma-separated list of filters. Each filter is of the form field:value. Read the endpoint description for a full list of available filter fields. | [optional] 
 **limit** | **int**| The maximum number of items to return. Defaults to 20. | [optional] 
 **offset** | **int**| Where to start in the list. Defaults to 0. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**ReleasePipelineCollection**](ReleasePipelineCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release pipeline collection |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_release_progressions_for_release_pipeline**
> PipelineReleaseProgressionCollection get_all_release_progressions_for_release_pipeline(project_key, pipeline_key, filter=filter, limit=limit, offset=offset)

Get release progressions for release pipeline

Get details on the progression of all releases, across all flags, for a release pipeline

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.pipeline_release_progression_collection import PipelineReleaseProgressionCollection
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
    api_instance = launchdarkly_api.ReleasePipelinesDeprecatedApi(api_client)
    project_key = 'project_key_example' # str | The project key
    pipeline_key = 'pipeline_key_example' # str | The pipeline key
    filter = 'filter_example' # str | Accepts filter by `status` and `activePhaseId`. `status` can take a value of `completed` or `active`. `activePhaseId` takes a UUID and will filter results down to releases active on the specified phase. Providing `status equals completed` along with an `activePhaseId` filter will return an error as they are disjoint sets of data. The combination of `status equals active` and `activePhaseId` will return the same results as `activePhaseId` alone. (optional)
    limit = 56 # int | The maximum number of items to return. Defaults to 20. (optional)
    offset = 56 # int | Where to start in the list. Defaults to 0. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # Get release progressions for release pipeline
        api_response = api_instance.get_all_release_progressions_for_release_pipeline(project_key, pipeline_key, filter=filter, limit=limit, offset=offset)
        print("The response of ReleasePipelinesDeprecatedApi->get_all_release_progressions_for_release_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePipelinesDeprecatedApi->get_all_release_progressions_for_release_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **pipeline_key** | **str**| The pipeline key | 
 **filter** | **str**| Accepts filter by &#x60;status&#x60; and &#x60;activePhaseId&#x60;. &#x60;status&#x60; can take a value of &#x60;completed&#x60; or &#x60;active&#x60;. &#x60;activePhaseId&#x60; takes a UUID and will filter results down to releases active on the specified phase. Providing &#x60;status equals completed&#x60; along with an &#x60;activePhaseId&#x60; filter will return an error as they are disjoint sets of data. The combination of &#x60;status equals active&#x60; and &#x60;activePhaseId&#x60; will return the same results as &#x60;activePhaseId&#x60; alone. | [optional] 
 **limit** | **int**| The maximum number of items to return. Defaults to 20. | [optional] 
 **offset** | **int**| Where to start in the list. Defaults to 0. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**PipelineReleaseProgressionCollection**](PipelineReleaseProgressionCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release progression collection |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_by_flag_key**
> PipelineRelease get_release_by_flag_key(project_key, flag_key)

Get release for flag

Get currently active release for a flag

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.pipeline_release import PipelineRelease
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
    api_instance = launchdarkly_api.ReleasePipelinesDeprecatedApi(api_client)
    project_key = 'project_key_example' # str | The project key
    flag_key = 'flag_key_example' # str | The flag key

    try:
        # Get release for flag
        api_response = api_instance.get_release_by_flag_key(project_key, flag_key)
        print("The response of ReleasePipelinesDeprecatedApi->get_release_by_flag_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePipelinesDeprecatedApi->get_release_by_flag_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **flag_key** | **str**| The flag key | 

### Return type

[**PipelineRelease**](PipelineRelease.md)

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

# **get_release_pipeline_by_key**
> ReleasePipeline get_release_pipeline_by_key(project_key, pipeline_key)

Get release pipeline by key

Get a release pipeline by key

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.release_pipeline import ReleasePipeline
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
    api_instance = launchdarkly_api.ReleasePipelinesDeprecatedApi(api_client)
    project_key = 'project_key_example' # str | The project key
    pipeline_key = 'pipeline_key_example' # str | The release pipeline key

    try:
        # Get release pipeline by key
        api_response = api_instance.get_release_pipeline_by_key(project_key, pipeline_key)
        print("The response of ReleasePipelinesDeprecatedApi->get_release_pipeline_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePipelinesDeprecatedApi->get_release_pipeline_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **pipeline_key** | **str**| The release pipeline key | 

### Return type

[**ReleasePipeline**](ReleasePipeline.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release pipeline response |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_release_by_flag_key**
> PipelineRelease patch_release_by_flag_key(project_key, flag_key, patch_operation)

Patch release for flag

This endpoint is only available for releases that are part of a legacy release pipeline. Releases for new release pipelines should use the [Update phase status for release](https://launchdarkly.com/docs/api/release-pipelines-deprecated/update-phase-status) endpoint.

Update currently active release for a flag. Updating releases requires the [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) format. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates).

You can only use this endpoint to mark a release phase complete or incomplete. To indicate which phase to update, use the array index in the `path`. For example, to mark the first phase of a release as complete, use the following request body:

```
  [
    {
      "op": "replace",
      "path": "/phase/0/complete",
      "value": true
    }
  ]
```


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.patch_operation import PatchOperation
from launchdarkly_api.models.pipeline_release import PipelineRelease
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
    api_instance = launchdarkly_api.ReleasePipelinesDeprecatedApi(api_client)
    project_key = 'project_key_example' # str | The project key
    flag_key = 'flag_key_example' # str | The flag key
    patch_operation = [{"op":"replace","path":"/phases/0/complete","value":true}] # List[PatchOperation] | 

    try:
        # Patch release for flag
        api_response = api_instance.patch_release_by_flag_key(project_key, flag_key, patch_operation)
        print("The response of ReleasePipelinesDeprecatedApi->patch_release_by_flag_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePipelinesDeprecatedApi->patch_release_by_flag_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **flag_key** | **str**| The flag key | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**PipelineRelease**](PipelineRelease.md)

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

# **post_release_pipeline**
> ReleasePipeline post_release_pipeline(project_key, create_release_pipeline_input)

Create a release pipeline

Creates a new release pipeline.

The first release pipeline you create is automatically set as the default release pipeline for your project. To change the default release pipeline, use the [Update project](https://launchdarkly.com/docs/api/projects/patch-project) API to set the `defaultReleasePipelineKey`.

You can create up to 20 release pipelines per project.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.create_release_pipeline_input import CreateReleasePipelineInput
from launchdarkly_api.models.release_pipeline import ReleasePipeline
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
    api_instance = launchdarkly_api.ReleasePipelinesDeprecatedApi(api_client)
    project_key = 'project_key_example' # str | The project key
    create_release_pipeline_input = launchdarkly_api.CreateReleasePipelineInput() # CreateReleasePipelineInput | 

    try:
        # Create a release pipeline
        api_response = api_instance.post_release_pipeline(project_key, create_release_pipeline_input)
        print("The response of ReleasePipelinesDeprecatedApi->post_release_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePipelinesDeprecatedApi->post_release_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **create_release_pipeline_input** | [**CreateReleasePipelineInput**](CreateReleasePipelineInput.md)|  | 

### Return type

[**ReleasePipeline**](ReleasePipeline.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Release pipeline response |  -  |
**400** | Invalid request |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_release_pipeline**
> ReleasePipeline put_release_pipeline(project_key, pipeline_key, update_release_pipeline_input)

Update a release pipeline

Updates a release pipeline.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.release_pipeline import ReleasePipeline
from launchdarkly_api.models.update_release_pipeline_input import UpdateReleasePipelineInput
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
    api_instance = launchdarkly_api.ReleasePipelinesDeprecatedApi(api_client)
    project_key = 'project_key_example' # str | The project key
    pipeline_key = 'pipeline_key_example' # str | The release pipeline key
    update_release_pipeline_input = launchdarkly_api.UpdateReleasePipelineInput() # UpdateReleasePipelineInput | 

    try:
        # Update a release pipeline
        api_response = api_instance.put_release_pipeline(project_key, pipeline_key, update_release_pipeline_input)
        print("The response of ReleasePipelinesDeprecatedApi->put_release_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePipelinesDeprecatedApi->put_release_pipeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **pipeline_key** | **str**| The release pipeline key | 
 **update_release_pipeline_input** | [**UpdateReleasePipelineInput**](UpdateReleasePipelineInput.md)|  | 

### Return type

[**ReleasePipeline**](ReleasePipeline.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release pipeline response |  -  |
**400** | Invalid request |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_phase_status**
> PipelineRelease update_phase_status(project_key, flag_key, phase_id, update_phase_status_input)

Update phase status for release

Updates the execution status of a phase of a release

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.pipeline_release import PipelineRelease
from launchdarkly_api.models.update_phase_status_input import UpdatePhaseStatusInput
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
    api_instance = launchdarkly_api.ReleasePipelinesDeprecatedApi(api_client)
    project_key = 'project_key_example' # str | The project key
    flag_key = 'flag_key_example' # str | The flag key
    phase_id = 'phase_id_example' # str | The phase ID
    update_phase_status_input = launchdarkly_api.UpdatePhaseStatusInput() # UpdatePhaseStatusInput | 

    try:
        # Update phase status for release
        api_response = api_instance.update_phase_status(project_key, flag_key, phase_id, update_phase_status_input)
        print("The response of ReleasePipelinesDeprecatedApi->update_phase_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePipelinesDeprecatedApi->update_phase_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **flag_key** | **str**| The flag key | 
 **phase_id** | **str**| The phase ID | 
 **update_phase_status_input** | [**UpdatePhaseStatusInput**](UpdatePhaseStatusInput.md)|  | 

### Return type

[**PipelineRelease**](PipelineRelease.md)

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

