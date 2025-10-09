# Team


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the team | [optional] 
**key** | **str** | The team key | [optional] 
**name** | **str** | A human-friendly name for the team | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**creation_date** | **int** |  | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**last_modified** | **int** |  | [optional] 
**version** | **int** | The team version | [optional] 
**idp_synced** | **bool** | Whether the team has been synced with an external identity provider (IdP). Team sync is available to customers on an Enterprise plan. | [optional] 
**role_attributes** | **Dict[str, List[str]]** |  | [optional] 
**roles** | [**TeamCustomRoles**](TeamCustomRoles.md) |  | [optional] 
**members** | [**TeamMembers**](TeamMembers.md) |  | [optional] 
**projects** | [**TeamProjects**](TeamProjects.md) |  | [optional] 
**maintainers** | [**TeamMaintainers**](TeamMaintainers.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print(Team.to_json())

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_from_dict = Team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


