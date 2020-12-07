# FeatureFlagConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on** | **bool** |  | [optional] 
**archived** | **bool** |  | [optional] 
**salt** | **str** |  | [optional] 
**sel** | **str** |  | [optional] 
**last_modified** | **int** |  | [optional] 
**version** | **int** |  | [optional] 
**targets** | [**list[Target]**](Target.md) |  | [optional] 
**rules** | [**list[Rule]**](Rule.md) |  | [optional] 
**fallthrough** | [**Fallthrough**](Fallthrough.md) |  | [optional] 
**off_variation** | **int** |  | [optional] 
**prerequisites** | [**list[Prerequisite]**](Prerequisite.md) |  | [optional] 
**track_events** | **bool** | Set to true to send detailed event information for this flag. | [optional] 
**track_events_fallthrough** | **bool** | Set to true to send detailed event information when targeting is enabled but no individual targeting rule is matched. | [optional] 
**site** | [**Site**](Site.md) |  | [optional] 
**environment_name** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


