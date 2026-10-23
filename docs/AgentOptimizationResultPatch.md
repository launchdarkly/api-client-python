# AgentOptimizationResultPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**AgentOptimizationResultStatus**](AgentOptimizationResultStatus.md) |  | [optional] 
**activity** | [**AgentOptimizationResultActivity**](AgentOptimizationResultActivity.md) |  | [optional] 
**completion_response** | **str** | The model response | [optional] 
**variation** | **Dict[str, object]** | The variation that was tested | [optional] 
**scores** | **Dict[str, object]** | The scores for the response | [optional] 
**generation_tokens** | **Dict[str, object]** | Token usage for generating the response | [optional] 
**evaluation_tokens** | **Dict[str, object]** | Token usage for judging the response | [optional] 
**generation_latency** | **int** | How long the response took to generate | [optional] 
**evaluation_latencies** | **Dict[str, object]** | How long each evaluation took | [optional] 
**created_variation_key** | **str** | The key of the variation created from this result | [optional] 

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


