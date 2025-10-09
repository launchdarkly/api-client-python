# TeamCustomRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the custom role | [optional] 
**name** | **str** | The name of the custom role | [optional] 
**projects** | [**TeamProjects**](TeamProjects.md) |  | [optional] 
**applied_on** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.team_custom_role import TeamCustomRole

# TODO update the JSON string below
json = "{}"
# create an instance of TeamCustomRole from a JSON string
team_custom_role_instance = TeamCustomRole.from_json(json)
# print the JSON string representation of the object
print(TeamCustomRole.to_json())

# convert the object into a dict
team_custom_role_dict = team_custom_role_instance.to_dict()
# create an instance of TeamCustomRole from a dict
team_custom_role_from_dict = TeamCustomRole.from_dict(team_custom_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


