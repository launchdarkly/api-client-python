# launchdarkly_api.ApprovalsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_approval_request**](ApprovalsApi.md#delete_approval_request) | **DELETE** /api/v2/approval-requests/{id} | Delete approval request
[**delete_approval_request_for_flag**](ApprovalsApi.md#delete_approval_request_for_flag) | **DELETE** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id} | Delete approval request for a flag
[**get_approval_for_flag**](ApprovalsApi.md#get_approval_for_flag) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id} | Get approval request for a flag
[**get_approval_request**](ApprovalsApi.md#get_approval_request) | **GET** /api/v2/approval-requests/{id} | Get approval request
[**get_approval_requests**](ApprovalsApi.md#get_approval_requests) | **GET** /api/v2/approval-requests | List approval requests
[**get_approvals_for_flag**](ApprovalsApi.md#get_approvals_for_flag) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests | List approval requests for a flag
[**post_approval_request**](ApprovalsApi.md#post_approval_request) | **POST** /api/v2/approval-requests | Create approval request
[**post_approval_request_apply**](ApprovalsApi.md#post_approval_request_apply) | **POST** /api/v2/approval-requests/{id}/apply | Apply approval request
[**post_approval_request_apply_for_flag**](ApprovalsApi.md#post_approval_request_apply_for_flag) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id}/apply | Apply approval request for a flag
[**post_approval_request_for_flag**](ApprovalsApi.md#post_approval_request_for_flag) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests | Create approval request for a flag
[**post_approval_request_review**](ApprovalsApi.md#post_approval_request_review) | **POST** /api/v2/approval-requests/{id}/reviews | Review approval request
[**post_approval_request_review_for_flag**](ApprovalsApi.md#post_approval_request_review_for_flag) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id}/reviews | Review approval request for a flag
[**post_flag_copy_config_approval_request**](ApprovalsApi.md#post_flag_copy_config_approval_request) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests-flag-copy | Create approval request to copy flag configurations across environments


# **delete_approval_request**
> delete_approval_request(id)

Delete approval request

Delete an approval request.

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
    api_instance = launchdarkly_api.ApprovalsApi(api_client)
    id = 'id_example' # str | The approval request ID

    try:
        # Delete approval request
        api_instance.delete_approval_request(id)
    except Exception as e:
        print("Exception when calling ApprovalsApi->delete_approval_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The approval request ID | 

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

# **delete_approval_request_for_flag**
> delete_approval_request_for_flag(project_key, feature_flag_key, environment_key, id)

Delete approval request for a flag

Delete an approval request for a feature flag.

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
    api_instance = launchdarkly_api.ApprovalsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    environment_key = 'environment_key_example' # str | The environment key
    id = 'id_example' # str | The feature flag approval request ID

    try:
        # Delete approval request for a flag
        api_instance.delete_approval_request_for_flag(project_key, feature_flag_key, environment_key, id)
    except Exception as e:
        print("Exception when calling ApprovalsApi->delete_approval_request_for_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **environment_key** | **str**| The environment key | 
 **id** | **str**| The feature flag approval request ID | 

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

# **get_approval_for_flag**
> FlagConfigApprovalRequestResponse get_approval_for_flag(project_key, feature_flag_key, environment_key, id)

Get approval request for a flag

Get a single approval request for a feature flag.

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
    api_instance = launchdarkly_api.ApprovalsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    environment_key = 'environment_key_example' # str | The environment key
    id = 'id_example' # str | The feature flag approval request ID

    try:
        # Get approval request for a flag
        api_response = api_instance.get_approval_for_flag(project_key, feature_flag_key, environment_key, id)
        print("The response of ApprovalsApi->get_approval_for_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsApi->get_approval_for_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **environment_key** | **str**| The environment key | 
 **id** | **str**| The feature flag approval request ID | 

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

# **get_approval_request**
> ExpandableApprovalRequestResponse get_approval_request(id, expand=expand)

Get approval request

Get an approval request by approval request ID.

### Expanding approval response

LaunchDarkly supports the `expand` query param to include additional fields in the response, with the following fields:

- `environments` includes the environments the approval request relates to
- `flag` includes the flag the approval request belongs to
- `project` includes the project the approval request belongs to
- `resource` includes details on the resource (flag or segment) the approval request relates to

For example, `expand=project,flag` includes the `project` and `flag` fields in the response.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.expandable_approval_request_response import ExpandableApprovalRequestResponse
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
    api_instance = launchdarkly_api.ApprovalsApi(api_client)
    id = 'id_example' # str | The approval request ID
    expand = 'expand_example' # str | A comma-separated list of fields to expand in the response. Supported fields are explained above. (optional)

    try:
        # Get approval request
        api_response = api_instance.get_approval_request(id, expand=expand)
        print("The response of ApprovalsApi->get_approval_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsApi->get_approval_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The approval request ID | 
 **expand** | **str**| A comma-separated list of fields to expand in the response. Supported fields are explained above. | [optional] 

### Return type

[**ExpandableApprovalRequestResponse**](ExpandableApprovalRequestResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Approval request response |  -  |
**400** | Invalid Request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Unable to find approval request |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approval_requests**
> ExpandableApprovalRequestsResponse get_approval_requests(filter=filter, expand=expand, limit=limit, offset=offset)

List approval requests

Get all approval requests.

### Filtering approvals

LaunchDarkly supports the `filter` query param for filtering, with the following fields:

- `notifyMemberIds` filters for only approvals that are assigned to a member in the specified list. For example: `filter=notifyMemberIds anyOf ["memberId1", "memberId2"]`.
- `requestorId` filters for only approvals that correspond to the ID of the member who requested the approval. For example: `filter=requestorId equals 457034721476302714390214`.
- `resourceId` filters for only approvals that correspond to the the specified resource identifier. For example: `filter=resourceId equals proj/my-project:env/my-environment:flag/my-flag`.
- `resourceKind` filters for only approvals that correspond to the specified resource kind. For example: `filter=resourceKind equals flag`. Currently, `flag`, `segment`, and `aiConfig` resource kinds are supported.
- `reviewStatus` filters for only approvals which correspond to the review status in the specified list. The possible values are `approved`, `declined`, and `pending`. For example: `filter=reviewStatus anyOf ["pending", "approved"]`.
- `status` filters for only approvals which correspond to the status in the specified list. The possible values are `pending`, `scheduled`, `failed`, and `completed`. For example: `filter=status anyOf ["pending", "scheduled"]`.

You can also apply multiple filters at once. For example, setting `filter=projectKey equals my-project, reviewStatus anyOf ["pending","approved"]` matches approval requests which correspond to the `my-project` project key, and a review status of either `pending` or `approved`.

### Expanding approval response

LaunchDarkly supports the `expand` query param to include additional fields in the response, with the following fields:

- `flag` includes the flag the approval request belongs to
- `project` includes the project the approval request belongs to
- `environments` includes the environments the approval request relates to

For example, `expand=project,flag` includes the `project` and `flag` fields in the response.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.expandable_approval_requests_response import ExpandableApprovalRequestsResponse
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
    api_instance = launchdarkly_api.ApprovalsApi(api_client)
    filter = 'filter_example' # str | A comma-separated list of filters. Each filter is of the form `field operator value`. Supported fields are explained above. (optional)
    expand = 'expand_example' # str | A comma-separated list of fields to expand in the response. Supported fields are explained above. (optional)
    limit = 56 # int | The number of approvals to return. Defaults to 20. Maximum limit is 200. (optional)
    offset = 56 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    try:
        # List approval requests
        api_response = api_instance.get_approval_requests(filter=filter, expand=expand, limit=limit, offset=offset)
        print("The response of ApprovalsApi->get_approval_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsApi->get_approval_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A comma-separated list of filters. Each filter is of the form &#x60;field operator value&#x60;. Supported fields are explained above. | [optional] 
 **expand** | **str**| A comma-separated list of fields to expand in the response. Supported fields are explained above. | [optional] 
 **limit** | **int**| The number of approvals to return. Defaults to 20. Maximum limit is 200. | [optional] 
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional] 

### Return type

[**ExpandableApprovalRequestsResponse**](ExpandableApprovalRequestsResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Approval request collection response |  -  |
**400** | Unsupported filter field. Filter field must be one of: requestorId, projectKey, notifyMemberIds, reviewStatus, or status |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approvals_for_flag**
> FlagConfigApprovalRequestsResponse get_approvals_for_flag(project_key, feature_flag_key, environment_key)

List approval requests for a flag

Get all approval requests for a feature flag.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.flag_config_approval_requests_response import FlagConfigApprovalRequestsResponse
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
    api_instance = launchdarkly_api.ApprovalsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    environment_key = 'environment_key_example' # str | The environment key

    try:
        # List approval requests for a flag
        api_response = api_instance.get_approvals_for_flag(project_key, feature_flag_key, environment_key)
        print("The response of ApprovalsApi->get_approvals_for_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsApi->get_approvals_for_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **environment_key** | **str**| The environment key | 

### Return type

[**FlagConfigApprovalRequestsResponse**](FlagConfigApprovalRequestsResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Approval request collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_approval_request**
> ApprovalRequestResponse post_approval_request(create_approval_request_request)

Create approval request

Create an approval request.

This endpoint requires a list of `instructions`, in semantic patch format, that will be applied when the approval request is approved and applied.

### Flags

If you are creating an approval request for a flag, you can use the following `instructions`:

- `addVariation`
- `removeVariation`
- `updateVariation`
- `updateDefaultVariation`

For details on using these instructions, read [Update feature flag](https://launchdarkly.com/docs/api/feature-flags/patch-feature-flag).

To create an approval for a flag specific to an environment, use [Create approval request for a flag](https://launchdarkly.com/docs/api/approvals/post-approval-request-for-flag).

### AI Configs

If you are creating an approval request for an AI Config, you can use the semantic patch instructions listed under [Update AI Config targeting](https://launchdarkly.com/docs/api/ai-configs/patch-ai-config-targeting).

### Segments

If you are creating an approval request for a segment, you can use the semantic patch instructions listed under [Patch segment](https://launchdarkly.com/docs/api/segments/patch-segment).


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.approval_request_response import ApprovalRequestResponse
from launchdarkly_api.models.create_approval_request_request import CreateApprovalRequestRequest
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
    api_instance = launchdarkly_api.ApprovalsApi(api_client)
    create_approval_request_request = launchdarkly_api.CreateApprovalRequestRequest() # CreateApprovalRequestRequest | 

    try:
        # Create approval request
        api_response = api_instance.post_approval_request(create_approval_request_request)
        print("The response of ApprovalsApi->post_approval_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsApi->post_approval_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_approval_request_request** | [**CreateApprovalRequestRequest**](CreateApprovalRequestRequest.md)|  | 

### Return type

[**ApprovalRequestResponse**](ApprovalRequestResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Approval request response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_approval_request_apply**
> ApprovalRequestResponse post_approval_request_apply(id, post_approval_request_apply_request)

Apply approval request

Apply an approval request that has been approved. This endpoint works with any approval requests.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.approval_request_response import ApprovalRequestResponse
from launchdarkly_api.models.post_approval_request_apply_request import PostApprovalRequestApplyRequest
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
    api_instance = launchdarkly_api.ApprovalsApi(api_client)
    id = 'id_example' # str | The approval request ID
    post_approval_request_apply_request = launchdarkly_api.PostApprovalRequestApplyRequest() # PostApprovalRequestApplyRequest | 

    try:
        # Apply approval request
        api_response = api_instance.post_approval_request_apply(id, post_approval_request_apply_request)
        print("The response of ApprovalsApi->post_approval_request_apply:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsApi->post_approval_request_apply: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The approval request ID | 
 **post_approval_request_apply_request** | [**PostApprovalRequestApplyRequest**](PostApprovalRequestApplyRequest.md)|  | 

### Return type

[**ApprovalRequestResponse**](ApprovalRequestResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Approval request apply response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_approval_request_apply_for_flag**
> FlagConfigApprovalRequestResponse post_approval_request_apply_for_flag(project_key, feature_flag_key, environment_key, id, post_approval_request_apply_request)

Apply approval request for a flag

Apply an approval request that has been approved. This endpoint requires a feature flag key, and can only be used for applying approval requests on flags.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.flag_config_approval_request_response import FlagConfigApprovalRequestResponse
from launchdarkly_api.models.post_approval_request_apply_request import PostApprovalRequestApplyRequest
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
    api_instance = launchdarkly_api.ApprovalsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    environment_key = 'environment_key_example' # str | The environment key
    id = 'id_example' # str | The feature flag approval request ID
    post_approval_request_apply_request = launchdarkly_api.PostApprovalRequestApplyRequest() # PostApprovalRequestApplyRequest | 

    try:
        # Apply approval request for a flag
        api_response = api_instance.post_approval_request_apply_for_flag(project_key, feature_flag_key, environment_key, id, post_approval_request_apply_request)
        print("The response of ApprovalsApi->post_approval_request_apply_for_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsApi->post_approval_request_apply_for_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **environment_key** | **str**| The environment key | 
 **id** | **str**| The feature flag approval request ID | 
 **post_approval_request_apply_request** | [**PostApprovalRequestApplyRequest**](PostApprovalRequestApplyRequest.md)|  | 

### Return type

[**FlagConfigApprovalRequestResponse**](FlagConfigApprovalRequestResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Approval request apply response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_approval_request_for_flag**
> FlagConfigApprovalRequestResponse post_approval_request_for_flag(project_key, feature_flag_key, environment_key, create_flag_config_approval_request_request)

Create approval request for a flag

Create an approval request for a feature flag.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.create_flag_config_approval_request_request import CreateFlagConfigApprovalRequestRequest
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
    api_instance = launchdarkly_api.ApprovalsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    environment_key = 'environment_key_example' # str | The environment key
    create_flag_config_approval_request_request = launchdarkly_api.CreateFlagConfigApprovalRequestRequest() # CreateFlagConfigApprovalRequestRequest | 

    try:
        # Create approval request for a flag
        api_response = api_instance.post_approval_request_for_flag(project_key, feature_flag_key, environment_key, create_flag_config_approval_request_request)
        print("The response of ApprovalsApi->post_approval_request_for_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsApi->post_approval_request_for_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **environment_key** | **str**| The environment key | 
 **create_flag_config_approval_request_request** | [**CreateFlagConfigApprovalRequestRequest**](CreateFlagConfigApprovalRequestRequest.md)|  | 

### Return type

[**FlagConfigApprovalRequestResponse**](FlagConfigApprovalRequestResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Approval request response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_approval_request_review**
> ApprovalRequestResponse post_approval_request_review(id, post_approval_request_review_request)

Review approval request

Review an approval request by approving or denying changes.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.approval_request_response import ApprovalRequestResponse
from launchdarkly_api.models.post_approval_request_review_request import PostApprovalRequestReviewRequest
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
    api_instance = launchdarkly_api.ApprovalsApi(api_client)
    id = 'id_example' # str | The approval request ID
    post_approval_request_review_request = launchdarkly_api.PostApprovalRequestReviewRequest() # PostApprovalRequestReviewRequest | 

    try:
        # Review approval request
        api_response = api_instance.post_approval_request_review(id, post_approval_request_review_request)
        print("The response of ApprovalsApi->post_approval_request_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsApi->post_approval_request_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The approval request ID | 
 **post_approval_request_review_request** | [**PostApprovalRequestReviewRequest**](PostApprovalRequestReviewRequest.md)|  | 

### Return type

[**ApprovalRequestResponse**](ApprovalRequestResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Approval request review response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**405** | Method not allowed |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_approval_request_review_for_flag**
> FlagConfigApprovalRequestResponse post_approval_request_review_for_flag(project_key, feature_flag_key, environment_key, id, post_approval_request_review_request)

Review approval request for a flag

Review an approval request by approving or denying changes.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.flag_config_approval_request_response import FlagConfigApprovalRequestResponse
from launchdarkly_api.models.post_approval_request_review_request import PostApprovalRequestReviewRequest
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
    api_instance = launchdarkly_api.ApprovalsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    environment_key = 'environment_key_example' # str | The environment key
    id = 'id_example' # str | The feature flag approval request ID
    post_approval_request_review_request = launchdarkly_api.PostApprovalRequestReviewRequest() # PostApprovalRequestReviewRequest | 

    try:
        # Review approval request for a flag
        api_response = api_instance.post_approval_request_review_for_flag(project_key, feature_flag_key, environment_key, id, post_approval_request_review_request)
        print("The response of ApprovalsApi->post_approval_request_review_for_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsApi->post_approval_request_review_for_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **environment_key** | **str**| The environment key | 
 **id** | **str**| The feature flag approval request ID | 
 **post_approval_request_review_request** | [**PostApprovalRequestReviewRequest**](PostApprovalRequestReviewRequest.md)|  | 

### Return type

[**FlagConfigApprovalRequestResponse**](FlagConfigApprovalRequestResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Approval request review response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_flag_copy_config_approval_request**
> FlagConfigApprovalRequestResponse post_flag_copy_config_approval_request(project_key, feature_flag_key, environment_key, create_copy_flag_config_approval_request_request)

Create approval request to copy flag configurations across environments

Create an approval request to copy a feature flag's configuration across environments.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.create_copy_flag_config_approval_request_request import CreateCopyFlagConfigApprovalRequestRequest
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
    api_instance = launchdarkly_api.ApprovalsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    feature_flag_key = 'feature_flag_key_example' # str | The feature flag key
    environment_key = 'environment_key_example' # str | The environment key for the target environment
    create_copy_flag_config_approval_request_request = launchdarkly_api.CreateCopyFlagConfigApprovalRequestRequest() # CreateCopyFlagConfigApprovalRequestRequest | 

    try:
        # Create approval request to copy flag configurations across environments
        api_response = api_instance.post_flag_copy_config_approval_request(project_key, feature_flag_key, environment_key, create_copy_flag_config_approval_request_request)
        print("The response of ApprovalsApi->post_flag_copy_config_approval_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsApi->post_flag_copy_config_approval_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **feature_flag_key** | **str**| The feature flag key | 
 **environment_key** | **str**| The environment key for the target environment | 
 **create_copy_flag_config_approval_request_request** | [**CreateCopyFlagConfigApprovalRequestRequest**](CreateCopyFlagConfigApprovalRequestRequest.md)|  | 

### Return type

[**FlagConfigApprovalRequestResponse**](FlagConfigApprovalRequestResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Approval request response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

