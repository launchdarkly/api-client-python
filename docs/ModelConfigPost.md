# ModelConfigPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human readable name of the model | 
**key** | **str** | Unique key for the model | 
**id** | **str** | Identifier for the model, for use with third party providers | 
**icon** | **str** | Icon for the model | [optional] 
**provider** | **str** | Provider for the model | [optional] 
**params** | **object** |  | [optional] 
**custom_params** | **object** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**cost_per_input_token** | **float** | Cost per input token in USD | [optional] 
**cost_per_output_token** | **float** | Cost per output token in USD | [optional] 

## Example

```python
from launchdarkly_api.models.model_config_post import ModelConfigPost

# TODO update the JSON string below
json = "{}"
# create an instance of ModelConfigPost from a JSON string
model_config_post_instance = ModelConfigPost.from_json(json)
# print the JSON string representation of the object
print(ModelConfigPost.to_json())

# convert the object into a dict
model_config_post_dict = model_config_post_instance.to_dict()
# create an instance of ModelConfigPost from a dict
model_config_post_from_dict = ModelConfigPost.from_dict(model_config_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


