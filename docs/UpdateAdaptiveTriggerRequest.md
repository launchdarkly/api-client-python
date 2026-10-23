# UpdateAdaptiveTriggerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**task** | [**AdaptiveTriggerTask**](AdaptiveTriggerTask.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.update_adaptive_trigger_request import UpdateAdaptiveTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdaptiveTriggerRequest from a JSON string
update_adaptive_trigger_request_instance = UpdateAdaptiveTriggerRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdaptiveTriggerRequest.to_json())

# convert the object into a dict
update_adaptive_trigger_request_dict = update_adaptive_trigger_request_instance.to_dict()
# create an instance of UpdateAdaptiveTriggerRequest from a dict
update_adaptive_trigger_request_from_dict = UpdateAdaptiveTriggerRequest.from_dict(update_adaptive_trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


