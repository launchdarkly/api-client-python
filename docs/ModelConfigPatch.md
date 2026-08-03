# ModelConfigPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Immutable provider model identifier. To use a different model identifier, create a new model config. | [optional] 
**provider** | **str** | Immutable model provider. To use a different provider, create a new model config. | [optional] 
**name** | **str** | Human-readable name of the model | [optional] 
**cost_per_input_token** | **float** | Cost per input token in USD | [optional] 
**cost_per_output_token** | **float** | Cost per output token in USD | [optional] 
**cost_per_cached_input_token** | **float** | Cost per cached input token in USD | [optional] 
**params** | **object** |  | [optional] 
**custom_params** | **object** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**maintainer_id** | **str** |  | [optional] 
**maintainer_team_key** | **str** |  | [optional] 

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


