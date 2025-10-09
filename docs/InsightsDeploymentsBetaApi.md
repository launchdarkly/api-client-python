# launchdarkly_api.InsightsDeploymentsBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deployment_event**](InsightsDeploymentsBetaApi.md#create_deployment_event) | **POST** /api/v2/engineering-insights/deployment-events | Create deployment event
[**get_deployment**](InsightsDeploymentsBetaApi.md#get_deployment) | **GET** /api/v2/engineering-insights/deployments/{deploymentID} | Get deployment
[**get_deployments**](InsightsDeploymentsBetaApi.md#get_deployments) | **GET** /api/v2/engineering-insights/deployments | List deployments
[**update_deployment**](InsightsDeploymentsBetaApi.md#update_deployment) | **PATCH** /api/v2/engineering-insights/deployments/{deploymentID} | Update deployment


# **create_deployment_event**
> create_deployment_event(post_deployment_event_input)

Create deployment event

Create deployment event

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.post_deployment_event_input import PostDeploymentEventInput
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
    api_instance = launchdarkly_api.InsightsDeploymentsBetaApi(api_client)
    post_deployment_event_input = launchdarkly_api.PostDeploymentEventInput() # PostDeploymentEventInput | 

    try:
        # Create deployment event
        api_instance.create_deployment_event(post_deployment_event_input)
    except Exception as e:
        print("Exception when calling InsightsDeploymentsBetaApi->create_deployment_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_deployment_event_input** | [**PostDeploymentEventInput**](PostDeploymentEventInput.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment**
> DeploymentRep get_deployment(deployment_id, expand=expand)

Get deployment

Get a deployment by ID.  The deployment ID is returned as part of the [List deployments](https://launchdarkly.com/docs/api/insights-deployments-beta/get-deployments) response. It is the `id` field of each element in the `items` array.  ### Expanding the deployment response  LaunchDarkly supports expanding the deployment response to include additional fields.  To expand the response, append the `expand` query parameter and include the following:  * `pullRequests` includes details on all of the pull requests associated with each deployment * `flagReferences` includes details on all of the references to flags in each deployment  For example, use `?expand=pullRequests` to include the `pullRequests` field in the response. By default, this field is **not** included in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.deployment_rep import DeploymentRep
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
    api_instance = launchdarkly_api.InsightsDeploymentsBetaApi(api_client)
    deployment_id = 'deployment_id_example' # str | The deployment ID
    expand = 'expand_example' # str | Expand properties in response. Options: `pullRequests`, `flagReferences` (optional)

    try:
        # Get deployment
        api_response = api_instance.get_deployment(deployment_id, expand=expand)
        print("The response of InsightsDeploymentsBetaApi->get_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsDeploymentsBetaApi->get_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| The deployment ID | 
 **expand** | **str**| Expand properties in response. Options: &#x60;pullRequests&#x60;, &#x60;flagReferences&#x60; | [optional] 

### Return type

[**DeploymentRep**](DeploymentRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deployment response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments**
> DeploymentCollectionRep get_deployments(project_key, environment_key, application_key=application_key, limit=limit, expand=expand, var_from=var_from, to=to, after=after, before=before, kind=kind, status=status)

List deployments

Get a list of deployments  ### Expanding the deployment collection response  LaunchDarkly supports expanding the deployment collection response to include additional fields.  To expand the response, append the `expand` query parameter and include the following:  * `pullRequests` includes details on all of the pull requests associated with each deployment * `flagReferences` includes details on all of the references to flags in each deployment  For example, use `?expand=pullRequests` to include the `pullRequests` field in the response. By default, this field is **not** included in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.deployment_collection_rep import DeploymentCollectionRep
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
    api_instance = launchdarkly_api.InsightsDeploymentsBetaApi(api_client)
    project_key = 'project_key_example' # str | The project key
    environment_key = 'environment_key_example' # str | The environment key
    application_key = 'application_key_example' # str | Comma separated list of application keys (optional)
    limit = 56 # int | The number of deployments to return. Default is 20. Maximum allowed is 100. (optional)
    expand = 'expand_example' # str | Expand properties in response. Options: `pullRequests`, `flagReferences` (optional)
    var_from = 56 # int | Unix timestamp in milliseconds. Default value is 7 days ago. (optional)
    to = 56 # int | Unix timestamp in milliseconds. Default value is now. (optional)
    after = 'after_example' # str | Identifier used for pagination (optional)
    before = 'before_example' # str | Identifier used for pagination (optional)
    kind = 'kind_example' # str | The deployment kind (optional)
    status = 'status_example' # str | The deployment status (optional)

    try:
        # List deployments
        api_response = api_instance.get_deployments(project_key, environment_key, application_key=application_key, limit=limit, expand=expand, var_from=var_from, to=to, after=after, before=before, kind=kind, status=status)
        print("The response of InsightsDeploymentsBetaApi->get_deployments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsDeploymentsBetaApi->get_deployments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key | 
 **environment_key** | **str**| The environment key | 
 **application_key** | **str**| Comma separated list of application keys | [optional] 
 **limit** | **int**| The number of deployments to return. Default is 20. Maximum allowed is 100. | [optional] 
 **expand** | **str**| Expand properties in response. Options: &#x60;pullRequests&#x60;, &#x60;flagReferences&#x60; | [optional] 
 **var_from** | **int**| Unix timestamp in milliseconds. Default value is 7 days ago. | [optional] 
 **to** | **int**| Unix timestamp in milliseconds. Default value is now. | [optional] 
 **after** | **str**| Identifier used for pagination | [optional] 
 **before** | **str**| Identifier used for pagination | [optional] 
 **kind** | **str**| The deployment kind | [optional] 
 **status** | **str**| The deployment status | [optional] 

### Return type

[**DeploymentCollectionRep**](DeploymentCollectionRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deployment collection response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_deployment**
> DeploymentRep update_deployment(deployment_id, patch_operation)

Update deployment

Update a deployment by ID. Updating a deployment uses a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes. To learn more, read [Updates](https://launchdarkly.com/docs/api#updates).<br/><br/>The deployment ID is returned as part of the [List deployments](https://launchdarkly.com/docs/api/insights-deployments-beta/get-deployments) response. It is the `id` field of each element in the `items` array.

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.deployment_rep import DeploymentRep
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
    api_instance = launchdarkly_api.InsightsDeploymentsBetaApi(api_client)
    deployment_id = 'deployment_id_example' # str | The deployment ID
    patch_operation = [{"op":"replace","path":"/status","value":"finished"}] # List[PatchOperation] | 

    try:
        # Update deployment
        api_response = api_instance.update_deployment(deployment_id, patch_operation)
        print("The response of InsightsDeploymentsBetaApi->update_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsDeploymentsBetaApi->update_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| The deployment ID | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)|  | 

### Return type

[**DeploymentRep**](DeploymentRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deployment response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

