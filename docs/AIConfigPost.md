# AIConfigPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the AI Config | [optional] [default to '']
**key** | **str** | A unique key for the AI Config | 
**maintainer_id** | **str** | The ID of the member who maintains this resource | [optional] 
**maintainer_team_key** | **str** | The key of the team that maintains this resource | [optional] 
**mode** | **str** | The AI Config mode | [optional] [default to 'completion']
**name** | **str** | A human-readable name for the AI Config | 
**tags** | **List[str]** | Tags for this resource | [optional] 
**view_keys** | **List[str]** | Keys of the views to add the AI Config to | [optional] 
**default_variation** | [**AIConfigVariationPost**](AIConfigVariationPost.md) |  | [optional] 
**evaluation_metric_key** | **str** | Evaluation metric key for this config | [optional] 
**is_inverted** | **bool** | Whether the evaluation metric is inverted, meaning a lower value is better if set as true | [optional] 

## Example

```python
from launchdarkly_api.models.ai_config_post import AIConfigPost

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigPost from a JSON string
ai_config_post_instance = AIConfigPost.from_json(json)
# print the JSON string representation of the object
print(AIConfigPost.to_json())

# convert the object into a dict
ai_config_post_dict = ai_config_post_instance.to_dict()
# create an instance of AIConfigPost from a dict
ai_config_post_from_dict = AIConfigPost.from_dict(ai_config_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


