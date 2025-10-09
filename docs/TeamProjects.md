# TeamProjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**items** | [**List[ProjectSummary]**](ProjectSummary.md) | Details on each project where team members have write privileges on at least one resource type (e.g. flags) | [optional] 

## Example

```python
from launchdarkly_api.models.team_projects import TeamProjects

# TODO update the JSON string below
json = "{}"
# create an instance of TeamProjects from a JSON string
team_projects_instance = TeamProjects.from_json(json)
# print the JSON string representation of the object
print(TeamProjects.to_json())

# convert the object into a dict
team_projects_dict = team_projects_instance.to_dict()
# create an instance of TeamProjects from a dict
team_projects_from_dict = TeamProjects.from_dict(team_projects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


