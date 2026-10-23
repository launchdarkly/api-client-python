# AIConfigVariation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ParentLink**](ParentLink.md) |  | [optional] 
**color** | **str** | The color used for this variation in the UI | [optional] 
**classifiers** | [**List[Classifier]**](Classifier.md) | Classifier rules for a judge variation. When this array is non-empty, messages must be empty.  | [optional] 
**comment** | **str** | A comment describing this version of the variation | [optional] 
**description** | **str** | Returns the description for the agent. This is only returned for agent variations. | [optional] 
**instructions** | **str** | Returns the instructions for the agent. This is only returned for agent variations. | [optional] 
**key** | **str** | The variation key | 
**id** | **str** | The variation ID | 
**messages** | [**List[Message]**](Message.md) | The prompt messages for this variation | [optional] 
**model** | **object** | Freeform JSON object. LaunchDarkly does not validate the keys. In a model config, &#x60;params&#x60; and &#x60;customParams&#x60; hold parameters that the provider&#39;s API accepts, for example &#x60;{\&quot;temperature\&quot;: 0.7, \&quot;maxTokens\&quot;: 4096}&#x60;. | 
**model_config_key** | **str** | The key of the model config that this variation uses, not the provider model ID. Absent when the variation does not use a model config.  | [optional] 
**model_config_version** | **int** | The version of the model config that this variation is pinned to, when it references a custom model config. Absent when the variation does not reference a model config, when the variation is not pinned to a specific version, or when custom model config versioning is not enabled for the project.  | [optional] 
**name** | **str** | The variation name | 
**output_format** | **Dict[str, object]** | JSON Schema defining the structured output format for the variation. | [optional] 
**created_at** | **int** |  | 
**version** | **int** | The version number of this resource | 
**state** | **str** | The state of the variation. - &#x60;archived&#x60;: The variation is archived. To restore it, update the variation with &#x60;state&#x60; set to &#x60;published&#x60;. - &#x60;published&#x60;: The variation is active.  | [optional] 
**archived_at** | **int** |  | [optional] 
**published_at** | **int** |  | [optional] 
**tools** | [**List[VariationTool]**](VariationTool.md) | The tools this variation can use | [optional] 
**skills** | [**List[VariationSkill]**](VariationSkill.md) | The agent skills this variation can use | [optional] 
**judge_configuration** | [**JudgeConfiguration**](JudgeConfiguration.md) |  | [optional] 
**judging_config_keys** | **List[str]** | Keys of the judge AI Configs attached to this variation | [optional] 

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


