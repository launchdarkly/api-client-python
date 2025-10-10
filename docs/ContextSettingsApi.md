# launchdarkly_api.ContextSettingsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**put_context_flag_setting**](ContextSettingsApi.md#put_context_flag_setting) | **PUT** /api/v2/projects/{projectKey}/environments/{environmentKey}/contexts/{contextKind}/{contextKey}/flags/{featureFlagKey} | Update flag settings for context


# **put_context_flag_setting**
> put_context_flag_setting(project_key, environment_key, context_kind, context_key, feature_flag_key, value_put)

Update flag settings for context


Enable or disable a feature flag for a context based on its context kind and key.

In the request body, the `setting` should be the variation value to set for the context. It must match the flag's variation type. For example, for a boolean flag you can use `"setting": true` or `"setting": false` in the request body. For a string flag, you can use `"setting": "existing_variation_value_to_use"`.

Omitting the `setting` attribute from the request body, or including a `setting` of `null`, erases the current setting for a context.

If you previously patched the flag, and the patch included the context's data, LaunchDarkly continues to use that data. If LaunchDarkly has never encountered the combination of the context's key and kind before, it calculates the flag values based on the context kind and key.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.value_put import ValuePut
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
    api_instance = launchdarkly_api.ContextSettingsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    context_kind = 'context_kind_example' # str | The context kind
    context_key = 'context_key_example' # str | The context key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    value_put = launchdarkly_api.ValuePut() # ValuePut | 

    try:
        # Update flag settings for context
        api_instance.put_context_flag_setting(project_key, environment_key, context_kind, context_key, feature_flag_key, value_put)
    except Exception as e:
        print("Exception when calling ContextSettingsApi->put_context_flag_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **context_kind** | **str**| The context kind | 
 **context_key** | **str**| The context key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **value_put** | [**ValuePut**](ValuePut.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Action succeeded |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

