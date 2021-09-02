# FeatureFlagConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on** | **bool** |  | 
**archived** | **bool** |  | 
**salt** | **str** |  | 
**sel** | **str** |  | 
**last_modified** | **int** |  | 
**version** | **int** |  | 
**targets** | [**[Target]**](Target.md) |  | 
**rules** | [**[Rule]**](Rule.md) |  | 
**fallthrough** | [**VariationOrRolloutRep**](VariationOrRolloutRep.md) |  | 
**prerequisites** | [**[Prerequisite]**](Prerequisite.md) |  | 
**site** | [**Link**](Link.md) |  | 
**environment_name** | **str** |  | 
**track_events** | **bool** |  | 
**track_events_fallthrough** | **bool** |  | 
**off_variation** | **int** |  | [optional] 
**access** | [**AccessRep**](AccessRep.md) |  | [optional] 
**debug_events_until_date** | **int** |  | [optional] 
**summary** | [**FlagSummary**](FlagSummary.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


