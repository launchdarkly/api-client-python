# AgentOptimizationJudge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**threshold** | **float** |  | 

## Example

```python
from launchdarkly_api.models.agent_optimization_judge import AgentOptimizationJudge

# TODO update the JSON string below
json = "{}"
# create an instance of AgentOptimizationJudge from a JSON string
agent_optimization_judge_instance = AgentOptimizationJudge.from_json(json)
# print the JSON string representation of the object
print(AgentOptimizationJudge.to_json())

# convert the object into a dict
agent_optimization_judge_dict = agent_optimization_judge_instance.to_dict()
# create an instance of AgentOptimizationJudge from a dict
agent_optimization_judge_from_dict = AgentOptimizationJudge.from_dict(agent_optimization_judge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


