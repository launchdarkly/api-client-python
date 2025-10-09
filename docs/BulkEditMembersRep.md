# BulkEditMembersRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | **List[str]** | A list of members IDs of the members who were successfully updated. | [optional] 
**errors** | **List[Dict[str, str]]** | A list of member IDs and errors for the members whose updates failed. | [optional] 

## Example

```python
from launchdarkly_api.models.bulk_edit_members_rep import BulkEditMembersRep

# TODO update the JSON string below
json = "{}"
# create an instance of BulkEditMembersRep from a JSON string
bulk_edit_members_rep_instance = BulkEditMembersRep.from_json(json)
# print the JSON string representation of the object
print(BulkEditMembersRep.to_json())

# convert the object into a dict
bulk_edit_members_rep_dict = bulk_edit_members_rep_instance.to_dict()
# create an instance of BulkEditMembersRep from a dict
bulk_edit_members_rep_from_dict = BulkEditMembersRep.from_dict(bulk_edit_members_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


