# AgentOptimizationPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_attempts** | **int** |  | [optional] 
**model_choices** | **List[str]** |  | [optional] 
**judge_model** | **str** |  | [optional] 
**variable_choices** | **List[Dict[str, object]]** |  | [optional] 
**acceptance_statements** | [**List[AgentOptimizationAcceptanceStatement]**](AgentOptimizationAcceptanceStatement.md) |  | [optional] 
**judges** | [**List[AgentOptimizationJudge]**](AgentOptimizationJudge.md) |  | [optional] 
**user_input_options** | **List[str]** |  | [optional] 
**ground_truth_responses** | **List[str]** |  | [optional] 
**metric_key** | **str** |  | [optional] 
**token_limit** | **int** |  | [optional] 
**variation_key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**latency_optimization** | **bool** |  | [optional] 
**token_optimization** | **bool** |  | [optional] 
**auto_commit** | **bool** |  | [optional] 

## Example

```python
from launchdarkly_api.models.agent_optimization_patch import AgentOptimizationPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AgentOptimizationPatch from a JSON string
agent_optimization_patch_instance = AgentOptimizationPatch.from_json(json)
# print the JSON string representation of the object
print(AgentOptimizationPatch.to_json())

# convert the object into a dict
agent_optimization_patch_dict = agent_optimization_patch_instance.to_dict()
# create an instance of AgentOptimizationPatch from a dict
agent_optimization_patch_from_dict = AgentOptimizationPatch.from_dict(agent_optimization_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


