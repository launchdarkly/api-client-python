# AgentGraphs

A collection of agent graphs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedLinks**](PaginatedLinks.md) |  | [optional] 
**items** | [**List[AgentGraph]**](AgentGraph.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.agent_graphs import AgentGraphs

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGraphs from a JSON string
agent_graphs_instance = AgentGraphs.from_json(json)
# print the JSON string representation of the object
print(AgentGraphs.to_json())

# convert the object into a dict
agent_graphs_dict = agent_graphs_instance.to_dict()
# create an instance of AgentGraphs from a dict
agent_graphs_from_dict = AgentGraphs.from_dict(agent_graphs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


