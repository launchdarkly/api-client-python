# AgentOptimizationRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **UUID** |  | 
**optimization_key** | **str** |  | 
**agent_optimization_id** | **UUID** |  | 
**agent_optimization_version** | **int** |  | 
**status** | [**AgentOptimizationResultStatus**](AgentOptimizationResultStatus.md) |  | 
**activity** | [**AgentOptimizationResultActivity**](AgentOptimizationResultActivity.md) |  | 
**created_at** | **int** |  | 
**completed_at** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.agent_optimization_run import AgentOptimizationRun

# TODO update the JSON string below
json = "{}"
# create an instance of AgentOptimizationRun from a JSON string
agent_optimization_run_instance = AgentOptimizationRun.from_json(json)
# print the JSON string representation of the object
print(AgentOptimizationRun.to_json())

# convert the object into a dict
agent_optimization_run_dict = agent_optimization_run_instance.to_dict()
# create an instance of AgentOptimizationRun from a dict
agent_optimization_run_from_dict = AgentOptimizationRun.from_dict(agent_optimization_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


