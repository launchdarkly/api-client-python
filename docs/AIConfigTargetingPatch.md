# AIConfigTargetingPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**environment_key** | **str** |  | 
**instructions** | **List[Dict[str, object]]** |  | 

## Example

```python
from launchdarkly_api.models.ai_config_targeting_patch import AIConfigTargetingPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigTargetingPatch from a JSON string
ai_config_targeting_patch_instance = AIConfigTargetingPatch.from_json(json)
# print the JSON string representation of the object
print(AIConfigTargetingPatch.to_json())

# convert the object into a dict
ai_config_targeting_patch_dict = ai_config_targeting_patch_instance.to_dict()
# create an instance of AIConfigTargetingPatch from a dict
ai_config_targeting_patch_from_dict = AIConfigTargetingPatch.from_dict(ai_config_targeting_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


