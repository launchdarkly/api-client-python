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
**site** | [**Link**](Link.md) |  | 
**environment_name** | **str** | The environment name | 
**track_events** | **bool** | Whether LaunchDarkly tracks events for the feature flag, for all rules | 
**track_events_fallthrough** | **bool** | Whether LaunchDarkly tracks events for the feature flag, for the default rule | 
**targets** | [**[Target]**](Target.md) | An array of the individual targets that will receive a specific variation based on their key | [optional] 
**context_targets** | [**[Target]**](Target.md) |  | [optional] 
**rules** | [**[Rule]**](Rule.md) | An array of the rules for how to serve a variation to specific targets based on their attributes | [optional] 
**fallthrough** | [**VariationOrRolloutRep**](VariationOrRolloutRep.md) |  | [optional] 
**off_variation** | **int** | The ID of the variation to serve when the flag is off | [optional] 
**prerequisites** | [**[Prerequisite]**](Prerequisite.md) | An array of the prerequisite flags and their variations that are required before this flag takes effect | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**debug_events_until_date** | **int** |  | [optional] 
**summary** | [**FlagSummary**](FlagSummary.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


