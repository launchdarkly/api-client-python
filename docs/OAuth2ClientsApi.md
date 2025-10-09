# launchdarkly_api.OAuth2ClientsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_o_auth2_client**](OAuth2ClientsApi.md#create_o_auth2_client) | **POST** /api/v2/oauth/clients | Create a LaunchDarkly OAuth 2.0 client
[**delete_o_auth_client**](OAuth2ClientsApi.md#delete_o_auth_client) | **DELETE** /api/v2/oauth/clients/{clientId} | Delete OAuth 2.0 client
[**get_o_auth_client_by_id**](OAuth2ClientsApi.md#get_o_auth_client_by_id) | **GET** /api/v2/oauth/clients/{clientId} | Get client by ID
[**get_o_auth_clients**](OAuth2ClientsApi.md#get_o_auth_clients) | **GET** /api/v2/oauth/clients | Get clients
[**patch_o_auth_client**](OAuth2ClientsApi.md#patch_o_auth_client) | **PATCH** /api/v2/oauth/clients/{clientId} | Patch client by ID


# **create_o_auth2_client**
> Client create_o_auth2_client(oauth_client_post)

Create a LaunchDarkly OAuth 2.0 client

Create (register) a LaunchDarkly OAuth2 client. OAuth2 clients allow you to build custom integrations using LaunchDarkly as your identity provider.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.client import Client
from launchdarkly_api.models.oauth_client_post import OauthClientPost
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
    api_instance = launchdarkly_api.OAuth2ClientsApi(api_client)
    oauth_client_post = launchdarkly_api.OauthClientPost() # OauthClientPost | 

    try:
        # Create a LaunchDarkly OAuth 2.0 client
        api_response = api_instance.create_o_auth2_client(oauth_client_post)
        print("The response of OAuth2ClientsApi->create_o_auth2_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2ClientsApi->create_o_auth2_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_client_post** | [**OauthClientPost**](OauthClientPost.md)|  | 

### Return type

[**Client**](Client.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OAuth 2.0 client response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_o_auth_client**
> delete_o_auth_client(client_id)

Delete OAuth 2.0 client

Delete an existing OAuth 2.0 client by unique client ID.

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
    api_instance = launchdarkly_api.OAuth2ClientsApi(api_client)
    client_id = 'client_id_example' # str | The client ID

    try:
        # Delete OAuth 2.0 client
        api_instance.delete_o_auth_client(client_id)
    except Exception as e:
        print("Exception when calling OAuth2ClientsApi->delete_o_auth_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The client ID | 

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

# **get_o_auth_client_by_id**
> Client get_o_auth_client_by_id(client_id)

Get client by ID

Get a registered OAuth 2.0 client by unique client ID.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.client import Client
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
    api_instance = launchdarkly_api.OAuth2ClientsApi(api_client)
    client_id = 'client_id_example' # str | The client ID

    try:
        # Get client by ID
        api_response = api_instance.get_o_auth_client_by_id(client_id)
        print("The response of OAuth2ClientsApi->get_o_auth_client_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2ClientsApi->get_o_auth_client_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The client ID | 

### Return type

[**Client**](Client.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OAuth 2.0 client response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth_clients**
> ClientCollection get_o_auth_clients()

Get clients

Get all OAuth 2.0 clients registered by your account.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.client_collection import ClientCollection
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
    api_instance = launchdarkly_api.OAuth2ClientsApi(api_client)

    try:
        # Get clients
        api_response = api_instance.get_o_auth_clients()
        print("The response of OAuth2ClientsApi->get_o_auth_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2ClientsApi->get_o_auth_clients: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClientCollection**](ClientCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OAuth 2.0 client collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_o_auth_client**
> Client patch_o_auth_client(client_id, patch_operation)

Patch client by ID

Patch an existing OAuth 2.0 client by client ID. Updating an OAuth2 client uses a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates). Only `name`, `description`, and `redirectUri` may be patched.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.client import Client
from launchdarkly_api.models.patch_operation import PatchOperation
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
    api_instance = launchdarkly_api.OAuth2ClientsApi(api_client)
    client_id = 'client_id_example' # str | The client ID
    patch_operation = [{"op":"replace","path":"/name","value":"Example Client V2"}] # List[PatchOperation] | 

    try:
        # Patch client by ID
        api_response = api_instance.patch_o_auth_client(client_id, patch_operation)
        print("The response of OAuth2ClientsApi->patch_o_auth_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2ClientsApi->patch_o_auth_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The client ID | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**Client**](Client.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OAuth 2.0 client response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

