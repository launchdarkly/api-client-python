# AdaptiveTriggerTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instructions** | [**List[AdaptiveTriggerInstruction]**](AdaptiveTriggerInstruction.md) |  | 

## Example

```python
from launchdarkly_api.models.adaptive_trigger_task import AdaptiveTriggerTask

# TODO update the JSON string below
json = "{}"
# create an instance of AdaptiveTriggerTask from a JSON string
adaptive_trigger_task_instance = AdaptiveTriggerTask.from_json(json)
# print the JSON string representation of the object
print(AdaptiveTriggerTask.to_json())

# convert the object into a dict
adaptive_trigger_task_dict = adaptive_trigger_task_instance.to_dict()
# create an instance of AdaptiveTriggerTask from a dict
adaptive_trigger_task_from_dict = AdaptiveTriggerTask.from_dict(adaptive_trigger_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


