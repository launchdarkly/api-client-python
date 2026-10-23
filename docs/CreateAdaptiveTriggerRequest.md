# CreateAdaptiveTriggerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**resource_kind** | [**AdaptiveTriggerResourceKind**](AdaptiveTriggerResourceKind.md) |  | 
**resource_key** | **str** |  | 
**trigger_source** | [**ObservabilityAlertSource**](ObservabilityAlertSource.md) |  | 
**task** | [**AdaptiveTriggerTask**](AdaptiveTriggerTask.md) |  | 

## Example

```python
from launchdarkly_api.models.create_adaptive_trigger_request import CreateAdaptiveTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdaptiveTriggerRequest from a JSON string
create_adaptive_trigger_request_instance = CreateAdaptiveTriggerRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdaptiveTriggerRequest.to_json())

# convert the object into a dict
create_adaptive_trigger_request_dict = create_adaptive_trigger_request_instance.to_dict()
# create an instance of CreateAdaptiveTriggerRequest from a dict
create_adaptive_trigger_request_from_dict = CreateAdaptiveTriggerRequest.from_dict(create_adaptive_trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


