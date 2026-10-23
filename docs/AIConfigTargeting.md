# AIConfigTargeting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** | Unix timestamp in milliseconds | 
**defaults** | [**AIConfigTargetingDefaults**](AIConfigTargetingDefaults.md) |  | [optional] 
**environments** | [**Dict[str, AIConfigTargetingEnvironment]**](AIConfigTargetingEnvironment.md) | Targeting for each environment, keyed by environment key | 
**experiments** | [**AiConfigsExperimentInfoRep**](AiConfigsExperimentInfoRep.md) |  | 
**key** | **str** | The AI Config key | 
**name** | **str** | The AI Config name | 
**tags** | **List[str]** | Tags for this resource | 
**variations** | [**List[AIConfigTargetingVariation]**](AIConfigTargetingVariation.md) | The variations of this AI Config | 
**version** | **int** | The version number of this resource | 

## Example

```python
from launchdarkly_api.models.ai_config_targeting import AIConfigTargeting

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigTargeting from a JSON string
ai_config_targeting_instance = AIConfigTargeting.from_json(json)
# print the JSON string representation of the object
print(AIConfigTargeting.to_json())

# convert the object into a dict
ai_config_targeting_dict = ai_config_targeting_instance.to_dict()
# create an instance of AIConfigTargeting from a dict
ai_config_targeting_from_dict = AIConfigTargeting.from_dict(ai_config_targeting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


