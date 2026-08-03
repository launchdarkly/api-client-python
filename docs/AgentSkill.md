# AgentSkill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**access** | [**AiConfigsAccess**](AiConfigsAccess.md) |  | [optional] 
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 
**maintainer** | [**AIConfigMaintainer**](AIConfigMaintainer.md) |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**markdown** | **str** | The verbatim SKILL.md content of the agent skill | 
**tags** | **List[str]** |  | 
**version** | **int** |  | 
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


