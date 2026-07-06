# AgentOptimizationResultPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**AgentOptimizationResultStatus**](AgentOptimizationResultStatus.md) |  | [optional] 
**activity** | [**AgentOptimizationResultActivity**](AgentOptimizationResultActivity.md) |  | [optional] 
**completion_response** | **str** |  | [optional] 
**variation** | **Dict[str, object]** |  | [optional] 
**scores** | **Dict[str, object]** |  | [optional] 
**generation_tokens** | **Dict[str, object]** |  | [optional] 
**evaluation_tokens** | **Dict[str, object]** |  | [optional] 
**generation_latency** | **int** |  | [optional] 
**evaluation_latencies** | **Dict[str, object]** |  | [optional] 
**created_variation_key** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.agent_optimization_result_patch import AgentOptimizationResultPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AgentOptimizationResultPatch from a JSON string
agent_optimization_result_patch_instance = AgentOptimizationResultPatch.from_json(json)
# print the JSON string representation of the object
print(AgentOptimizationResultPatch.to_json())

# convert the object into a dict
agent_optimization_result_patch_dict = agent_optimization_result_patch_instance.to_dict()
# create an instance of AgentOptimizationResultPatch from a dict
agent_optimization_result_patch_from_dict = AgentOptimizationResultPatch.from_dict(agent_optimization_result_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


