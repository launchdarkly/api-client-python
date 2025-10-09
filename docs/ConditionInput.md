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
**notify_member_ids** | **List[str]** | A list of member IDs for the members to request approval from for this stage | [optional] 
**notify_team_keys** | **List[str]** | A list of team keys for the teams to request approval from for this stage | [optional] 
**integration_config** | **Dict[str, object]** |  | [optional] 
**kind** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.condition_input import ConditionInput

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionInput from a JSON string
condition_input_instance = ConditionInput.from_json(json)
# print the JSON string representation of the object
print(ConditionInput.to_json())

# convert the object into a dict
condition_input_dict = condition_input_instance.to_dict()
# create an instance of ConditionInput from a dict
condition_input_from_dict = ConditionInput.from_dict(condition_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


