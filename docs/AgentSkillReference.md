# AgentSkillReference

A usage of an agent skill in a specific config variation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_config_key** | **str** | The key of the config with a variation that references this skill. | 
**ai_config_name** | **str** | The name of the config with a variation that references this skill. | 
**variation_id** | **str** | The ID of the variation that references this skill. | 
**variation_key** | **str** | The key of the config variation that references this skill. | 
**variation_name** | **str** | The name of the variation that references this skill. | 
**resource_version** | **int** | The version of the skill being referenced. | 

## Example

```python
from launchdarkly_api.models.agent_skill_reference import AgentSkillReference

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSkillReference from a JSON string
agent_skill_reference_instance = AgentSkillReference.from_json(json)
# print the JSON string representation of the object
print(AgentSkillReference.to_json())

# convert the object into a dict
agent_skill_reference_dict = agent_skill_reference_instance.to_dict()
# create an instance of AgentSkillReference from a dict
agent_skill_reference_from_dict = AgentSkillReference.from_dict(agent_skill_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


