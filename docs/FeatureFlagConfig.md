# FeatureFlagConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on** | **bool** | Whether the flag is on | 
**archived** | **bool** | Boolean indicating if the feature flag is archived | 
**salt** | **str** |  | 
**sel** | **str** |  | 
**last_modified** | **int** |  | 
**version** | **int** | Version of the feature flag | 
**targets** | [**List[Target]**](Target.md) | An array of the individual targets that will receive a specific variation based on their key. Individual targets with a context kind of &#39;user&#39; are included here. | [optional] 
**context_targets** | [**List[Target]**](Target.md) | An array of the individual targets that will receive a specific variation based on their key. Individual targets with context kinds other than &#39;user&#39; are included here. | [optional] 
**rules** | [**List[Rule]**](Rule.md) | An array of the rules for how to serve a variation to specific targets based on their attributes | [optional] 
**fallthrough** | [**VariationOrRolloutRep**](VariationOrRolloutRep.md) |  | [optional] 
**off_variation** | **int** | The ID of the variation to serve when the flag is off | [optional] 
**prerequisites** | [**List[Prerequisite]**](Prerequisite.md) | An array of the prerequisite flags and their variations that are required before this flag takes effect | [optional] 
**site** | [**Link**](Link.md) |  | 
**access** | [**Access**](Access.md) |  | [optional] 
**environment_name** | **str** | The environment name | 
**track_events** | **bool** | Whether LaunchDarkly tracks events for the feature flag, for all rules | 
**track_events_fallthrough** | **bool** | Whether LaunchDarkly tracks events for the feature flag, for the default rule | 
**debug_events_until_date** | **int** |  | [optional] 
**summary** | [**FlagSummary**](FlagSummary.md) |  | [optional] 
**evaluation** | [**FlagConfigEvaluation**](FlagConfigEvaluation.md) |  | [optional] 
**migration_settings** | [**FlagConfigMigrationSettingsRep**](FlagConfigMigrationSettingsRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.feature_flag_config import FeatureFlagConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlagConfig from a JSON string
feature_flag_config_instance = FeatureFlagConfig.from_json(json)
# print the JSON string representation of the object
print(FeatureFlagConfig.to_json())

# convert the object into a dict
feature_flag_config_dict = feature_flag_config_instance.to_dict()
# create an instance of FeatureFlagConfig from a dict
feature_flag_config_from_dict = FeatureFlagConfig.from_dict(feature_flag_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


