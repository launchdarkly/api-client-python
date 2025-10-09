# ApplicationCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**items** | [**List[ApplicationRep]**](ApplicationRep.md) | A list of applications | [optional] 
**total_count** | **int** | The number of applications | [optional] 

## Example

```python
from launchdarkly_api.models.application_collection_rep import ApplicationCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCollectionRep from a JSON string
application_collection_rep_instance = ApplicationCollectionRep.from_json(json)
# print the JSON string representation of the object
print(ApplicationCollectionRep.to_json())

# convert the object into a dict
application_collection_rep_dict = application_collection_rep_instance.to_dict()
# create an instance of ApplicationCollectionRep from a dict
application_collection_rep_from_dict = ApplicationCollectionRep.from_dict(application_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


