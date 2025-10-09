# FlagEventMemberRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The member ID | 
**email** | **str** | The member email | 
**first_name** | **str** | The member first name | 
**last_name** | **str** | The member last name | 

## Example

```python
from launchdarkly_api.models.flag_event_member_rep import FlagEventMemberRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagEventMemberRep from a JSON string
flag_event_member_rep_instance = FlagEventMemberRep.from_json(json)
# print the JSON string representation of the object
print(FlagEventMemberRep.to_json())

# convert the object into a dict
flag_event_member_rep_dict = flag_event_member_rep_instance.to_dict()
# create an instance of FlagEventMemberRep from a dict
flag_event_member_rep_from_dict = FlagEventMemberRep.from_dict(flag_event_member_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


