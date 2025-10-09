# ExtinctionCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**items** | **Dict[str, List[Extinction]]** | An array of extinction events | 

## Example

```python
from launchdarkly_api.models.extinction_collection_rep import ExtinctionCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of ExtinctionCollectionRep from a JSON string
extinction_collection_rep_instance = ExtinctionCollectionRep.from_json(json)
# print the JSON string representation of the object
print(ExtinctionCollectionRep.to_json())

# convert the object into a dict
extinction_collection_rep_dict = extinction_collection_rep_instance.to_dict()
# create an instance of ExtinctionCollectionRep from a dict
extinction_collection_rep_from_dict = ExtinctionCollectionRep.from_dict(extinction_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


