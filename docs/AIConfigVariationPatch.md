# AIConfigVariationPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classifiers** | [**List[Classifier]**](Classifier.md) | Replaces classifier rules on a judge variation. An empty array clears them. When this array is non-empty, messages must be empty.  | [optional] 
**comment** | **str** | Human-readable description of what this patch changes | [optional] 
**description** | **str** | Description for agent when the config is in agent mode. | [optional] 
**instructions** | **str** | Instructions for agent when the config is in agent mode. | [optional] 
**messages** | [**List[Message]**](Message.md) | The prompt messages for this variation | [optional] 
**model** | **object** | Freeform JSON object. LaunchDarkly does not validate the keys. In a model config, &#x60;params&#x60; and &#x60;customParams&#x60; hold parameters that the provider&#39;s API accepts, for example &#x60;{\&quot;temperature\&quot;: 0.7, \&quot;maxTokens\&quot;: 4096}&#x60;. | [optional] 
**model_config_key** | **str** | The key that GET /api/v2/projects/{projectKey}/ai-configs/model-configs returns for the model config. Do not use a custom model config&#39;s ID, which is the provider model ID.  | [optional] 
**model_config_version** | **int** | The exact model config version to set this variation to. Requires modelConfigKey to be set (either in this patch or already on the variation), and the version must exist for that model config. When omitted, the variation keeps the version it is currently set to, unless the patch changes modelConfigKey, in which case the variation records the new model config&#39;s current (latest) version.  | [optional] 
**name** | **str** | A human-readable name for the variation | [optional] 
**output_format** | **Dict[str, object]** | JSON Schema defining the structured output format for the variation. | [optional] 
**published** | **bool** | Whether to publish this version of the variation | [optional] 
**state** | **str** | The state to move the variation to. Omit this field to keep the current state. - &#x60;archived&#x60;: Archive a published variation. You cannot archive a variation that is already archived. You also cannot archive the only variation of an AI Config. An AI Config itself cannot be archived. - &#x60;published&#x60;: Restore an archived variation. You cannot publish a variation that is already published.  | [optional] 
**tools** | [**List[VariationToolPost]**](VariationToolPost.md) | List of tools to use for this variation. The latest version of the tool will be used. | [optional] 
**tool_keys** | **List[str]** | List of tool keys to use for this variation. The latest version of the tool will be used. | [optional] 
**skills** | [**List[VariationSkillPost]**](VariationSkillPost.md) | List of agent skills to attach to this variation. Replaces the current attachments. | [optional] 
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


