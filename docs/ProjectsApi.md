# launchdarkly_api.ProjectsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /api/v2/projects/{projectKey} | Delete project
[**get_flag_defaults_by_project**](ProjectsApi.md#get_flag_defaults_by_project) | **GET** /api/v2/projects/{projectKey}/flag-defaults | Get flag defaults for project
[**get_project**](ProjectsApi.md#get_project) | **GET** /api/v2/projects/{projectKey} | Get project
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /api/v2/projects | List projects
[**patch_flag_defaults_by_project**](ProjectsApi.md#patch_flag_defaults_by_project) | **PATCH** /api/v2/projects/{projectKey}/flag-defaults | Update flag default for project
[**patch_project**](ProjectsApi.md#patch_project) | **PATCH** /api/v2/projects/{projectKey} | Update project
[**post_project**](ProjectsApi.md#post_project) | **POST** /api/v2/projects | Create project
[**put_flag_defaults_by_project**](ProjectsApi.md#put_flag_defaults_by_project) | **PUT** /api/v2/projects/{projectKey}/flag-defaults | Create or update flag defaults for project


# **delete_project**
> delete_project(project_key)

Delete project

Delete a project by key. Use this endpoint with caution. Deleting a project will delete all associated environments and feature flags. You cannot delete the last project in an account.

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
    api_instance = launchdarkly_api.ProjectsApi(api_client)
    project_key = 'project_key_example' # str | The project key

    try:
        # Delete project
        api_instance.delete_project(project_key)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 

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

# **get_flag_defaults_by_project**
> FlagDefaultsRep get_flag_defaults_by_project(project_key)

Get flag defaults for project

Get the flag defaults for a specific project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.flag_defaults_rep import FlagDefaultsRep
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
    api_instance = launchdarkly_api.ProjectsApi(api_client)
    project_key = 'project_key_example' # str | The project key

    try:
        # Get flag defaults for project
        api_response = api_instance.get_flag_defaults_by_project(project_key)
        print("The response of ProjectsApi->get_flag_defaults_by_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_flag_defaults_by_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 

### Return type

[**FlagDefaultsRep**](FlagDefaultsRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag defaults response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(project_key, expand=expand)

Get project

Get a single project by key.

### Expanding the project response

LaunchDarkly supports one field for expanding the "Get project" response. By default, these fields are **not** included in the response.

To expand the response, append the `expand` query parameter and add a comma-separated list with any of the following fields:
* `environments` includes a paginated list of the project environments.

For example, `expand=environments` includes the `environments` field for the project in the response.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.project import Project
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
    api_instance = launchdarkly_api.ProjectsApi(api_client)
    project_key = 'project_key_example' # str | The project key.
    expand = 'expand_example' # str | A comma-separated list of properties that can reveal additional information in the response. (optional)

    try:
        # Get project
        api_response = api_instance.get_project(project_key, expand=expand)
        print("The response of ProjectsApi->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key. | 
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> Projects get_projects(limit=limit, offset=offset, filter=filter, sort=sort, expand=expand)

List projects

Return a list of projects.

By default, this returns the first 20 projects. Page through this list with the `limit` parameter and by following the `first`, `prev`, `next`, and `last` links in the `_links` field that returns. If those links do not appear, the pages they refer to don't exist. For example, the `first` and `prev` links will be missing from the response on the first page, because there is no previous page and you cannot return to the first page when you are already on the first page.

### Filtering projects

LaunchDarkly supports three fields for filters:
- `query` is a string that matches against the projects' names and keys. It is not case sensitive.
- `tags` is a `+`-separated list of project tags. It filters the list of projects that have all of the tags in the list.
- `keys` is a `|` separated list of project keys. It filters the list to projects that have any of the keys in the list.

For example, the filter `filter=query:abc,tags:tag-1+tag-2` matches projects with the string `abc` in their name or key and also are tagged with `tag-1` and `tag-2`. The filter is not case-sensitive.

The documented values for `filter` query parameters are prior to URL encoding. For example, the `+` in `filter=tags:tag-1+tag-2` must be encoded to `%2B`.

### Sorting projects

LaunchDarkly supports two fields for sorting:
- `name` sorts by project name.
- `createdOn` sorts by the creation date of the project.

For example, `sort=name` sorts the response by project name in ascending order.

### Expanding the projects response

LaunchDarkly supports one field for expanding the "List projects" response. By default, these fields are **not** included in the response.

To expand the response, append the `expand` query parameter and add a comma-separated list with the `environments` field.

* `environments` includes a paginated list of the project environments.

For example, `expand=environments` includes the `environments` field for each project in the response.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.projects import Projects
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
    api_instance = launchdarkly_api.ProjectsApi(api_client)
    limit = 56 # int | The number of projects to return in the response. Defaults to 20. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and returns the next `limit` items. (optional)
    filter = 'filter_example' # str | A comma-separated list of filters. Each filter is constructed as `field:value`. (optional)
    sort = 'sort_example' # str | A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order. (optional)
    expand = 'expand_example' # str | A comma-separated list of properties that can reveal additional information in the response. (optional)

    try:
        # List projects
        api_response = api_instance.get_projects(limit=limit, offset=offset, filter=filter, sort=sort, expand=expand)
        print("The response of ProjectsApi->get_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of projects to return in the response. Defaults to 20. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and returns the next &#x60;limit&#x60; items. | [optional] 
 **filter** | **str**| A comma-separated list of filters. Each filter is constructed as &#x60;field:value&#x60;. | [optional] 
 **sort** | **str**| A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order. | [optional] 
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. | [optional] 

### Return type

[**Projects**](Projects.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_flag_defaults_by_project**
> UpsertPayloadRep patch_flag_defaults_by_project(project_key, patch_operation)

Update flag default for project

Update a flag default. Updating a flag default uses a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) or [JSON merge patch](https://datatracker.ietf.org/doc/html/rfc7386) representation of the desired changes. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.patch_operation import PatchOperation
from launchdarkly_api.models.upsert_payload_rep import UpsertPayloadRep
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
    api_instance = launchdarkly_api.ProjectsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    patch_operation = [launchdarkly_api.PatchOperation()] # List[PatchOperation] | 

    try:
        # Update flag default for project
        api_response = api_instance.patch_flag_defaults_by_project(project_key, patch_operation)
        print("The response of ProjectsApi->patch_flag_defaults_by_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->patch_flag_defaults_by_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**UpsertPayloadRep**](UpsertPayloadRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag default response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_project**
> ProjectRep patch_project(project_key, patch_operation)

Update project

Update a project. Updating a project uses a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates).<br/><br/>To add an element to the project fields that are arrays, set the `path` to the name of the field and then append `/<array index>`. Use `/0` to add to the beginning of the array. Use `/-` to add to the end of the array.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.patch_operation import PatchOperation
from launchdarkly_api.models.project_rep import ProjectRep
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
    api_instance = launchdarkly_api.ProjectsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    patch_operation = [{"op":"add","path":"/tags/0","value":"another-tag"}] # List[PatchOperation] | 

    try:
        # Update project
        api_response = api_instance.patch_project(project_key, patch_operation)
        print("The response of ProjectsApi->patch_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->patch_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**ProjectRep**](ProjectRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project**
> ProjectRep post_project(project_post)

Create project

Create a new project with the given key and name. Project keys must be unique within an account.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.project_post import ProjectPost
from launchdarkly_api.models.project_rep import ProjectRep
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
    api_instance = launchdarkly_api.ProjectsApi(api_client)
    project_post = {"key":"project-key-123abc","name":"My Project"} # ProjectPost | 

    try:
        # Create project
        api_response = api_instance.post_project(project_post)
        print("The response of ProjectsApi->post_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->post_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_post** | [**ProjectPost**](ProjectPost.md)|  | 

### Return type

[**ProjectRep**](ProjectRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Project response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_flag_defaults_by_project**
> UpsertPayloadRep put_flag_defaults_by_project(project_key, upsert_flag_defaults_payload)

Create or update flag defaults for project

Create or update flag defaults for a project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.upsert_flag_defaults_payload import UpsertFlagDefaultsPayload
from launchdarkly_api.models.upsert_payload_rep import UpsertPayloadRep
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
    api_instance = launchdarkly_api.ProjectsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    upsert_flag_defaults_payload = launchdarkly_api.UpsertFlagDefaultsPayload() # UpsertFlagDefaultsPayload | 

    try:
        # Create or update flag defaults for project
        api_response = api_instance.put_flag_defaults_by_project(project_key, upsert_flag_defaults_payload)
        print("The response of ProjectsApi->put_flag_defaults_by_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->put_flag_defaults_by_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **upsert_flag_defaults_payload** | [**UpsertFlagDefaultsPayload**](UpsertFlagDefaultsPayload.md)|  | 

### Return type

[**UpsertPayloadRep**](UpsertPayloadRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag default response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

