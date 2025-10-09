# RepositoryCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) |  | 
**items** | [**List[RepositoryRep]**](RepositoryRep.md) | An array of repositories | 

## Example

```python
from launchdarkly_api.models.repository_collection_rep import RepositoryCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryCollectionRep from a JSON string
repository_collection_rep_instance = RepositoryCollectionRep.from_json(json)
# print the JSON string representation of the object
print(RepositoryCollectionRep.to_json())

# convert the object into a dict
repository_collection_rep_dict = repository_collection_rep_instance.to_dict()
# create an instance of RepositoryCollectionRep from a dict
repository_collection_rep_from_dict = RepositoryCollectionRep.from_dict(repository_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


