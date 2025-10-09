# CustomRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the custom role | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**access** | [**Access**](Access.md) |  | [optional] 
**description** | **str** | The description of the custom role | [optional] 
**key** | **str** | The key of the custom role | 
**name** | **str** | The name of the custom role | 
**policy** | [**List[Statement]**](Statement.md) | An array of the policies that comprise this custom role | 
**base_permissions** | **str** |  | [optional] 
**resource_category** | **str** |  | [optional] 
**assigned_to** | [**AssignedToRep**](AssignedToRep.md) |  | [optional] 
**preset_bundle_version** | **int** | If created from a preset, the preset bundle version | [optional] 
**preset_statements** | [**List[Statement]**](Statement.md) | If created from a preset, the read-only statements copied from the preset | [optional] 

## Example

```python
from launchdarkly_api.models.custom_role import CustomRole

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRole from a JSON string
custom_role_instance = CustomRole.from_json(json)
# print the JSON string representation of the object
print(CustomRole.to_json())

# convert the object into a dict
custom_role_dict = custom_role_instance.to_dict()
# create an instance of CustomRole from a dict
custom_role_from_dict = CustomRole.from_dict(custom_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


