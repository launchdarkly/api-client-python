# launchdarkly_api.ViewsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_view**](ViewsBetaApi.md#create_view) | **POST** /api/v2/projects/{projectKey}/views | Create view
[**delete_view**](ViewsBetaApi.md#delete_view) | **DELETE** /api/v2/projects/{projectKey}/views/{viewKey} | Delete view
[**get_linked_resources**](ViewsBetaApi.md#get_linked_resources) | **GET** /api/v2/projects/{projectKey}/views/{viewKey}/linked/{resourceType} | Get linked resources
[**get_linked_views**](ViewsBetaApi.md#get_linked_views) | **GET** /api/v2/projects/{projectKey}/view-associations/{resourceType}/{resourceKey} | Get linked views for a given resource
[**get_view**](ViewsBetaApi.md#get_view) | **GET** /api/v2/projects/{projectKey}/views/{viewKey} | Get view
[**get_views**](ViewsBetaApi.md#get_views) | **GET** /api/v2/projects/{projectKey}/views | List views
[**link_resource**](ViewsBetaApi.md#link_resource) | **POST** /api/v2/projects/{projectKey}/views/{viewKey}/link/{resourceType} | Link resource
[**unlink_resource**](ViewsBetaApi.md#unlink_resource) | **DELETE** /api/v2/projects/{projectKey}/views/{viewKey}/link/{resourceType} | Unlink resource
[**update_view**](ViewsBetaApi.md#update_view) | **PATCH** /api/v2/projects/{projectKey}/views/{viewKey} | Update view


# **create_view**
> View create_view(ld_api_version, project_key, view_post)

Create view

Create a new view in the given project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.view import View
from launchdarkly_api.models.view_post import ViewPost
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
    api_instance = launchdarkly_api.ViewsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    view_post = launchdarkly_api.ViewPost() # ViewPost | View object to create

    try:
        # Create view
        api_response = api_instance.create_view(ld_api_version, project_key, view_post)
        print("The response of ViewsBetaApi->create_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsBetaApi->create_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **view_post** | [**ViewPost**](ViewPost.md)| View object to create | 

### Return type

[**View**](View.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_view**
> delete_view(ld_api_version, project_key, view_key)

Delete view

Delete a specific view by its key.

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
    api_instance = launchdarkly_api.ViewsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    view_key = 'my-view' # str | 

    try:
        # Delete view
        api_instance.delete_view(ld_api_version, project_key, view_key)
    except Exception as e:
        print("Exception when calling ViewsBetaApi->delete_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **view_key** | **str**|  | 

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
**204** | No content |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_resources**
> ViewLinkedResources get_linked_resources(ld_api_version, project_key, view_key, resource_type, limit=limit, offset=offset, sort=sort)

Get linked resources

Get a list of all linked resources for a given view.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.view_linked_resources import ViewLinkedResources
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
    api_instance = launchdarkly_api.ViewsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    view_key = 'my-view' # str | 
    resource_type = 'flags' # str | 
    limit = 56 # int | The number of views to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    sort = linkedAt # str | Field to sort by. Default field is `linkedAt`, default order is ascending. (optional) (default to linkedAt)

    try:
        # Get linked resources
        api_response = api_instance.get_linked_resources(ld_api_version, project_key, view_key, resource_type, limit=limit, offset=offset, sort=sort)
        print("The response of ViewsBetaApi->get_linked_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsBetaApi->get_linked_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **view_key** | **str**|  | 
 **resource_type** | **str**|  | 
 **limit** | **int**| The number of views to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 
 **sort** | **str**| Field to sort by. Default field is &#x60;linkedAt&#x60;, default order is ascending. | [optional] [default to linkedAt]

### Return type

[**ViewLinkedResources**](ViewLinkedResources.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_views**
> Views get_linked_views(ld_api_version, project_key, resource_type, resource_key, environment_id=environment_id, limit=limit, offset=offset)

Get linked views for a given resource

Get a list of all linked views for a resource. Flags, AI configs and metrics are identified by key. Segments are identified by segment ID.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.views import Views
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
    api_instance = launchdarkly_api.ViewsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    resource_type = 'flags' # str | 
    resource_key = 'my-flag' # str | 
    environment_id = '6890ff25c3e3830ba1a352e4' # str | Environment ID. Required when resourceType is 'segments' (optional)
    limit = 56 # int | The number of views to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # Get linked views for a given resource
        api_response = api_instance.get_linked_views(ld_api_version, project_key, resource_type, resource_key, environment_id=environment_id, limit=limit, offset=offset)
        print("The response of ViewsBetaApi->get_linked_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsBetaApi->get_linked_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_key** | **str**|  | 
 **environment_id** | **str**| Environment ID. Required when resourceType is &#39;segments&#39; | [optional] 
 **limit** | **int**| The number of views to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**Views**](Views.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view**
> View get_view(ld_api_version, project_key, view_key, sort=sort, limit=limit, offset=offset, filter=filter, expand=expand)

Get view

Retrieve a specific view by its key.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.view import View
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
    api_instance = launchdarkly_api.ViewsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    view_key = 'my-view' # str | 
    sort = 'sort_example' # str | A sort to apply to the list of views. (optional)
    limit = 56 # int | The number of views to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = 'filter_example' # str | A filter to apply to the list of views. (optional)
    expand = ['expand_example'] # List[str] | A comma-separated list of fields to expand. (optional)

    try:
        # Get view
        api_response = api_instance.get_view(ld_api_version, project_key, view_key, sort=sort, limit=limit, offset=offset, filter=filter, expand=expand)
        print("The response of ViewsBetaApi->get_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsBetaApi->get_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **view_key** | **str**|  | 
 **sort** | **str**| A sort to apply to the list of views. | [optional] 
 **limit** | **int**| The number of views to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 
 **filter** | **str**| A filter to apply to the list of views. | [optional] 
 **expand** | [**List[str]**](str.md)| A comma-separated list of fields to expand. | [optional] 

### Return type

[**View**](View.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_views**
> Views get_views(ld_api_version, project_key, sort=sort, limit=limit, offset=offset, filter=filter, expand=expand)

List views

Get a list of all views in the given project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.views import Views
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
    api_instance = launchdarkly_api.ViewsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    sort = 'sort_example' # str | A sort to apply to the list of views. (optional)
    limit = 56 # int | The number of views to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    filter = 'filter_example' # str | A filter to apply to the list of views. (optional)
    expand = ['expand_example'] # List[str] | A comma-separated list of fields to expand. (optional)

    try:
        # List views
        api_response = api_instance.get_views(ld_api_version, project_key, sort=sort, limit=limit, offset=offset, filter=filter, expand=expand)
        print("The response of ViewsBetaApi->get_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsBetaApi->get_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **sort** | **str**| A sort to apply to the list of views. | [optional] 
 **limit** | **int**| The number of views to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 
 **filter** | **str**| A filter to apply to the list of views. | [optional] 
 **expand** | [**List[str]**](str.md)| A comma-separated list of fields to expand. | [optional] 

### Return type

[**Views**](Views.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_resource**
> LinkResourceSuccessResponse link_resource(ld_api_version, project_key, view_key, resource_type, view_link_request)

Link resource

Link one or multiple resources to a view:
- Link flags using flag keys
- Link AI configs using AI config keys
- Link metrics using metric keys
- Link segments using segment IDs


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.link_resource_success_response import LinkResourceSuccessResponse
from launchdarkly_api.models.view_link_request import ViewLinkRequest
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
    api_instance = launchdarkly_api.ViewsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    view_key = 'my-view' # str | 
    resource_type = 'flags' # str | 
    view_link_request = launchdarkly_api.ViewLinkRequest() # ViewLinkRequest | The resource to link to the view. Flags are identified by key. Segments are identified by segment ID.

    try:
        # Link resource
        api_response = api_instance.link_resource(ld_api_version, project_key, view_key, resource_type, view_link_request)
        print("The response of ViewsBetaApi->link_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsBetaApi->link_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **view_key** | **str**|  | 
 **resource_type** | **str**|  | 
 **view_link_request** | [**ViewLinkRequest**](ViewLinkRequest.md)| The resource to link to the view. Flags are identified by key. Segments are identified by segment ID. | 

### Return type

[**LinkResourceSuccessResponse**](LinkResourceSuccessResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_resource**
> UnlinkResourceSuccessResponse unlink_resource(ld_api_version, project_key, view_key, resource_type, view_link_request)

Unlink resource

Unlink one or multiple resources from a view:
- Unlink flags using flag keys
- Unlink segments using segment IDs
- Unlink AI configs using AI config keys
- Unlink metrics using metric keys


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.unlink_resource_success_response import UnlinkResourceSuccessResponse
from launchdarkly_api.models.view_link_request import ViewLinkRequest
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
    api_instance = launchdarkly_api.ViewsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    view_key = 'my-view' # str | 
    resource_type = 'flags' # str | 
    view_link_request = launchdarkly_api.ViewLinkRequest() # ViewLinkRequest | The resource to link to the view. Flags are identified by key. Segments are identified by segment ID.

    try:
        # Unlink resource
        api_response = api_instance.unlink_resource(ld_api_version, project_key, view_key, resource_type, view_link_request)
        print("The response of ViewsBetaApi->unlink_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsBetaApi->unlink_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **view_key** | **str**|  | 
 **resource_type** | **str**|  | 
 **view_link_request** | [**ViewLinkRequest**](ViewLinkRequest.md)| The resource to link to the view. Flags are identified by key. Segments are identified by segment ID. | 

### Return type

[**UnlinkResourceSuccessResponse**](UnlinkResourceSuccessResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with unlink details |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_view**
> View update_view(ld_api_version, project_key, view_key, view_patch)

Update view

Edit an existing view.

The request body must be a JSON object of the fields to update. The values you include replace the existing values for the fields.

Here's an example:
  ```
    {
      "description": "Example updated description",
      "tags": ["new-tag"]
    }
  ```


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.view import View
from launchdarkly_api.models.view_patch import ViewPatch
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
    api_instance = launchdarkly_api.ViewsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    view_key = 'my-view' # str | 
    view_patch = launchdarkly_api.ViewPatch() # ViewPatch | A JSON representation of the view including only the fields to update.

    try:
        # Update view
        api_response = api_instance.update_view(ld_api_version, project_key, view_key, view_patch)
        print("The response of ViewsBetaApi->update_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsBetaApi->update_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **view_key** | **str**|  | 
 **view_patch** | [**ViewPatch**](ViewPatch.md)| A JSON representation of the view including only the fields to update. | 

### Return type

[**View**](View.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

