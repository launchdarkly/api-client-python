# AIConfigVariationPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Human-readable description of what this patch changes | [optional] 
**description** | **str** | Description for agent when AI Config is in agent mode. | [optional] 
**instructions** | **str** | Instructions for agent when AI Config is in agent mode. | [optional] 
**messages** | [**List[Message]**](Message.md) |  | [optional] 
**model** | **object** |  | [optional] 
**model_config_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**published** | **bool** |  | [optional] 
**state** | **str** | One of &#39;archived&#39;, &#39;published&#39; | [optional] 
**tools** | [**List[VariationToolPost]**](VariationToolPost.md) | List of tools to use for this variation. The latest version of the tool will be used. | [optional] 
**tool_keys** | **List[str]** | List of tool keys to use for this variation. The latest version of the tool will be used. | [optional] 
**judge_configuration** | [**JudgeConfiguration**](JudgeConfiguration.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.ai_config_variation_patch import AIConfigVariationPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigVariationPatch from a JSON string
ai_config_variation_patch_instance = AIConfigVariationPatch.from_json(json)
# print the JSON string representation of the object
print(AIConfigVariationPatch.to_json())

# convert the object into a dict
ai_config_variation_patch_dict = ai_config_variation_patch_instance.to_dict()
# create an instance of AIConfigVariationPatch from a dict
ai_config_variation_patch_from_dict = AIConfigVariationPatch.from_dict(ai_config_variation_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


