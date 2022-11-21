# launchdarkly_api.WorkflowTemplatesBetaApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow_template**](WorkflowTemplatesBetaApi.md#create_workflow_template) | **POST** /api/v2/templates | Create workflow template
[**delete_workflow_template**](WorkflowTemplatesBetaApi.md#delete_workflow_template) | **DELETE** /api/v2/templates/{templateKey} | Delete workflow template
[**get_workflow_templates**](WorkflowTemplatesBetaApi.md#get_workflow_templates) | **GET** /api/v2/templates | Get workflow templates


# **create_workflow_template**
> WorkflowTemplateOutput create_workflow_template(create_workflow_template_input)

Create workflow template

Create a template for a feature flag workflow

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import workflow_templates_beta_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.workflow_template_output import WorkflowTemplateOutput
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.create_workflow_template_input import CreateWorkflowTemplateInput
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
    api_instance = workflow_templates_beta_api.WorkflowTemplatesBetaApi(api_client)
    create_workflow_template_input = CreateWorkflowTemplateInput(
        key="key_example",
        name="name_example",
        description="description_example",
        workflow_id="workflow_id_example",
        stages=[
            StageInput(
                name="10% rollout on day 1",
                execute_conditions_in_sequence=True,
                conditions=[
                    ConditionInput(
                        schedule_kind="schedule_kind_example",
                        execution_date=1,
                        wait_duration=2,
                        wait_duration_unit="wait_duration_unit_example",
                        execute_now=False,
                        description="description_example",
                        notify_member_ids=[
                            "notify_member_ids_example",
                        ],
                        notify_team_keys=[
                            "notify_team_keys_example",
                        ],
                        kind="kind_example",
                    ),
                ],
                action=ActionInput(
                    instructions=None,
                ),
            ),
        ],
        project_key="project_key_example",
        environment_key="environment_key_example",
        flag_key="flag_key_example",
    ) # CreateWorkflowTemplateInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create workflow template
        api_response = api_instance.create_workflow_template(create_workflow_template_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling WorkflowTemplatesBetaApi->create_workflow_template: %s\n" % e)
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
import time
import launchdarkly_api
from launchdarkly_api.api import workflow_templates_beta_api
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
    api_instance = workflow_templates_beta_api.WorkflowTemplatesBetaApi(api_client)
    template_key = "templateKey_example" # str | The template key

    # example passing only required values which don't have defaults set
    try:
        # Delete workflow template
        api_instance.delete_workflow_template(template_key)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling WorkflowTemplatesBetaApi->delete_workflow_template: %s\n" % e)
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
> WorkflowTemplatesListingOutputRep get_workflow_templates()

Get workflow templates

Get workflow templates belonging to an account, or can optionally return templates_endpoints.workflowTemplateSummariesListingOutputRep when summary query param is true

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import workflow_templates_beta_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.workflow_templates_listing_output_rep import WorkflowTemplatesListingOutputRep
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
    api_instance = workflow_templates_beta_api.WorkflowTemplatesBetaApi(api_client)
    search = "search_example" # str | The substring in either the name or description of a template (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get workflow templates
        api_response = api_instance.get_workflow_templates(search=search)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling WorkflowTemplatesBetaApi->get_workflow_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

