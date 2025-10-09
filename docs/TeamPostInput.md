# TeamPostInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_role_keys** | **List[str]** | List of custom role keys the team will access | [optional] 
**description** | **str** | A description of the team | [optional] 
**key** | **str** | The team key | 
**member_ids** | **List[str]** | A list of member IDs who belong to the team | [optional] 
**name** | **str** | A human-friendly name for the team | 
**permission_grants** | [**List[PermissionGrantInput]**](PermissionGrantInput.md) | A list of permission grants. Permission grants allow access to a specific action, without having to create or update a custom role. | [optional] 
**role_attributes** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from launchdarkly_api.models.team_post_input import TeamPostInput

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPostInput from a JSON string
team_post_input_instance = TeamPostInput.from_json(json)
# print the JSON string representation of the object
print(TeamPostInput.to_json())

# convert the object into a dict
team_post_input_dict = team_post_input_instance.to_dict()
# create an instance of TeamPostInput from a dict
team_post_input_from_dict = TeamPostInput.from_dict(team_post_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


