# AgentOptimizationPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key for the agent optimization | 
**ai_config_key** | **str** | The key of the AI Config to optimize | 
**max_attempts** | **int** | The maximum number of attempts | 
**model_choices** | **List[str]** | The models to try | [optional] 
**judge_model** | **str** | The model used to judge responses | 
**variable_choices** | **List[Dict[str, object]]** | Sets of prompt variable values to try | [optional] 
**acceptance_statements** | [**List[AgentOptimizationAcceptanceStatement]**](AgentOptimizationAcceptanceStatement.md) | Statements a response must satisfy to pass | [optional] 
**judges** | [**List[AgentOptimizationJudge]**](AgentOptimizationJudge.md) | Judges that score each response | [optional] 
**user_input_options** | **List[str]** | User inputs to test with | [optional] 
**ground_truth_responses** | **List[str]** | Expected responses to compare against | [optional] 
**metric_key** | **str** | The key of the metric to optimize | [optional] 
**token_limit** | **int** | The maximum number of tokens to use | [optional] 
**variation_key** | **str** | The key of the variation to start from | [optional] 
**label** | **str** | A label for the optimization | [optional] 
**latency_optimization** | **bool** | Whether to optimize for lower latency | [optional] 
**token_optimization** | **bool** | Whether to optimize for lower token use | [optional] 
**auto_commit** | **bool** | Whether to save the best result as a new variation automatically | [optional] 

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


