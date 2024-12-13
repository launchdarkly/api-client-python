# TeamPostInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The team key | 
**name** | **str** | A human-friendly name for the team | 
**custom_role_keys** | **[str]** | List of custom role keys the team will access | [optional] 
**description** | **str** | A description of the team | [optional] 
**member_ids** | **[str]** | A list of member IDs who belong to the team | [optional] 
**permission_grants** | [**[PermissionGrantInput]**](PermissionGrantInput.md) | A list of permission grants. Permission grants allow access to a specific action, without having to create or update a custom role. | [optional] 
**role_attributes** | [**RoleAttributeMap**](RoleAttributeMap.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


