# CreateApprovalRequestRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | String representation of a resource | 
**description** | **str** | A brief description of the changes you&#39;re requesting | 
**instructions** | [**Instructions**](Instructions.md) |  | 
**comment** | **str** | Optional comment describing the approval request | [optional] 
**notify_member_ids** | **[str]** | An array of member IDs. These members are notified to review the approval request. | [optional] 
**notify_team_keys** | **[str]** | An array of team keys. The members of these teams are notified to review the approval request. | [optional] 
**integration_config** | [**FormVariableConfig**](FormVariableConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


