# IterationInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hypothesis** | **str** | The expected outcome of this experiment | 
**metrics** | [**MetricsInput**](MetricsInput.md) |  | 
**treatments** | [**TreatmentsInput**](TreatmentsInput.md) |  | 
**flags** | [**FlagsInput**](FlagsInput.md) |  | 
**can_reshuffle_traffic** | **bool** | Whether to allow the experiment to reassign users to different variations (true) or keep users assigned to their initial variation (false). Defaults to true. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


