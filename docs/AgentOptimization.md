# AgentOptimization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**AiConfigsAccess**](AiConfigsAccess.md) |  | [optional] 
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 
**id** | **str** |  | 
**key** | **str** |  | 
**ai_config_key** | **str** |  | 
**max_attempts** | **int** |  | 
**model_choices** | **List[str]** |  | 
**judge_model** | **str** |  | 
**variable_choices** | **List[Dict[str, object]]** |  | 
**acceptance_statements** | [**List[AgentOptimizationAcceptanceStatement]**](AgentOptimizationAcceptanceStatement.md) |  | 
**judges** | [**List[AgentOptimizationJudge]**](AgentOptimizationJudge.md) |  | 
**user_input_options** | **List[str]** |  | 
**ground_truth_responses** | **List[str]** |  | 
**metric_key** | **str** |  | [optional] 
**token_limit** | **int** |  | [optional] 
**variation_key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**latency_optimization** | **bool** |  | [optional] 
**token_optimization** | **bool** |  | [optional] 
**auto_commit** | **bool** |  | [optional] 
**version** | **int** |  | 
**created_at** | **int** |  | 

## Example

```python
from launchdarkly_api.models.agent_optimization import AgentOptimization

# TODO update the JSON string below
json = "{}"
# create an instance of AgentOptimization from a JSON string
agent_optimization_instance = AgentOptimization.from_json(json)
# print the JSON string representation of the object
print(AgentOptimization.to_json())

# convert the object into a dict
agent_optimization_dict = agent_optimization_instance.to_dict()
# create an instance of AgentOptimization from a dict
agent_optimization_from_dict = AgentOptimization.from_dict(agent_optimization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


