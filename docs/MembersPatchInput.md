# MembersPatchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment describing the update | [optional] 
**instructions** | **List[Dict[str, object]]** |  | 

## Example

```python
from launchdarkly_api.models.members_patch_input import MembersPatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of MembersPatchInput from a JSON string
members_patch_input_instance = MembersPatchInput.from_json(json)
# print the JSON string representation of the object
print(MembersPatchInput.to_json())

# convert the object into a dict
members_patch_input_dict = members_patch_input_instance.to_dict()
# create an instance of MembersPatchInput from a dict
members_patch_input_from_dict = MembersPatchInput.from_dict(members_patch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


