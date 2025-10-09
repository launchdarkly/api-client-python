# launchdarkly_api.FlagLinksBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_flag_link**](FlagLinksBetaApi.md#create_flag_link) | **POST** /api/v2/flag-links/projects/{projectKey}/flags/{featureFlagKey} | Create flag link
[**delete_flag_link**](FlagLinksBetaApi.md#delete_flag_link) | **DELETE** /api/v2/flag-links/projects/{projectKey}/flags/{featureFlagKey}/{id} | Delete flag link
[**get_flag_links**](FlagLinksBetaApi.md#get_flag_links) | **GET** /api/v2/flag-links/projects/{projectKey}/flags/{featureFlagKey} | List flag links
[**update_flag_link**](FlagLinksBetaApi.md#update_flag_link) | **PATCH** /api/v2/flag-links/projects/{projectKey}/flags/{featureFlagKey}/{id} | Update flag link


# **create_flag_link**
> FlagLinkRep create_flag_link(project_key, feature_flag_key, flag_link_post)

Create flag link

Create a new flag link. Flag links let you reference external resources and associate them with your flags.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.flag_link_post import FlagLinkPost
from launchdarkly_api.models.flag_link_rep import FlagLinkRep
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
    api_instance = launchdarkly_api.FlagLinksBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    flag_link_post = {"deepLink":"https://example.com/archives/123123123","description":"Example link description","key":"flag-link-key-123abc","title":"Example link title"} # FlagLinkPost | 

    try:
        # Create flag link
        api_response = api_instance.create_flag_link(project_key, feature_flag_key, flag_link_post)
        print("The response of FlagLinksBetaApi->create_flag_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlagLinksBetaApi->create_flag_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **flag_link_post** | [**FlagLinkPost**](FlagLinkPost.md)|  | 

### Return type

[**FlagLinkRep**](FlagLinkRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Flag link response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_flag_link**
> delete_flag_link(project_key, feature_flag_key, id)

Delete flag link

Delete a flag link by ID or key.

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
    api_instance = launchdarkly_api.FlagLinksBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    id = 'id_example' # str | The flag link ID or Key

    try:
        # Delete flag link
        api_instance.delete_flag_link(project_key, feature_flag_key, id)
    except Exception as e:
        print("Exception when calling FlagLinksBetaApi->delete_flag_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **id** | **str**| The flag link ID or Key | 

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

# **get_flag_links**
> FlagLinkCollectionRep get_flag_links(project_key, feature_flag_key)

List flag links

Get a list of all flag links.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.flag_link_collection_rep import FlagLinkCollectionRep
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
    api_instance = launchdarkly_api.FlagLinksBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key

    try:
        # List flag links
        api_response = api_instance.get_flag_links(project_key, feature_flag_key)
        print("The response of FlagLinksBetaApi->get_flag_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlagLinksBetaApi->get_flag_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **feature_flag_key** | **str**| The feature flag key | 

### Return type

[**FlagLinkCollectionRep**](FlagLinkCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag link collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_flag_link**
> FlagLinkRep update_flag_link(project_key, feature_flag_key, id, patch_operation)

Update flag link

Update a flag link. Updating a flag link uses a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.flag_link_rep import FlagLinkRep
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
    api_instance = launchdarkly_api.FlagLinksBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    id = 'id_example' # str | The flag link ID
    patch_operation = [{"op":"replace","path":"/title","value":"Updated flag link title"}] # List[PatchOperation] | 

    try:
        # Update flag link
        api_response = api_instance.update_flag_link(project_key, feature_flag_key, id, patch_operation)
        print("The response of FlagLinksBetaApi->update_flag_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlagLinksBetaApi->update_flag_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **id** | **str**| The flag link ID | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**FlagLinkRep**](FlagLinkRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag link response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

