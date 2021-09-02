# CreateFlagConfigApprovalRequestRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A human-friendly name for the approval request | 
**instructions** | [**Instructions**](Instructions.md) |  | 
**notify_member_ids** | **[str]** | An array of member IDs. These members are notified to review the approval request | 
**comment** | **str** | A comment describing the approval request | [optional] 
**execution_date** | **int** |  | [optional] 
**operating_on_id** | **str** | ID of scheduled change to edit or delete | [optional] 
**integration_config** | [**FormVariableConfig**](FormVariableConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


