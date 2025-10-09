# launchdarkly_api.AnnouncementsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_announcement_public**](AnnouncementsApi.md#create_announcement_public) | **POST** /api/v2/announcements | Create an announcement
[**delete_announcement_public**](AnnouncementsApi.md#delete_announcement_public) | **DELETE** /api/v2/announcements/{announcementId} | Delete an announcement
[**get_announcements_public**](AnnouncementsApi.md#get_announcements_public) | **GET** /api/v2/announcements | Get announcements
[**update_announcement_public**](AnnouncementsApi.md#update_announcement_public) | **PATCH** /api/v2/announcements/{announcementId} | Update an announcement


# **create_announcement_public**
> AnnouncementResponse create_announcement_public(create_announcement_body)

Create an announcement

Create an announcement

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.announcement_response import AnnouncementResponse
from launchdarkly_api.models.create_announcement_body import CreateAnnouncementBody
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
    api_instance = launchdarkly_api.AnnouncementsApi(api_client)
    create_announcement_body = launchdarkly_api.CreateAnnouncementBody() # CreateAnnouncementBody | Announcement request body

    try:
        # Create an announcement
        api_response = api_instance.create_announcement_public(create_announcement_body)
        print("The response of AnnouncementsApi->create_announcement_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->create_announcement_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_announcement_body** | [**CreateAnnouncementBody**](CreateAnnouncementBody.md)| Announcement request body | 

### Return type

[**AnnouncementResponse**](AnnouncementResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created announcement |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_announcement_public**
> delete_announcement_public(announcement_id)

Delete an announcement

Delete an announcement

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
    api_instance = launchdarkly_api.AnnouncementsApi(api_client)
    announcement_id = '1234567890' # str | 

    try:
        # Delete an announcement
        api_instance.delete_announcement_public(announcement_id)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->delete_announcement_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **announcement_id** | **str**|  | 

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
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_announcements_public**
> GetAnnouncementsPublic200Response get_announcements_public(status=status, limit=limit, offset=offset)

Get announcements

Get announcements

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.get_announcements_public200_response import GetAnnouncementsPublic200Response
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
    api_instance = launchdarkly_api.AnnouncementsApi(api_client)
    status = 'active' # str | Filter announcements by status. (optional)
    limit = 56 # int | The number of announcements to return. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # Get announcements
        api_response = api_instance.get_announcements_public(status=status, limit=limit, offset=offset)
        print("The response of AnnouncementsApi->get_announcements_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->get_announcements_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter announcements by status. | [optional] 
 **limit** | **int**| The number of announcements to return. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**GetAnnouncementsPublic200Response**](GetAnnouncementsPublic200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Announcement response |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_announcement_public**
> AnnouncementResponse update_announcement_public(announcement_id, announcement_patch_operation)

Update an announcement

Update an announcement

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.announcement_patch_operation import AnnouncementPatchOperation
from launchdarkly_api.models.announcement_response import AnnouncementResponse
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
    api_instance = launchdarkly_api.AnnouncementsApi(api_client)
    announcement_id = '1234567890' # str | 
    announcement_patch_operation = [launchdarkly_api.AnnouncementPatchOperation()] # List[AnnouncementPatchOperation] | Update announcement request body

    try:
        # Update an announcement
        api_response = api_instance.update_announcement_public(announcement_id, announcement_patch_operation)
        print("The response of AnnouncementsApi->update_announcement_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->update_announcement_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **announcement_id** | **str**|  | 
 **announcement_patch_operation** | [**List[AnnouncementPatchOperation]**](AnnouncementPatchOperation.md)| Update announcement request body | 

### Return type

[**AnnouncementResponse**](AnnouncementResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated announcement |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

