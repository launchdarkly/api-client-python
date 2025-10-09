# LayerSnapshotRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of the layer the experiment was part of | 
**name** | **str** | Layer name at the time this experiment iteration was stopped | 
**reservation_percent** | **int** | Percent of layer traffic that was reserved in the layer for this experiment iteration | 
**other_reservation_percent** | **int** | Percent of layer traffic that was reserved for other experiments in the same environment, when this experiment iteration was stopped | 

## Example

```python
from launchdarkly_api.models.layer_snapshot_rep import LayerSnapshotRep

# TODO update the JSON string below
json = "{}"
# create an instance of LayerSnapshotRep from a JSON string
layer_snapshot_rep_instance = LayerSnapshotRep.from_json(json)
# print the JSON string representation of the object
print(LayerSnapshotRep.to_json())

# convert the object into a dict
layer_snapshot_rep_dict = layer_snapshot_rep_instance.to_dict()
# create an instance of LayerSnapshotRep from a dict
layer_snapshot_rep_from_dict = LayerSnapshotRep.from_dict(layer_snapshot_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


