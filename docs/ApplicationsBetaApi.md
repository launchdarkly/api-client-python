# launchdarkly_api.ApplicationsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_application**](ApplicationsBetaApi.md#delete_application) | **DELETE** /api/v2/applications/{applicationKey} | Delete application
[**delete_application_version**](ApplicationsBetaApi.md#delete_application_version) | **DELETE** /api/v2/applications/{applicationKey}/versions/{versionKey} | Delete application version
[**get_application**](ApplicationsBetaApi.md#get_application) | **GET** /api/v2/applications/{applicationKey} | Get application by key
[**get_application_versions**](ApplicationsBetaApi.md#get_application_versions) | **GET** /api/v2/applications/{applicationKey}/versions | Get application versions by application key
[**get_applications**](ApplicationsBetaApi.md#get_applications) | **GET** /api/v2/applications | Get applications
[**patch_application**](ApplicationsBetaApi.md#patch_application) | **PATCH** /api/v2/applications/{applicationKey} | Update application
[**patch_application_version**](ApplicationsBetaApi.md#patch_application_version) | **PATCH** /api/v2/applications/{applicationKey}/versions/{versionKey} | Update application version


# **delete_application**
> delete_application(application_key)

Delete application

Delete an application.

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
    api_instance = launchdarkly_api.ApplicationsBetaApi(api_client)
    application_key = 'application_key_example' # str | The application key

    try:
        # Delete application
        api_instance.delete_application(application_key)
    except Exception as e:
        print("Exception when calling ApplicationsBetaApi->delete_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_key** | **str**| The application key | 

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
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_version**
> delete_application_version(application_key, version_key)

Delete application version

Delete an application version.

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
    api_instance = launchdarkly_api.ApplicationsBetaApi(api_client)
    application_key = 'application_key_example' # str | The application key
    version_key = 'version_key_example' # str | The application version key

    try:
        # Delete application version
        api_instance.delete_application_version(application_key, version_key)
    except Exception as e:
        print("Exception when calling ApplicationsBetaApi->delete_application_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_key** | **str**| The application key | 
 **version_key** | **str**| The application version key | 

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
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> ApplicationRep get_application(application_key, expand=expand)

Get application by key


Retrieve an application by the application key.

### Expanding the application response

LaunchDarkly supports expanding the "Get application" response to include additional fields.

To expand the response, append the `expand` query parameter and include the following:

* `flags` includes details on the flags that have been evaluated by the application

For example, use `?expand=flags` to include the `flags` field in the response. By default, this field is **not** included in the response.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.application_rep import ApplicationRep
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
    api_instance = launchdarkly_api.ApplicationsBetaApi(api_client)
    application_key = 'application_key_example' # str | The application key
    expand = 'expand_example' # str | A comma-separated list of properties that can reveal additional information in the response. Options: `flags`. (optional)

    try:
        # Get application by key
        api_response = api_instance.get_application(application_key, expand=expand)
        print("The response of ApplicationsBetaApi->get_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsBetaApi->get_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_key** | **str**| The application key | 
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. Options: &#x60;flags&#x60;. | [optional] 

### Return type

[**ApplicationRep**](ApplicationRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_versions**
> ApplicationVersionsCollectionRep get_application_versions(application_key, filter=filter, limit=limit, offset=offset, sort=sort)

Get application versions by application key

Get a list of versions for a specific application in an account.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.application_versions_collection_rep import ApplicationVersionsCollectionRep
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
    api_instance = launchdarkly_api.ApplicationsBetaApi(api_client)
    application_key = 'application_key_example' # str | The application key
    filter = 'filter_example' # str | Accepts filter by `key`, `name`, `supported`, and `autoAdded`. To learn more about the filter syntax, read [Filtering applications and application versions](https://launchdarkly.com/docs/api/applications-beta#filtering-applications-and-application-versions). (optional)
    limit = 56 # int | The number of versions to return. Defaults to 50. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    sort = 'sort_example' # str | Accepts sorting order and fields. Fields can be comma separated. Possible fields are `creationDate`, `name`. Examples: `sort=name` sort by names ascending, `sort=-name,creationDate` sort by names descending and creationDate ascending. (optional)

    try:
        # Get application versions by application key
        api_response = api_instance.get_application_versions(application_key, filter=filter, limit=limit, offset=offset, sort=sort)
        print("The response of ApplicationsBetaApi->get_application_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsBetaApi->get_application_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_key** | **str**| The application key | 
 **filter** | **str**| Accepts filter by &#x60;key&#x60;, &#x60;name&#x60;, &#x60;supported&#x60;, and &#x60;autoAdded&#x60;. To learn more about the filter syntax, read [Filtering applications and application versions](https://launchdarkly.com/docs/api/applications-beta#filtering-applications-and-application-versions). | [optional] 
 **limit** | **int**| The number of versions to return. Defaults to 50. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 
 **sort** | **str**| Accepts sorting order and fields. Fields can be comma separated. Possible fields are &#x60;creationDate&#x60;, &#x60;name&#x60;. Examples: &#x60;sort&#x3D;name&#x60; sort by names ascending, &#x60;sort&#x3D;-name,creationDate&#x60; sort by names descending and creationDate ascending. | [optional] 

### Return type

[**ApplicationVersionsCollectionRep**](ApplicationVersionsCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application versions response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications**
> ApplicationCollectionRep get_applications(filter=filter, limit=limit, offset=offset, sort=sort, expand=expand)

Get applications


Get a list of applications.

### Expanding the applications response

LaunchDarkly supports expanding the "Get applications" response to include additional fields.

To expand the response, append the `expand` query parameter and include the following:

* `flags` includes details on the flags that have been evaluated by the application

For example, use `?expand=flags` to include the `flags` field in the response. By default, this field is **not** included in the response.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.application_collection_rep import ApplicationCollectionRep
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
    api_instance = launchdarkly_api.ApplicationsBetaApi(api_client)
    filter = 'filter_example' # str | Accepts filter by `key`, `name`, `kind`, and `autoAdded`. To learn more about the filter syntax, read [Filtering applications and application versions](https://launchdarkly.com/docs/api/applications-beta#filtering-applications-and-application-versions). (optional)
    limit = 56 # int | The number of applications to return. Defaults to 10. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    sort = 'sort_example' # str | Accepts sorting order and fields. Fields can be comma separated. Possible fields are `creationDate`, `name`. Examples: `sort=name` sort by names ascending, `sort=-name,creationDate` sort by names descending and creationDate ascending. (optional)
    expand = 'expand_example' # str | A comma-separated list of properties that can reveal additional information in the response. Options: `flags`. (optional)

    try:
        # Get applications
        api_response = api_instance.get_applications(filter=filter, limit=limit, offset=offset, sort=sort, expand=expand)
        print("The response of ApplicationsBetaApi->get_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsBetaApi->get_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Accepts filter by &#x60;key&#x60;, &#x60;name&#x60;, &#x60;kind&#x60;, and &#x60;autoAdded&#x60;. To learn more about the filter syntax, read [Filtering applications and application versions](https://launchdarkly.com/docs/api/applications-beta#filtering-applications-and-application-versions). | [optional] 
 **limit** | **int**| The number of applications to return. Defaults to 10. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 
 **sort** | **str**| Accepts sorting order and fields. Fields can be comma separated. Possible fields are &#x60;creationDate&#x60;, &#x60;name&#x60;. Examples: &#x60;sort&#x3D;name&#x60; sort by names ascending, &#x60;sort&#x3D;-name,creationDate&#x60; sort by names descending and creationDate ascending. | [optional] 
 **expand** | **str**| A comma-separated list of properties that can reveal additional information in the response. Options: &#x60;flags&#x60;. | [optional] 

### Return type

[**ApplicationCollectionRep**](ApplicationCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applications response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_application**
> ApplicationRep patch_application(application_key, patch_operation)

Update application

Update an application. You can update the `description` and `kind` fields. Requires a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes to the application. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.application_rep import ApplicationRep
from launchdarkly_api.models.patch_operation import PatchOperation
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
    api_instance = launchdarkly_api.ApplicationsBetaApi(api_client)
    application_key = 'application_key_example' # str | The application key
    patch_operation = [{"op":"replace","path":"/description","value":"Updated description"}] # List[PatchOperation] | 

    try:
        # Update application
        api_response = api_instance.patch_application(application_key, patch_operation)
        print("The response of ApplicationsBetaApi->patch_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsBetaApi->patch_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_key** | **str**| The application key | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**ApplicationRep**](ApplicationRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_application_version**
> ApplicationVersionRep patch_application_version(application_key, version_key, patch_operation)

Update application version

Update an application version. You can update the `supported` field. Requires a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes to the application version. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.application_version_rep import ApplicationVersionRep
from launchdarkly_api.models.patch_operation import PatchOperation
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
    api_instance = launchdarkly_api.ApplicationsBetaApi(api_client)
    application_key = 'application_key_example' # str | The application key
    version_key = 'version_key_example' # str | The application version key
    patch_operation = [{"op":"replace","path":"/supported","value":"false"}] # List[PatchOperation] | 

    try:
        # Update application version
        api_response = api_instance.patch_application_version(application_key, version_key, patch_operation)
        print("The response of ApplicationsBetaApi->patch_application_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsBetaApi->patch_application_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_key** | **str**| The application key | 
 **version_key** | **str**| The application version key | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**ApplicationVersionRep**](ApplicationVersionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application version response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

