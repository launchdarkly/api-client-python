# RecentTriggerBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** |  | [optional] 
**json_body** | **Dict[str, object]** | The marshalled JSON request body for the incoming trigger webhook. If this is empty or contains invalid JSON, the timestamp is recorded but this field will be empty. | [optional] 

## Example

```python
from launchdarkly_api.models.recent_trigger_body import RecentTriggerBody

# TODO update the JSON string below
json = "{}"
# create an instance of RecentTriggerBody from a JSON string
recent_trigger_body_instance = RecentTriggerBody.from_json(json)
# print the JSON string representation of the object
print(RecentTriggerBody.to_json())

# convert the object into a dict
recent_trigger_body_dict = recent_trigger_body_instance.to_dict()
# create an instance of RecentTriggerBody from a dict
recent_trigger_body_from_dict = RecentTriggerBody.from_dict(recent_trigger_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


