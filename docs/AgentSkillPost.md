# AgentSkillPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key for the agent skill. The key must match &#x60;^[a-z0-9][a-z0-9-]*$&#x60;: it can only contain lowercase letters, numbers, or &#39;-&#39;, and must start with a lowercase letter or number. The key can be at most 64 characters, and Windows reserved file names (&#x60;con&#x60;, &#x60;prn&#x60;, &#x60;aux&#x60;, &#x60;nul&#x60;, &#x60;com0&#x60;-&#x60;com9&#x60;, and &#x60;lpt0&#x60;-&#x60;lpt9&#x60;) aren&#39;t allowed. | 
**name** | **str** | Human-readable name of the agent skill. | 
**description** | **str** | Human-readable description of what the agent skill does. | [optional] 
**markdown** | **str** | The verbatim SKILL.md content of the agent skill | 
**maintainer_id** | **str** | The ID of the member who maintains this resource | [optional] 
**maintainer_team_key** | **str** | The key of the team that maintains this resource | [optional] 
**tags** | **List[str]** | Tags for the agent skill. Tags can be used in custom role policies. | [optional] 

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


