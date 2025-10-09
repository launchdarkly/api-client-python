# launchdarkly_api.DataExportDestinationsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_destination**](DataExportDestinationsApi.md#delete_destination) | **DELETE** /api/v2/destinations/{projectKey}/{environmentKey}/{id} | Delete Data Export destination
[**get_destination**](DataExportDestinationsApi.md#get_destination) | **GET** /api/v2/destinations/{projectKey}/{environmentKey}/{id} | Get destination
[**get_destinations**](DataExportDestinationsApi.md#get_destinations) | **GET** /api/v2/destinations | List destinations
[**patch_destination**](DataExportDestinationsApi.md#patch_destination) | **PATCH** /api/v2/destinations/{projectKey}/{environmentKey}/{id} | Update Data Export destination
[**post_destination**](DataExportDestinationsApi.md#post_destination) | **POST** /api/v2/destinations/{projectKey}/{environmentKey} | Create Data Export destination
[**post_generate_warehouse_destination_key_pair**](DataExportDestinationsApi.md#post_generate_warehouse_destination_key_pair) | **POST** /api/v2/destinations/generate-warehouse-destination-key-pair | Generate Snowflake destination key pair


# **delete_destination**
> delete_destination(project_key, environment_key, id)

Delete Data Export destination

Delete a Data Export destination by ID.

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
    api_instance = launchdarkly_api.DataExportDestinationsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    id = 'id_example' # str | The Data Export destination ID

    try:
        # Delete Data Export destination
        api_instance.delete_destination(project_key, environment_key, id)
    except Exception as e:
        print("Exception when calling DataExportDestinationsApi->delete_destination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **id** | **str**| The Data Export destination ID | 

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
**204** | Destination response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destination**
> Destination get_destination(project_key, environment_key, id)

Get destination

Get a single Data Export destination by ID.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.destination import Destination
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
    api_instance = launchdarkly_api.DataExportDestinationsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    id = 'id_example' # str | The Data Export destination ID

    try:
        # Get destination
        api_response = api_instance.get_destination(project_key, environment_key, id)
        print("The response of DataExportDestinationsApi->get_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataExportDestinationsApi->get_destination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **id** | **str**| The Data Export destination ID | 

### Return type

[**Destination**](Destination.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Destination response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destinations**
> Destinations get_destinations()

List destinations

Get a list of Data Export destinations configured across all projects and environments.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.destinations import Destinations
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
    api_instance = launchdarkly_api.DataExportDestinationsApi(api_client)

    try:
        # List destinations
        api_response = api_instance.get_destinations()
        print("The response of DataExportDestinationsApi->get_destinations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataExportDestinationsApi->get_destinations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Destinations**](Destinations.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Destination collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_destination**
> Destination patch_destination(project_key, environment_key, id, patch_operation)

Update Data Export destination

Update a Data Export destination. Updating a destination uses a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) or [JSON merge patch](https://datatracker.ietf.org/doc/html/rfc7386) representation of the desired changes. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates).

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.destination import Destination
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
    api_instance = launchdarkly_api.DataExportDestinationsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    id = 'id_example' # str | The Data Export destination ID
    patch_operation = [{"op":"replace","path":"/config/topic","value":"ld-pubsub-test-192302"}] # List[PatchOperation] | 

    try:
        # Update Data Export destination
        api_response = api_instance.patch_destination(project_key, environment_key, id, patch_operation)
        print("The response of DataExportDestinationsApi->patch_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataExportDestinationsApi->patch_destination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **id** | **str**| The Data Export destination ID | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**Destination**](Destination.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Destination response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_destination**
> Destination post_destination(project_key, environment_key, destination_post)

Create Data Export destination

 Create a new Data Export destination.  In the `config` request body parameter, the fields required depend on the type of Data Export destination.  <details> <summary>Click to expand <code>config</code> parameter details</summary>  #### Azure Event Hubs  To create a Data Export destination with a `kind` of `azure-event-hubs`, the `config` object requires the following fields:  * `namespace`: The Event Hub Namespace name * `name`: The Event Hub name * `policyName`: The shared access signature policy name. You can find your policy name in the settings of your Azure Event Hubs Namespace. * `policyKey`: The shared access signature key. You can find your policy key in the settings of your Azure Event Hubs Namespace.  #### Google Cloud Pub/Sub  To create a Data Export destination with a `kind` of `google-pubsub`, the `config` object requires the following fields:  * `project`: The Google PubSub project ID for the project to publish to * `topic`: The Google PubSub topic ID for the topic to publish to  #### Amazon Kinesis  To create a Data Export destination with a `kind` of `kinesis`, the `config` object requires the following fields:  * `region`: The Kinesis stream's AWS region key * `roleArn`: The Amazon Resource Name (ARN) of the AWS role that will be writing to Kinesis * `streamName`: The name of the Kinesis stream that LaunchDarkly is sending events to. This is not the ARN of the stream.  #### mParticle  To create a Data Export destination with a `kind` of `mparticle`, the `config` object requires the following fields:  * `apiKey`: The mParticle API key * `secret`: The mParticle API secret * `userIdentity`: The type of identifier you use to identify your end users in mParticle * `anonymousUserIdentity`: The type of identifier you use to identify your anonymous end users in mParticle  #### Segment  To create a Data Export destination with a `kind` of `segment`, the `config` object requires the following fields:  * `writeKey`: The Segment write key. This is used to authenticate LaunchDarkly's calls to Segment.  #### Snowflake  To create a Data Export destination with a `kind` of `snowflake-v2`, the `config` object requires the following fields:  * `publicKey`: The `publicKey` is returned as part of the [Generate Snowflake destination key pair](https://launchdarkly.com/docs/api/data-export-destinations/post-generate-warehouse-destination-key-pair) response. It is the `public_key` field. * `snowflakeHostAddress`: Your Snowflake account URL.  </details> 

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.destination import Destination
from launchdarkly_api.models.destination_post import DestinationPost
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
    api_instance = launchdarkly_api.DataExportDestinationsApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    destination_post = {"config":{"project":"test-prod","topic":"ld-pubsub-test-192301"},"kind":"google-pubsub"} # DestinationPost | 

    try:
        # Create Data Export destination
        api_response = api_instance.post_destination(project_key, environment_key, destination_post)
        print("The response of DataExportDestinationsApi->post_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataExportDestinationsApi->post_destination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **destination_post** | [**DestinationPost**](DestinationPost.md)|  | 

### Return type

[**Destination**](Destination.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Destination response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_generate_warehouse_destination_key_pair**
> GenerateWarehouseDestinationKeyPairPostRep post_generate_warehouse_destination_key_pair()

Generate Snowflake destination key pair

Generate key pair to allow Data Export to authenticate into a Snowflake warehouse destination

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.generate_warehouse_destination_key_pair_post_rep import GenerateWarehouseDestinationKeyPairPostRep
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
    api_instance = launchdarkly_api.DataExportDestinationsApi(api_client)

    try:
        # Generate Snowflake destination key pair
        api_response = api_instance.post_generate_warehouse_destination_key_pair()
        print("The response of DataExportDestinationsApi->post_generate_warehouse_destination_key_pair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataExportDestinationsApi->post_generate_warehouse_destination_key_pair: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GenerateWarehouseDestinationKeyPairPostRep**](GenerateWarehouseDestinationKeyPairPostRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Generate warehouse destination key pair response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**409** | Status conflict |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

