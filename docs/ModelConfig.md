# ModelConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**AiConfigsAccess**](AiConfigsAccess.md) |  | [optional] 
**maintainer** | [**AIConfigMaintainer**](AIConfigMaintainer.md) |  | [optional] 
**name** | **str** | Human-readable name of the model | 
**key** | **str** | Unique key for the model config in the project, in the format &#x60;Provider.model-id&#x60;. Use this value as &#x60;modelConfigKey&#x60; on a config variation. | 
**id** | **str** | Model ID that the provider&#39;s API uses. This is different from &#x60;key&#x60;. Use this value as &#x60;modelName&#x60; on a config variation. | 
**icon** | **str** | Icon for the model | [optional] 
**provider** | **str** | Provider for the model. Matches the provider prefix of &#x60;key&#x60;. | [optional] 
**var_global** | **bool** | Whether the model is in the LaunchDarkly global catalog. Global models are read-only. Model configs that you create are always custom, with &#x60;global&#x60; set to &#x60;false&#x60;. | 
**params** | **object** | Freeform JSON object. LaunchDarkly does not validate the keys. In a model config, &#x60;params&#x60; and &#x60;customParams&#x60; hold parameters that the provider&#39;s API accepts, for example &#x60;{\&quot;temperature\&quot;: 0.7, \&quot;maxTokens\&quot;: 4096}&#x60;. | [optional] 
**custom_params** | **object** | Freeform JSON object. LaunchDarkly does not validate the keys. In a model config, &#x60;params&#x60; and &#x60;customParams&#x60; hold parameters that the provider&#39;s API accepts, for example &#x60;{\&quot;temperature\&quot;: 0.7, \&quot;maxTokens\&quot;: 4096}&#x60;. | [optional] 
**tags** | **List[str]** | Tags for the model config. Tags can be used in custom role policies. | 
**version** | **int** | Version of the model config. Starts at 1, and each update that changes the model config adds a new version. | 
**cost_per_input_token** | **float** | Cost per input token in USD | [optional] 
**cost_per_output_token** | **float** | Cost per output token in USD | [optional] 
**cost_per_cached_input_token** | **float** | Cost per cached input token in USD | [optional] 
**is_restricted** | **bool** | Whether the model is on the project&#39;s restricted list. Config variations cannot select a restricted model. To change this, use the add or remove restricted models endpoints. | 
**used_in_count** | **int** | Number of distinct AgentControl configs that reference this model | [optional] 

## Example

```python
from launchdarkly_api.models.model_config import ModelConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ModelConfig from a JSON string
model_config_instance = ModelConfig.from_json(json)
# print the JSON string representation of the object
print(ModelConfig.to_json())

# convert the object into a dict
model_config_dict = model_config_instance.to_dict()
# create an instance of ModelConfig from a dict
model_config_from_dict = ModelConfig.from_dict(model_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


