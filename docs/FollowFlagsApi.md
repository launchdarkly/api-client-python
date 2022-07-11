# launchdarkly_api.FollowFlagsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_flag_followers**](FollowFlagsApi.md#delete_flag_followers) | **DELETE** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/followers/{memberId} | Remove a member as a follower of a flag in a project and environment
[**get_flag_followers**](FollowFlagsApi.md#get_flag_followers) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/followers | Get followers of a flag in a project and environment
[**get_followers_by_proj_env**](FollowFlagsApi.md#get_followers_by_proj_env) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/followers | Get followers of all flags in a given project and environment
[**put_flag_followers**](FollowFlagsApi.md#put_flag_followers) | **PUT** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/followers/{memberId} | Add a member as a follower of a flag in a project and environment


# **delete_flag_followers**
> delete_flag_followers(project_key, feature_flag_key, environment_key, member_id)

Remove a member as a follower of a flag in a project and environment

Remove a member as a follower to a flag in a project and environment

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import follow_flags_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
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
    api_instance = follow_flags_api.FollowFlagsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    member_id = "memberId_example" # str | The memberId of the member to remove as a follower of the flag

    # example passing only required values which don't have defaults set
    try:
        # Remove a member as a follower of a flag in a project and environment
        api_instance.delete_flag_followers(project_key, feature_flag_key, environment_key, member_id)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FollowFlagsApi->delete_flag_followers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **environment_key** | **str**| The environment key |
 **member_id** | **str**| The memberId of the member to remove as a follower of the flag |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flag_followers**
> FlagFollowersGetRep get_flag_followers(project_key, feature_flag_key, environment_key)

Get followers of a flag in a project and environment

Get a list of members following a flag in a project and environment

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import follow_flags_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.flag_followers_get_rep import FlagFollowersGetRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
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
    api_instance = follow_flags_api.FollowFlagsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key

    # example passing only required values which don't have defaults set
    try:
        # Get followers of a flag in a project and environment
        api_response = api_instance.get_flag_followers(project_key, feature_flag_key, environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FollowFlagsApi->get_flag_followers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **environment_key** | **str**| The environment key |

### Return type

[**FlagFollowersGetRep**](FlagFollowersGetRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag followers response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_followers_by_proj_env**
> FlagFollowersByProjEnvGetRep get_followers_by_proj_env(project_key, environment_key)

Get followers of all flags in a given project and environment

Get followers of all flags in a given environment and project

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import follow_flags_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.flag_followers_by_proj_env_get_rep import FlagFollowersByProjEnvGetRep
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
    api_instance = follow_flags_api.FollowFlagsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key

    # example passing only required values which don't have defaults set
    try:
        # Get followers of all flags in a given project and environment
        api_response = api_instance.get_followers_by_proj_env(project_key, environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FollowFlagsApi->get_followers_by_proj_env: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |

### Return type

[**FlagFollowersByProjEnvGetRep**](FlagFollowersByProjEnvGetRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag followers response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_flag_followers**
> put_flag_followers(project_key, feature_flag_key, environment_key, member_id)

Add a member as a follower of a flag in a project and environment

Add a member as a follower to a flag in a project and environment

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import follow_flags_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
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
    api_instance = follow_flags_api.FollowFlagsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    member_id = "memberId_example" # str | The memberId of the member to add as a follower of the flag

    # example passing only required values which don't have defaults set
    try:
        # Add a member as a follower of a flag in a project and environment
        api_instance.put_flag_followers(project_key, feature_flag_key, environment_key, member_id)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling FollowFlagsApi->put_flag_followers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **environment_key** | **str**| The environment key |
 **member_id** | **str**| The memberId of the member to add as a follower of the flag |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

