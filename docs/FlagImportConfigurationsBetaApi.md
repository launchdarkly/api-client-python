# launchdarkly_api.FlagImportConfigurationsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_flag_import_configuration**](FlagImportConfigurationsBetaApi.md#create_flag_import_configuration) | **POST** /api/v2/integration-capabilities/flag-import/{projectKey}/{integrationKey} | Create a flag import configuration
[**delete_flag_import_configuration**](FlagImportConfigurationsBetaApi.md#delete_flag_import_configuration) | **DELETE** /api/v2/integration-capabilities/flag-import/{projectKey}/{integrationKey}/{integrationId} | Delete a flag import configuration
[**get_flag_import_configuration**](FlagImportConfigurationsBetaApi.md#get_flag_import_configuration) | **GET** /api/v2/integration-capabilities/flag-import/{projectKey}/{integrationKey}/{integrationId} | Get a single flag import configuration
[**get_flag_import_configurations**](FlagImportConfigurationsBetaApi.md#get_flag_import_configurations) | **GET** /api/v2/integration-capabilities/flag-import | List all flag import configurations
[**patch_flag_import_configuration**](FlagImportConfigurationsBetaApi.md#patch_flag_import_configuration) | **PATCH** /api/v2/integration-capabilities/flag-import/{projectKey}/{integrationKey}/{integrationId} | Update a flag import configuration
[**trigger_flag_import_job**](FlagImportConfigurationsBetaApi.md#trigger_flag_import_job) | **POST** /api/v2/integration-capabilities/flag-import/{projectKey}/{integrationKey}/{integrationId}/trigger | Trigger a single flag import run


# **create_flag_import_configuration**
> FlagImportIntegration create_flag_import_configuration(project_key, integration_key, flag_import_configuration_post)

Create a flag import configuration

Create a new flag import configuration. The `integrationKey` path parameter identifies the feature management system from which the import occurs, for example, `split`. The `config` object in the request body schema is described by the global integration settings, as specified by the <code>formVariables</code> in the <code>manifest.json</code> for this integration. It varies slightly based on the `integrationKey`.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.flag_import_configuration_post import FlagImportConfigurationPost
from launchdarkly_api.models.flag_import_integration import FlagImportIntegration
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
    api_instance = launchdarkly_api.FlagImportConfigurationsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    integration_key = 'integration_key_example' # str | The integration key
    flag_import_configuration_post = {"config":{"environmentId":"The ID of the environment in the external system","ldApiKey":"An API key with create flag permissions in your LaunchDarkly account","ldMaintainer":"The ID of the member who will be the maintainer of the imported flags","ldTag":"A tag to apply to all flags imported to LaunchDarkly","splitTag":"If provided, imports only the flags from the external system with this tag. Leave blank to import all flags.","workspaceApiKey":"An API key with read permissions in the external feature management system","workspaceId":"The ID of the workspace in the external system"},"name":"Sample configuration","tags":["example-tag"]} # FlagImportConfigurationPost | 

    try:
        # Create a flag import configuration
        api_response = api_instance.create_flag_import_configuration(project_key, integration_key, flag_import_configuration_post)
        print("The response of FlagImportConfigurationsBetaApi->create_flag_import_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlagImportConfigurationsBetaApi->create_flag_import_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **integration_key** | **str**| The integration key | 
 **flag_import_configuration_post** | [**FlagImportConfigurationPost**](FlagImportConfigurationPost.md)|  | 

### Return type

[**FlagImportIntegration**](FlagImportIntegration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag Import Configuration response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Project not found |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_flag_import_configuration**
> delete_flag_import_configuration(project_key, integration_key, integration_id)

Delete a flag import configuration

Delete a flag import configuration by ID. The `integrationKey` path parameter identifies the feature management system from which the import occurs, for example, `split`.

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
    api_instance = launchdarkly_api.FlagImportConfigurationsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    integration_key = 'integration_key_example' # str | The integration key
    integration_id = 'integration_id_example' # str | The integration ID

    try:
        # Delete a flag import configuration
        api_instance.delete_flag_import_configuration(project_key, integration_key, integration_id)
    except Exception as e:
        print("Exception when calling FlagImportConfigurationsBetaApi->delete_flag_import_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **integration_key** | **str**| The integration key | 
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
**404** | Project or import configuration not found |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flag_import_configuration**
> FlagImportIntegration get_flag_import_configuration(project_key, integration_key, integration_id)

Get a single flag import configuration

Get a single flag import configuration by ID. The `integrationKey` path parameter identifies the feature management system from which the import occurs, for example, `split`.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.flag_import_integration import FlagImportIntegration
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
    api_instance = launchdarkly_api.FlagImportConfigurationsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    integration_key = 'integration_key_example' # str | The integration key, for example, `split`
    integration_id = 'integration_id_example' # str | The integration ID

    try:
        # Get a single flag import configuration
        api_response = api_instance.get_flag_import_configuration(project_key, integration_key, integration_id)
        print("The response of FlagImportConfigurationsBetaApi->get_flag_import_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlagImportConfigurationsBetaApi->get_flag_import_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **integration_key** | **str**| The integration key, for example, &#x60;split&#x60; | 
 **integration_id** | **str**| The integration ID | 

### Return type

[**FlagImportIntegration**](FlagImportIntegration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag import response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Project or import configuration not found |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flag_import_configurations**
> FlagImportIntegrationCollection get_flag_import_configurations()

List all flag import configurations

List all flag import configurations.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.flag_import_integration_collection import FlagImportIntegrationCollection
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
    api_instance = launchdarkly_api.FlagImportConfigurationsBetaApi(api_client)

    try:
        # List all flag import configurations
        api_response = api_instance.get_flag_import_configurations()
        print("The response of FlagImportConfigurationsBetaApi->get_flag_import_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlagImportConfigurationsBetaApi->get_flag_import_configurations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FlagImportIntegrationCollection**](FlagImportIntegrationCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag Import Configuration response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Project not found |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_flag_import_configuration**
> FlagImportIntegration patch_flag_import_configuration(project_key, integration_key, integration_id, patch_operation)

Update a flag import configuration

Updating a flag import configuration uses a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates).<br/><br/>To add an element to the import configuration fields that are arrays, set the `path` to the name of the field and then append `/<array index>`. Use `/0` to add to the beginning of the array. Use `/-` to add to the end of the array.<br/><br/>You can update the `config`, `tags`, and `name` of the flag import configuration.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.flag_import_integration import FlagImportIntegration
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
    api_instance = launchdarkly_api.FlagImportConfigurationsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    integration_key = 'integration_key_example' # str | The integration key
    integration_id = 'integration_id_example' # str | The integration ID
    patch_operation = [launchdarkly_api.PatchOperation()] # List[PatchOperation] | 

    try:
        # Update a flag import configuration
        api_response = api_instance.patch_flag_import_configuration(project_key, integration_key, integration_id, patch_operation)
        print("The response of FlagImportConfigurationsBetaApi->patch_flag_import_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlagImportConfigurationsBetaApi->patch_flag_import_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **integration_key** | **str**| The integration key | 
 **integration_id** | **str**| The integration ID | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**FlagImportIntegration**](FlagImportIntegration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag import response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Project or import configuration not found |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_flag_import_job**
> trigger_flag_import_job(project_key, integration_key, integration_id)

Trigger a single flag import run

Trigger a single flag import run for an existing flag import configuration. The `integrationKey` path parameter identifies the feature management system from which the import occurs, for example, `split`.

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
    api_instance = launchdarkly_api.FlagImportConfigurationsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    integration_key = 'integration_key_example' # str | The integration key
    integration_id = 'integration_id_example' # str | The integration ID

    try:
        # Trigger a single flag import run
        api_instance.trigger_flag_import_job(project_key, integration_key, integration_id)
    except Exception as e:
        print("Exception when calling FlagImportConfigurationsBetaApi->trigger_flag_import_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **integration_key** | **str**| The integration key | 
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
**201** | Import job queued successfully |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Project or import configuration not found |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

