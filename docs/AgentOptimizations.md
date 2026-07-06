# AgentOptimizations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedLinks**](PaginatedLinks.md) |  | [optional] 
**items** | [**List[AgentOptimization]**](AgentOptimization.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.agent_optimizations import AgentOptimizations

# TODO update the JSON string below
json = "{}"
# create an instance of AgentOptimizations from a JSON string
agent_optimizations_instance = AgentOptimizations.from_json(json)
# print the JSON string representation of the object
print(AgentOptimizations.to_json())

# convert the object into a dict
agent_optimizations_dict = agent_optimizations_instance.to_dict()
# create an instance of AgentOptimizations from a dict
agent_optimizations_from_dict = AgentOptimizations.from_dict(agent_optimizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


