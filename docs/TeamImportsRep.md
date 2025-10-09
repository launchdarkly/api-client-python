# TeamImportsRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MemberImportItem]**](MemberImportItem.md) | An array of details about the members requested to be added to this team | [optional] 

## Example

```python
from launchdarkly_api.models.team_imports_rep import TeamImportsRep

# TODO update the JSON string below
json = "{}"
# create an instance of TeamImportsRep from a JSON string
team_imports_rep_instance = TeamImportsRep.from_json(json)
# print the JSON string representation of the object
print(TeamImportsRep.to_json())

# convert the object into a dict
team_imports_rep_dict = team_imports_rep_instance.to_dict()
# create an instance of TeamImportsRep from a dict
team_imports_rep_from_dict = TeamImportsRep.from_dict(team_imports_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


