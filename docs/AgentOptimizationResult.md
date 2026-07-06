# AgentOptimizationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**AiConfigsAccess**](AiConfigsAccess.md) |  | [optional] 
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 
**id** | **UUID** |  | 
**run_id** | **UUID** |  | 
**agent_optimization_id** | **UUID** |  | 
**agent_optimization_version** | **int** |  | 
**status** | [**AgentOptimizationResultStatus**](AgentOptimizationResultStatus.md) |  | 
**activity** | [**AgentOptimizationResultActivity**](AgentOptimizationResultActivity.md) |  | 
**iteration** | **int** |  | 
**instructions** | **str** |  | 
**parameters** | **Dict[str, object]** |  | [optional] 
**user_input** | **str** |  | 
**completion_response** | **str** |  | [optional] 
**variation** | **Dict[str, object]** |  | [optional] 
**scores** | **Dict[str, object]** |  | [optional] 
**generation_tokens** | **Dict[str, object]** |  | [optional] 
**evaluation_tokens** | **Dict[str, object]** |  | [optional] 
**generation_latency** | **int** |  | [optional] 
**evaluation_latencies** | **Dict[str, object]** |  | [optional] 
**completed_at** | **int** |  | [optional] 
**created_variation_key** | **str** |  | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from launchdarkly_api.models.agent_optimization_result import AgentOptimizationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AgentOptimizationResult from a JSON string
agent_optimization_result_instance = AgentOptimizationResult.from_json(json)
# print the JSON string representation of the object
print(AgentOptimizationResult.to_json())

# convert the object into a dict
agent_optimization_result_dict = agent_optimization_result_instance.to_dict()
# create an instance of AgentOptimizationResult from a dict
agent_optimization_result_from_dict = AgentOptimizationResult.from_dict(agent_optimization_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


