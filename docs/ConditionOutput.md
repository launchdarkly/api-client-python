# ConditionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**kind** | **str** |  | [optional] 
**execution** | [**ExecutionOutput**](ExecutionOutput.md) |  | 
**schedule_kind** | **str** |  | [optional] 
**execution_date** | **int** |  | [optional] 
**wait_duration** | **int** |  | [optional] 
**wait_duration_unit** | **str** |  | [optional] 
**description** | **str** |  | 
**notify_member_ids** | **List[str]** |  | 
**all_reviews** | [**List[ReviewOutput]**](ReviewOutput.md) |  | 
**review_status** | **str** |  | 
**applied_date** | **int** |  | [optional] 
**creation_config** | **Dict[str, object]** |  | [optional] 

## Example

```python
from launchdarkly_api.models.condition_output import ConditionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionOutput from a JSON string
condition_output_instance = ConditionOutput.from_json(json)
# print the JSON string representation of the object
print(ConditionOutput.to_json())

# convert the object into a dict
condition_output_dict = condition_output_instance.to_dict()
# create an instance of ConditionOutput from a dict
condition_output_from_dict = ConditionOutput.from_dict(condition_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


