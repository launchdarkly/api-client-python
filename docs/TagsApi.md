# launchdarkly_api.TagsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tags**](TagsApi.md#get_tags) | **GET** /api/v2/tags | List tags


# **get_tags**
> TagsCollection get_tags()

List tags

Get a list of tags.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import tags_api
from launchdarkly_api.model.tags_collection import TagsCollection
from launchdarkly_api.model.error import Error
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
    api_instance = tags_api.TagsApi(api_client)
    kind = [
        "kind_example",
    ] # [str] | Fetch tags associated with the specified resource type. Options are `flag`, `project`, `environment`, `segment`. Returns all types by default. (optional)
    pre = "pre_example" # str | Return tags with the specified prefix (optional)
    archived = True # bool | Whether or not to return archived flags (optional)
    limit = 1 # int | The number of tags to return. Maximum is 1000. (optional)
    offset = 1 # int | The index of the first tag to return. Default is 0. (optional)
    as_of = "asOf_example" # str | The time to retrieve tags as of. Default is the current time. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List tags
        api_response = api_instance.get_tags(kind=kind, pre=pre, archived=archived, limit=limit, offset=offset, as_of=as_of)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling TagsApi->get_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **[str]**| Fetch tags associated with the specified resource type. Options are &#x60;flag&#x60;, &#x60;project&#x60;, &#x60;environment&#x60;, &#x60;segment&#x60;. Returns all types by default. | [optional]
 **pre** | **str**| Return tags with the specified prefix | [optional]
 **archived** | **bool**| Whether or not to return archived flags | [optional]
 **limit** | **int**| The number of tags to return. Maximum is 1000. | [optional]
 **offset** | **int**| The index of the first tag to return. Default is 0. | [optional]
 **as_of** | **str**| The time to retrieve tags as of. Default is the current time. | [optional]

### Return type

[**TagsCollection**](TagsCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag collection response |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate Limited |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

