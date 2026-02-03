# AIConfigPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**maintainer_id** | **str** |  | [optional] 
**maintainer_team_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**evaluation_metric_key** | **str** | Evaluation metric key for this AI Config | [optional] 
**is_inverted** | **bool** | Whether the evaluation metric is inverted, meaning a lower value is better if set as true | [optional] 

## Example

```python
from launchdarkly_api.models.ai_config_patch import AIConfigPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigPatch from a JSON string
ai_config_patch_instance = AIConfigPatch.from_json(json)
# print the JSON string representation of the object
print(AIConfigPatch.to_json())

# convert the object into a dict
ai_config_patch_dict = ai_config_patch_instance.to_dict()
# create an instance of AIConfigPatch from a dict
ai_config_patch_from_dict = AIConfigPatch.from_dict(ai_config_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


