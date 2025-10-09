# StageInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The stage name | [optional] 
**execute_conditions_in_sequence** | **bool** | Whether to execute the conditions in sequence for the given stage | [optional] 
**conditions** | [**List[ConditionInput]**](ConditionInput.md) | An array of conditions for the stage | [optional] 
**action** | [**ActionInput**](ActionInput.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.stage_input import StageInput

# TODO update the JSON string below
json = "{}"
# create an instance of StageInput from a JSON string
stage_input_instance = StageInput.from_json(json)
# print the JSON string representation of the object
print(StageInput.to_json())

# convert the object into a dict
stage_input_dict = stage_input_instance.to_dict()
# create an instance of StageInput from a dict
stage_input_from_dict = StageInput.from_dict(stage_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


