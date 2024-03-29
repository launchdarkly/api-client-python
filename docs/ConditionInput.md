# ConditionInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_kind** | **str** |  | [optional] 
**execution_date** | **int** |  | [optional] 
**wait_duration** | **int** | For workflow stages whose scheduled execution is relative, how far in the future the stage should start. | [optional] 
**wait_duration_unit** | **str** |  | [optional] 
**execute_now** | **bool** | Whether the workflow stage should be executed immediately | [optional] 
**description** | **str** | A description of the approval required for this stage | [optional] 
**notify_member_ids** | **[str]** | A list of member IDs for the members to request approval from for this stage | [optional] 
**notify_team_keys** | **[str]** | A list of team keys for the teams to request approval from for this stage | [optional] 
**kind** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


