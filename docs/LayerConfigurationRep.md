# LayerConfigurationRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservations** | [**List[LayerReservationRep]**](LayerReservationRep.md) | The experiment reservations for the layer | 

## Example

```python
from launchdarkly_api.models.layer_configuration_rep import LayerConfigurationRep

# TODO update the JSON string below
json = "{}"
# create an instance of LayerConfigurationRep from a JSON string
layer_configuration_rep_instance = LayerConfigurationRep.from_json(json)
# print the JSON string representation of the object
print(LayerConfigurationRep.to_json())

# convert the object into a dict
layer_configuration_rep_dict = layer_configuration_rep_instance.to_dict()
# create an instance of LayerConfigurationRep from a dict
layer_configuration_rep_from_dict = LayerConfigurationRep.from_dict(layer_configuration_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


