# AIToolPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key for the tool | 
**maintainer_id** | **str** | The ID of the member who maintains this resource | [optional] 
**maintainer_team_key** | **str** | The key of the team that maintains this resource | [optional] 
**description** | **str** | A description of the tool | [optional] 
**var_schema** | **object** | JSON Schema defining the tool&#39;s parameters for LLM consumption | 
**custom_parameters** | **object** | Custom metadata and configuration for application-level use (not sent to LLM) | [optional] 
**tags** | **List[str]** | Tags for the tool. Tags can be used in custom role policies. | [optional] 

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


