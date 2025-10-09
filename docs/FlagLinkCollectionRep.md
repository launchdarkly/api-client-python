# FlagLinkCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FlagLinkRep]**](FlagLinkRep.md) | An array of flag links | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.flag_link_collection_rep import FlagLinkCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagLinkCollectionRep from a JSON string
flag_link_collection_rep_instance = FlagLinkCollectionRep.from_json(json)
# print the JSON string representation of the object
print(FlagLinkCollectionRep.to_json())

# convert the object into a dict
flag_link_collection_rep_dict = flag_link_collection_rep_instance.to_dict()
# create an instance of FlagLinkCollectionRep from a dict
flag_link_collection_rep_from_dict = FlagLinkCollectionRep.from_dict(flag_link_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


