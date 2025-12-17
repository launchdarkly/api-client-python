# AgentGraph

An agent graph representing a directed graph of AI Configs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key for the agent graph | 
**name** | **str** | A human-readable name for the agent graph | 
**description** | **str** | A description of the agent graph | [optional] 
**root_config_key** | **str** | The AI Config key of the root node | [optional] 
**edges** | [**List[AgentGraphEdge]**](AgentGraphEdge.md) | The edges in the graph | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from launchdarkly_api.models.agent_graph import AgentGraph

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGraph from a JSON string
agent_graph_instance = AgentGraph.from_json(json)
# print the JSON string representation of the object
print(AgentGraph.to_json())

# convert the object into a dict
agent_graph_dict = agent_graph_instance.to_dict()
# create an instance of AgentGraph from a dict
agent_graph_from_dict = AgentGraph.from_dict(agent_graph_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


