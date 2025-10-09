# ModelConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**AiConfigsAccess**](AiConfigsAccess.md) |  | [optional] 
**name** | **str** | Human readable name of the model | 
**key** | **str** | Unique key for the model | 
**id** | **str** | Identifier for the model, for use with third party providers | 
**icon** | **str** | Icon for the model | [optional] 
**provider** | **str** | Provider for the model | [optional] 
**var_global** | **bool** | Whether the model is global | 
**params** | **object** |  | [optional] 
**custom_params** | **object** |  | [optional] 
**tags** | **List[str]** |  | 
**version** | **int** |  | 
**cost_per_input_token** | **float** | Cost per input token in USD | [optional] 
**cost_per_output_token** | **float** | Cost per output token in USD | [optional] 
**is_restricted** | **bool** | Whether the model is restricted | 

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


