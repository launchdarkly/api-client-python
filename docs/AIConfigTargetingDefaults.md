# AIConfigTargetingDefaults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_variation** | **int** |  | 
**off_variation** | **int** |  | 

## Example

```python
from launchdarkly_api.models.ai_config_targeting_defaults import AIConfigTargetingDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigTargetingDefaults from a JSON string
ai_config_targeting_defaults_instance = AIConfigTargetingDefaults.from_json(json)
# print the JSON string representation of the object
print(AIConfigTargetingDefaults.to_json())

# convert the object into a dict
ai_config_targeting_defaults_dict = ai_config_targeting_defaults_instance.to_dict()
# create an instance of AIConfigTargetingDefaults from a dict
ai_config_targeting_defaults_from_dict = AIConfigTargetingDefaults.from_dict(ai_config_targeting_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


