# MemberTeamsPostInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_keys** | **List[str]** | List of team keys | 

## Example

```python
from launchdarkly_api.models.member_teams_post_input import MemberTeamsPostInput

# TODO update the JSON string below
json = "{}"
# create an instance of MemberTeamsPostInput from a JSON string
member_teams_post_input_instance = MemberTeamsPostInput.from_json(json)
# print the JSON string representation of the object
print(MemberTeamsPostInput.to_json())

# convert the object into a dict
member_teams_post_input_dict = member_teams_post_input_instance.to_dict()
# create an instance of MemberTeamsPostInput from a dict
member_teams_post_input_from_dict = MemberTeamsPostInput.from_dict(member_teams_post_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


