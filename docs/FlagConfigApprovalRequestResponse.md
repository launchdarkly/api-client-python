# FlagConfigApprovalRequestResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of this approval request | 
**version** | **int** | Version of the approval request | 
**creation_date** | **int** |  | 
**service_kind** | **str** |  | 
**review_status** | **str** | Current status of the review of this approval request | 
**all_reviews** | [**[ReviewResponse]**](ReviewResponse.md) | An array of individual reviews of this approval request | 
**notify_member_ids** | **[str]** | An array of member IDs. These members are notified to review the approval request. | 
**status** | **str** | Current status of the approval request | 
**instructions** | [**Instructions**](Instructions.md) |  | 
**conflicts** | [**[Conflict]**](Conflict.md) | Details on any conflicting approval requests | 
**links** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The location and content type of related resources | 
**requestor_id** | **str** | The ID of the member who requested the approval | [optional] 
**description** | **str** | A human-friendly name for the approval request | [optional] 
**applied_date** | **int** |  | [optional] 
**applied_by_member_id** | **str** | The member ID of the member who applied the approval request | [optional] 
**execution_date** | **int** |  | [optional] 
**operating_on_id** | **str** | ID of scheduled change to edit or delete | [optional] 
**integration_metadata** | [**IntegrationMetadata**](IntegrationMetadata.md) |  | [optional] 
**source** | [**CopiedFromEnv**](CopiedFromEnv.md) |  | [optional] 
**custom_workflow_metadata** | [**CustomWorkflowMeta**](CustomWorkflowMeta.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


