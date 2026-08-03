# AgentSkillPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**markdown** | **str** | The verbatim SKILL.md content of the agent skill | 
**maintainer_id** | **str** |  | [optional] 
**maintainer_team_key** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from launchdarkly_api.models.agent_skill_post import AgentSkillPost

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSkillPost from a JSON string
agent_skill_post_instance = AgentSkillPost.from_json(json)
# print the JSON string representation of the object
print(AgentSkillPost.to_json())

# convert the object into a dict
agent_skill_post_dict = agent_skill_post_instance.to_dict()
# create an instance of AgentSkillPost from a dict
agent_skill_post_from_dict = AgentSkillPost.from_dict(agent_skill_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


