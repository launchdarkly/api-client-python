# launchdarkly_api.ContextsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_context_kinds_by_project_key**](ContextsBetaApi.md#get_context_kinds_by_project_key) | **GET** /api/v2/projects/{projectKey}/context-kinds | Get context kinds
[**put_context_kind**](ContextsBetaApi.md#put_context_kind) | **PUT** /api/v2/projects/{projectKey}/context-kinds/{key} | Create or update context kind


# **get_context_kinds_by_project_key**
> ContextKindsCollectionRep get_context_kinds_by_project_key(project_key)

Get context kinds

Get all context kinds for a given project.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import contexts_beta_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.context_kinds_collection_rep import ContextKindsCollectionRep
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
    api_instance = contexts_beta_api.ContextsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key

    # example passing only required values which don't have defaults set
    try:
        # Get context kinds
        api_response = api_instance.get_context_kinds_by_project_key(project_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsBetaApi->get_context_kinds_by_project_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |

### Return type

[**ContextKindsCollectionRep**](ContextKindsCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Context kinds collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_context_kind**
> UpsertResponseRep put_context_kind(project_key, key, upsert_context_kind_payload)

Create or update context kind

Create or update a context kind by key. Only the included fields will be updated.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import contexts_beta_api
from launchdarkly_api.model.upsert_response_rep import UpsertResponseRep
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.upsert_context_kind_payload import UpsertContextKindPayload
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
    api_instance = contexts_beta_api.ContextsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    key = "key_example" # str | The context kind key
    upsert_context_kind_payload = UpsertContextKindPayload(
        name="organization",
        description="An example context kind for organizations",
        hide_in_targeting=False,
        version=1,
    ) # UpsertContextKindPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update context kind
        api_response = api_instance.put_context_kind(project_key, key, upsert_context_kind_payload)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsBetaApi->put_context_kind: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **key** | **str**| The context kind key |
 **upsert_context_kind_payload** | [**UpsertContextKindPayload**](UpsertContextKindPayload.md)|  |

### Return type

[**UpsertResponseRep**](UpsertResponseRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Context kind upsert response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

