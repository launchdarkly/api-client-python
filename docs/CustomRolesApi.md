# launchdarkly_api.CustomRolesApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_custom_role**](CustomRolesApi.md#delete_custom_role) | **DELETE** /api/v2/roles/{key} | Delete custom role
[**get_custom_role**](CustomRolesApi.md#get_custom_role) | **GET** /api/v2/roles/{key} | Get custom role
[**get_custom_roles**](CustomRolesApi.md#get_custom_roles) | **GET** /api/v2/roles | List custom roles
[**patch_custom_role**](CustomRolesApi.md#patch_custom_role) | **PATCH** /api/v2/roles/{key} | Update custom role
[**post_custom_role**](CustomRolesApi.md#post_custom_role) | **POST** /api/v2/roles | Create custom role


# **delete_custom_role**
> delete_custom_role(key)

Delete custom role

Delete a custom role by key

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import custom_roles_api
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
    api_instance = custom_roles_api.CustomRolesApi(api_client)
    key = "key_example" # str | The key of the custom role to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete custom role
        api_instance.delete_custom_role(key)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CustomRolesApi->delete_custom_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the custom role to delete |

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
**404** | Invalid resource specifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_role**
> CustomRolePost get_custom_role(key)

Get custom role

Get a single custom role by key or ID

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import custom_roles_api
from launchdarkly_api.model.custom_role_post import CustomRolePost
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
    api_instance = custom_roles_api.CustomRolesApi(api_client)
    key = "key_example" # str | The custom role's key or ID

    # example passing only required values which don't have defaults set
    try:
        # Get custom role
        api_response = api_instance.get_custom_role(key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CustomRolesApi->get_custom_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The custom role&#39;s key or ID |

### Return type

[**CustomRolePost**](CustomRolePost.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom role response |  -  |
**401** | Invalid access token |  -  |
**403** | Access to the requested resource was denied |  -  |
**404** | Invalid resource specifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_roles**
> CustomRoles get_custom_roles()

List custom roles

Get a complete list of custom roles. Custom roles let you create flexible policies providing fine-grained access control to everything in LaunchDarkly, from feature flags to goals, environments, and teams. With custom roles, it's possible to enforce access policies that meet your exact workflow needs. Custom roles are available to customers on our enterprise plans. If you're interested in learning more about our enterprise plans, contact sales@launchdarkly.com.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import custom_roles_api
from launchdarkly_api.model.custom_roles import CustomRoles
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
    api_instance = custom_roles_api.CustomRolesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List custom roles
        api_response = api_instance.get_custom_roles()
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CustomRolesApi->get_custom_roles: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomRoles**](CustomRoles.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom roles collection response. |  -  |
**401** | Invalid access token. |  -  |
**403** | Access to the requested resource was denied |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_custom_role**
> CustomRole patch_custom_role(key, patch_with_comment)

Update custom role

Update a single custom role. The request must be a valid JSON Patch document describing the changes to be made to the custom role.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import custom_roles_api
from launchdarkly_api.model.custom_role import CustomRole
from launchdarkly_api.model.patch_with_comment import PatchWithComment
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
    api_instance = custom_roles_api.CustomRolesApi(api_client)
    key = "key_example" # str | The key of the custom role to update
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
        # Update custom role
        api_response = api_instance.patch_custom_role(key, patch_with_comment)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CustomRolesApi->patch_custom_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the custom role to update |
 **patch_with_comment** | [**PatchWithComment**](PatchWithComment.md)|  |

### Return type

[**CustomRole**](CustomRole.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom role response |  -  |
**400** | Invalid request body |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource specifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_custom_role**
> CustomRole post_custom_role(statement_post_list)

Create custom role

Create a new custom role

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import custom_roles_api
from launchdarkly_api.model.custom_role import CustomRole
from launchdarkly_api.model.statement_post_list import StatementPostList
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
    api_instance = custom_roles_api.CustomRolesApi(api_client)
    statement_post_list = StatementPostList([
        StatementPost(
            resources=[
                "resources_example",
            ],
            not_resources=[
                "not_resources_example",
            ],
            actions=[
                "actions_example",
            ],
            not_actions=[
                "not_actions_example",
            ],
            effect="effect_example",
        ),
    ]) # StatementPostList | 

    # example passing only required values which don't have defaults set
    try:
        # Create custom role
        api_response = api_instance.post_custom_role(statement_post_list)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling CustomRolesApi->post_custom_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statement_post_list** | [**StatementPostList**](StatementPostList.md)|  |

### Return type

[**CustomRole**](CustomRole.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Custom role response |  -  |
**400** | Invalid request body |  -  |
**401** | Invalid access token |  -  |
**403** | Access to the requested resource was denied |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

