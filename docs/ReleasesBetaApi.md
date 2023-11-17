# launchdarkly_api.ReleasesBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_release_by_flag_key**](ReleasesBetaApi.md#get_release_by_flag_key) | **GET** /api/v2/flags/{projectKey}/{flagKey}/release | Get release for flag
[**patch_release_by_flag_key**](ReleasesBetaApi.md#patch_release_by_flag_key) | **PATCH** /api/v2/flags/{projectKey}/{flagKey}/release | Patch release for flag


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
> patch_release_by_flag_key(project_key, flag_key, json_patch)

Patch release for flag

Update currently active release for a flag. Updating releases requires the [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) format. To learn more, read [Updates](/#section/Overview/Updates).  You can only use this endpoint to mark a release phase complete or incomplete. To indicate which phase to update, use the array index in the `path`. For example, to mark the first phase of a release as complete, use the following request body:  ```   [     {       \"op\": \"replace\",       \"path\": \"/phase/0/complete\",       \"value\": true     }   ] ``` 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import releases_beta_api
from launchdarkly_api.model.json_patch import JSONPatch
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
        api_instance.patch_release_by_flag_key(project_key, flag_key, json_patch)
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

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

