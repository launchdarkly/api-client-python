# FlagConfigApprovalRequestResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **int** |  | 
**creation_date** | **int** |  | 
**service_kind** | **str** |  | 
**review_status** | **str** |  | 
**all_reviews** | [**[ReviewResponse]**](ReviewResponse.md) |  | 
**notify_member_ids** | **[str]** | An array of member IDs. These members are notified to review the approval request. | 
**status** | **str** |  | 
**instructions** | [**Instructions**](Instructions.md) |  | 
**conflicts** | [**[Conflict]**](Conflict.md) |  | 
**links** | [**{str: (Link,)}**](Link.md) |  | 
**requestor_id** | **str** |  | [optional] 
**description** | **str** | A human-friendly name for the approval request | [optional] 
**applied_date** | **int** |  | [optional] 
**applied_by_member_id** | **str** |  | [optional] 
**execution_date** | **int** |  | [optional] 
**operating_on_id** | **str** | ID of scheduled change to edit or delete | [optional] 
**integration_metadata** | [**IntegrationMetadata**](IntegrationMetadata.md) |  | [optional] 
**source** | [**CopiedFromEnv**](CopiedFromEnv.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


