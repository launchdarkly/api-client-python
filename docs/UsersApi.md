# launchdarkly_api.UsersApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /api/v2/users/{projKey}/{envKey}/{key} | Delete user
[**get_search_users**](UsersApi.md#get_search_users) | **GET** /api/v2/user-search/{projKey}/{envKey} | Find users
[**get_user**](UsersApi.md#get_user) | **GET** /api/v2/users/{projKey}/{envKey}/{key} | Get user
[**get_users**](UsersApi.md#get_users) | **GET** /api/v2/users/{projKey}/{envKey} | List users


# **delete_user**
> delete_user(proj_key, env_key, key)

Delete user

Delete a user by key

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    proj_key = "projKey_example" # str | The project key
    env_key = "envKey_example" # str | The environment key
    key = "key_example" # str | The user key

    # example passing only required values which don't have defaults set
    try:
        # Delete user
        api_instance.delete_user(proj_key, env_key, key)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **env_key** | **str**| The environment key |
 **key** | **str**| The user key |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Action completed successfully |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_users**
> Users get_search_users(proj_key, env_key)

Find users

Search users in LaunchDarkly based on their last active date, or a search query. Do not use to enumerate all users in LaunchDarkly. Instead use the [List users](getUsers) API resource.  > ### `offset` is deprecated > > `offset` is deprecated and will be removed in a future API version. You can still use `offset` and `limit` for pagination, but we recommend you use `sort` and `searchAfter` instead. `searchAfter` allows you to page through more than 10,000 users, but `offset` and `limit` do not. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import users_api
from launchdarkly_api.model.users import Users
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
    api_instance = users_api.UsersApi(api_client)
    proj_key = "projKey_example" # str | The project key
    env_key = "envKey_example" # str | The environment key
    q = "q_example" # str | Full-text search for users based on name, first name, last name, e-mail address, or key (optional)
    limit = 1 # int | Specifies the maximum number of items in the collection to return (max: 50, default: 20) (optional)
    offset = 1 # int | Specifies the first item to return in the collection (optional)
    after = 1 # int | A unix epoch time in milliseconds specifying the maximum last time a user requested a feature flag from LaunchDarkly (optional)
    search_after = "searchAfter_example" # str | Limits results to users with sort values after the value you specify. You can use this for pagination, but we recommend using the `next` link we provide instead. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Find users
        api_response = api_instance.get_search_users(proj_key, env_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling UsersApi->get_search_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Find users
        api_response = api_instance.get_search_users(proj_key, env_key, q=q, limit=limit, offset=offset, after=after, search_after=search_after)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling UsersApi->get_search_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **env_key** | **str**| The environment key |
 **q** | **str**| Full-text search for users based on name, first name, last name, e-mail address, or key | [optional]
 **limit** | **int**| Specifies the maximum number of items in the collection to return (max: 50, default: 20) | [optional]
 **offset** | **int**| Specifies the first item to return in the collection | [optional]
 **after** | **int**| A unix epoch time in milliseconds specifying the maximum last time a user requested a feature flag from LaunchDarkly | [optional]
 **search_after** | **str**| Limits results to users with sort values after the value you specify. You can use this for pagination, but we recommend using the &#x60;next&#x60; link we provide instead. | [optional]

### Return type

[**Users**](Users.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users collection response |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(proj_key, env_key, key)

Get user

Get a user by key. The `user` object contains all attributes sent in `variation` calls for that key.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import users_api
from launchdarkly_api.model.user import User
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
    api_instance = users_api.UsersApi(api_client)
    proj_key = "projKey_example" # str | The project key
    env_key = "envKey_example" # str | The environment key
    key = "key_example" # str | The user key

    # example passing only required values which don't have defaults set
    try:
        # Get user
        api_response = api_instance.get_user(proj_key, env_key, key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **env_key** | **str**| The environment key |
 **key** | **str**| The user key |

### Return type

[**User**](User.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User response |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> Users get_users(proj_key, env_key)

List users

List all users in the environment. Includes the total count of users. In each page, there is up to `limit` users returned. The default is 20. This is useful for exporting all users in the system for further analysis. To paginate through, follow the `next` link in the `_links` object, as [described in Representations](/#section/Representations). 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import users_api
from launchdarkly_api.model.users import Users
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
    api_instance = users_api.UsersApi(api_client)
    proj_key = "projKey_example" # str | The project key
    env_key = "envKey_example" # str | The environment key
    limit = 1 # int | The number of elements to return per page (optional)
    search_after = "searchAfter_example" # str | Limits results to users with sort values after the value you specify. You can use this for pagination, but we recommend using the `next` link we provide instead. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List users
        api_response = api_instance.get_users(proj_key, env_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List users
        api_response = api_instance.get_users(proj_key, env_key, limit=limit, search_after=search_after)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proj_key** | **str**| The project key |
 **env_key** | **str**| The environment key |
 **limit** | **int**| The number of elements to return per page | [optional]
 **search_after** | **str**| Limits results to users with sort values after the value you specify. You can use this for pagination, but we recommend using the &#x60;next&#x60; link we provide instead. | [optional]

### Return type

[**Users**](Users.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users collection response |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

