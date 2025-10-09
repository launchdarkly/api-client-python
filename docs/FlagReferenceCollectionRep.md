# FlagReferenceCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of flag references | 
**items** | [**List[FlagReferenceRep]**](FlagReferenceRep.md) | A list of flag references | 

## Example

```python
from launchdarkly_api.models.flag_reference_collection_rep import FlagReferenceCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagReferenceCollectionRep from a JSON string
flag_reference_collection_rep_instance = FlagReferenceCollectionRep.from_json(json)
# print the JSON string representation of the object
print(FlagReferenceCollectionRep.to_json())

# convert the object into a dict
flag_reference_collection_rep_dict = flag_reference_collection_rep_instance.to_dict()
# create an instance of FlagReferenceCollectionRep from a dict
flag_reference_collection_rep_from_dict = FlagReferenceCollectionRep.from_dict(flag_reference_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


