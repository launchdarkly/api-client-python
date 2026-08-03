# AgentSkillReferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedLinks**](PaginatedLinks.md) |  | [optional] 
**resource_key** | **str** | The key of the agent skill. | 
**resource_type** | **str** | The type of the resource being referenced. | 
**items** | [**List[AgentSkillReference]**](AgentSkillReference.md) |  | 
**total_count** | **int** | The total number of references. | 

## Example

```python
from launchdarkly_api.models.agent_skill_references import AgentSkillReferences

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSkillReferences from a JSON string
agent_skill_references_instance = AgentSkillReferences.from_json(json)
# print the JSON string representation of the object
print(AgentSkillReferences.to_json())

# convert the object into a dict
agent_skill_references_dict = agent_skill_references_instance.to_dict()
# create an instance of AgentSkillReferences from a dict
agent_skill_references_from_dict = AgentSkillReferences.from_dict(agent_skill_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


