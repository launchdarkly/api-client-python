# LayerRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the layer | 
**name** | **str** | The name of the layer | 
**description** | **str** | The description of the layer | 
**created_at** | **int** |  | 
**randomization_unit** | **str** | The unit of randomization for the layer | [optional] 
**environments** | [**Dict[str, LayerConfigurationRep]**](LayerConfigurationRep.md) | The layer configurations for each requested environment | [optional] 

## Example

```python
from launchdarkly_api.models.layer_rep import LayerRep

# TODO update the JSON string below
json = "{}"
# create an instance of LayerRep from a JSON string
layer_rep_instance = LayerRep.from_json(json)
# print the JSON string representation of the object
print(LayerRep.to_json())

# convert the object into a dict
layer_rep_dict = layer_rep_instance.to_dict()
# create an instance of LayerRep from a dict
layer_rep_from_dict = LayerRep.from_dict(layer_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


