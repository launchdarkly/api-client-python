# AgentSkill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The agent skill key | 
**access** | [**AiConfigsAccess**](AiConfigsAccess.md) |  | [optional] 
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 
**maintainer** | [**AIConfigMaintainer**](AIConfigMaintainer.md) |  | [optional] 
**name** | **str** | Human-readable name of the agent skill. | 
**description** | **str** | Human-readable description of what the agent skill does. | [optional] 
**markdown** | **str** | The verbatim SKILL.md content of the agent skill | 
**tags** | **List[str]** | Tags for the agent skill. Tags can be used in custom role policies. | 
**version** | **int** | Version of the agent skill. Starts at 1, and each update that changes the name, description, or markdown creates a new version. Pass this value with &#x60;key&#x60; in a variation&#39;s &#x60;skills: [{key, version}]&#x60;. | 
**created_at** | **int** |  | 

## Example

```python
from launchdarkly_api.models.agent_skill import AgentSkill

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSkill from a JSON string
agent_skill_instance = AgentSkill.from_json(json)
# print the JSON string representation of the object
print(AgentSkill.to_json())

# convert the object into a dict
agent_skill_dict = agent_skill_instance.to_dict()
# create an instance of AgentSkill from a dict
agent_skill_from_dict = AgentSkill.from_dict(agent_skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


