# launchdarkly_api.SegmentsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_segment**](SegmentsApi.md#delete_segment) | **DELETE** /api/v2/segments/{projKey}/{envKey}/{key} | Delete segment
[**get_expiring_user_targets_for_segment**](SegmentsApi.md#get_expiring_user_targets_for_segment) | **GET** /api/v2/segments/{projKey}/{segmentKey}/expiring-user-targets/{envKey} | Get expiring user targets for segment
[**get_segment**](SegmentsApi.md#get_segment) | **GET** /api/v2/segments/{projKey}/{envKey}/{key} | Get segment
[**get_segment_membership_for_user**](SegmentsApi.md#get_segment_membership_for_user) | **GET** /api/v2/segments/{projKey}/{envKey}/{key}/users/{userKey} | Get Big Segment membership for user
[**get_segments**](SegmentsApi.md#get_segments) | **GET** /api/v2/segments/{projKey}/{envKey} | List segments
[**patch_expiring_user_targets_for_segment**](SegmentsApi.md#patch_expiring_user_targets_for_segment) | **PATCH** /api/v2/segments/{projKey}/{segmentKey}/expiring-user-targets/{envKey} | Update expiring user targets for segment
[**patch_segment**](SegmentsApi.md#patch_segment) | **PATCH** /api/v2/segments/{projKey}/{envKey}/{key} | Patch segment
[**post_segment**](SegmentsApi.md#post_segment) | **POST** /api/v2/segments/{projKey}/{envKey} | Create segment
[**update_big_segment_targets**](SegmentsApi.md#update_big_segment_targets) | **POST** /api/v2/segments/{projKey}/{envKey}/{key}/users | Update targets on a Big Segment


# **delete_segment**
> delete_segment(proj_key, env_key, key)

Delete segment

Delete a user segment.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import segments_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
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
    api_instance = segments_api.SegmentsApi(api_client)
    proj_key = "projKey_example" # str | The project key.
    env_key = "envKey_example" # str | The environment key.
    key = "key_example" # str | The user segment key.

    # example passing only required values which don't have defaults set
    try:
        # Delete segment
        api_instance.delete_segment(proj_key, env_key, key)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling SegmentsApi->delete_segment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **env_key** | **str**| The environment key. |
 **key** | **str**| The user segment key. |

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
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expiring_user_targets_for_segment**
> ExpiringUserTargetGetResponse get_expiring_user_targets_for_segment(proj_key, env_key, segment_key)

Get expiring user targets for segment

Get a list of a segment's user targets that are scheduled for removal

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import segments_api
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.expiring_user_target_get_response import ExpiringUserTargetGetResponse
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
    api_instance = segments_api.SegmentsApi(api_client)
    proj_key = "projKey_example" # str | The project key.
    env_key = "envKey_example" # str | The environment key.
    segment_key = "segmentKey_example" # str | The segment key.

    # example passing only required values which don't have defaults set
    try:
        # Get expiring user targets for segment
        api_response = api_instance.get_expiring_user_targets_for_segment(proj_key, env_key, segment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling SegmentsApi->get_expiring_user_targets_for_segment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **env_key** | **str**| The environment key. |
 **segment_key** | **str**| The segment key. |

### Return type

[**ExpiringUserTargetGetResponse**](ExpiringUserTargetGetResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expiring user target response |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment**
> UserSegment get_segment(proj_key, env_key, key)

Get segment

Get a single user segment by key

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import segments_api
from launchdarkly_api.model.user_segment import UserSegment
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
    api_instance = segments_api.SegmentsApi(api_client)
    proj_key = "projKey_example" # str | The project key.
    env_key = "envKey_example" # str | The environment key.
    key = "key_example" # str | The segment key

    # example passing only required values which don't have defaults set
    try:
        # Get segment
        api_response = api_instance.get_segment(proj_key, env_key, key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling SegmentsApi->get_segment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **env_key** | **str**| The environment key. |
 **key** | **str**| The segment key |

### Return type

[**UserSegment**](UserSegment.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Segment response |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment_membership_for_user**
> BigSegmentTarget get_segment_membership_for_user(proj_key, env_key, key, user_key)

Get Big Segment membership for user

Returns the membership status (included/excluded) for a given user in this segment. This operation does not support basic Segments.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import segments_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.big_segment_target import BigSegmentTarget
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
    api_instance = segments_api.SegmentsApi(api_client)
    proj_key = "projKey_example" # str | The project key.
    env_key = "envKey_example" # str | The environment key.
    key = "key_example" # str | The segment key.
    user_key = "userKey_example" # str | The user key.

    # example passing only required values which don't have defaults set
    try:
        # Get Big Segment membership for user
        api_response = api_instance.get_segment_membership_for_user(proj_key, env_key, key, user_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling SegmentsApi->get_segment_membership_for_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **env_key** | **str**| The environment key. |
 **key** | **str**| The segment key. |
 **user_key** | **str**| The user key. |

### Return type

[**BigSegmentTarget**](BigSegmentTarget.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Segment membership for user response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segments**
> UserSegments get_segments(proj_key, env_key)

List segments

Get a list of all user segments in the given project

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import segments_api
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.user_segments import UserSegments
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
    api_instance = segments_api.SegmentsApi(api_client)
    proj_key = "projKey_example" # str | The project key.
    env_key = "envKey_example" # str | The environment key.

    # example passing only required values which don't have defaults set
    try:
        # List segments
        api_response = api_instance.get_segments(proj_key, env_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling SegmentsApi->get_segments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **env_key** | **str**| The environment key. |

### Return type

[**UserSegments**](UserSegments.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Segment collection response |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_expiring_user_targets_for_segment**
> ExpiringUserTargetPatchResponse patch_expiring_user_targets_for_segment(proj_key, env_key, segment_key, patch_segment_request)

Update expiring user targets for segment

Update the list of a segment's user targets that are scheduled for removal<br /><br />Requires a semantic patch representation of the desired changes to the resource. To learn more about semantic patches, read [Updates](/reference#updates-via-semantic-patches).<br /><br />If the request is well-formed but any of its instructions failed to process, this operation returns status code `200`. In this case, the response `errors` array will be non-empty.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import segments_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.expiring_user_target_patch_response import ExpiringUserTargetPatchResponse
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.patch_segment_request import PatchSegmentRequest
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
    api_instance = segments_api.SegmentsApi(api_client)
    proj_key = "projKey_example" # str | The project key.
    env_key = "envKey_example" # str | The environment key.
    segment_key = "segmentKey_example" # str | The user segment key.
    patch_segment_request = PatchSegmentRequest(
        comment="comment_example",
        instructions=[
            PatchSegmentInstruction(
                kind="kind_example",
                user_key="user_key_example",
                target_type="target_type_example",
                value=1,
                version=1,
            ),
        ],
    ) # PatchSegmentRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update expiring user targets for segment
        api_response = api_instance.patch_expiring_user_targets_for_segment(proj_key, env_key, segment_key, patch_segment_request)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling SegmentsApi->patch_expiring_user_targets_for_segment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **env_key** | **str**| The environment key. |
 **segment_key** | **str**| The user segment key. |
 **patch_segment_request** | [**PatchSegmentRequest**](PatchSegmentRequest.md)|  |

### Return type

[**ExpiringUserTargetPatchResponse**](ExpiringUserTargetPatchResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expiring user target response. |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_segment**
> UserSegment patch_segment(proj_key, env_key, key, patch_with_comment)

Patch segment

Update a user segment. The request body must be a valid JSON patch or JSON merge patch document. To learn more about semantic patches, read [Updates](/#section/Overview/Updates).

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import segments_api
from launchdarkly_api.model.user_segment import UserSegment
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.patch_with_comment import PatchWithComment
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
    api_instance = segments_api.SegmentsApi(api_client)
    proj_key = "projKey_example" # str | The project key.
    env_key = "envKey_example" # str | The environment key.
    key = "key_example" # str | The user segment key.
    patch_with_comment = PatchWithComment(
        patch=JSONPatch([
            PatchOperation(
                op="replace",
                path="/biscuits",
                value=None,
            ),
        ]),
        comment="comment_example",
    ) # PatchWithComment | 

    # example passing only required values which don't have defaults set
    try:
        # Patch segment
        api_response = api_instance.patch_segment(proj_key, env_key, key, patch_with_comment)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling SegmentsApi->patch_segment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **env_key** | **str**| The environment key. |
 **key** | **str**| The user segment key. |
 **patch_with_comment** | [**PatchWithComment**](PatchWithComment.md)|  |

### Return type

[**UserSegment**](UserSegment.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Segment response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_segment**
> UserSegment post_segment(proj_key, env_key, segment_body)

Create segment

Create a new user segment

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import segments_api
from launchdarkly_api.model.user_segment import UserSegment
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.segment_body import SegmentBody
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
    api_instance = segments_api.SegmentsApi(api_client)
    proj_key = "projKey_example" # str | The project key.
    env_key = "envKey_example" # str | The environment key.
    segment_body = SegmentBody(
        name="name_example",
        key="key_example",
        description="description_example",
        tags=["ops"],
        unbounded=True,
    ) # SegmentBody | 

    # example passing only required values which don't have defaults set
    try:
        # Create segment
        api_response = api_instance.post_segment(proj_key, env_key, segment_body)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling SegmentsApi->post_segment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **env_key** | **str**| The environment key. |
 **segment_body** | [**SegmentBody**](SegmentBody.md)|  |

### Return type

[**UserSegment**](UserSegment.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Segment response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_big_segment_targets**
> update_big_segment_targets(proj_key, env_key, key, segment_user_state)

Update targets on a Big Segment

Update targets included or excluded in a Big Segment

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import segments_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.segment_user_state import SegmentUserState
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
    api_instance = segments_api.SegmentsApi(api_client)
    proj_key = "projKey_example" # str | The project key.
    env_key = "envKey_example" # str | The environment key.
    key = "key_example" # str | The segment key.
    segment_user_state = SegmentUserState(
        included=SegmentUserList(
            add=[
                "add_example",
            ],
            remove=[
                "remove_example",
            ],
        ),
        excluded=SegmentUserList(
            add=[
                "add_example",
            ],
            remove=[
                "remove_example",
            ],
        ),
    ) # SegmentUserState | 

    # example passing only required values which don't have defaults set
    try:
        # Update targets on a Big Segment
        api_instance.update_big_segment_targets(proj_key, env_key, key, segment_user_state)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling SegmentsApi->update_big_segment_targets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key. |
 **env_key** | **str**| The environment key. |
 **key** | **str**| The segment key. |
 **segment_user_state** | [**SegmentUserState**](SegmentUserState.md)|  |

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
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

