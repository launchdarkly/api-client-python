# AIConfigTargetingVariation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**description** | **str** |  | 
**name** | **str** |  | 
**value** | [**AIConfigTargetingVariationValue**](AIConfigTargetingVariationValue.md) |  | 

## Example

```python
from launchdarkly_api.models.ai_config_targeting_variation import AIConfigTargetingVariation

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigTargetingVariation from a JSON string
ai_config_targeting_variation_instance = AIConfigTargetingVariation.from_json(json)
# print the JSON string representation of the object
print(AIConfigTargetingVariation.to_json())

# convert the object into a dict
ai_config_targeting_variation_dict = ai_config_targeting_variation_instance.to_dict()
# create an instance of AIConfigTargetingVariation from a dict
ai_config_targeting_variation_from_dict = AIConfigTargetingVariation.from_dict(ai_config_targeting_variation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


