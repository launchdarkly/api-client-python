# AIConfigVariationPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Human-readable description of this variation | [optional] 
**description** | **str** | Returns the description for the agent. This is only returned for agent variations. | [optional] 
**instructions** | **str** | Returns the instructions for the agent. This is only returned for agent variations. | [optional] 
**key** | **str** |  | 
**messages** | [**List[Message]**](Message.md) |  | 
**model** | **object** |  | [optional] 
**name** | **str** |  | 
**model_config_key** | **str** |  | [optional] 
**tools** | [**List[VariationToolPost]**](VariationToolPost.md) | List of tools to use for this variation. The latest version of the tool will be used. | [optional] 
**tool_keys** | **List[str]** | List of tool keys to use for this variation. The latest version of the tool will be used. | [optional] 
**judge_configuration** | [**JudgeConfiguration**](JudgeConfiguration.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.ai_config_variation_post import AIConfigVariationPost

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigVariationPost from a JSON string
ai_config_variation_post_instance = AIConfigVariationPost.from_json(json)
# print the JSON string representation of the object
print(AIConfigVariationPost.to_json())

# convert the object into a dict
ai_config_variation_post_dict = ai_config_variation_post_instance.to_dict()
# create an instance of AIConfigVariationPost from a dict
ai_config_variation_post_from_dict = AIConfigVariationPost.from_dict(ai_config_variation_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


