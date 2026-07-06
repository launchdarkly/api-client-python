# AgentOptimizationResultPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **UUID** |  | 
**agent_optimization_version** | **int** |  | 
**iteration** | **int** |  | 
**instructions** | **str** |  | 
**user_input** | **str** |  | 
**parameters** | **Dict[str, object]** |  | [optional] 

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


