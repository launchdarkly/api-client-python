# AgentGraphMaintainer

The member or team that maintains this agent graph

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] 
**id** | **str** | The member ID | 
**email** | **str** | The member email address | 
**first_name** | **str** | The member first name | [optional] 
**last_name** | **str** | The member last name | [optional] 
**role** | **str** | The member role | 
**key** | **str** | The team key | 
**name** | **str** | The team name | 

## Example

```python
from launchdarkly_api.models.agent_graph_maintainer import AgentGraphMaintainer

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGraphMaintainer from a JSON string
agent_graph_maintainer_instance = AgentGraphMaintainer.from_json(json)
# print the JSON string representation of the object
print(AgentGraphMaintainer.to_json())

# convert the object into a dict
agent_graph_maintainer_dict = agent_graph_maintainer_instance.to_dict()
# create an instance of AgentGraphMaintainer from a dict
agent_graph_maintainer_from_dict = AgentGraphMaintainer.from_dict(agent_graph_maintainer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


