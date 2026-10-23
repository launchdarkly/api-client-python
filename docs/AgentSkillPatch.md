# AgentSkillPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name of the agent skill. | [optional] 
**description** | **str** | Human-readable description of what the agent skill does. | [optional] 
**markdown** | **str** | The verbatim SKILL.md content of the agent skill | [optional] 
**maintainer_id** | **str** | The ID of the member who maintains this resource | [optional] 
**maintainer_team_key** | **str** | The key of the team that maintains this resource | [optional] 
**tags** | **List[str]** | Replaces the tags on the agent skill. Tags can be used in custom role policies. Changing only the tags does not create a new version. | [optional] 

## Example

```python
from launchdarkly_api.models.agent_skill_patch import AgentSkillPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSkillPatch from a JSON string
agent_skill_patch_instance = AgentSkillPatch.from_json(json)
# print the JSON string representation of the object
print(AgentSkillPatch.to_json())

# convert the object into a dict
agent_skill_patch_dict = agent_skill_patch_instance.to_dict()
# create an instance of AgentSkillPatch from a dict
agent_skill_patch_from_dict = AgentSkillPatch.from_dict(agent_skill_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


