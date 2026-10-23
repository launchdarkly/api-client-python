# AgentOptimizationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**AiConfigsAccess**](AiConfigsAccess.md) |  | [optional] 
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 
**id** | **UUID** | The result ID | 
**run_id** | **UUID** | The ID of the run this result belongs to | 
**agent_optimization_id** | **UUID** | The agent optimization ID | 
**agent_optimization_version** | **int** | The version of the agent optimization used | 
**status** | [**AgentOptimizationResultStatus**](AgentOptimizationResultStatus.md) |  | 
**activity** | [**AgentOptimizationResultActivity**](AgentOptimizationResultActivity.md) |  | 
**iteration** | **int** | The iteration number within the run | 
**instructions** | **str** | The instructions used for this attempt | 
**parameters** | **Dict[str, object]** | The model parameters used for this attempt | [optional] 
**user_input** | **str** | The user input used for this attempt | 
**completion_response** | **str** | The model response | [optional] 
**variation** | **Dict[str, object]** | The variation that was tested | [optional] 
**scores** | **Dict[str, object]** | The scores for the response | [optional] 
**generation_tokens** | **Dict[str, object]** | Token usage for generating the response | [optional] 
**evaluation_tokens** | **Dict[str, object]** | Token usage for judging the response | [optional] 
**generation_latency** | **int** | How long the response took to generate | [optional] 
**evaluation_latencies** | **Dict[str, object]** | How long each evaluation took | [optional] 
**completed_at** | **int** | When this finished, in Unix milliseconds | [optional] 
**created_variation_key** | **str** | The key of the variation created from this result | [optional] 
**created_at** | **int** | When this resource was created, in Unix milliseconds | 
**updated_at** | **int** | When this resource was last updated, in Unix milliseconds | 

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


