# FlagEventRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The flag event ID | 
**project_id** | **str** | The project ID | 
**project_key** | **str** | The project key | 
**environment_id** | **str** | The environment ID | [optional] 
**environment_key** | **str** | The environment key | [optional] 
**flag_key** | **str** | The flag key | 
**event_type** | **str** |  | 
**event_time** | **int** |  | 
**description** | **str** | The event description | 
**audit_log_entry_id** | **str** | The audit log entry ID | [optional] 
**member** | [**FlagEventMemberRep**](FlagEventMemberRep.md) |  | [optional] 
**actions** | **List[str]** | The resource actions | [optional] 
**impact** | [**FlagEventImpactRep**](FlagEventImpactRep.md) |  | 
**experiments** | [**FlagEventExperimentCollection**](FlagEventExperimentCollection.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.flag_event_rep import FlagEventRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagEventRep from a JSON string
flag_event_rep_instance = FlagEventRep.from_json(json)
# print the JSON string representation of the object
print(FlagEventRep.to_json())

# convert the object into a dict
flag_event_rep_dict = flag_event_rep_instance.to_dict()
# create an instance of FlagEventRep from a dict
flag_event_rep_from_dict = FlagEventRep.from_dict(flag_event_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


