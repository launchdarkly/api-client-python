# LayerCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[LayerRep]**](LayerRep.md) | The layers in the project | 
**total_count** | **int** | The total number of layers in the project | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.layer_collection_rep import LayerCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of LayerCollectionRep from a JSON string
layer_collection_rep_instance = LayerCollectionRep.from_json(json)
# print the JSON string representation of the object
print(LayerCollectionRep.to_json())

# convert the object into a dict
layer_collection_rep_dict = layer_collection_rep_instance.to_dict()
# create an instance of LayerCollectionRep from a dict
layer_collection_rep_from_dict = LayerCollectionRep.from_dict(layer_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


