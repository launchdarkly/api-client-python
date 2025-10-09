# FlagEventCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of flag events | 
**items** | [**List[FlagEventRep]**](FlagEventRep.md) | A list of flag events | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.flag_event_collection_rep import FlagEventCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagEventCollectionRep from a JSON string
flag_event_collection_rep_instance = FlagEventCollectionRep.from_json(json)
# print the JSON string representation of the object
print(FlagEventCollectionRep.to_json())

# convert the object into a dict
flag_event_collection_rep_dict = flag_event_collection_rep_instance.to_dict()
# create an instance of FlagEventCollectionRep from a dict
flag_event_collection_rep_from_dict = FlagEventCollectionRep.from_dict(flag_event_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


