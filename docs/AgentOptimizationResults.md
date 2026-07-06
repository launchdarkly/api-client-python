# AgentOptimizationResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedLinks**](PaginatedLinks.md) |  | [optional] 
**items** | [**List[AgentOptimizationResult]**](AgentOptimizationResult.md) |  | 
**total_count** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.agent_optimization_results import AgentOptimizationResults

# TODO update the JSON string below
json = "{}"
# create an instance of AgentOptimizationResults from a JSON string
agent_optimization_results_instance = AgentOptimizationResults.from_json(json)
# print the JSON string representation of the object
print(AgentOptimizationResults.to_json())

# convert the object into a dict
agent_optimization_results_dict = agent_optimization_results_instance.to_dict()
# create an instance of AgentOptimizationResults from a dict
agent_optimization_results_from_dict = AgentOptimizationResults.from_dict(agent_optimization_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


