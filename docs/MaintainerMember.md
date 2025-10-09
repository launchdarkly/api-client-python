# MaintainerMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**role** | **str** |  | 

## Example

```python
from launchdarkly_api.models.maintainer_member import MaintainerMember

# TODO update the JSON string below
json = "{}"
# create an instance of MaintainerMember from a JSON string
maintainer_member_instance = MaintainerMember.from_json(json)
# print the JSON string representation of the object
print(MaintainerMember.to_json())

# convert the object into a dict
maintainer_member_dict = maintainer_member_instance.to_dict()
# create an instance of MaintainerMember from a dict
maintainer_member_from_dict = MaintainerMember.from_dict(maintainer_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


