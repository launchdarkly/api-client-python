# AIConfigPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_variation_key** | **str** | Key of the variation this config serves by default | [optional] 
**description** | **str** | A description of the AI Config | [optional] 
**maintainer_id** | **str** | The ID of the member who maintains this resource | [optional] 
**maintainer_team_key** | **str** | The key of the team that maintains this resource | [optional] 
**name** | **str** | A human-readable name for the AI Config | [optional] 
**tags** | **List[str]** | Tags for this resource | [optional] 
**evaluation_metric_key** | **str** | Evaluation metric key for this config | [optional] 
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


