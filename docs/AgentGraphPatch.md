# AgentGraphPatch

Request body for updating an agent graph. If rootConfigKey or edges are present, both must be present.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-readable name for the agent graph | [optional] 
**description** | **str** | A description of the agent graph | [optional] 
**root_config_key** | **str** | The AI Config key of the root node. If present, edges must also be present. | [optional] 
**edges** | [**List[AgentGraphEdge]**](AgentGraphEdge.md) | The edges in the graph. If present, rootConfigKey must also be present. Replaces all existing edges. | [optional] 

## Example

```python
from launchdarkly_api.models.agent_graph_patch import AgentGraphPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGraphPatch from a JSON string
agent_graph_patch_instance = AgentGraphPatch.from_json(json)
# print the JSON string representation of the object
print(AgentGraphPatch.to_json())

# convert the object into a dict
agent_graph_patch_dict = agent_graph_patch_instance.to_dict()
# create an instance of AgentGraphPatch from a dict
agent_graph_patch_from_dict = AgentGraphPatch.from_dict(agent_graph_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


