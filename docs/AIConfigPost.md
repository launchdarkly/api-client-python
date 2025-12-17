# AIConfigPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] [default to '']
**key** | **str** |  | 
**maintainer_id** | **str** |  | [optional] 
**maintainer_team_key** | **str** |  | [optional] 
**mode** | **str** |  | [optional] [default to 'completion']
**name** | **str** |  | 
**tags** | **List[str]** |  | [optional] 
**default_variation** | [**AIConfigVariationPost**](AIConfigVariationPost.md) |  | [optional] 

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


