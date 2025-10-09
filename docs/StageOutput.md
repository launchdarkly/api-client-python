# StageOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of this stage | 
**name** | **str** | The stage name | [optional] 
**conditions** | [**List[ConditionOutput]**](ConditionOutput.md) | An array of conditions for the stage | 
**action** | [**ActionOutput**](ActionOutput.md) |  | 
**execution** | [**ExecutionOutput**](ExecutionOutput.md) |  | 

## Example

```python
from launchdarkly_api.models.stage_output import StageOutput

# TODO update the JSON string below
json = "{}"
# create an instance of StageOutput from a JSON string
stage_output_instance = StageOutput.from_json(json)
# print the JSON string representation of the object
print(StageOutput.to_json())

# convert the object into a dict
stage_output_dict = stage_output_instance.to_dict()
# create an instance of StageOutput from a dict
stage_output_from_dict = StageOutput.from_dict(stage_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


