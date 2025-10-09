# AIConfigTargetingEnvironmentTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_kind** | **str** |  | 
**values** | **List[str]** |  | 
**variation** | **int** |  | 

## Example

```python
from launchdarkly_api.models.ai_config_targeting_environment_target import AIConfigTargetingEnvironmentTarget

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigTargetingEnvironmentTarget from a JSON string
ai_config_targeting_environment_target_instance = AIConfigTargetingEnvironmentTarget.from_json(json)
# print the JSON string representation of the object
print(AIConfigTargetingEnvironmentTarget.to_json())

# convert the object into a dict
ai_config_targeting_environment_target_dict = ai_config_targeting_environment_target_instance.to_dict()
# create an instance of AIConfigTargetingEnvironmentTarget from a dict
ai_config_targeting_environment_target_from_dict = AIConfigTargetingEnvironmentTarget.from_dict(ai_config_targeting_environment_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


