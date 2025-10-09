# AIConfigTargetingEnvironmentFallthroughRollout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_by** | **str** |  | [optional] 
**context_kind** | **str** |  | 
**experiment_allocation** | [**AIConfigTargetingEnvironmentFallthroughRolloutExperimentationAllocation**](AIConfigTargetingEnvironmentFallthroughRolloutExperimentationAllocation.md) |  | [optional] 
**seed** | **int** |  | [optional] 
**variations** | [**List[AIConfigTargetingEnvironmentFallthroughRolloutVariation]**](AIConfigTargetingEnvironmentFallthroughRolloutVariation.md) |  | 

## Example

```python
from launchdarkly_api.models.ai_config_targeting_environment_fallthrough_rollout import AIConfigTargetingEnvironmentFallthroughRollout

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigTargetingEnvironmentFallthroughRollout from a JSON string
ai_config_targeting_environment_fallthrough_rollout_instance = AIConfigTargetingEnvironmentFallthroughRollout.from_json(json)
# print the JSON string representation of the object
print(AIConfigTargetingEnvironmentFallthroughRollout.to_json())

# convert the object into a dict
ai_config_targeting_environment_fallthrough_rollout_dict = ai_config_targeting_environment_fallthrough_rollout_instance.to_dict()
# create an instance of AIConfigTargetingEnvironmentFallthroughRollout from a dict
ai_config_targeting_environment_fallthrough_rollout_from_dict = AIConfigTargetingEnvironmentFallthroughRollout.from_dict(ai_config_targeting_environment_fallthrough_rollout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


