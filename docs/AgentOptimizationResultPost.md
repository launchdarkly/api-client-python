# AgentOptimizationResultPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **UUID** | The ID of the run this result belongs to | 
**agent_optimization_version** | **int** | The version of the agent optimization used | 
**iteration** | **int** | The iteration number within the run | 
**instructions** | **str** | The instructions used for this attempt | 
**user_input** | **str** | The user input used for this attempt | 
**parameters** | **Dict[str, object]** | The model parameters used for this attempt | [optional] 

## Example

```python
from launchdarkly_api.models.agent_optimization_result_post import AgentOptimizationResultPost

# TODO update the JSON string below
json = "{}"
# create an instance of AgentOptimizationResultPost from a JSON string
agent_optimization_result_post_instance = AgentOptimizationResultPost.from_json(json)
# print the JSON string representation of the object
print(AgentOptimizationResultPost.to_json())

# convert the object into a dict
agent_optimization_result_post_dict = agent_optimization_result_post_instance.to_dict()
# create an instance of AgentOptimizationResultPost from a dict
agent_optimization_result_post_from_dict = AgentOptimizationResultPost.from_dict(agent_optimization_result_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


