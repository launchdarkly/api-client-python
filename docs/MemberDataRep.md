# MemberDataRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) |  | [optional] 
**id** | **str** | The member ID | [optional] 
**email** | **str** | The member email | [optional] 
**first_name** | **str** | The member first name | [optional] 
**last_name** | **str** | The member last name | [optional] 

## Example

```python
from launchdarkly_api.models.member_data_rep import MemberDataRep

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDataRep from a JSON string
member_data_rep_instance = MemberDataRep.from_json(json)
# print the JSON string representation of the object
print(MemberDataRep.to_json())

# convert the object into a dict
member_data_rep_dict = member_data_rep_instance.to_dict()
# create an instance of MemberDataRep from a dict
member_data_rep_from_dict = MemberDataRep.from_dict(member_data_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


