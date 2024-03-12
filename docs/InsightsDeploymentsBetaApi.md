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
import time
import launchdarkly_api
from launchdarkly_api.api import insights_deployments_beta_api
from launchdarkly_api.model.validation_failed_error_rep import ValidationFailedErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.post_deployment_event_input import PostDeploymentEventInput
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
    api_instance = insights_deployments_beta_api.InsightsDeploymentsBetaApi(api_client)
    post_deployment_event_input = PostDeploymentEventInput(
        project_key="default",
        environment_key="production",
        application_key="billing-service",
        application_name="Billing Service",
        application_kind="server",
        version="a90a8a2",
        version_name="v1.0.0",
        event_type="started",
        event_time=1,
        event_metadata={
            "key": None,
        },
        deployment_metadata={
            "key": None,
        },
    ) # PostDeploymentEventInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create deployment event
        api_instance.create_deployment_event(post_deployment_event_input)
    except launchdarkly_api.ApiException as e:
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
> DeploymentRep get_deployment(deployment_id)

Get deployment

Get a deployment by ID.  The deployment ID is returned as part of the [List deployments](#operation/getDeployments) response. It is the `id` field of each element in the `items` array.  ### Expanding the deployment response  LaunchDarkly supports expanding the deployment response to include additional fields.  To expand the response, append the `expand` query parameter and include the following:  * `pullRequests` includes details on all of the pull requests associated with each deployment * `flagReferences` includes details on all of the references to flags in each deployment  For example, use `?expand=pullRequests` to include the `pullRequests` field in the response. By default, this field is **not** included in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import insights_deployments_beta_api
from launchdarkly_api.model.validation_failed_error_rep import ValidationFailedErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.deployment_rep import DeploymentRep
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
    api_instance = insights_deployments_beta_api.InsightsDeploymentsBetaApi(api_client)
    deployment_id = "deploymentID_example" # str | The deployment ID
    expand = "expand_example" # str | Expand properties in response. Options: `pullRequests`, `flagReferences` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get deployment
        api_response = api_instance.get_deployment(deployment_id)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling InsightsDeploymentsBetaApi->get_deployment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get deployment
        api_response = api_instance.get_deployment(deployment_id, expand=expand)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
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
> DeploymentCollectionRep get_deployments(project_key, environment_key)

List deployments

Get a list of deployments  ### Expanding the deployment collection response  LaunchDarkly supports expanding the deployment collection response to include additional fields.  To expand the response, append the `expand` query parameter and include the following:  * `pullRequests` includes details on all of the pull requests associated with each deployment * `flagReferences` includes details on all of the references to flags in each deployment  For example, use `?expand=pullRequests` to include the `pullRequests` field in the response. By default, this field is **not** included in the response. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import insights_deployments_beta_api
from launchdarkly_api.model.validation_failed_error_rep import ValidationFailedErrorRep
from launchdarkly_api.model.deployment_collection_rep import DeploymentCollectionRep
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
    api_instance = insights_deployments_beta_api.InsightsDeploymentsBetaApi(api_client)
    project_key = "projectKey_example" # str | The project key
    environment_key = "environmentKey_example" # str | The environment key
    application_key = "applicationKey_example" # str | Comma separated list of application keys (optional)
    limit = 1 # int | The number of deployments to return. Default is 20. Maximum allowed is 100. (optional)
    expand = "expand_example" # str | Expand properties in response. Options: `pullRequests`, `flagReferences` (optional)
    _from = 1 # int | Unix timestamp in milliseconds. Default value is 7 days ago. (optional)
    to = 1 # int | Unix timestamp in milliseconds. Default value is now. (optional)
    after = "after_example" # str | Identifier used for pagination (optional)
    before = "before_example" # str | Identifier used for pagination (optional)
    kind = "kind_example" # str | The deployment kind (optional)
    status = "status_example" # str | The deployment status (optional)

    # example passing only required values which don't have defaults set
    try:
        # List deployments
        api_response = api_instance.get_deployments(project_key, environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling InsightsDeploymentsBetaApi->get_deployments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List deployments
        api_response = api_instance.get_deployments(project_key, environment_key, application_key=application_key, limit=limit, expand=expand, _from=_from, to=to, after=after, before=before, kind=kind, status=status)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
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
 **_from** | **int**| Unix timestamp in milliseconds. Default value is 7 days ago. | [optional]
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
> DeploymentRep update_deployment(deployment_id, json_patch)

Update deployment

Update a deployment by ID. Updating a deployment uses a [JSON patch](https://datatracker.ietf.org/doc/html/rfc6902) representation of the desired changes. To learn more, read [Updates](/#section/Overview/Updates).<br/><br/>The deployment ID is returned as part of the [List deployments](#operation/getDeployments) response. It is the `id` field of each element in the `items` array.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import insights_deployments_beta_api
from launchdarkly_api.model.json_patch import JSONPatch
from launchdarkly_api.model.validation_failed_error_rep import ValidationFailedErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.deployment_rep import DeploymentRep
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
    api_instance = insights_deployments_beta_api.InsightsDeploymentsBetaApi(api_client)
    deployment_id = "deploymentID_example" # str | The deployment ID
    json_patch = JSONPatch([
        PatchOperation(
            op="replace",
            path="/exampleField",
            value=None,
        ),
    ]) # JSONPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update deployment
        api_response = api_instance.update_deployment(deployment_id, json_patch)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling InsightsDeploymentsBetaApi->update_deployment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| The deployment ID |
 **json_patch** | [**JSONPatch**](JSONPatch.md)|  |

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

