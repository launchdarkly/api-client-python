# ModelConfigPatch

Fields to update. Omitted fields keep their current values. `params`, `customParams`, and `tags` replace the current values. Global model configs cannot be updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Immutable provider model identifier. To use a different model identifier, create a new model config. | [optional] 
**provider** | **str** | Immutable model provider. To use a different provider, create a new model config. | [optional] 
**name** | **str** | Human-readable name of the model | [optional] 
**cost_per_input_token** | **float** | Cost per input token in USD | [optional] 
**cost_per_output_token** | **float** | Cost per output token in USD | [optional] 
**cost_per_cached_input_token** | **float** | Cost per cached input token in USD | [optional] 
**params** | **object** | Freeform JSON object. LaunchDarkly does not validate the keys. In a model config, &#x60;params&#x60; and &#x60;customParams&#x60; hold parameters that the provider&#39;s API accepts, for example &#x60;{\&quot;temperature\&quot;: 0.7, \&quot;maxTokens\&quot;: 4096}&#x60;. | [optional] 
**custom_params** | **object** | Freeform JSON object. LaunchDarkly does not validate the keys. In a model config, &#x60;params&#x60; and &#x60;customParams&#x60; hold parameters that the provider&#39;s API accepts, for example &#x60;{\&quot;temperature\&quot;: 0.7, \&quot;maxTokens\&quot;: 4096}&#x60;. | [optional] 
**tags** | **List[str]** | Tags for the model config. Replaces the current tags. | [optional] 
**maintainer_id** | **str** | The member ID of the new maintainer. Set &#x60;maintainerId&#x60; or &#x60;maintainerTeamKey&#x60;, not both. An empty string removes the maintainer. | [optional] 
**maintainer_team_key** | **str** | The key of the team to set as the new maintainer. Set &#x60;maintainerId&#x60; or &#x60;maintainerTeamKey&#x60;, not both. | [optional] 

## Example

```python
from launchdarkly_api.models.model_config_patch import ModelConfigPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ModelConfigPatch from a JSON string
model_config_patch_instance = ModelConfigPatch.from_json(json)
# print the JSON string representation of the object
print(ModelConfigPatch.to_json())

# convert the object into a dict
model_config_patch_dict = model_config_patch_instance.to_dict()
# create an instance of ModelConfigPatch from a dict
model_config_patch_from_dict = ModelConfigPatch.from_dict(model_config_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


