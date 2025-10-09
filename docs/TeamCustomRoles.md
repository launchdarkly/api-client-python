# TeamCustomRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The number of custom roles assigned to this team | [optional] 
**items** | [**List[TeamCustomRole]**](TeamCustomRole.md) | An array of the custom roles that have been assigned to this team | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.team_custom_roles import TeamCustomRoles

# TODO update the JSON string below
json = "{}"
# create an instance of TeamCustomRoles from a JSON string
team_custom_roles_instance = TeamCustomRoles.from_json(json)
# print the JSON string representation of the object
print(TeamCustomRoles.to_json())

# convert the object into a dict
team_custom_roles_dict = team_custom_roles_instance.to_dict()
# create an instance of TeamCustomRoles from a dict
team_custom_roles_from_dict = TeamCustomRoles.from_dict(team_custom_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


