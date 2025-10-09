# ContextKindsCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ContextKindRep]**](ContextKindRep.md) | An array of context kinds | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.context_kinds_collection_rep import ContextKindsCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of ContextKindsCollectionRep from a JSON string
context_kinds_collection_rep_instance = ContextKindsCollectionRep.from_json(json)
# print the JSON string representation of the object
print(ContextKindsCollectionRep.to_json())

# convert the object into a dict
context_kinds_collection_rep_dict = context_kinds_collection_rep_instance.to_dict()
# create an instance of ContextKindsCollectionRep from a dict
context_kinds_collection_rep_from_dict = ContextKindsCollectionRep.from_dict(context_kinds_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


