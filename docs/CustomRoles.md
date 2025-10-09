# CustomRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**items** | [**List[CustomRole]**](CustomRole.md) | An array of custom roles | 
**total_count** | **int** | The total number of custom roles | [optional] 

## Example

```python
from launchdarkly_api.models.custom_roles import CustomRoles

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRoles from a JSON string
custom_roles_instance = CustomRoles.from_json(json)
# print the JSON string representation of the object
print(CustomRoles.to_json())

# convert the object into a dict
custom_roles_dict = custom_roles_instance.to_dict()
# create an instance of CustomRoles from a dict
custom_roles_from_dict = CustomRoles.from_dict(custom_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


