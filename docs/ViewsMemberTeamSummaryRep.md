# ViewsMemberTeamSummaryRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_role_keys** | **List[str]** | A list of keys of the custom roles this team has access to | 
**key** | **str** | The team key | 
**links** | [**Dict[str, ViewsLink]**](ViewsLink.md) |  | [optional] 
**name** | **str** | The team name | 

## Example

```python
from launchdarkly_api.models.views_member_team_summary_rep import ViewsMemberTeamSummaryRep

# TODO update the JSON string below
json = "{}"
# create an instance of ViewsMemberTeamSummaryRep from a JSON string
views_member_team_summary_rep_instance = ViewsMemberTeamSummaryRep.from_json(json)
# print the JSON string representation of the object
print(ViewsMemberTeamSummaryRep.to_json())

# convert the object into a dict
views_member_team_summary_rep_dict = views_member_team_summary_rep_instance.to_dict()
# create an instance of ViewsMemberTeamSummaryRep from a dict
views_member_team_summary_rep_from_dict = ViewsMemberTeamSummaryRep.from_dict(views_member_team_summary_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


