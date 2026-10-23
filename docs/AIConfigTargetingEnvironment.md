# AIConfigTargetingEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_targets** | [**List[AIConfigTargetingEnvironmentTarget]**](AIConfigTargetingEnvironmentTarget.md) | Individual context targets for non-user context kinds | 
**enabled** | **bool** | Whether targeting is on in this environment | 
**fallthrough** | [**AIConfigTargetingEnvironmentFallthrough**](AIConfigTargetingEnvironmentFallthrough.md) |  | 
**last_modified** | **int** |  | 
**off_variation** | **int** | Index of the variation served when targeting is off | [optional] 
**rules** | [**List[AIConfigTargetingEnvironmentRule]**](AIConfigTargetingEnvironmentRule.md) | The targeting rules | 
**targets** | [**List[AIConfigTargetingEnvironmentTarget]**](AIConfigTargetingEnvironmentTarget.md) | Individual user targets | 
**track_events** | **bool** | Whether to send detailed events for all evaluations | 
**track_events_fallthrough** | **bool** | Whether to send detailed events for evaluations that fall through to the default rule | 
**environment_name** | **str** | The environment name | 
**version** | **int** | The version of the targeting in this environment | 

## Example

```python
from launchdarkly_api.models.ai_config_targeting_environment import AIConfigTargetingEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigTargetingEnvironment from a JSON string
ai_config_targeting_environment_instance = AIConfigTargetingEnvironment.from_json(json)
# print the JSON string representation of the object
print(AIConfigTargetingEnvironment.to_json())

# convert the object into a dict
ai_config_targeting_environment_dict = ai_config_targeting_environment_instance.to_dict()
# create an instance of AIConfigTargetingEnvironment from a dict
ai_config_targeting_environment_from_dict = AIConfigTargetingEnvironment.from_dict(ai_config_targeting_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


