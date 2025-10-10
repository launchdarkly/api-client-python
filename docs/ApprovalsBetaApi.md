# launchdarkly_api.ApprovalsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_approval_request_settings**](ApprovalsBetaApi.md#get_approval_request_settings) | **GET** /api/v2/approval-requests/projects/{projectKey}/settings | Get approval request settings
[**patch_approval_request**](ApprovalsBetaApi.md#patch_approval_request) | **PATCH** /api/v2/approval-requests/{id} | Update approval request
[**patch_approval_request_settings**](ApprovalsBetaApi.md#patch_approval_request_settings) | **PATCH** /api/v2/approval-requests/projects/{projectKey}/settings | Update approval request settings
[**patch_flag_config_approval_request**](ApprovalsBetaApi.md#patch_flag_config_approval_request) | **PATCH** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id} | Update flag approval request


# **get_approval_request_settings**
> Dict[str, ApprovalRequestSettingWithEnvs] get_approval_request_settings(ld_api_version, project_key, environment_key=environment_key, resource_kind=resource_kind, expand=expand)

Get approval request settings

Get the approval request settings for the given project, optionally filtered by environment and resource kind.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.approval_request_setting_with_envs import ApprovalRequestSettingWithEnvs
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
    api_instance = launchdarkly_api.ApprovalsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    environment_key = 'environment_key_example' # str | An environment key filter to apply to the approval request settings. (optional)
    resource_kind = 'resource_kind_example' # str | A resource kind filter to apply to the approval request settings. (optional)
    expand = 'default,strict' # str | A comma-separated list of fields to expand in the response. Options include 'default' and 'strict'. (optional)

    try:
        # Get approval request settings
        api_response = api_instance.get_approval_request_settings(ld_api_version, project_key, environment_key=environment_key, resource_kind=resource_kind, expand=expand)
        print("The response of ApprovalsBetaApi->get_approval_request_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsBetaApi->get_approval_request_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **environment_key** | **str**| An environment key filter to apply to the approval request settings. | [optional] 
 **resource_kind** | **str**| A resource kind filter to apply to the approval request settings. | [optional] 
 **expand** | **str**| A comma-separated list of fields to expand in the response. Options include &#39;default&#39; and &#39;strict&#39;. | [optional] 

### Return type

[**Dict[str, ApprovalRequestSettingWithEnvs]**](ApprovalRequestSettingWithEnvs.md)

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

# **patch_approval_request**
> FlagConfigApprovalRequestResponse patch_approval_request(id)

Update approval request

Perform a partial update to an approval request. Updating an approval request uses the semantic patch format. This endpoint works with any approval requests.

To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](https://launchdarkly.com/docs/api#updates-using-semantic-patch).

### Instructions

Semantic patch requests support the following `kind` instruction for updating an approval request.

#### addReviewers

Adds the specified members and teams to the existing list of reviewers. You must include at least one of `notifyMemberIds` and `notifyTeamKeys`.

##### Parameters

- `notifyMemberIds`: (Optional) List of member IDs.
- `notifyTeamKeys`: (Optional) List of team keys.

Here's an example:

```json
{
  "instructions": [{
    "kind": "addReviewers",
    "notifyMemberIds": [ "user-key-123abc", "user-key-456def" ],
    "notifyTeamKeys": [ "team-key-789abc"]
  }]
}
```


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.flag_config_approval_request_response import FlagConfigApprovalRequestResponse
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
    api_instance = launchdarkly_api.ApprovalsBetaApi(api_client)
    id = 'id_example' # str | The approval ID

    try:
        # Update approval request
        api_response = api_instance.patch_approval_request(id)
        print("The response of ApprovalsBetaApi->patch_approval_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsBetaApi->patch_approval_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The approval ID | 

### Return type

[**FlagConfigApprovalRequestResponse**](FlagConfigApprovalRequestResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Approval request response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_approval_request_settings**
> Dict[str, ApprovalRequestSettingWithEnvs] patch_approval_request_settings(ld_api_version, project_key, approval_request_settings_patch=approval_request_settings_patch)

Update approval request settings

Perform a partial update to approval request settings

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.approval_request_setting_with_envs import ApprovalRequestSettingWithEnvs
from launchdarkly_api.models.approval_request_settings_patch import ApprovalRequestSettingsPatch
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
    api_instance = launchdarkly_api.ApprovalsBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | 
    approval_request_settings_patch = launchdarkly_api.ApprovalRequestSettingsPatch() # ApprovalRequestSettingsPatch | Approval request settings to update (optional)

    try:
        # Update approval request settings
        api_response = api_instance.patch_approval_request_settings(ld_api_version, project_key, approval_request_settings_patch=approval_request_settings_patch)
        print("The response of ApprovalsBetaApi->patch_approval_request_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsBetaApi->patch_approval_request_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**|  | 
 **approval_request_settings_patch** | [**ApprovalRequestSettingsPatch**](ApprovalRequestSettingsPatch.md)| Approval request settings to update | [optional] 

### Return type

[**Dict[str, ApprovalRequestSettingWithEnvs]**](ApprovalRequestSettingWithEnvs.md)

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

# **patch_flag_config_approval_request**
> FlagConfigApprovalRequestResponse patch_flag_config_approval_request(project_key, feature_flag_key, environment_key, id)

Update flag approval request

Perform a partial update to an approval request. Updating an approval request uses the semantic patch format. This endpoint requires a feature flag key, and can only be used for updating approval requests for flags.

To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](https://launchdarkly.com/docs/api#updates-using-semantic-patch).

### Instructions

Semantic patch requests support the following `kind` instruction for updating an approval request.

#### addReviewers

Adds the specified members and teams to the existing list of reviewers. You must include at least one of `notifyMemberIds` and `notifyTeamKeys`.

##### Parameters

- `notifyMemberIds`: (Optional) List of member IDs.
- `notifyTeamKeys`: (Optional) List of team keys.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.flag_config_approval_request_response import FlagConfigApprovalRequestResponse
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
    api_instance = launchdarkly_api.ApprovalsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    environment_key = 'environment_key_example' # str | The environment key
    id = 'id_example' # str | The approval ID

    try:
        # Update flag approval request
        api_response = api_instance.patch_flag_config_approval_request(project_key, feature_flag_key, environment_key, id)
        print("The response of ApprovalsBetaApi->patch_flag_config_approval_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsBetaApi->patch_flag_config_approval_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **environment_key** | **str**| The environment key | 
 **id** | **str**| The approval ID | 

### Return type

[**FlagConfigApprovalRequestResponse**](FlagConfigApprovalRequestResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Approval request response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

