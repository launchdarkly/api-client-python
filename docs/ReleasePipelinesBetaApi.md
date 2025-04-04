# launchdarkly_api.ReleasePipelinesBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_release_pipeline**](ReleasePipelinesBetaApi.md#delete_release_pipeline) | **DELETE** /api/v2/projects/{projectKey}/release-pipelines/{pipelineKey} | Delete release pipeline
[**get_all_release_pipelines**](ReleasePipelinesBetaApi.md#get_all_release_pipelines) | **GET** /api/v2/projects/{projectKey}/release-pipelines | Get all release pipelines
[**get_all_release_progressions_for_release_pipeline**](ReleasePipelinesBetaApi.md#get_all_release_progressions_for_release_pipeline) | **GET** /api/v2/projects/{projectKey}/release-pipelines/{pipelineKey}/releases | Get release progressions for release pipeline
[**get_release_pipeline_by_key**](ReleasePipelinesBetaApi.md#get_release_pipeline_by_key) | **GET** /api/v2/projects/{projectKey}/release-pipelines/{pipelineKey} | Get release pipeline by key
[**post_release_pipeline**](ReleasePipelinesBetaApi.md#post_release_pipeline) | **POST** /api/v2/projects/{projectKey}/release-pipelines | Create a release pipeline
[**put_release_pipeline**](ReleasePipelinesBetaApi.md#put_release_pipeline) | **PUT** /api/v2/projects/{projectKey}/release-pipelines/{pipelineKey} | Update a release pipeline


# **delete_release_pipeline**
> delete_release_pipeline(project_key, pipeline_key)

Delete release pipeline

Deletes a release pipeline.  You cannot delete the default release pipeline.  If you want to delete a release pipeline that is currently the default, create a second release pipeline and set it as the default. Then delete the first release pipeline. To change the default release pipeline, use the [Update project](https://launchdarkly.com/docs/ld-docs/api/projects/patch-project) API to set the `defaultReleasePipelineKey`. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import release_pipelines_beta_api
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
    api_instance = release_pipelines_beta_api.ReleasePipelinesBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    pipeline_key = "pipelineKey_example" # str | The release pipeline key

    # example passing only required values which don't have defaults set
    try:
        # Delete release pipeline
        api_instance.delete_release_pipeline(project_key, pipeline_key)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ReleasePipelinesBetaApi->delete_release_pipeline: %s\n" % e)
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
> ReleasePipelineCollection get_all_release_pipelines(project_key)

Get all release pipelines

Get all release pipelines for a project.  ### Filtering release pipelines  LaunchDarkly supports the following fields for filters:  - `query` is a string that matches against the release pipeline `key`, `name`, and `description`. It is not case sensitive. For example: `?filter=query:examplePipeline`.  - `env` is a string that matches an environment key. For example: `?filter=env:production`. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import release_pipelines_beta_api
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.release_pipeline_collection import ReleasePipelineCollection
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
    api_instance = release_pipelines_beta_api.ReleasePipelinesBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    filter = "filter_example" # str | A comma-separated list of filters. Each filter is of the form field:value. Read the endpoint description for a full list of available filter fields. (optional)
    limit = 1 # int | The maximum number of items to return. Defaults to 20. (optional)
    offset = 1 # int | Where to start in the list. Defaults to 0. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all release pipelines
        api_response = api_instance.get_all_release_pipelines(project_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ReleasePipelinesBetaApi->get_all_release_pipelines: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all release pipelines
        api_response = api_instance.get_all_release_pipelines(project_key, filter=filter, limit=limit, offset=offset)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ReleasePipelinesBetaApi->get_all_release_pipelines: %s\n" % e)
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
> ReleaseProgressionCollection get_all_release_progressions_for_release_pipeline(project_key, pipeline_key)

Get release progressions for release pipeline

Get details on the progression of all releases, across all flags, for a release pipeline

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import release_pipelines_beta_api
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.release_progression_collection import ReleaseProgressionCollection
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
    api_instance = release_pipelines_beta_api.ReleasePipelinesBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    pipeline_key = "pipelineKey_example" # str | The pipeline key
    filter = "filter_example" # str | Accepts filter by `status` and `activePhaseId`. `status` can take a value of `completed` or `active`. `activePhaseId` takes a UUID and will filter results down to releases active on the specified phase. Providing `status equals completed` along with an `activePhaseId` filter will return an error as they are disjoint sets of data. The combination of `status equals active` and `activePhaseId` will return the same results as `activePhaseId` alone. (optional)
    limit = 1 # int | The maximum number of items to return. Defaults to 20. (optional)
    offset = 1 # int | Where to start in the list. Defaults to 0. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get release progressions for release pipeline
        api_response = api_instance.get_all_release_progressions_for_release_pipeline(project_key, pipeline_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ReleasePipelinesBetaApi->get_all_release_progressions_for_release_pipeline: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get release progressions for release pipeline
        api_response = api_instance.get_all_release_progressions_for_release_pipeline(project_key, pipeline_key, filter=filter, limit=limit, offset=offset)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ReleasePipelinesBetaApi->get_all_release_progressions_for_release_pipeline: %s\n" % e)
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

[**ReleaseProgressionCollection**](ReleaseProgressionCollection.md)

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

# **get_release_pipeline_by_key**
> ReleasePipeline get_release_pipeline_by_key(project_key, pipeline_key)

Get release pipeline by key

Get a release pipeline by key

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import release_pipelines_beta_api
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.release_pipeline import ReleasePipeline
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
    api_instance = release_pipelines_beta_api.ReleasePipelinesBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    pipeline_key = "pipelineKey_example" # str | The release pipeline key

    # example passing only required values which don't have defaults set
    try:
        # Get release pipeline by key
        api_response = api_instance.get_release_pipeline_by_key(project_key, pipeline_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ReleasePipelinesBetaApi->get_release_pipeline_by_key: %s\n" % e)
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

# **post_release_pipeline**
> ReleasePipeline post_release_pipeline(project_key, create_release_pipeline_input)

Create a release pipeline

Creates a new release pipeline.  The first release pipeline you create is automatically set as the default release pipeline for your project. To change the default release pipeline, use the [Update project](https://launchdarkly.com/docs/ld-docs/api/projects/patch-project) API to set the `defaultReleasePipelineKey`.  You can create up to 20 release pipelines per project. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import release_pipelines_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.create_release_pipeline_input import CreateReleasePipelineInput
from launchdarkly_api.model.release_pipeline import ReleasePipeline
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
    api_instance = release_pipelines_beta_api.ReleasePipelinesBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    create_release_pipeline_input = CreateReleasePipelineInput(
        description="Standard pipeline to roll out to production",
        key="standard-pipeline",
        name="Standard Pipeline",
        phases=[
            CreatePhaseInput(
                audiences=[
                    AudiencePost(
                        environment_key="environment_key_example",
                        name="name_example",
                        segment_keys=[
                            "segment_keys_example",
                        ],
                        configuration=AudienceConfiguration(
                            release_strategy="release_strategy_example",
                            require_approval=True,
                            notify_member_ids=["1234a56b7c89d012345e678f"],
                            notify_team_keys=["example-reviewer-team"],
                            release_guardian_configuration=ReleaseGuardianConfiguration(
                                monitoring_window_milliseconds=60000,
                                rollout_weight=50,
                                rollback_on_regression=True,
                                randomization_unit="user",
                            ),
                        ),
                    ),
                ],
                name="Phase 1 - Testing",
                configuration={},
            ),
        ],
        tags=["example-tag"],
        is_project_default=True,
        is_legacy=True,
    ) # CreateReleasePipelineInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create a release pipeline
        api_response = api_instance.post_release_pipeline(project_key, create_release_pipeline_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ReleasePipelinesBetaApi->post_release_pipeline: %s\n" % e)
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
import time
import launchdarkly_api
from launchdarkly_api.api import release_pipelines_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.update_release_pipeline_input import UpdateReleasePipelineInput
from launchdarkly_api.model.release_pipeline import ReleasePipeline
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
    api_instance = release_pipelines_beta_api.ReleasePipelinesBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    pipeline_key = "pipelineKey_example" # str | The release pipeline key
    update_release_pipeline_input = UpdateReleasePipelineInput(
        description="Standard pipeline to roll out to production",
        name="Standard Pipeline",
        phases=[
            CreatePhaseInput(
                audiences=[
                    AudiencePost(
                        environment_key="environment_key_example",
                        name="name_example",
                        segment_keys=[
                            "segment_keys_example",
                        ],
                        configuration=AudienceConfiguration(
                            release_strategy="release_strategy_example",
                            require_approval=True,
                            notify_member_ids=["1234a56b7c89d012345e678f"],
                            notify_team_keys=["example-reviewer-team"],
                            release_guardian_configuration=ReleaseGuardianConfiguration(
                                monitoring_window_milliseconds=60000,
                                rollout_weight=50,
                                rollback_on_regression=True,
                                randomization_unit="user",
                            ),
                        ),
                    ),
                ],
                name="Phase 1 - Testing",
                configuration={},
            ),
        ],
        tags=["example-tag"],
    ) # UpdateReleasePipelineInput | 

    # example passing only required values which don't have defaults set
    try:
        # Update a release pipeline
        api_response = api_instance.put_release_pipeline(project_key, pipeline_key, update_release_pipeline_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ReleasePipelinesBetaApi->put_release_pipeline: %s\n" % e)
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

