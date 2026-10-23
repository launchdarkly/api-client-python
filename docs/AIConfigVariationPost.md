# AIConfigVariationPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classifiers** | [**List[Classifier]**](Classifier.md) | Classifier rules for a judge variation. When this array is non-empty, messages must be empty.  | [optional] 
**comment** | **str** | Human-readable description of this variation | [optional] 
**description** | **str** | Returns the description for the agent. This is only returned for agent variations. | [optional] 
**instructions** | **str** | Returns the instructions for the agent. This is only returned for agent variations. | [optional] 
**key** | **str** | A unique key for the variation | 
**messages** | [**List[Message]**](Message.md) | The prompt messages for this variation | [optional] 
**model** | **object** | Freeform JSON object. LaunchDarkly does not validate the keys. In a model config, &#x60;params&#x60; and &#x60;customParams&#x60; hold parameters that the provider&#39;s API accepts, for example &#x60;{\&quot;temperature\&quot;: 0.7, \&quot;maxTokens\&quot;: 4096}&#x60;. | [optional] 
**name** | **str** | A human-readable name for the variation | 
**model_config_key** | **str** | The key that GET /api/v2/projects/{projectKey}/ai-configs/model-configs returns for the model config. Do not use a custom model config&#39;s ID, which is the provider model ID.  | [optional] 
**model_config_version** | **int** | The exact model config version to set this variation to. Requires modelConfigKey to be set, and the version must exist for that model config. When omitted, the variation records the model config&#39;s current (latest) version.  | [optional] 
**output_format** | **Dict[str, object]** | JSON Schema defining the structured output format for the variation. | [optional] 
**tools** | [**List[VariationToolPost]**](VariationToolPost.md) | List of tools to use for this variation. The latest version of the tool will be used. | [optional] 
**tool_keys** | **List[str]** | List of tool keys to use for this variation. The latest version of the tool will be used. | [optional] 
**skills** | [**List[VariationSkillPost]**](VariationSkillPost.md) | List of agent skills to attach to this variation. | [optional] 
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


