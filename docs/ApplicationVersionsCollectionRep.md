# ApplicationVersionsCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**items** | [**List[ApplicationVersionRep]**](ApplicationVersionRep.md) | A list of the versions for this application | [optional] 
**total_count** | **int** | The number of versions for this application | [optional] 

## Example

```python
from launchdarkly_api.models.application_versions_collection_rep import ApplicationVersionsCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationVersionsCollectionRep from a JSON string
application_versions_collection_rep_instance = ApplicationVersionsCollectionRep.from_json(json)
# print the JSON string representation of the object
print(ApplicationVersionsCollectionRep.to_json())

# convert the object into a dict
application_versions_collection_rep_dict = application_versions_collection_rep_instance.to_dict()
# create an instance of ApplicationVersionsCollectionRep from a dict
application_versions_collection_rep_from_dict = ApplicationVersionsCollectionRep.from_dict(application_versions_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


