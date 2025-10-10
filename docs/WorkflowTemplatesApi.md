# launchdarkly_api.WorkflowTemplatesApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow_template**](WorkflowTemplatesApi.md#create_workflow_template) | **POST** /api/v2/templates | Create workflow template
[**delete_workflow_template**](WorkflowTemplatesApi.md#delete_workflow_template) | **DELETE** /api/v2/templates/{templateKey} | Delete workflow template
[**get_workflow_templates**](WorkflowTemplatesApi.md#get_workflow_templates) | **GET** /api/v2/templates | Get workflow templates


# **create_workflow_template**
> WorkflowTemplateOutput create_workflow_template(create_workflow_template_input)

Create workflow template

> ### Workflows are in maintenance mode
>
> The workflows feature is in maintenance mode, and is planned for future deprecation at a date not yet specified. We will work with existing customers using workflows to migrate to a replacement solution when deprecation occurs.

Create a template for a feature flag workflow.


### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.create_workflow_template_input import CreateWorkflowTemplateInput
from launchdarkly_api.models.workflow_template_output import WorkflowTemplateOutput
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
    api_instance = launchdarkly_api.WorkflowTemplatesApi(api_client)
    create_workflow_template_input = launchdarkly_api.CreateWorkflowTemplateInput() # CreateWorkflowTemplateInput | 

    try:
        # Create workflow template
        api_response = api_instance.create_workflow_template(create_workflow_template_input)
        print("The response of WorkflowTemplatesApi->create_workflow_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowTemplatesApi->create_workflow_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workflow_template_input** | [**CreateWorkflowTemplateInput**](CreateWorkflowTemplateInput.md)|  | 

### Return type

[**WorkflowTemplateOutput**](WorkflowTemplateOutput.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Workflow template response JSON |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workflow_template**
> delete_workflow_template(template_key)

Delete workflow template

Delete a workflow template

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
    api_instance = launchdarkly_api.WorkflowTemplatesApi(api_client)
    template_key = 'template_key_example' # str | The template key

    try:
        # Delete workflow template
        api_instance.delete_workflow_template(template_key)
    except Exception as e:
        print("Exception when calling WorkflowTemplatesApi->delete_workflow_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_key** | **str**| The template key | 

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
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_templates**
> WorkflowTemplatesListingOutputRep get_workflow_templates(summary=summary, search=search)

Get workflow templates

Get workflow templates belonging to an account, or can optionally return templates_endpoints.workflowTemplateSummariesListingOutputRep when summary query param is true

### Example

* Api Key Authentication (ApiKey):

```python
import launchdarkly_api
from launchdarkly_api.models.workflow_templates_listing_output_rep import WorkflowTemplatesListingOutputRep
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
    api_instance = launchdarkly_api.WorkflowTemplatesApi(api_client)
    summary = True # bool | Whether the entire template object or just a summary should be returned (optional)
    search = 'search_example' # str | The substring in either the name or description of a template (optional)

    try:
        # Get workflow templates
        api_response = api_instance.get_workflow_templates(summary=summary, search=search)
        print("The response of WorkflowTemplatesApi->get_workflow_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowTemplatesApi->get_workflow_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summary** | **bool**| Whether the entire template object or just a summary should be returned | [optional] 
 **search** | **str**| The substring in either the name or description of a template | [optional] 

### Return type

[**WorkflowTemplatesListingOutputRep**](WorkflowTemplatesListingOutputRep.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workflow templates list response JSON |  -  |
**401** | Invalid access token |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

