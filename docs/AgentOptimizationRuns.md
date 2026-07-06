# AgentOptimizationRuns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedLinks**](PaginatedLinks.md) |  | [optional] 
**items** | [**List[AgentOptimizationRun]**](AgentOptimizationRun.md) |  | 
**total_count** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.agent_optimization_runs import AgentOptimizationRuns

# TODO update the JSON string below
json = "{}"
# create an instance of AgentOptimizationRuns from a JSON string
agent_optimization_runs_instance = AgentOptimizationRuns.from_json(json)
# print the JSON string representation of the object
print(AgentOptimizationRuns.to_json())

# convert the object into a dict
agent_optimization_runs_dict = agent_optimization_runs_instance.to_dict()
# create an instance of AgentOptimizationRuns from a dict
agent_optimization_runs_from_dict = AgentOptimizationRuns.from_dict(agent_optimization_runs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


