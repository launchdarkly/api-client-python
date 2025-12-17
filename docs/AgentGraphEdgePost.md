# AgentGraphEdgePost

An edge in an agent graph connecting two AI Configs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_config** | **str** | The AI Config key that is the source of this edge | 
**target_config** | **str** | The AI Config key that is the target of this edge | 
**handoff** | **object** | The handoff options from the source AI Config to the target AI Config | [optional] 

## Example

```python
from launchdarkly_api.models.agent_graph_edge_post import AgentGraphEdgePost

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGraphEdgePost from a JSON string
agent_graph_edge_post_instance = AgentGraphEdgePost.from_json(json)
# print the JSON string representation of the object
print(AgentGraphEdgePost.to_json())

# convert the object into a dict
agent_graph_edge_post_dict = agent_graph_edge_post_instance.to_dict()
# create an instance of AgentGraphEdgePost from a dict
agent_graph_edge_post_from_dict = AgentGraphEdgePost.from_dict(agent_graph_edge_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


