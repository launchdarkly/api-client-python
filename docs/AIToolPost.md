# AIToolPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**maintainer_id** | **str** |  | [optional] 
**maintainer_team_key** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**var_schema** | **object** |  | 

## Example

```python
from launchdarkly_api.models.ai_tool_post import AIToolPost

# TODO update the JSON string below
json = "{}"
# create an instance of AIToolPost from a JSON string
ai_tool_post_instance = AIToolPost.from_json(json)
# print the JSON string representation of the object
print(AIToolPost.to_json())

# convert the object into a dict
ai_tool_post_dict = ai_tool_post_instance.to_dict()
# create an instance of AIToolPost from a dict
ai_tool_post_from_dict = AIToolPost.from_dict(ai_tool_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


