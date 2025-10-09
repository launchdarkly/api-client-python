# FlagConfigApprovalRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of this approval request | 
**version** | **int** | Version of the approval request | 
**creation_date** | **int** |  | 
**service_kind** | **str** |  | 
**requestor_id** | **str** | The ID of the member who requested the approval | [optional] 
**description** | **str** | A human-friendly name for the approval request | [optional] 
**review_status** | **str** | Current status of the review of this approval request | 
**all_reviews** | [**List[ReviewResponse]**](ReviewResponse.md) | An array of individual reviews of this approval request | 
**notify_member_ids** | **List[str]** | An array of member IDs. These members are notified to review the approval request. | 
**applied_date** | **int** |  | [optional] 
**applied_by_member_id** | **str** | The member ID of the member who applied the approval request | [optional] 
**applied_by_service_token_id** | **str** | The service token ID of the service token which applied the approval request | [optional] 
**status** | **str** | Current status of the approval request | 
**instructions** | **List[Dict[str, object]]** |  | 
**conflicts** | [**List[Conflict]**](Conflict.md) | Details on any conflicting approval requests | 
**links** | **Dict[str, object]** | The location and content type of related resources | 
**execution_date** | **int** |  | [optional] 
**operating_on_id** | **str** | ID of scheduled change to edit or delete | [optional] 
**integration_metadata** | [**IntegrationMetadata**](IntegrationMetadata.md) |  | [optional] 
**source** | [**CopiedFromEnv**](CopiedFromEnv.md) |  | [optional] 
**custom_workflow_metadata** | [**CustomWorkflowMeta**](CustomWorkflowMeta.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.flag_config_approval_request_response import FlagConfigApprovalRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlagConfigApprovalRequestResponse from a JSON string
flag_config_approval_request_response_instance = FlagConfigApprovalRequestResponse.from_json(json)
# print the JSON string representation of the object
print(FlagConfigApprovalRequestResponse.to_json())

# convert the object into a dict
flag_config_approval_request_response_dict = flag_config_approval_request_response_instance.to_dict()
# create an instance of FlagConfigApprovalRequestResponse from a dict
flag_config_approval_request_response_from_dict = FlagConfigApprovalRequestResponse.from_dict(flag_config_approval_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


