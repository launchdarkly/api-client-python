# AgentOptimizationPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**ai_config_key** | **str** |  | 
**max_attempts** | **int** |  | 
**model_choices** | **List[str]** |  | [optional] 
**judge_model** | **str** |  | 
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
from launchdarkly_api.models.agent_optimization_post import AgentOptimizationPost

# TODO update the JSON string below
json = "{}"
# create an instance of AgentOptimizationPost from a JSON string
agent_optimization_post_instance = AgentOptimizationPost.from_json(json)
# print the JSON string representation of the object
print(AgentOptimizationPost.to_json())

# convert the object into a dict
agent_optimization_post_dict = agent_optimization_post_instance.to_dict()
# create an instance of AgentOptimizationPost from a dict
agent_optimization_post_from_dict = AgentOptimizationPost.from_dict(agent_optimization_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


