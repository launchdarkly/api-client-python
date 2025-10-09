# FlagStatusRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Status of the flag | 
**last_requested** | **datetime** | Timestamp of last time flag was requested | [optional] 
**default** | **object** | Default value seen from code | [optional] 
**links** | [**Dict[str, Link]**](Link.md) |  | 

## Example

```python
from launchdarkly_api.models.flag_status_rep import FlagStatusRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagStatusRep from a JSON string
flag_status_rep_instance = FlagStatusRep.from_json(json)
# print the JSON string representation of the object
print(FlagStatusRep.to_json())

# convert the object into a dict
flag_status_rep_dict = flag_status_rep_instance.to_dict()
# create an instance of FlagStatusRep from a dict
flag_status_rep_from_dict = FlagStatusRep.from_dict(flag_status_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


