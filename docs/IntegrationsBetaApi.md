# launchdarkly_api.IntegrationsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_integration_configuration**](IntegrationsBetaApi.md#create_integration_configuration) | **POST** /api/v2/integration-configurations/keys/{integrationKey} | Create integration configuration
[**delete_integration_configuration**](IntegrationsBetaApi.md#delete_integration_configuration) | **DELETE** /api/v2/integration-configurations/{integrationConfigurationId} | Delete integration configuration
[**get_all_integration_configurations**](IntegrationsBetaApi.md#get_all_integration_configurations) | **GET** /api/v2/integration-configurations/keys/{integrationKey} | Get all configurations for the integration
[**get_integration_configuration**](IntegrationsBetaApi.md#get_integration_configuration) | **GET** /api/v2/integration-configurations/{integrationConfigurationId} | Get an integration configuration
[**update_integration_configuration**](IntegrationsBetaApi.md#update_integration_configuration) | **PATCH** /api/v2/integration-configurations/{integrationConfigurationId} | Update integration configuration


# **create_integration_configuration**
> IntegrationConfigurationsRep create_integration_configuration(integration_key, integration_configuration_post)

Create integration configuration

Create a new integration configuration. (Excludes [persistent store](/tag/Persistent-store-integrations-(beta)) and [flag import configurations](/tag/Flag-import-configurations-(beta)).)

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import integrations_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.integration_configurations_rep import IntegrationConfigurationsRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.integration_configuration_post import IntegrationConfigurationPost
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
    api_instance = integrations_beta_api.IntegrationsBetaApi(api_client)
    integration_key = "integrationKey_example" # str | The integration key
    integration_configuration_post = IntegrationConfigurationPost(
        name="Example integration configuration",
        enabled=True,
        tags=["ops"],
        config_values={
            "key": None,
        },
        capability_config=CapabilityConfigPost(
            approvals=ApprovalsCapabilityConfig(
                additional_form_variables=[
                    FormVariable(
                        key="key_example",
                        name="name_example",
                        type="type_example",
                        description="description_example",
                        placeholder="placeholder_example",
                        is_optional=True,
                        default_value=None,
                        allowed_values=[
                            "allowed_values_example",
                        ],
                        dynamic_options=DynamicOptions(
                            endpoint=Endpoint(
                                headers=[
                                    HeaderItems(
                                        name="name_example",
                                        value="value_example",
                                    ),
                                ],
                                hmac_signature=HMACSignature(
                                    header_name="header_name_example",
                                    hmac_secret_form_variable_key="hmac_secret_form_variable_key_example",
                                ),
                                method="method_example",
                                url="url_example",
                            ),
                            parser=DynamicOptionsParser(
                                options_items=OptionsArray(
                                    label="label_example",
                                    value="value_example",
                                ),
                                options_path="options_path_example",
                            ),
                        ),
                    ),
                ],
            ),
            audit_log_events_hook=AuditLogEventsHookCapabilityConfigPost(
                statements=StatementPostList([
                    StatementPost(
                        resources=["proj/*:env/*:flag/*;testing-tag"],
                        not_resources=[
                            "not_resources_example",
                        ],
                        actions=["*"],
                        not_actions=[
                            "not_actions_example",
                        ],
                        effect="allow",
                    ),
                ]),
            ),
        ),
    ) # IntegrationConfigurationPost | 

    # example passing only required values which don't have defaults set
    try:
        # Create integration configuration
        api_response = api_instance.create_integration_configuration(integration_key, integration_configuration_post)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling IntegrationsBetaApi->create_integration_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_key** | **str**| The integration key |
 **integration_configuration_post** | [**IntegrationConfigurationPost**](IntegrationConfigurationPost.md)|  |

### Return type

[**IntegrationConfigurationsRep**](IntegrationConfigurationsRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Integration Configuration response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Integration key not found |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_integration_configuration**
> delete_integration_configuration(integration_configuration_id)

Delete integration configuration

Delete an integration configuration by ID. (Excludes [persistent store](/tag/Persistent-store-integrations-(beta)) and [flag import configurations](/tag/Flag-import-configurations-(beta)).)

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import integrations_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
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
    api_instance = integrations_beta_api.IntegrationsBetaApi(api_client)
    integration_configuration_id = "integrationConfigurationId_example" # str | The ID of the integration configuration to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Delete integration configuration
        api_instance.delete_integration_configuration(integration_configuration_id)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling IntegrationsBetaApi->delete_integration_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_configuration_id** | **str**| The ID of the integration configuration to be deleted |

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

# **get_all_integration_configurations**
> IntegrationConfigurationCollectionRep get_all_integration_configurations(integration_key)

Get all configurations for the integration

Get all integration configurations with the specified integration key. (Excludes [persistent store](/tag/Persistent-store-integrations-(beta)) and [flag import configurations](/tag/Flag-import-configurations-(beta))).

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import integrations_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.integration_configuration_collection_rep import IntegrationConfigurationCollectionRep
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
    api_instance = integrations_beta_api.IntegrationsBetaApi(api_client)
    integration_key = "integrationKey_example" # str | Integration key

    # example passing only required values which don't have defaults set
    try:
        # Get all configurations for the integration
        api_response = api_instance.get_all_integration_configurations(integration_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling IntegrationsBetaApi->get_all_integration_configurations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_key** | **str**| Integration key |

### Return type

[**IntegrationConfigurationCollectionRep**](IntegrationConfigurationCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Integration Configurations |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Integration key not found |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_configuration**
> IntegrationConfigurationsRep get_integration_configuration(integration_configuration_id)

Get an integration configuration

Get integration configuration with the specified ID. (Excludes [persistent store](/tag/Persistent-store-integrations-(beta)) and [flag import configurations](/tag/Flag-import-configurations-(beta)).)

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import integrations_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.integration_configurations_rep import IntegrationConfigurationsRep
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
    api_instance = integrations_beta_api.IntegrationsBetaApi(api_client)
    integration_configuration_id = "integrationConfigurationId_example" # str | Integration configuration ID

    # example passing only required values which don't have defaults set
    try:
        # Get an integration configuration
        api_response = api_instance.get_integration_configuration(integration_configuration_id)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling IntegrationsBetaApi->get_integration_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_configuration_id** | **str**| Integration configuration ID |

### Return type

[**IntegrationConfigurationsRep**](IntegrationConfigurationsRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration Configuration response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Integration ID not found |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integration_configuration**
> IntegrationConfigurationsRep update_integration_configuration(integration_configuration_id, json_patch)

Update integration configuration

Update an integration configuration. Updating an integration configuration uses a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes. To learn more, read [Updates](/#section/Overview/Updates).

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import integrations_beta_api
from launchdarkly_api.model.json_patch import JSONPatch
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.integration_configurations_rep import IntegrationConfigurationsRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
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
    api_instance = integrations_beta_api.IntegrationsBetaApi(api_client)
    integration_configuration_id = "integrationConfigurationId_example" # str | The ID of the integration configuration
    json_patch = JSONPatch([
        PatchOperation(
            op="replace",
            path="/exampleField",
            value=None,
        ),
    ]) # JSONPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update integration configuration
        api_response = api_instance.update_integration_configuration(integration_configuration_id, json_patch)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling IntegrationsBetaApi->update_integration_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_configuration_id** | **str**| The ID of the integration configuration |
 **json_patch** | [**JSONPatch**](JSONPatch.md)|  |

### Return type

[**IntegrationConfigurationsRep**](IntegrationConfigurationsRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration configuration response |  -  |
**400** | Invalid request |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

