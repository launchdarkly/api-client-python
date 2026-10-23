# AdaptiveTriggers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**AdaptiveTriggersPaginatedLinks**](AdaptiveTriggersPaginatedLinks.md) |  | [optional] 
**items** | [**List[AdaptiveTrigger]**](AdaptiveTrigger.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.adaptive_triggers import AdaptiveTriggers

# TODO update the JSON string below
json = "{}"
# create an instance of AdaptiveTriggers from a JSON string
adaptive_triggers_instance = AdaptiveTriggers.from_json(json)
# print the JSON string representation of the object
print(AdaptiveTriggers.to_json())

# convert the object into a dict
adaptive_triggers_dict = adaptive_triggers_instance.to_dict()
# create an instance of AdaptiveTriggers from a dict
adaptive_triggers_from_dict = AdaptiveTriggers.from_dict(adaptive_triggers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


