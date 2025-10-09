# LayerReservationRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_key** | **str** | The key of the experiment | 
**flag_key** | **str** | The key of the flag | 
**reservation_percent** | **int** | The percentage of traffic reserved for the experiment | 

## Example

```python
from launchdarkly_api.models.layer_reservation_rep import LayerReservationRep

# TODO update the JSON string below
json = "{}"
# create an instance of LayerReservationRep from a JSON string
layer_reservation_rep_instance = LayerReservationRep.from_json(json)
# print the JSON string representation of the object
print(LayerReservationRep.to_json())

# convert the object into a dict
layer_reservation_rep_dict = layer_reservation_rep_instance.to_dict()
# create an instance of LayerReservationRep from a dict
layer_reservation_rep_from_dict = LayerReservationRep.from_dict(layer_reservation_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


