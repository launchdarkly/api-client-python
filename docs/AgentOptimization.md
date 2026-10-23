# AgentOptimization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**AiConfigsAccess**](AiConfigsAccess.md) |  | [optional] 
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 
**id** | **str** | The agent optimization ID | 
**key** | **str** | The agent optimization key | 
**ai_config_key** | **str** | The key of the AI Config to optimize | 
**max_attempts** | **int** | The maximum number of attempts | 
**model_choices** | **List[str]** | The models to try | 
**judge_model** | **str** | The model used to judge responses | 
**variable_choices** | **List[Dict[str, object]]** | Sets of prompt variable values to try | 
**acceptance_statements** | [**List[AgentOptimizationAcceptanceStatement]**](AgentOptimizationAcceptanceStatement.md) | Statements a response must satisfy to pass | 
**judges** | [**List[AgentOptimizationJudge]**](AgentOptimizationJudge.md) | Judges that score each response | 
**user_input_options** | **List[str]** | User inputs to test with | 
**ground_truth_responses** | **List[str]** | Expected responses to compare against | 
**metric_key** | **str** | The key of the metric to optimize | [optional] 
**token_limit** | **int** | The maximum number of tokens to use | [optional] 
**variation_key** | **str** | The key of the variation to start from | [optional] 
**label** | **str** | A label for the optimization | [optional] 
**latency_optimization** | **bool** | Whether to optimize for lower latency | [optional] 
**token_optimization** | **bool** | Whether to optimize for lower token use | [optional] 
**auto_commit** | **bool** | Whether to save the best result as a new variation automatically | [optional] 
**version** | **int** | The version number of this resource | 
**created_at** | **int** | When this resource was created, in Unix milliseconds | 

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


