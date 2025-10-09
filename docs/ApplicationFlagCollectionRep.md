# ApplicationFlagCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FlagListingRep]**](FlagListingRep.md) | A list of the flags that have been evaluated by the application | [optional] 
**total_count** | **int** | The number of flags that have been evaluated by the application | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.application_flag_collection_rep import ApplicationFlagCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFlagCollectionRep from a JSON string
application_flag_collection_rep_instance = ApplicationFlagCollectionRep.from_json(json)
# print the JSON string representation of the object
print(ApplicationFlagCollectionRep.to_json())

# convert the object into a dict
application_flag_collection_rep_dict = application_flag_collection_rep_instance.to_dict()
# create an instance of ApplicationFlagCollectionRep from a dict
application_flag_collection_rep_from_dict = ApplicationFlagCollectionRep.from_dict(application_flag_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


