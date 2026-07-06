# AgentOptimizationAcceptanceStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement** | **str** |  | 
**threshold** | **float** |  | 

## Example

```python
from launchdarkly_api.models.agent_optimization_acceptance_statement import AgentOptimizationAcceptanceStatement

# TODO update the JSON string below
json = "{}"
# create an instance of AgentOptimizationAcceptanceStatement from a JSON string
agent_optimization_acceptance_statement_instance = AgentOptimizationAcceptanceStatement.from_json(json)
# print the JSON string representation of the object
print(AgentOptimizationAcceptanceStatement.to_json())

# convert the object into a dict
agent_optimization_acceptance_statement_dict = agent_optimization_acceptance_statement_instance.to_dict()
# create an instance of AgentOptimizationAcceptanceStatement from a dict
agent_optimization_acceptance_statement_from_dict = AgentOptimizationAcceptanceStatement.from_dict(agent_optimization_acceptance_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


