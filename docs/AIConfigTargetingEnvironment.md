# AIConfigTargetingEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_targets** | [**List[AIConfigTargetingEnvironmentTarget]**](AIConfigTargetingEnvironmentTarget.md) |  | 
**enabled** | **bool** |  | 
**fallthrough** | [**AIConfigTargetingEnvironmentFallthrough**](AIConfigTargetingEnvironmentFallthrough.md) |  | 
**last_modified** | **int** |  | 
**off_variation** | **int** |  | [optional] 
**rules** | [**List[AIConfigTargetingEnvironmentRule]**](AIConfigTargetingEnvironmentRule.md) |  | 
**targets** | [**List[AIConfigTargetingEnvironmentTarget]**](AIConfigTargetingEnvironmentTarget.md) |  | 
**track_events** | **bool** |  | 
**track_events_fallthrough** | **bool** |  | 
**environment_name** | **str** |  | 
**version** | **int** |  | 

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


