# launchdarkly_api.ReleasePoliciesBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_release_policy**](ReleasePoliciesBetaApi.md#delete_release_policy) | **DELETE** /api/v2/projects/{projectKey}/release-policies/{policyKey} | Delete a release policy
[**get_release_policies**](ReleasePoliciesBetaApi.md#get_release_policies) | **GET** /api/v2/projects/{projectKey}/release-policies | List release policies
[**get_release_policy**](ReleasePoliciesBetaApi.md#get_release_policy) | **GET** /api/v2/projects/{projectKey}/release-policies/{policyKey} | Get a release policy by key
[**post_release_policies_order**](ReleasePoliciesBetaApi.md#post_release_policies_order) | **POST** /api/v2/projects/{projectKey}/release-policies/order | Update the order of existing release policies
[**post_release_policy**](ReleasePoliciesBetaApi.md#post_release_policy) | **POST** /api/v2/projects/{projectKey}/release-policies | Create a release policy
[**put_release_policy**](ReleasePoliciesBetaApi.md#put_release_policy) | **PUT** /api/v2/projects/{projectKey}/release-policies/{policyKey} | Update a release policy


# **delete_release_policy**
> delete_release_policy(ld_api_version, project_key, policy_key)

Delete a release policy

Delete an existing release policy for the specified project.

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
    api_instance = launchdarkly_api.ReleasePoliciesBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | The project key
    policy_key = 'production-release' # str | The human-readable key of the release policy

    try:
        # Delete a release policy
        api_instance.delete_release_policy(ld_api_version, project_key, policy_key)
    except Exception as e:
        print("Exception when calling ReleasePoliciesBetaApi->delete_release_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**| The project key | 
 **policy_key** | **str**| The human-readable key of the release policy | 

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
**204** | Release policy deleted successfully |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_policies**
> ReleasePoliciesResponse get_release_policies(ld_api_version, project_key, exclude_default=exclude_default)

List release policies

Get a list of release policies for the specified project with optional filtering.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.release_policies_response import ReleasePoliciesResponse
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
    api_instance = launchdarkly_api.ReleasePoliciesBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | The project key
    exclude_default = False # bool | When true, exclude the default release policy from the response. When false or omitted, include the default policy if an environment filter is present. (optional) (default to False)

    try:
        # List release policies
        api_response = api_instance.get_release_policies(ld_api_version, project_key, exclude_default=exclude_default)
        print("The response of ReleasePoliciesBetaApi->get_release_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePoliciesBetaApi->get_release_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**| The project key | 
 **exclude_default** | **bool**| When true, exclude the default release policy from the response. When false or omitted, include the default policy if an environment filter is present. | [optional] [default to False]

### Return type

[**ReleasePoliciesResponse**](ReleasePoliciesResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of release policies |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_policy**
> ReleasePolicy get_release_policy(ld_api_version, project_key, policy_key)

Get a release policy by key

Retrieve a single release policy by its key for the specified project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.release_policy import ReleasePolicy
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
    api_instance = launchdarkly_api.ReleasePoliciesBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | The project key
    policy_key = 'production-release' # str | The release policy key

    try:
        # Get a release policy by key
        api_response = api_instance.get_release_policy(ld_api_version, project_key, policy_key)
        print("The response of ReleasePoliciesBetaApi->get_release_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePoliciesBetaApi->get_release_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**| The project key | 
 **policy_key** | **str**| The release policy key | 

### Return type

[**ReleasePolicy**](ReleasePolicy.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release policy found |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_release_policies_order**
> List[ReleasePolicy] post_release_policies_order(ld_api_version, project_key, request_body)

Update the order of existing release policies

Update the order of existing release policies for the specified project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.release_policy import ReleasePolicy
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
    api_instance = launchdarkly_api.ReleasePoliciesBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | The project key
    request_body = ['request_body_example'] # List[str] | Array of release policy keys in the desired rank order (scoped policies only). These keys must include _all_ of the scoped release policies for the project.

    try:
        # Update the order of existing release policies
        api_response = api_instance.post_release_policies_order(ld_api_version, project_key, request_body)
        print("The response of ReleasePoliciesBetaApi->post_release_policies_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePoliciesBetaApi->post_release_policies_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**| The project key | 
 **request_body** | [**List[str]**](str.md)| Array of release policy keys in the desired rank order (scoped policies only). These keys must include _all_ of the scoped release policies for the project. | 

### Return type

[**List[ReleasePolicy]**](ReleasePolicy.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release policies updated successfully |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_release_policy**
> ReleasePolicy post_release_policy(ld_api_version, project_key, post_release_policy_request)

Create a release policy

Create a new release policy for the specified project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.post_release_policy_request import PostReleasePolicyRequest
from launchdarkly_api.models.release_policy import ReleasePolicy
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
    api_instance = launchdarkly_api.ReleasePoliciesBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | The project key
    post_release_policy_request = launchdarkly_api.PostReleasePolicyRequest() # PostReleasePolicyRequest | Release policy to create

    try:
        # Create a release policy
        api_response = api_instance.post_release_policy(ld_api_version, project_key, post_release_policy_request)
        print("The response of ReleasePoliciesBetaApi->post_release_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePoliciesBetaApi->post_release_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**| The project key | 
 **post_release_policy_request** | [**PostReleasePolicyRequest**](PostReleasePolicyRequest.md)| Release policy to create | 

### Return type

[**ReleasePolicy**](ReleasePolicy.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Release policy created successfully |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_release_policy**
> ReleasePolicy put_release_policy(ld_api_version, project_key, policy_key, put_release_policy_request)

Update a release policy

Update an existing release policy for the specified project.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.put_release_policy_request import PutReleasePolicyRequest
from launchdarkly_api.models.release_policy import ReleasePolicy
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
    api_instance = launchdarkly_api.ReleasePoliciesBetaApi(api_client)
    ld_api_version = 'ld_api_version_example' # str | Version of the endpoint.
    project_key = 'default' # str | The project key
    policy_key = 'production-release' # str | The human-readable key of the release policy
    put_release_policy_request = launchdarkly_api.PutReleasePolicyRequest() # PutReleasePolicyRequest | Release policy data to update

    try:
        # Update a release policy
        api_response = api_instance.put_release_policy(ld_api_version, project_key, policy_key, put_release_policy_request)
        print("The response of ReleasePoliciesBetaApi->put_release_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasePoliciesBetaApi->put_release_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ld_api_version** | **str**| Version of the endpoint. | 
 **project_key** | **str**| The project key | 
 **policy_key** | **str**| The human-readable key of the release policy | 
 **put_release_policy_request** | [**PutReleasePolicyRequest**](PutReleasePolicyRequest.md)| Release policy data to update | 

### Return type

[**ReleasePolicy**](ReleasePolicy.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release policy updated successfully |  -  |
**400** | Bad request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

