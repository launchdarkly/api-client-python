# AIConfigVariation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ParentLink**](ParentLink.md) |  | [optional] 
**color** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**description** | **str** | Returns the description for the agent. This is only returned for agent variations. | [optional] 
**instructions** | **str** | Returns the instructions for the agent. This is only returned for agent variations. | [optional] 
**key** | **str** |  | 
**id** | **str** |  | 
**messages** | [**List[Message]**](Message.md) |  | [optional] 
**model** | **object** |  | 
**model_config_key** | **str** |  | [optional] 
**name** | **str** |  | 
**created_at** | **int** |  | 
**version** | **int** |  | 
**state** | **str** |  | [optional] 
**archived_at** | **int** |  | [optional] 
**published_at** | **int** |  | [optional] 
**tools** | [**List[VariationTool]**](VariationTool.md) |  | [optional] 
**judge_configuration** | [**JudgeConfiguration**](JudgeConfiguration.md) |  | [optional] 
**judging_config_keys** | **List[str]** |  | [optional] 

## Example

```python
from launchdarkly_api.models.ai_config_variation import AIConfigVariation

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigVariation from a JSON string
ai_config_variation_instance = AIConfigVariation.from_json(json)
# print the JSON string representation of the object
print(AIConfigVariation.to_json())

# convert the object into a dict
ai_config_variation_dict = ai_config_variation_instance.to_dict()
# create an instance of AIConfigVariation from a dict
ai_config_variation_from_dict = AIConfigVariation.from_dict(ai_config_variation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


