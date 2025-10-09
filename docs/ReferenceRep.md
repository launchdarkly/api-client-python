# ReferenceRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | File path of the reference | 
**hint** | **str** | Programming language used in the file | [optional] 
**hunks** | [**List[HunkRep]**](HunkRep.md) |  | 

## Example

```python
from launchdarkly_api.models.reference_rep import ReferenceRep

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceRep from a JSON string
reference_rep_instance = ReferenceRep.from_json(json)
# print the JSON string representation of the object
print(ReferenceRep.to_json())

# convert the object into a dict
reference_rep_dict = reference_rep_instance.to_dict()
# create an instance of ReferenceRep from a dict
reference_rep_from_dict = ReferenceRep.from_dict(reference_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


