# launchdarkly_api.LayersApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_layer**](LayersApi.md#create_layer) | **POST** /api/v2/projects/{projectKey}/layers | Create layer
[**get_layers**](LayersApi.md#get_layers) | **GET** /api/v2/projects/{projectKey}/layers | Get layers
[**update_layer**](LayersApi.md#update_layer) | **PATCH** /api/v2/projects/{projectKey}/layers/{layerKey} | Update layer


# **create_layer**
> LayerRep create_layer(project_key, layer_post)

Create layer

Create a layer. Experiments running in the same layer are granted mutually-exclusive traffic. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import layers_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.layer_post import LayerPost
from launchdarkly_api.model.layer_rep import LayerRep
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
    api_instance = layers_api.LayersApi(api_client)
    project_key = "projectKey_example" # str | The project key
    layer_post = LayerPost(
        key="checkout-flow",
        name="Checkout Flow",
        description="description_example",
    ) # LayerPost | 

    # example passing only required values which don't have defaults set
    try:
        # Create layer
        api_response = api_instance.create_layer(project_key, layer_post)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling LayersApi->create_layer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **layer_post** | [**LayerPost**](LayerPost.md)|  |

### Return type

[**LayerRep**](LayerRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Layer response |  -  |
**400** | Invalid request |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_layers**
> LayerCollectionRep get_layers(project_key)

Get layers

Get a collection of all layers for a project

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import layers_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.layer_collection_rep import LayerCollectionRep
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
    api_instance = layers_api.LayersApi(api_client)
    project_key = "projectKey_example" # str | The project key
    filter = "filter_example" # str | A comma-separated list of filters. This endpoint only accepts filtering by `experimentKey`. The filter returns layers which include that experiment for the selected environment(s). For example: `filter=reservations.experimentKey contains expKey`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get layers
        api_response = api_instance.get_layers(project_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling LayersApi->get_layers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get layers
        api_response = api_instance.get_layers(project_key, filter=filter)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling LayersApi->get_layers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **filter** | **str**| A comma-separated list of filters. This endpoint only accepts filtering by &#x60;experimentKey&#x60;. The filter returns layers which include that experiment for the selected environment(s). For example: &#x60;filter&#x3D;reservations.experimentKey contains expKey&#x60;. | [optional]

### Return type

[**LayerCollectionRep**](LayerCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Layer Collection response |  -  |
**400** | Invalid request |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_layer**
> LayerRep update_layer(project_key, layer_key, layer_patch_input)

Update layer

Update a layer by adding, changing, or removing traffic reservations for experiments, or by changing layer name or description. Updating a layer uses the semantic patch format.  To make a semantic patch request, you must append `domain-model=launchdarkly.semanticpatch` to your `Content-Type` header. To learn more, read [Updates using semantic patch](/reference#updates-using-semantic-patch).  ### Instructions  Semantic patch requests support the following `kind` instructions for updating layers.  <details> <summary>Click to expand instructions for <strong>updating layers</strong></summary>  #### updateName  Updates the layer name.  ##### Parameters  - `name`: The new layer name.  Here's an example:  ```json {   \"instructions\": [{       \"kind\": \"updateName\",       \"name\": \"New name\"   }] } ```  #### updateDescription  Updates the layer description.  ##### Parameters  - `description`: The new description.  Here's an example:  ```json {   \"instructions\": [{       \"kind\": \"updateDescription\",       \"description\": \"New description\"   }] } ```  #### updateExperimentReservation  Adds or updates a traffic reservation for an experiment in a layer.  ##### Parameters  - `experimentKey`: The key of the experiment whose reservation you are adding to or updating in the layer. - `reservationPercent`: The amount of traffic in the layer to reserve. Must be an integer. Zero is allowed until iteration start.  Here's an example:  ```json {   \"environmentKey\": \"production\",   \"instructions\": [{       \"kind\": \"updateExperimentReservation\",       \"experimentKey\": \"exp-key\",       \"reservationPercent\": 10   }] } ```  #### removeExperiment  Removes a traffic reservation for an experiment from a layer.  ##### Parameters  - `experimentKey`: The key of the experiment whose reservation you want to remove from the layer.  Here's an example:  ```json {   \"environmentKey\": \"production\",   \"instructions\": [{       \"kind\": \"removeExperiment\",       \"experimentKey\": \"exp-key\"   }] } ```  </details> 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import layers_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.layer_rep import LayerRep
from launchdarkly_api.model.layer_patch_input import LayerPatchInput
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
    api_instance = layers_api.LayersApi(api_client)
    project_key = "projectKey_example" # str | The project key
    layer_key = "layerKey_example" # str | The layer key
    layer_patch_input = LayerPatchInput(
        comment="Optional comment",
        environment_key="production",
        instructions=Instructions([
            Instruction(
                key=None,
            ),
        ]),
    ) # LayerPatchInput | 

    # example passing only required values which don't have defaults set
    try:
        # Update layer
        api_response = api_instance.update_layer(project_key, layer_key, layer_patch_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling LayersApi->update_layer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **layer_key** | **str**| The layer key |
 **layer_patch_input** | [**LayerPatchInput**](LayerPatchInput.md)|  |

### Return type

[**LayerRep**](LayerRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Layer response |  -  |
**400** | Invalid request |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

