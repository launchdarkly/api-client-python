# MutableFieldsByStatusRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_started** | **Dict[str, List[str]]** |  | [optional] 
**running** | **Dict[str, List[str]]** |  | [optional] 
**stopped** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from launchdarkly_api.models.mutable_fields_by_status_rep import MutableFieldsByStatusRep

# TODO update the JSON string below
json = "{}"
# create an instance of MutableFieldsByStatusRep from a JSON string
mutable_fields_by_status_rep_instance = MutableFieldsByStatusRep.from_json(json)
# print the JSON string representation of the object
print(MutableFieldsByStatusRep.to_json())

# convert the object into a dict
mutable_fields_by_status_rep_dict = mutable_fields_by_status_rep_instance.to_dict()
# create an instance of MutableFieldsByStatusRep from a dict
mutable_fields_by_status_rep_from_dict = MutableFieldsByStatusRep.from_dict(mutable_fields_by_status_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


