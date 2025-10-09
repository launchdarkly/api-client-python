# TeamMaintainers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The number of maintainers of the team | [optional] 
**items** | [**List[MemberSummary]**](MemberSummary.md) | Details on the members that have been assigned as maintainers of the team | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.team_maintainers import TeamMaintainers

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMaintainers from a JSON string
team_maintainers_instance = TeamMaintainers.from_json(json)
# print the JSON string representation of the object
print(TeamMaintainers.to_json())

# convert the object into a dict
team_maintainers_dict = team_maintainers_instance.to_dict()
# create an instance of TeamMaintainers from a dict
team_maintainers_from_dict = TeamMaintainers.from_dict(team_maintainers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


