# launchdarkly_api.ApprovalsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_approval_request**](ApprovalsApi.md#delete_approval_request) | **DELETE** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id} | Delete approval request
[**get_approval**](ApprovalsApi.md#get_approval) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id} | Get approval request
[**get_approvals**](ApprovalsApi.md#get_approvals) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests | List all approval requests
[**post_approval_request**](ApprovalsApi.md#post_approval_request) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests | Create approval request
[**post_approval_request_apply_request**](ApprovalsApi.md#post_approval_request_apply_request) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id}/apply | Apply approval request
[**post_approval_request_review**](ApprovalsApi.md#post_approval_request_review) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{id}/reviews | Review approval request
[**post_flag_copy_config_approval_request**](ApprovalsApi.md#post_flag_copy_config_approval_request) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests-flag-copy | Create approval request to copy flag configurations across environments


# **delete_approval_request**
> delete_approval_request(project_key, feature_flag_key, environment_key, id)

Delete approval request

Delete an approval request for a feature flag.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import approvals_api
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
    api_instance = approvals_api.ApprovalsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    id = "id_example" # str | The feature flag approval request ID

    # example passing only required values which don't have defaults set
    try:
        # Delete approval request
        api_instance.delete_approval_request(project_key, feature_flag_key, environment_key, id)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ApprovalsApi->delete_approval_request: %s\n" % e)
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

# **get_approval**
> FlagConfigApprovalRequestResponse get_approval(project_key, feature_flag_key, environment_key, id)

Get approval request

Get a single approval request for a feature flag.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import approvals_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.flag_config_approval_request_response import FlagConfigApprovalRequestResponse
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
    api_instance = approvals_api.ApprovalsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    id = "id_example" # str | The feature flag approval request ID

    # example passing only required values which don't have defaults set
    try:
        # Get approval request
        api_response = api_instance.get_approval(project_key, feature_flag_key, environment_key, id)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ApprovalsApi->get_approval: %s\n" % e)
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

# **get_approvals**
> FlagConfigApprovalRequestsResponse get_approvals(project_key, feature_flag_key, environment_key)

List all approval requests

Get all approval requests for a feature flag.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import approvals_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.flag_config_approval_requests_response import FlagConfigApprovalRequestsResponse
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
    api_instance = approvals_api.ApprovalsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key

    # example passing only required values which don't have defaults set
    try:
        # List all approval requests
        api_response = api_instance.get_approvals(project_key, feature_flag_key, environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ApprovalsApi->get_approvals: %s\n" % e)
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
> FlagConfigApprovalRequestResponse post_approval_request(project_key, feature_flag_key, environment_key, create_flag_config_approval_request_request)

Create approval request

Create an approval request for a feature flag.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import approvals_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.flag_config_approval_request_response import FlagConfigApprovalRequestResponse
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.create_flag_config_approval_request_request import CreateFlagConfigApprovalRequestRequest
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
    api_instance = approvals_api.ApprovalsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    create_flag_config_approval_request_request = CreateFlagConfigApprovalRequestRequest(
        comment="optional comment",
        description="Requesting to update targeting",
        instructions=Instructions([
            Instruction(
                key=None,
            ),
        ]),
        notify_member_ids=["1234a56b7c89d012345e678f"],
        notify_team_keys=["example-reviewer-team"],
        execution_date=1,
        operating_on_id="6297ed79dee7dc14e1f9a80c",
        integration_config=FormVariableConfig(
            key=None,
        ),
    ) # CreateFlagConfigApprovalRequestRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create approval request
        api_response = api_instance.post_approval_request(project_key, feature_flag_key, environment_key, create_flag_config_approval_request_request)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ApprovalsApi->post_approval_request: %s\n" % e)
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

# **post_approval_request_apply_request**
> FlagConfigApprovalRequestResponse post_approval_request_apply_request(project_key, feature_flag_key, environment_key, id, post_approval_request_apply_request)

Apply approval request

Apply an approval request that has been approved.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import approvals_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.post_approval_request_apply_request import PostApprovalRequestApplyRequest
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.flag_config_approval_request_response import FlagConfigApprovalRequestResponse
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
    api_instance = approvals_api.ApprovalsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    id = "id_example" # str | The feature flag approval request ID
    post_approval_request_apply_request = PostApprovalRequestApplyRequest(
        comment="Looks good, thanks for updating",
    ) # PostApprovalRequestApplyRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Apply approval request
        api_response = api_instance.post_approval_request_apply_request(project_key, feature_flag_key, environment_key, id, post_approval_request_apply_request)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ApprovalsApi->post_approval_request_apply_request: %s\n" % e)
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

# **post_approval_request_review**
> FlagConfigApprovalRequestResponse post_approval_request_review(project_key, feature_flag_key, environment_key, id, post_approval_request_review_request)

Review approval request

Review an approval request by approving or denying changes.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import approvals_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.post_approval_request_review_request import PostApprovalRequestReviewRequest
from launchdarkly_api.model.flag_config_approval_request_response import FlagConfigApprovalRequestResponse
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
    api_instance = approvals_api.ApprovalsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    id = "id_example" # str | The feature flag approval request ID
    post_approval_request_review_request = PostApprovalRequestReviewRequest(
        kind="approve",
        comment="Looks good, thanks for updating",
    ) # PostApprovalRequestReviewRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Review approval request
        api_response = api_instance.post_approval_request_review(project_key, feature_flag_key, environment_key, id, post_approval_request_review_request)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ApprovalsApi->post_approval_request_review: %s\n" % e)
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
import time
import launchdarkly_api
from launchdarkly_api.api import approvals_api
from launchdarkly_api.model.create_copy_flag_config_approval_request_request import CreateCopyFlagConfigApprovalRequestRequest
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.flag_config_approval_request_response import FlagConfigApprovalRequestResponse
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.status_conflict_error_rep import StatusConflictErrorRep
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
    api_instance = approvals_api.ApprovalsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key for the target environment
    create_copy_flag_config_approval_request_request = CreateCopyFlagConfigApprovalRequestRequest(
        comment="optional comment",
        description="copy flag settings to another environment",
        notify_member_ids=["1234a56b7c89d012345e678f"],
        notify_team_keys=["example-reviewer-team"],
        source=SourceFlag(
            key="example-environment-key",
            version=1,
        ),
        included_actions=["updateOn"],
        excluded_actions=["updateOn"],
    ) # CreateCopyFlagConfigApprovalRequestRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create approval request to copy flag configurations across environments
        api_response = api_instance.post_flag_copy_config_approval_request(project_key, feature_flag_key, environment_key, create_copy_flag_config_approval_request_request)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
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

