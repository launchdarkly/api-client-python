# FlagLinkMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) |  | 
**id** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.flag_link_member import FlagLinkMember

# TODO update the JSON string below
json = "{}"
# create an instance of FlagLinkMember from a JSON string
flag_link_member_instance = FlagLinkMember.from_json(json)
# print the JSON string representation of the object
print(FlagLinkMember.to_json())

# convert the object into a dict
flag_link_member_dict = flag_link_member_instance.to_dict()
# create an instance of FlagLinkMember from a dict
flag_link_member_from_dict = FlagLinkMember.from_dict(flag_link_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


