# FlagReferenceRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_key** | **str** | The project key | 
**flag_key** | **str** | The flag key | 
**references_added** | **int** | The number of references added | 
**references_removed** | **int** | The number of references removed | 

## Example

```python
from launchdarkly_api.models.flag_reference_rep import FlagReferenceRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagReferenceRep from a JSON string
flag_reference_rep_instance = FlagReferenceRep.from_json(json)
# print the JSON string representation of the object
print(FlagReferenceRep.to_json())

# convert the object into a dict
flag_reference_rep_dict = flag_reference_rep_instance.to_dict()
# create an instance of FlagReferenceRep from a dict
flag_reference_rep_from_dict = FlagReferenceRep.from_dict(flag_reference_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


