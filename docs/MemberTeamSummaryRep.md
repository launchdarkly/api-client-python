# MemberTeamSummaryRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_role_keys** | **List[str]** | A list of keys of the custom roles this team has access to | 
**key** | **str** | The team key | 
**links** | [**Dict[str, Link]**](Link.md) |  | [optional] 
**name** | **str** | The team name | 

## Example

```python
from launchdarkly_api.models.member_team_summary_rep import MemberTeamSummaryRep

# TODO update the JSON string below
json = "{}"
# create an instance of MemberTeamSummaryRep from a JSON string
member_team_summary_rep_instance = MemberTeamSummaryRep.from_json(json)
# print the JSON string representation of the object
print(MemberTeamSummaryRep.to_json())

# convert the object into a dict
member_team_summary_rep_dict = member_team_summary_rep_instance.to_dict()
# create an instance of MemberTeamSummaryRep from a dict
member_team_summary_rep_from_dict = MemberTeamSummaryRep.from_dict(member_team_summary_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


