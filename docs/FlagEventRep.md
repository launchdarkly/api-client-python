# FlagEventRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The flag event ID | 
**project_id** | **str** | The project ID | 
**project_key** | **str** | The project key | 
**flag_key** | **str** | The flag key | 
**event_type** | **str** |  | 
**event_time** | **int** |  | 
**description** | **str** | The event description | 
**impact** | [**FlagEventImpactRep**](FlagEventImpactRep.md) |  | 
**environment_id** | **str** | The environment ID | [optional] 
**environment_key** | **str** | The environment key | [optional] 
**audit_log_entry_id** | **str** | The audit log entry ID | [optional] 
**member** | [**FlagEventMemberRep**](FlagEventMemberRep.md) |  | [optional] 
**actions** | **[str]** | The resource actions | [optional] 
**experiments** | [**FlagEventExperimentCollection**](FlagEventExperimentCollection.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


