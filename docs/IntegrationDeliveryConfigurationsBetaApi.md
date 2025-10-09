# launchdarkly_api.IntegrationDeliveryConfigurationsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_integration_delivery_configuration**](IntegrationDeliveryConfigurationsBetaApi.md#create_integration_delivery_configuration) | **POST** /api/v2/integration-capabilities/featureStore/{projectKey}/{environmentKey}/{integrationKey} | Create delivery configuration
[**delete_integration_delivery_configuration**](IntegrationDeliveryConfigurationsBetaApi.md#delete_integration_delivery_configuration) | **DELETE** /api/v2/integration-capabilities/featureStore/{projectKey}/{environmentKey}/{integrationKey}/{id} | Delete delivery configuration
[**get_integration_delivery_configuration_by_environment**](IntegrationDeliveryConfigurationsBetaApi.md#get_integration_delivery_configuration_by_environment) | **GET** /api/v2/integration-capabilities/featureStore/{projectKey}/{environmentKey} | Get delivery configurations by environment
[**get_integration_delivery_configuration_by_id**](IntegrationDeliveryConfigurationsBetaApi.md#get_integration_delivery_configuration_by_id) | **GET** /api/v2/integration-capabilities/featureStore/{projectKey}/{environmentKey}/{integrationKey}/{id} | Get delivery configuration by ID
[**get_integration_delivery_configurations**](IntegrationDeliveryConfigurationsBetaApi.md#get_integration_delivery_configurations) | **GET** /api/v2/integration-capabilities/featureStore | List all delivery configurations
[**patch_integration_delivery_configuration**](IntegrationDeliveryConfigurationsBetaApi.md#patch_integration_delivery_configuration) | **PATCH** /api/v2/integration-capabilities/featureStore/{projectKey}/{environmentKey}/{integrationKey}/{id} | Update delivery configuration
[**validate_integration_delivery_configuration**](IntegrationDeliveryConfigurationsBetaApi.md#validate_integration_delivery_configuration) | **POST** /api/v2/integration-capabilities/featureStore/{projectKey}/{environmentKey}/{integrationKey}/{id}/validate | Validate delivery configuration


# **create_integration_delivery_configuration**
> IntegrationDeliveryConfiguration create_integration_delivery_configuration(project_key, environment_key, integration_key, integration_delivery_configuration_post)

Create delivery configuration

Create a delivery configuration.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.integration_delivery_configuration import IntegrationDeliveryConfiguration
from launchdarkly_api.models.integration_delivery_configuration_post import IntegrationDeliveryConfigurationPost
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
    api_instance = launchdarkly_api.IntegrationDeliveryConfigurationsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    integration_key = 'integration_key_example' # str | The integration key
    integration_delivery_configuration_post = {"config":{"optional":"example value for optional formVariables property for sample-integration","required":"example value for required formVariables property for sample-integration"},"name":"Sample integration","on":false,"tags":["example-tag"]} # IntegrationDeliveryConfigurationPost | 

    try:
        # Create delivery configuration
        api_response = api_instance.create_integration_delivery_configuration(project_key, environment_key, integration_key, integration_delivery_configuration_post)
        print("The response of IntegrationDeliveryConfigurationsBetaApi->create_integration_delivery_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationDeliveryConfigurationsBetaApi->create_integration_delivery_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **integration_key** | **str**| The integration key | 
 **integration_delivery_configuration_post** | [**IntegrationDeliveryConfigurationPost**](IntegrationDeliveryConfigurationPost.md)|  | 

### Return type

[**IntegrationDeliveryConfiguration**](IntegrationDeliveryConfiguration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Integration delivery configuration response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_integration_delivery_configuration**
> delete_integration_delivery_configuration(project_key, environment_key, integration_key, id)

Delete delivery configuration

Delete a delivery configuration.

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
    api_instance = launchdarkly_api.IntegrationDeliveryConfigurationsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    integration_key = 'integration_key_example' # str | The integration key
    id = 'id_example' # str | The configuration ID

    try:
        # Delete delivery configuration
        api_instance.delete_integration_delivery_configuration(project_key, environment_key, integration_key, id)
    except Exception as e:
        print("Exception when calling IntegrationDeliveryConfigurationsBetaApi->delete_integration_delivery_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **integration_key** | **str**| The integration key | 
 **id** | **str**| The configuration ID | 

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
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_delivery_configuration_by_environment**
> IntegrationDeliveryConfigurationCollection get_integration_delivery_configuration_by_environment(project_key, environment_key)

Get delivery configurations by environment

Get delivery configurations by environment.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.integration_delivery_configuration_collection import IntegrationDeliveryConfigurationCollection
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
    api_instance = launchdarkly_api.IntegrationDeliveryConfigurationsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key

    try:
        # Get delivery configurations by environment
        api_response = api_instance.get_integration_delivery_configuration_by_environment(project_key, environment_key)
        print("The response of IntegrationDeliveryConfigurationsBetaApi->get_integration_delivery_configuration_by_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationDeliveryConfigurationsBetaApi->get_integration_delivery_configuration_by_environment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 

### Return type

[**IntegrationDeliveryConfigurationCollection**](IntegrationDeliveryConfigurationCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration delivery configuration collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_delivery_configuration_by_id**
> IntegrationDeliveryConfiguration get_integration_delivery_configuration_by_id(project_key, environment_key, integration_key, id)

Get delivery configuration by ID

Get delivery configuration by ID.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.integration_delivery_configuration import IntegrationDeliveryConfiguration
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
    api_instance = launchdarkly_api.IntegrationDeliveryConfigurationsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    integration_key = 'integration_key_example' # str | The integration key
    id = 'id_example' # str | The configuration ID

    try:
        # Get delivery configuration by ID
        api_response = api_instance.get_integration_delivery_configuration_by_id(project_key, environment_key, integration_key, id)
        print("The response of IntegrationDeliveryConfigurationsBetaApi->get_integration_delivery_configuration_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationDeliveryConfigurationsBetaApi->get_integration_delivery_configuration_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **integration_key** | **str**| The integration key | 
 **id** | **str**| The configuration ID | 

### Return type

[**IntegrationDeliveryConfiguration**](IntegrationDeliveryConfiguration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration delivery configuration response |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_delivery_configurations**
> IntegrationDeliveryConfigurationCollection get_integration_delivery_configurations()

List all delivery configurations

List all delivery configurations.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.integration_delivery_configuration_collection import IntegrationDeliveryConfigurationCollection
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
    api_instance = launchdarkly_api.IntegrationDeliveryConfigurationsBetaApi(api_client)

    try:
        # List all delivery configurations
        api_response = api_instance.get_integration_delivery_configurations()
        print("The response of IntegrationDeliveryConfigurationsBetaApi->get_integration_delivery_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationDeliveryConfigurationsBetaApi->get_integration_delivery_configurations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IntegrationDeliveryConfigurationCollection**](IntegrationDeliveryConfigurationCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration delivery configuration collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_integration_delivery_configuration**
> IntegrationDeliveryConfiguration patch_integration_delivery_configuration(project_key, environment_key, integration_key, id, patch_operation)

Update delivery configuration

Update an integration delivery configuration. Updating an integration delivery configuration uses a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.integration_delivery_configuration import IntegrationDeliveryConfiguration
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
    api_instance = launchdarkly_api.IntegrationDeliveryConfigurationsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    integration_key = 'integration_key_example' # str | The integration key
    id = 'id_example' # str | The configuration ID
    patch_operation = [{"op":"replace","path":"/on","value":true}] # List[PatchOperation] | 

    try:
        # Update delivery configuration
        api_response = api_instance.patch_integration_delivery_configuration(project_key, environment_key, integration_key, id, patch_operation)
        print("The response of IntegrationDeliveryConfigurationsBetaApi->patch_integration_delivery_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationDeliveryConfigurationsBetaApi->patch_integration_delivery_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **integration_key** | **str**| The integration key | 
 **id** | **str**| The configuration ID | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**IntegrationDeliveryConfiguration**](IntegrationDeliveryConfiguration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration delivery configuration response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**422** | Invalid patch content |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_integration_delivery_configuration**
> IntegrationDeliveryConfigurationResponse validate_integration_delivery_configuration(project_key, environment_key, integration_key, id)

Validate delivery configuration

Validate the saved delivery configuration, using the `validationRequest` in the integration's `manifest.json` file.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.integration_delivery_configuration_response import IntegrationDeliveryConfigurationResponse
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
    api_instance = launchdarkly_api.IntegrationDeliveryConfigurationsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    integration_key = 'integration_key_example' # str | The integration key
    id = 'id_example' # str | The configuration ID

    try:
        # Validate delivery configuration
        api_response = api_instance.validate_integration_delivery_configuration(project_key, environment_key, integration_key, id)
        print("The response of IntegrationDeliveryConfigurationsBetaApi->validate_integration_delivery_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationDeliveryConfigurationsBetaApi->validate_integration_delivery_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **integration_key** | **str**| The integration key | 
 **id** | **str**| The configuration ID | 

### Return type

[**IntegrationDeliveryConfigurationResponse**](IntegrationDeliveryConfigurationResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration delivery configuration validation response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

