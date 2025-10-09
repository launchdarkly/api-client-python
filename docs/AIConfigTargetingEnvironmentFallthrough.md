# AIConfigTargetingEnvironmentFallthrough


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation** | **int** |  | [optional] 
**rollout** | [**AIConfigTargetingEnvironmentFallthroughRollout**](AIConfigTargetingEnvironmentFallthroughRollout.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.ai_config_targeting_environment_fallthrough import AIConfigTargetingEnvironmentFallthrough

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigTargetingEnvironmentFallthrough from a JSON string
ai_config_targeting_environment_fallthrough_instance = AIConfigTargetingEnvironmentFallthrough.from_json(json)
# print the JSON string representation of the object
print(AIConfigTargetingEnvironmentFallthrough.to_json())

# convert the object into a dict
ai_config_targeting_environment_fallthrough_dict = ai_config_targeting_environment_fallthrough_instance.to_dict()
# create an instance of AIConfigTargetingEnvironmentFallthrough from a dict
ai_config_targeting_environment_fallthrough_from_dict = AIConfigTargetingEnvironmentFallthrough.from_dict(ai_config_targeting_environment_fallthrough_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


