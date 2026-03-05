# AIToolPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maintainer_id** | **str** |  | [optional] 
**maintainer_team_key** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**var_schema** | **object** | JSON Schema defining the tool&#39;s parameters for LLM consumption | [optional] 
**custom_parameters** | **object** | Custom metadata and configuration for application-level use (not sent to LLM) | [optional] 

## Example

```python
from launchdarkly_api.models.ai_tool_patch import AIToolPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AIToolPatch from a JSON string
ai_tool_patch_instance = AIToolPatch.from_json(json)
# print the JSON string representation of the object
print(AIToolPatch.to_json())

# convert the object into a dict
ai_tool_patch_dict = ai_tool_patch_instance.to_dict()
# create an instance of AIToolPatch from a dict
ai_tool_patch_from_dict = AIToolPatch.from_dict(ai_tool_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


