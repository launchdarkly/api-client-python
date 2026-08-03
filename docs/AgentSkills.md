# AgentSkills


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedLinks**](PaginatedLinks.md) |  | [optional] 
**items** | [**List[AgentSkill]**](AgentSkill.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.agent_skills import AgentSkills

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSkills from a JSON string
agent_skills_instance = AgentSkills.from_json(json)
# print the JSON string representation of the object
print(AgentSkills.to_json())

# convert the object into a dict
agent_skills_dict = agent_skills_instance.to_dict()
# create an instance of AgentSkills from a dict
agent_skills_from_dict = AgentSkills.from_dict(agent_skills_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


