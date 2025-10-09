# LayerPatchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment describing the update | [optional] 
**environment_key** | **str** | The environment key used for making environment specific updates. For example, updating the reservation of an experiment | [optional] 
**instructions** | **List[Dict[str, object]]** |  | 

## Example

```python
from launchdarkly_api.models.layer_patch_input import LayerPatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of LayerPatchInput from a JSON string
layer_patch_input_instance = LayerPatchInput.from_json(json)
# print the JSON string representation of the object
print(LayerPatchInput.to_json())

# convert the object into a dict
layer_patch_input_dict = layer_patch_input_instance.to_dict()
# create an instance of LayerPatchInput from a dict
layer_patch_input_from_dict = LayerPatchInput.from_dict(layer_patch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


