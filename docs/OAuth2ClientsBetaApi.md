# launchdarkly_api.OAuth2ClientsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_o_auth2_client**](OAuth2ClientsBetaApi.md#create_o_auth2_client) | **POST** /api/v2/oauth/clients | Create a LaunchDarkly OAuth 2.0 client
[**delete_o_auth_client**](OAuth2ClientsBetaApi.md#delete_o_auth_client) | **DELETE** /api/v2/oauth/clients/{clientId} | Delete OAuth 2.0 client
[**get_o_auth_client_by_id**](OAuth2ClientsBetaApi.md#get_o_auth_client_by_id) | **GET** /api/v2/oauth/clients/{clientId} | Get client by ID
[**get_o_auth_clients**](OAuth2ClientsBetaApi.md#get_o_auth_clients) | **GET** /api/v2/oauth/clients | Get clients
[**patch_o_auth_client**](OAuth2ClientsBetaApi.md#patch_o_auth_client) | **PATCH** /api/v2/oauth/clients/{clientId} | Patch client by ID


# **create_o_auth2_client**
> Client create_o_auth2_client(oauth_client_post)

Create a LaunchDarkly OAuth 2.0 client

Create (register) a LaunchDarkly OAuth2 client. OAuth2 clients allow you to build custom integrations using LaunchDarkly as your identity provider.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import o_auth2_clients__beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.oauth_client_post import OauthClientPost
from launchdarkly_api.model.client import Client
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
    api_instance = o_auth2_clients__beta_api.OAuth2ClientsBetaApi(api_client)
    oauth_client_post = OauthClientPost(
        name="name_example",
        redirect_uri="redirect_uri_example",
        description="description_example",
    ) # OauthClientPost | 

    # example passing only required values which don't have defaults set
    try:
        # Create a LaunchDarkly OAuth 2.0 client
        api_response = api_instance.create_o_auth2_client(oauth_client_post)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling OAuth2ClientsBetaApi->create_o_auth2_client: %s\n" % e)
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
**201** | Successful OAuth 2.0 client creation response |  -  |
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
import time
import launchdarkly_api
from launchdarkly_api.api import o_auth2_clients__beta_api
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
    api_instance = o_auth2_clients__beta_api.OAuth2ClientsBetaApi(api_client)
    client_id = "clientId_example" # str | The client ID

    # example passing only required values which don't have defaults set
    try:
        # Delete OAuth 2.0 client
        api_instance.delete_o_auth_client(client_id)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling OAuth2ClientsBetaApi->delete_o_auth_client: %s\n" % e)
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
import time
import launchdarkly_api
from launchdarkly_api.api import o_auth2_clients__beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.client import Client
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
    api_instance = o_auth2_clients__beta_api.OAuth2ClientsBetaApi(api_client)
    client_id = "clientId_example" # str | The client ID

    # example passing only required values which don't have defaults set
    try:
        # Get client by ID
        api_response = api_instance.get_o_auth_client_by_id(client_id)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling OAuth2ClientsBetaApi->get_o_auth_client_by_id: %s\n" % e)
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
import time
import launchdarkly_api
from launchdarkly_api.api import o_auth2_clients__beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.client_collection import ClientCollection
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
    api_instance = o_auth2_clients__beta_api.OAuth2ClientsBetaApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get clients
        api_response = api_instance.get_o_auth_clients()
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling OAuth2ClientsBetaApi->get_o_auth_clients: %s\n" % e)
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
> Client patch_o_auth_client(client_id, json_patch)

Patch client by ID

Patch an existing OAuth 2.0 client by client ID. Requires a [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes to the client. Only `name`, `description`, and `redirectUri` may be patched.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import o_auth2_clients__beta_api
from launchdarkly_api.model.json_patch import JSONPatch
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.client import Client
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
    api_instance = o_auth2_clients__beta_api.OAuth2ClientsBetaApi(api_client)
    client_id = "clientId_example" # str | The client ID
    json_patch = JSONPatch([
        PatchOperation(
            op="replace",
            path="/exampleField",
            value=None,
        ),
    ]) # JSONPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Patch client by ID
        api_response = api_instance.patch_o_auth_client(client_id, json_patch)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling OAuth2ClientsBetaApi->patch_o_auth_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The client ID |
 **json_patch** | [**JSONPatch**](JSONPatch.md)|  |

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
**200** | Successful |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

