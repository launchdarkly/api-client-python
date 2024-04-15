# launchdarkly_api.WorkflowsApi

All URIs are relative to *https://app.launchdarkly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_workflow**](WorkflowsApi.md#delete_workflow) | **DELETE** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/workflows/{workflowId} | Delete workflow
[**get_custom_workflow**](WorkflowsApi.md#get_custom_workflow) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/workflows/{workflowId} | Get custom workflow
[**get_workflows**](WorkflowsApi.md#get_workflows) | **GET** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/workflows | Get workflows
[**post_workflow**](WorkflowsApi.md#post_workflow) | **POST** /api/v2/projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/workflows | Create workflow


# **delete_workflow**
> delete_workflow(project_key, feature_flag_key, environment_key, workflow_id)

Delete workflow

Delete a workflow from a feature flag.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import workflows_api
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    workflow_id = "workflowId_example" # str | The workflow id

    # example passing only required values which don't have defaults set
    try:
        # Delete workflow
        api_instance.delete_workflow(project_key, feature_flag_key, environment_key, workflow_id)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling WorkflowsApi->delete_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **environment_key** | **str**| The environment key |
 **workflow_id** | **str**| The workflow id |

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

# **get_custom_workflow**
> CustomWorkflowOutput get_custom_workflow(project_key, feature_flag_key, environment_key, workflow_id)

Get custom workflow

Get a specific workflow by ID.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import workflows_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.custom_workflow_output import CustomWorkflowOutput
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    workflow_id = "workflowId_example" # str | The workflow ID

    # example passing only required values which don't have defaults set
    try:
        # Get custom workflow
        api_response = api_instance.get_custom_workflow(project_key, feature_flag_key, environment_key, workflow_id)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling WorkflowsApi->get_custom_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **environment_key** | **str**| The environment key |
 **workflow_id** | **str**| The workflow ID |

### Return type

[**CustomWorkflowOutput**](CustomWorkflowOutput.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workflow response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflows**
> CustomWorkflowsListingOutput get_workflows(project_key, feature_flag_key, environment_key)

Get workflows

Display workflows associated with a feature flag.

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import workflows_api
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.custom_workflows_listing_output import CustomWorkflowsListingOutput
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    status = "status_example" # str | Filter results by workflow status. Valid status filters are `active`, `completed`, and `failed`. (optional)
    sort = "sort_example" # str | A field to sort the items by. Prefix field by a dash ( - ) to sort in descending order. This endpoint supports sorting by `creationDate` or `stopDate`. (optional)
    limit = 1 # int | The maximum number of workflows to return. Defaults to 20. (optional)
    offset = 1 # int | Where to start in the list. Defaults to 0. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query `limit`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get workflows
        api_response = api_instance.get_workflows(project_key, feature_flag_key, environment_key)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflows: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get workflows
        api_response = api_instance.get_workflows(project_key, feature_flag_key, environment_key, status=status, sort=sort, limit=limit, offset=offset)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **environment_key** | **str**| The environment key |
 **status** | **str**| Filter results by workflow status. Valid status filters are &#x60;active&#x60;, &#x60;completed&#x60;, and &#x60;failed&#x60;. | [optional]
 **sort** | **str**| A field to sort the items by. Prefix field by a dash ( - ) to sort in descending order. This endpoint supports sorting by &#x60;creationDate&#x60; or &#x60;stopDate&#x60;. | [optional]
 **limit** | **int**| The maximum number of workflows to return. Defaults to 20. | [optional]
 **offset** | **int**| Where to start in the list. Defaults to 0. Use this with pagination. For example, an offset of 10 skips the first ten items and then returns the next items in the list, up to the query &#x60;limit&#x60;. | [optional]

### Return type

[**CustomWorkflowsListingOutput**](CustomWorkflowsListingOutput.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workflows collection response |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_workflow**
> CustomWorkflowOutput post_workflow(project_key, feature_flag_key, environment_key, custom_workflow_input)

Create workflow

Create a workflow for a feature flag. You can create a workflow directly, or you can apply a template to create a new workflow.  ### Creating a workflow  You can use the create workflow endpoint to create a workflow directly by adding a `stages` array to the request body.  For each stage, define the `name`, `conditions` when the stage should be executed, and `action` that describes the stage.  <details> <summary>Click to expand example</summary>  _Example request body_ ```json {   \"name\": \"Progressive rollout starting in two days\",   \"description\": \"Turn flag targeting on and increase feature rollout in 10% increments each day\",   \"stages\": [     {       \"name\": \"10% rollout on day 1\",       \"conditions\": [         {           \"kind\": \"schedule\",           \"scheduleKind\": \"relative\", // or \"absolute\"               //  If \"scheduleKind\" is \"absolute\", set \"executionDate\";               // \"waitDuration\" and \"waitDurationUnit\" will be ignored           \"waitDuration\": 2,           \"waitDurationUnit\": \"calendarDay\"         },         {           \"kind\": \"ld-approval\",           \"notifyMemberIds\": [ \"507f1f77bcf86cd799439011\" ],           \"notifyTeamKeys\": [ \"team-key-123abc\" ]         }       ],       \"action\": {         \"instructions\": [           {             \"kind\": \"turnFlagOn\"           },           {             \"kind\": \"updateFallthroughVariationOrRollout\",             \"rolloutWeights\": {               \"452f5fb5-7320-4ba3-81a1-8f4324f79d49\": 90000,               \"fc15f6a4-05d3-4aa4-a997-446be461345d\": 10000             }           }         ]       }     }   ] } ``` </details>  ### Creating a workflow by applying a workflow template  You can also create a workflow by applying a workflow template. If you pass a valid workflow template key as the `templateKey` query parameter with the request, the API will attempt to create a new workflow with the stages defined in the workflow template with the corresponding key.  #### Applicability of stages Templates are created in the context of a particular flag in a particular environment in a particular project. However, because workflows created from a template can be applied to any project, environment, and flag, some steps of the workflow may need to be updated in order to be applicable for the target resource.  You can pass a `dryRun` query parameter to tell the API to return a report of which steps of the workflow template are applicable in the target project/environment/flag, and which will need to be updated. When the `dryRun` query parameter is present the response body includes a `meta` property that holds a list of parameters that could potentially be inapplicable for the target resource. Each of these parameters will include a `valid` field. You will need to update any invalid parameters in order to create the new workflow. You can do this using the `parameters` property, which overrides the workflow template parameters.  #### Overriding template parameters You can use the `parameters` property in the request body to tell the API to override the specified workflow template parameters with new values that are specific to your target project/environment/flag.  <details> <summary>Click to expand example</summary>  _Example request body_ ```json {  \"name\": \"workflow created from my-template\",  \"description\": \"description of my workflow\",  \"parameters\": [   {    \"_id\": \"62cf2bc4cadbeb7697943f3b\",    \"path\": \"/clauses/0/values\",    \"default\": {     \"value\": [\"updated-segment\"]    }   },   {    \"_id\": \"62cf2bc4cadbeb7697943f3d\",    \"path\": \"/variationId\",    \"default\": {     \"value\": \"abcd1234-abcd-1234-abcd-1234abcd12\"    }   }  ] } ``` </details>  If there are any steps in the template that are not applicable to the target resource, the workflow will not be created, and the `meta` property will be included in the response body detailing which parameters need to be updated. 

### Example

* Api Key Authentication (ApiKey):

```python
import time
import launchdarkly_api
from launchdarkly_api.api import workflows_api
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.custom_workflow_output import CustomWorkflowOutput
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.custom_workflow_input import CustomWorkflowInput
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    project_key = "projectKey_example" # str | The project key
    feature_flag_key = "featureFlagKey_example" # str | The feature flag key
    environment_key = "environmentKey_example" # str | The environment key
    custom_workflow_input = CustomWorkflowInput(
        maintainer_id="maintainer_id_example",
        name="Progressive rollout starting in two days",
        description="Turn flag on for 10% of users each day",
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
                        description="Require example-team approval for final stage",
                        notify_member_ids=["507f1f77bcf86cd799439011"],
                        notify_team_keys=["example-team"],
                        kind="kind_example",
                    ),
                ],
                action=ActionInput(
                    instructions=None,
                ),
            ),
        ],
        template_key="template_key_example",
    ) # CustomWorkflowInput | 
    template_key = "templateKey_example" # str | The template key to apply as a starting point for the new workflow (optional)
    dry_run = True # bool | Whether to call the endpoint in dry-run mode (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create workflow
        api_response = api_instance.post_workflow(project_key, feature_flag_key, environment_key, custom_workflow_input)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling WorkflowsApi->post_workflow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create workflow
        api_response = api_instance.post_workflow(project_key, feature_flag_key, environment_key, custom_workflow_input, template_key=template_key, dry_run=dry_run)
        pprint(api_response)
    except launchdarkly_api.ApiException as e:
        print("Exception when calling WorkflowsApi->post_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key |
 **feature_flag_key** | **str**| The feature flag key |
 **environment_key** | **str**| The environment key |
 **custom_workflow_input** | [**CustomWorkflowInput**](CustomWorkflowInput.md)|  |
 **template_key** | **str**| The template key to apply as a starting point for the new workflow | [optional]
 **dry_run** | **bool**| Whether to call the endpoint in dry-run mode | [optional]

### Return type

[**CustomWorkflowOutput**](CustomWorkflowOutput.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Workflow response |  -  |
**400** | Invalid request |  -  |
**401** | Invalid access token |  -  |
**403** | Forbidden |  -  |
**404** | Invalid resource identifier |  -  |
**429** | Rate limited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

