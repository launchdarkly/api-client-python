# BulkEditTeamsRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_ids** | **List[str]** | A list of member IDs of the members who were added to the teams. | [optional] 
**team_keys** | **List[str]** | A list of team keys of the teams that were successfully updated. | [optional] 
**errors** | **List[Dict[str, str]]** | A list of team keys and errors for the teams whose updates failed. | [optional] 

## Example

```python
from launchdarkly_api.models.bulk_edit_teams_rep import BulkEditTeamsRep

# TODO update the JSON string below
json = "{}"
# create an instance of BulkEditTeamsRep from a JSON string
bulk_edit_teams_rep_instance = BulkEditTeamsRep.from_json(json)
# print the JSON string representation of the object
print(BulkEditTeamsRep.to_json())

# convert the object into a dict
bulk_edit_teams_rep_dict = bulk_edit_teams_rep_instance.to_dict()
# create an instance of BulkEditTeamsRep from a dict
bulk_edit_teams_rep_from_dict = BulkEditTeamsRep.from_dict(bulk_edit_teams_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


