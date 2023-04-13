# launchdarkly_api.ApprovalsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_approval_request**](ApprovalsBetaApi.md#delete_approval_request) | **DELETE** /api/v2/approval-requests/{id} | Delete approval request
[**get_approval_request**](ApprovalsBetaApi.md#get_approval_request) | **GET** /api/v2/approval-requests/{id} | Get approval request
[**get_approval_requests**](ApprovalsBetaApi.md#get_approval_requests) | **GET** /api/v2/approval-requests | List approval requests
[**post_approval_request**](ApprovalsBetaApi.md#post_approval_request) | **POST** /api/v2/approval-requests | Create approval request
[**post_approval_request_apply**](ApprovalsBetaApi.md#post_approval_request_apply) | **POST** /api/v2/approval-requests/{id}/apply | Apply approval request
[**post_approval_request_review**](ApprovalsBetaApi.md#post_approval_request_review) | **POST** /api/v2/approval-requests/{id}/reviews | Review approval request


# **delete_approval_request**
> delete_approval_request(id)

Delete approval request

Delete an approval request.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import approvals_beta_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = approvals_beta_api.ApprovalsBetaApi(api_client)
    id = "id_example" # str | The approval request ID

    # example passing only required values which don't have defaults set
    try:
        # Delete approval request
        api_instance.delete_approval_request(id)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ApprovalsBetaApi->delete_approval_request: %s\n" % e)
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

# **get_approval_request**
> ExpandableApprovalRequestResponse get_approval_request(id)

Get approval request

Get an approval request by approval request ID.  ### Expanding approval response  LaunchDarkly supports the `expand` query param to include additional fields in the response, with the following fields:  - `flag` includes the flag the approval request belongs to - `project` includes the project the approval request belongs to - `environments` includes the environments the approval request relates to  For example, `expand=project,flag` includes the `project` and `flag` fields in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import approvals_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.expandable_approval_request_response import ExpandableApprovalRequestResponse
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = approvals_beta_api.ApprovalsBetaApi(api_client)
    id = "id_example" # str | The approval request ID
    expand = "expand_example" # str | A comma-separated list of fields to expand in the response. Supported fields are explained above. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get approval request
        api_response = api_instance.get_approval_request(id)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ApprovalsBetaApi->get_approval_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get approval request
        api_response = api_instance.get_approval_request(id, expand=expand)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ApprovalsBetaApi->get_approval_request: %s\n" % e)
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
> ExpandableApprovalRequestsResponse get_approval_requests()

List approval requests

Get all approval requests.  ### Filtering approvals  LaunchDarkly supports the `filter` query param for filtering, with the following fields:  - `notifyMemberIds` filters for only approvals that are assigned to a member in the specified list. For example: `filter=notifyMemberIds anyOf [\"memberId1\", \"memberId2\"]`. - `requestorId` filters for only approvals that correspond to the ID of the member who requested the approval. For example: `filter=requestorId equals 457034721476302714390214`. - `resourceId` filters for only approvals that correspond to the the specified resource identifier. For example: `filter=resourceId equals proj/my-project:env/my-environment:flag/my-flag`. - `reviewStatus` filters for only approvals which correspond to the review status in the specified list. The possible values are `approved`, `declined`, and `pending`. For example: `filter=reviewStatus anyOf [\"pending\", \"approved\"]`. - `status` filters for only approvals which correspond to the status in the specified list. The possible values are `pending`, `scheduled`, `failed`, and `completed`. For example: `filter=status anyOf [\"pending\", \"scheduled\"]`.  You can also apply multiple filters at once. For example, setting `filter=projectKey equals my-project, reviewStatus anyOf [\"pending\",\"approved\"]` matches approval requests which correspond to the `my-project` project key, and a review status of either `pending` or `approved`.  ### Expanding approval response  LaunchDarkly supports the `expand` query param to include additional fields in the response, with the following fields:  - `flag` includes the flag the approval request belongs to - `project` includes the project the approval request belongs to - `environments` includes the environments the approval request relates to  For example, `expand=project,flag` includes the `project` and `flag` fields in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import approvals_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.expandable_approval_requests_response import ExpandableApprovalRequestsResponse
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = approvals_beta_api.ApprovalsBetaApi(api_client)
    filter = "filter_example" # str | A comma-separated list of filters. Each filter is of the form `field operator value`. Supported fields are explained above. (optional)
    expand = "expand_example" # str | A comma-separated list of fields to expand in the response. Supported fields are explained above. (optional)
    limit = 1 # int | The number of approvals to return. Defaults to -1, which returns all approvals. (optional)
    offset = 1 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List approval requests
        api_response = api_instance.get_approval_requests(filter=filter, expand=expand, limit=limit, offset=offset)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ApprovalsBetaApi->get_approval_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A comma-separated list of filters. Each filter is of the form &#x60;field operator value&#x60;. Supported fields are explained above. | [optional]
 **expand** | **str**| A comma-separated list of fields to expand in the response. Supported fields are explained above. | [optional]
 **limit** | **int**| The number of approvals to return. Defaults to -1, which returns all approvals. | [optional]
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

# **post_approval_request**
> ApprovalRequestResponse post_approval_request(create_approval_request_request)

Create approval request

Create an approval request.  This endpoint currently supports creating an approval request for a flag across all environments with the following instructions:  - `addVariation` - `removeVariation` - `updateVariation` - `updateDefaultVariation`  For details on using these instructions, read [Update feature flag](/tag/Feature-flags#operation/patchFeatureFlag).  To create an approval for a flag specific to an environment, use [Create approval request for a flag](/tag/Approvals#operation/postApprovalRequestForFlag). 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import approvals_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.approval_request_response import ApprovalRequestResponse
from launchdarkly_api.model.create_approval_request_request import CreateApprovalRequestRequest
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = approvals_beta_api.ApprovalsBetaApi(api_client)
    create_approval_request_request = CreateApprovalRequestRequest(
        resource_id="resource_id_example",
        comment="optional comment",
        description="Requesting to update targeting",
        instructions=Instructions([
            Instruction(
                key=None,
            ),
        ]),
        notify_member_ids=["1234a56b7c89d012345e678f"],
        notify_team_keys=["example-reviewer-team"],
        integration_config=FormVariableConfig(
            key=None,
        ),
    ) # CreateApprovalRequestRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create approval request
        api_response = api_instance.post_approval_request(create_approval_request_request)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ApprovalsBetaApi->post_approval_request: %s\n" % e)
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

Apply an approval request that has been approved.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import approvals_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.post_approval_request_apply_request import PostApprovalRequestApplyRequest
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.approval_request_response import ApprovalRequestResponse
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = approvals_beta_api.ApprovalsBetaApi(api_client)
    id = "id_example" # str | The feature flag approval request ID
    post_approval_request_apply_request = PostApprovalRequestApplyRequest(
        comment="Looks good, thanks for updating",
    ) # PostApprovalRequestApplyRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Apply approval request
        api_response = api_instance.post_approval_request_apply(id, post_approval_request_apply_request)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ApprovalsBetaApi->post_approval_request_apply: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The feature flag approval request ID |
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

# **post_approval_request_review**
> ApprovalRequestResponse post_approval_request_review(id, post_approval_request_review_request)

Review approval request

Review an approval request by approving or denying changes.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import approvals_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.post_approval_request_review_request import PostApprovalRequestReviewRequest
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.approval_request_response import ApprovalRequestResponse
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
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
    api_instance = approvals_beta_api.ApprovalsBetaApi(api_client)
    id = "id_example" # str | The approval request ID
    post_approval_request_review_request = PostApprovalRequestReviewRequest(
        kind="approve",
        comment="Looks good, thanks for updating",
    ) # PostApprovalRequestReviewRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Review approval request
        api_response = api_instance.post_approval_request_review(id, post_approval_request_review_request)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ApprovalsBetaApi->post_approval_request_review: %s\n" % e)
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
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

