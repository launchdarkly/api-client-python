# BranchCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**items** | [**List[BranchRep]**](BranchRep.md) | An array of branches | 

## Example

```python
from launchdarkly_api.models.branch_collection_rep import BranchCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of BranchCollectionRep from a JSON string
branch_collection_rep_instance = BranchCollectionRep.from_json(json)
# print the JSON string representation of the object
print(BranchCollectionRep.to_json())

# convert the object into a dict
branch_collection_rep_dict = branch_collection_rep_instance.to_dict()
# create an instance of BranchCollectionRep from a dict
branch_collection_rep_from_dict = BranchCollectionRep.from_dict(branch_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


