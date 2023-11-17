# launchdarkly_api.ContextsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_context_instances**](ContextsApi.md#delete_context_instances) | **DELETE** /api/v2/projects/{projectKey}/environments/{environmentKey}/context-instances/{id} | Delete context instances
[**evaluate_context_instance**](ContextsApi.md#evaluate_context_instance) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/flags/evaluate | Evaluate flags for context instance
[**get_context_attribute_names**](ContextsApi.md#get_context_attribute_names) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/context-attributes | Get context attribute names
[**get_context_attribute_values**](ContextsApi.md#get_context_attribute_values) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/context-attributes/{attributeName} | Get context attribute values
[**get_context_instances**](ContextsApi.md#get_context_instances) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/context-instances/{id} | Get context instances
[**get_context_kinds_by_project_key**](ContextsApi.md#get_context_kinds_by_project_key) | **GET** /api/v2/projects/{projectKey}/context-kinds | Get context kinds
[**get_contexts**](ContextsApi.md#get_contexts) | **GET** /api/v2/projects/{projectKey}/environments/{environmentKey}/contexts/{kind}/{key} | Get contexts
[**put_context_kind**](ContextsApi.md#put_context_kind) | **PUT** /api/v2/projects/{projectKey}/context-kinds/{key} | Create or update context kind
[**search_context_instances**](ContextsApi.md#search_context_instances) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/context-instances/search | Search for context instances
[**search_contexts**](ContextsApi.md#search_contexts) | **POST** /api/v2/projects/{projectKey}/environments/{environmentKey}/contexts/search | Search for contexts


# **delete_context_instances**
> delete_context_instances(project_key, environment_key, id)

Delete context instances

Delete context instances by ID.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import contexts_api
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
    api_instance = contexts_api.ContextsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    id = "id_example" # str | The context instance ID

    # example passing only required values which don't have defaults set
    try:
        # Delete context instances
        api_instance.delete_context_instances(project_key, environment_key, id)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->delete_context_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **id** | **str**| The context instance ID |

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

# **evaluate_context_instance**
> ContextInstanceEvaluations evaluate_context_instance(project_key, environment_key, context_instance)

Evaluate flags for context instance

Evaluate flags for a context instance, for example, to determine the expected flag variation. **Do not use this API instead of an SDK.** The LaunchDarkly SDKs are specialized for the tasks of evaluating feature flags in your application at scale and generating analytics events based on those evaluations. This API is not designed for that use case. Any evaluations you perform with this API will not be reflected in features such as flag statuses and flag insights. Context instances evaluated by this API will not appear in the Contexts list. To learn more, read [Comparing LaunchDarkly's SDKs and REST API](https://docs.launchdarkly.com/guide/api/comparing-sdk-rest-api).  ### Filtering   LaunchDarkly supports the `filter` query param for filtering, with the following fields:  - `query` filters for a string that matches against the flags' keys and names. It is not case sensitive. For example: `filter=query equals dark-mode`. - `tags` filters the list to flags that have all of the tags in the list. For example: `filter=tags contains [\"beta\",\"q1\"]`.  You can also apply multiple filters at once. For example, setting `filter=query equals dark-mode, tags contains [\"beta\",\"q1\"]` matches flags which match the key or name `dark-mode` and are tagged `beta` and `q1`. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import contexts_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.context_instance_evaluations import ContextInstanceEvaluations
from launchdarkly_api.model.context_instance import ContextInstance
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
    api_instance = contexts_api.ContextsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    context_instance = ContextInstance(
        key=None,
    ) # ContextInstance | 
    limit = 1 # int | The number of feature flags to return. Defaults to -1, which returns all flags (optional)
    offset = 1 # int | Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)
    sort = "sort_example" # str | A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order (optional)
    filter = "filter_example" # str | A comma-separated list of filters. Each filter is of the form `field operator value`. Supported fields are explained above. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Evaluate flags for context instance
        api_response = api_instance.evaluate_context_instance(project_key, environment_key, context_instance)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->evaluate_context_instance: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Evaluate flags for context instance
        api_response = api_instance.evaluate_context_instance(project_key, environment_key, context_instance, limit=limit, offset=offset, sort=sort, filter=filter)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->evaluate_context_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **context_instance** | [**ContextInstance**](ContextInstance.md)|  |
 **limit** | **int**| The number of feature flags to return. Defaults to -1, which returns all flags | [optional]
 **offset** | **int**| Where to start in the list. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional]
 **sort** | **str**| A comma-separated list of fields to sort by. Fields prefixed by a dash ( - ) sort in descending order | [optional]
 **filter** | **str**| A comma-separated list of filters. Each filter is of the form &#x60;field operator value&#x60;. Supported fields are explained above. | [optional]

### Return type

[**ContextInstanceEvaluations**](ContextInstanceEvaluations.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag evaluation collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_context_attribute_names**
> ContextAttributeNamesCollection get_context_attribute_names(project_key, environment_key)

Get context attribute names

Get context attribute names.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import contexts_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.context_attribute_names_collection import ContextAttributeNamesCollection
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
    api_instance = contexts_api.ContextsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    filter = "filter_example" # str | A comma-separated list of context filters. This endpoint only accepts `kind` filters, with the `equals` operator, and `name` filters, with the `startsWith` operator. To learn more about the filter syntax, read [Filtering contexts and context instances](/tag/Contexts#filtering-contexts-and-context-instances). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get context attribute names
        api_response = api_instance.get_context_attribute_names(project_key, environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->get_context_attribute_names: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get context attribute names
        api_response = api_instance.get_context_attribute_names(project_key, environment_key, filter=filter)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->get_context_attribute_names: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **filter** | **str**| A comma-separated list of context filters. This endpoint only accepts &#x60;kind&#x60; filters, with the &#x60;equals&#x60; operator, and &#x60;name&#x60; filters, with the &#x60;startsWith&#x60; operator. To learn more about the filter syntax, read [Filtering contexts and context instances](/tag/Contexts#filtering-contexts-and-context-instances). | [optional]

### Return type

[**ContextAttributeNamesCollection**](ContextAttributeNamesCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Context attribute names collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_context_attribute_values**
> ContextAttributeValuesCollection get_context_attribute_values(project_key, environment_key, attribute_name)

Get context attribute values

Get context attribute values.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import contexts_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.context_attribute_values_collection import ContextAttributeValuesCollection
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
    api_instance = contexts_api.ContextsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    attribute_name = "attributeName_example" # str | The attribute name
    filter = "filter_example" # str | A comma-separated list of context filters. This endpoint only accepts `kind` filters, with the `equals` operator, and `value` filters, with the `startsWith` operator. To learn more about the filter syntax, read [Filtering contexts and context instances](/tag/Contexts#filtering-contexts-and-context-instances). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get context attribute values
        api_response = api_instance.get_context_attribute_values(project_key, environment_key, attribute_name)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->get_context_attribute_values: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get context attribute values
        api_response = api_instance.get_context_attribute_values(project_key, environment_key, attribute_name, filter=filter)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->get_context_attribute_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **attribute_name** | **str**| The attribute name |
 **filter** | **str**| A comma-separated list of context filters. This endpoint only accepts &#x60;kind&#x60; filters, with the &#x60;equals&#x60; operator, and &#x60;value&#x60; filters, with the &#x60;startsWith&#x60; operator. To learn more about the filter syntax, read [Filtering contexts and context instances](/tag/Contexts#filtering-contexts-and-context-instances). | [optional]

### Return type

[**ContextAttributeValuesCollection**](ContextAttributeValuesCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Context attribute values collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_context_instances**
> ContextInstances get_context_instances(project_key, environment_key, id)

Get context instances

Get context instances by ID.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import contexts_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.context_instances import ContextInstances
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
    api_instance = contexts_api.ContextsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    id = "id_example" # str | The context instance ID
    limit = 1 # int | Specifies the maximum number of context instances to return (max: 50, default: 20) (optional)
    continuation_token = "continuationToken_example" # str | Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead. (optional)
    sort = "sort_example" # str | Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`. (optional)
    filter = "filter_example" # str | A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](/tag/Contexts#filtering-contexts-and-context-instances). (optional)
    include_total_count = True # bool | Specifies whether to include or omit the total count of matching context instances. Defaults to true. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get context instances
        api_response = api_instance.get_context_instances(project_key, environment_key, id)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->get_context_instances: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get context instances
        api_response = api_instance.get_context_instances(project_key, environment_key, id, limit=limit, continuation_token=continuation_token, sort=sort, filter=filter, include_total_count=include_total_count)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->get_context_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **id** | **str**| The context instance ID |
 **limit** | **int**| Specifies the maximum number of context instances to return (max: 50, default: 20) | [optional]
 **continuation_token** | **str**| Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the &#x60;next&#x60; link we provide instead. | [optional]
 **sort** | **str**| Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying &#x60;ts&#x60; for this value, or descending order by specifying &#x60;-ts&#x60;. | [optional]
 **filter** | **str**| A comma-separated list of context filters. This endpoint only accepts an &#x60;applicationId&#x60; filter. To learn more about the filter syntax, read [Filtering contexts and context instances](/tag/Contexts#filtering-contexts-and-context-instances). | [optional]
 **include_total_count** | **bool**| Specifies whether to include or omit the total count of matching context instances. Defaults to true. | [optional]

### Return type

[**ContextInstances**](ContextInstances.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Context instances collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_context_kinds_by_project_key**
> ContextKindsCollectionRep get_context_kinds_by_project_key(project_key)

Get context kinds

Get all context kinds for a given project.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import contexts_api
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
    api_instance = contexts_api.ContextsApi(api_client)
    project_key = "projectKey_example" # str | The project key

    # example passing only required values which don't have defaults set
    try:
        # Get context kinds
        api_response = api_instance.get_context_kinds_by_project_key(project_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->get_context_kinds_by_project_key: %s\n" % e)
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

# **get_contexts**
> Contexts get_contexts(project_key, environment_key, kind, key)

Get contexts

Get contexts based on kind and key.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import contexts_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.contexts import Contexts
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
    api_instance = contexts_api.ContextsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    kind = "kind_example" # str | The context kind
    key = "key_example" # str | The context key
    limit = 1 # int | Specifies the maximum number of items in the collection to return (max: 50, default: 20) (optional)
    continuation_token = "continuationToken_example" # str | Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead. (optional)
    sort = "sort_example" # str | Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`. (optional)
    filter = "filter_example" # str | A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](/tag/Contexts#filtering-contexts-and-context-instances). (optional)
    include_total_count = True # bool | Specifies whether to include or omit the total count of matching contexts. Defaults to true. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get contexts
        api_response = api_instance.get_contexts(project_key, environment_key, kind, key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->get_contexts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get contexts
        api_response = api_instance.get_contexts(project_key, environment_key, kind, key, limit=limit, continuation_token=continuation_token, sort=sort, filter=filter, include_total_count=include_total_count)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->get_contexts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **kind** | **str**| The context kind |
 **key** | **str**| The context key |
 **limit** | **int**| Specifies the maximum number of items in the collection to return (max: 50, default: 20) | [optional]
 **continuation_token** | **str**| Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the &#x60;next&#x60; link we provide instead. | [optional]
 **sort** | **str**| Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying &#x60;ts&#x60; for this value, or descending order by specifying &#x60;-ts&#x60;. | [optional]
 **filter** | **str**| A comma-separated list of context filters. This endpoint only accepts an &#x60;applicationId&#x60; filter. To learn more about the filter syntax, read [Filtering contexts and context instances](/tag/Contexts#filtering-contexts-and-context-instances). | [optional]
 **include_total_count** | **bool**| Specifies whether to include or omit the total count of matching contexts. Defaults to true. | [optional]

### Return type

[**Contexts**](Contexts.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contexts collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

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
from launchdarkly_api.api import contexts_api
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
    api_instance = contexts_api.ContextsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    key = "key_example" # str | The context kind key
    upsert_context_kind_payload = UpsertContextKindPayload(
        name="organization",
        description="An example context kind for organizations",
        hide_in_targeting=False,
        archived=False,
        version=1,
    ) # UpsertContextKindPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update context kind
        api_response = api_instance.put_context_kind(project_key, key, upsert_context_kind_payload)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->put_context_kind: %s\n" % e)
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

# **search_context_instances**
> ContextInstances search_context_instances(project_key, environment_key, context_instance_search)

Search for context instances

 Search for context instances.  You can use either the query parameters or the request body parameters. If both are provided, there is an error.  To learn more about the filter syntax, read [Filtering contexts and context instances](/tag/Contexts#filtering-contexts-and-context-instances). To learn more about context instances, read [Understanding context instances](https://docs.launchdarkly.com/home/contexts#understanding-context-instances). 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import contexts_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.context_instance_search import ContextInstanceSearch
from launchdarkly_api.model.context_instances import ContextInstances
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
    api_instance = contexts_api.ContextsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    context_instance_search = ContextInstanceSearch(
        filter="{"filter": "kindKeys:{"contains": ["user:Henry"]},"sort": "-ts","limit": 50}",
        sort="-ts",
        limit=10,
        continuation_token="QAGFKH1313KUGI2351",
    ) # ContextInstanceSearch | 
    limit = 1 # int | Specifies the maximum number of items in the collection to return (max: 50, default: 20) (optional)
    continuation_token = "continuationToken_example" # str | Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead. (optional)
    sort = "sort_example" # str | Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`. (optional)
    filter = "filter_example" # str | A comma-separated list of context filters. This endpoint only accepts an `applicationId` filter. To learn more about the filter syntax, read [Filtering contexts and context instances](/tag/Contexts#filtering-contexts-and-context-instances). (optional)
    include_total_count = True # bool | Specifies whether to include or omit the total count of matching context instances. Defaults to true. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search for context instances
        api_response = api_instance.search_context_instances(project_key, environment_key, context_instance_search)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->search_context_instances: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for context instances
        api_response = api_instance.search_context_instances(project_key, environment_key, context_instance_search, limit=limit, continuation_token=continuation_token, sort=sort, filter=filter, include_total_count=include_total_count)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->search_context_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **context_instance_search** | [**ContextInstanceSearch**](ContextInstanceSearch.md)|  |
 **limit** | **int**| Specifies the maximum number of items in the collection to return (max: 50, default: 20) | [optional]
 **continuation_token** | **str**| Limits results to context instances with sort values after the value specified. You can use this for pagination, however, we recommend using the &#x60;next&#x60; link we provide instead. | [optional]
 **sort** | **str**| Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying &#x60;ts&#x60; for this value, or descending order by specifying &#x60;-ts&#x60;. | [optional]
 **filter** | **str**| A comma-separated list of context filters. This endpoint only accepts an &#x60;applicationId&#x60; filter. To learn more about the filter syntax, read [Filtering contexts and context instances](/tag/Contexts#filtering-contexts-and-context-instances). | [optional]
 **include_total_count** | **bool**| Specifies whether to include or omit the total count of matching context instances. Defaults to true. | [optional]

### Return type

[**ContextInstances**](ContextInstances.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Context instances collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_contexts**
> Contexts search_contexts(project_key, environment_key, context_search)

Search for contexts

 Search for contexts.  You can use either the query parameters or the request body parameters. If both are provided, there is an error.  To learn more about the filter syntax, read [Filtering contexts and context instances](/tag/Contexts#filtering-contexts-and-context-instances). To learn more about contexts, read [Understanding contexts and context kinds](https://docs.launchdarkly.com/home/contexts#understanding-contexts-and-context-kinds). 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import contexts_api
from launchdarkly_api.model.context_search import ContextSearch
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.contexts import Contexts
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
    api_instance = contexts_api.ContextsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    context_search = ContextSearch(
        filter="*.name startsWith Jo,kind anyOf ["user","organization"]",
        sort="-ts",
        limit=10,
        continuation_token="QAGFKH1313KUGI2351",
    ) # ContextSearch | 
    limit = 1 # int | Specifies the maximum number of items in the collection to return (max: 50, default: 20) (optional)
    continuation_token = "continuationToken_example" # str | Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the `next` link we provide instead. (optional)
    sort = "sort_example" # str | Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying `ts` for this value, or descending order by specifying `-ts`. (optional)
    filter = "filter_example" # str | A comma-separated list of context filters. To learn more about the filter syntax, read [Filtering contexts and context instances](/tag/Contexts#filtering-contexts-and-context-instances). (optional)
    include_total_count = True # bool | Specifies whether to include or omit the total count of matching contexts. Defaults to true. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search for contexts
        api_response = api_instance.search_contexts(project_key, environment_key, context_search)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->search_contexts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for contexts
        api_response = api_instance.search_contexts(project_key, environment_key, context_search, limit=limit, continuation_token=continuation_token, sort=sort, filter=filter, include_total_count=include_total_count)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling ContextsApi->search_contexts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **environment_key** | **str**| The environment key |
 **context_search** | [**ContextSearch**](ContextSearch.md)|  |
 **limit** | **int**| Specifies the maximum number of items in the collection to return (max: 50, default: 20) | [optional]
 **continuation_token** | **str**| Limits results to contexts with sort values after the value specified. You can use this for pagination, however, we recommend using the &#x60;next&#x60; link we provide instead. | [optional]
 **sort** | **str**| Specifies a field by which to sort. LaunchDarkly supports sorting by timestamp in ascending order by specifying &#x60;ts&#x60; for this value, or descending order by specifying &#x60;-ts&#x60;. | [optional]
 **filter** | **str**| A comma-separated list of context filters. To learn more about the filter syntax, read [Filtering contexts and context instances](/tag/Contexts#filtering-contexts-and-context-instances). | [optional]
 **include_total_count** | **bool**| Specifies whether to include or omit the total count of matching contexts. Defaults to true. | [optional]

### Return type

[**Contexts**](Contexts.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contexts collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

