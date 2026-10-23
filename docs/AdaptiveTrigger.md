# AdaptiveTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**resource_kind** | [**AdaptiveTriggerResourceKind**](AdaptiveTriggerResourceKind.md) |  | 
**resource_key** | **str** |  | 
**enabled** | **bool** |  | 
**trigger_source** | [**ObservabilityAlertSource**](ObservabilityAlertSource.md) |  | 
**task** | [**AdaptiveTriggerTask**](AdaptiveTriggerTask.md) |  | 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from launchdarkly_api.models.adaptive_trigger import AdaptiveTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of AdaptiveTrigger from a JSON string
adaptive_trigger_instance = AdaptiveTrigger.from_json(json)
# print the JSON string representation of the object
print(AdaptiveTrigger.to_json())

# convert the object into a dict
adaptive_trigger_dict = adaptive_trigger_instance.to_dict()
# create an instance of AdaptiveTrigger from a dict
adaptive_trigger_from_dict = AdaptiveTrigger.from_dict(adaptive_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


