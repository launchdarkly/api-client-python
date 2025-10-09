# launchdarkly_api.PersistentStoreIntegrationsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_big_segment_store_integration**](PersistentStoreIntegrationsBetaApi.md#create_big_segment_store_integration) | **POST** /api/v2/integration-capabilities/big-segment-store/{projectKey}/{environmentKey}/{integrationKey} | Create big segment store integration
[**delete_big_segment_store_integration**](PersistentStoreIntegrationsBetaApi.md#delete_big_segment_store_integration) | **DELETE** /api/v2/integration-capabilities/big-segment-store/{projectKey}/{environmentKey}/{integrationKey}/{integrationId} | Delete big segment store integration
[**get_big_segment_store_integration**](PersistentStoreIntegrationsBetaApi.md#get_big_segment_store_integration) | **GET** /api/v2/integration-capabilities/big-segment-store/{projectKey}/{environmentKey}/{integrationKey}/{integrationId} | Get big segment store integration by ID
[**get_big_segment_store_integrations**](PersistentStoreIntegrationsBetaApi.md#get_big_segment_store_integrations) | **GET** /api/v2/integration-capabilities/big-segment-store | List all big segment store integrations
[**patch_big_segment_store_integration**](PersistentStoreIntegrationsBetaApi.md#patch_big_segment_store_integration) | **PATCH** /api/v2/integration-capabilities/big-segment-store/{projectKey}/{environmentKey}/{integrationKey}/{integrationId} | Update big segment store integration


# **create_big_segment_store_integration**
> BigSegmentStoreIntegration create_big_segment_store_integration(project_key, environment_key, integration_key, integration_delivery_configuration_post)

Create big segment store integration

 Create a persistent store integration.  If you are using server-side SDKs, segments synced from external tools and larger list-based segments require a persistent store within your infrastructure. LaunchDarkly keeps the persistent store up to date and consults it during flag evaluation.  You can use either Redis or DynamoDB as your persistent store. When you create a persistent store integration, the fields in the `config` object in the request vary depending on which persistent store you use.  If you are using Redis to create your persistent store integration, you will need to know:  * Your Redis host * Your Redis port * Your Redis username * Your Redis password * Whether or not LaunchDarkly should connect using TLS  If you are using DynamoDB to create your persistent store integration, you will need to know:  * Your DynamoDB table name. The table must have the following schema:   * Partition key: `namespace` (string)   * Sort key: `key` (string) * Your DynamoDB Amazon Web Services (AWS) region. * Your AWS role Amazon Resource Name (ARN). This is the role that LaunchDarkly will assume to manage your DynamoDB table. * The External ID you specified when creating your Amazon Resource Name (ARN).  To learn more, read [Segment configuration](https://launchdarkly.com/docs/home/flags/segment-config). 

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.big_segment_store_integration import BigSegmentStoreIntegration
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
    api_instance = launchdarkly_api.PersistentStoreIntegrationsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    integration_key = 'integration_key_example' # str | The integration key, either `redis` or `dynamodb`
    integration_delivery_configuration_post = {"config":{"optional":"example value for optional formVariables property for sample-integration","required":"example value for required formVariables property for sample-integration"},"name":"Example persistent store integration","on":false,"tags":["example-tag"]} # IntegrationDeliveryConfigurationPost | 

    try:
        # Create big segment store integration
        api_response = api_instance.create_big_segment_store_integration(project_key, environment_key, integration_key, integration_delivery_configuration_post)
        print("The response of PersistentStoreIntegrationsBetaApi->create_big_segment_store_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersistentStoreIntegrationsBetaApi->create_big_segment_store_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **integration_key** | **str**| The integration key, either &#x60;redis&#x60; or &#x60;dynamodb&#x60; | 
 **integration_delivery_configuration_post** | [**IntegrationDeliveryConfigurationPost**](IntegrationDeliveryConfigurationPost.md)|  | 

### Return type

[**BigSegmentStoreIntegration**](BigSegmentStoreIntegration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Big segment store response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Environment or project not found |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_big_segment_store_integration**
> delete_big_segment_store_integration(project_key, environment_key, integration_key, integration_id)

Delete big segment store integration

Delete a persistent store integration. Each integration uses either Redis or DynamoDB.

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
    api_instance = launchdarkly_api.PersistentStoreIntegrationsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    integration_key = 'integration_key_example' # str | The integration key, either `redis` or `dynamodb`
    integration_id = 'integration_id_example' # str | The integration ID

    try:
        # Delete big segment store integration
        api_instance.delete_big_segment_store_integration(project_key, environment_key, integration_key, integration_id)
    except Exception as e:
        print("Exception when calling PersistentStoreIntegrationsBetaApi->delete_big_segment_store_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **integration_key** | **str**| The integration key, either &#x60;redis&#x60; or &#x60;dynamodb&#x60; | 
 **integration_id** | **str**| The integration ID | 

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
**204** | Action completed successfully |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Environment or project not found |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_big_segment_store_integration**
> BigSegmentStoreIntegration get_big_segment_store_integration(project_key, environment_key, integration_key, integration_id)

Get big segment store integration by ID

Get a big segment store integration by ID.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.big_segment_store_integration import BigSegmentStoreIntegration
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
    api_instance = launchdarkly_api.PersistentStoreIntegrationsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    integration_key = 'integration_key_example' # str | The integration key, either `redis` or `dynamodb`
    integration_id = 'integration_id_example' # str | The integration ID

    try:
        # Get big segment store integration by ID
        api_response = api_instance.get_big_segment_store_integration(project_key, environment_key, integration_key, integration_id)
        print("The response of PersistentStoreIntegrationsBetaApi->get_big_segment_store_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersistentStoreIntegrationsBetaApi->get_big_segment_store_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **integration_key** | **str**| The integration key, either &#x60;redis&#x60; or &#x60;dynamodb&#x60; | 
 **integration_id** | **str**| The integration ID | 

### Return type

[**BigSegmentStoreIntegration**](BigSegmentStoreIntegration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Big segment store response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Environment or project not found |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_big_segment_store_integrations**
> BigSegmentStoreIntegrationCollection get_big_segment_store_integrations()

List all big segment store integrations

List all big segment store integrations.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.big_segment_store_integration_collection import BigSegmentStoreIntegrationCollection
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
    api_instance = launchdarkly_api.PersistentStoreIntegrationsBetaApi(api_client)

    try:
        # List all big segment store integrations
        api_response = api_instance.get_big_segment_store_integrations()
        print("The response of PersistentStoreIntegrationsBetaApi->get_big_segment_store_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersistentStoreIntegrationsBetaApi->get_big_segment_store_integrations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BigSegmentStoreIntegrationCollection**](BigSegmentStoreIntegrationCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Big segment store collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Environment or project not found |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_big_segment_store_integration**
> BigSegmentStoreIntegration patch_big_segment_store_integration(project_key, environment_key, integration_key, integration_id, patch_operation)

Update big segment store integration

Update a big segment store integration. Updating a big segment store requires a [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.big_segment_store_integration import BigSegmentStoreIntegration
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
    api_instance = launchdarkly_api.PersistentStoreIntegrationsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    integration_key = 'integration_key_example' # str | The integration key, either `redis` or `dynamodb`
    integration_id = 'integration_id_example' # str | The integration ID
    patch_operation = [launchdarkly_api.PatchOperation()] # List[PatchOperation] | 

    try:
        # Update big segment store integration
        api_response = api_instance.patch_big_segment_store_integration(project_key, environment_key, integration_key, integration_id, patch_operation)
        print("The response of PersistentStoreIntegrationsBetaApi->patch_big_segment_store_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersistentStoreIntegrationsBetaApi->patch_big_segment_store_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **integration_key** | **str**| The integration key, either &#x60;redis&#x60; or &#x60;dynamodb&#x60; | 
 **integration_id** | **str**| The integration ID | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**BigSegmentStoreIntegration**](BigSegmentStoreIntegration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Big segment store response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Environment or project not found |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

