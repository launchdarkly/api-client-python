# AgentGraphPost

Request body for creating an agent graph

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key for the agent graph | 
**name** | **str** | A human-readable name for the agent graph | 
**description** | **str** | A description of the agent graph | [optional] 
**root_config_key** | **str** | The AI Config key of the root node. A missing root implies a newly created graph with metadata only. | [optional] 
**edges** | [**List[AgentGraphEdgePost]**](AgentGraphEdgePost.md) | The edges in the graph. If edges or rootConfigKey is present, both must be present. | [optional] 

## Example

```python
from launchdarkly_api.models.agent_graph_post import AgentGraphPost

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGraphPost from a JSON string
agent_graph_post_instance = AgentGraphPost.from_json(json)
# print the JSON string representation of the object
print(AgentGraphPost.to_json())

# convert the object into a dict
agent_graph_post_dict = agent_graph_post_instance.to_dict()
# create an instance of AgentGraphPost from a dict
agent_graph_post_from_dict = AgentGraphPost.from_dict(agent_graph_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


