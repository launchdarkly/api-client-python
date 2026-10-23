# AdaptiveTriggerInstruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**variation_id** | **UUID** |  | 
**rule_id** | **UUID** | The targeting rule this adaptive trigger acts on. Required for updateRuleVariationOrRollout instructions. | [optional] 

## Example

```python
from launchdarkly_api.models.adaptive_trigger_instruction import AdaptiveTriggerInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of AdaptiveTriggerInstruction from a JSON string
adaptive_trigger_instruction_instance = AdaptiveTriggerInstruction.from_json(json)
# print the JSON string representation of the object
print(AdaptiveTriggerInstruction.to_json())

# convert the object into a dict
adaptive_trigger_instruction_dict = adaptive_trigger_instruction_instance.to_dict()
# create an instance of AdaptiveTriggerInstruction from a dict
adaptive_trigger_instruction_from_dict = AdaptiveTriggerInstruction.from_dict(adaptive_trigger_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


