# TreatmentResultRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**treatment_id** | **str** | The ID of the treatment | [optional] 
**treatment_name** | **str** | The name of the treatment | [optional] 
**mean** | **float** | The average value of the variation in this sample. It doesn’t capture the uncertainty in the measurement, so it should not be the only measurement you use to make decisions. | [optional] 
**credible_interval** | [**CredibleIntervalRep**](CredibleIntervalRep.md) |  | [optional] 
**p_best** | **float** | The likelihood that this variation has the biggest effect on the primary metric. Of all the variations in the experiment, the one with highest probability is likely the best option to choose. | [optional] 
**relative_differences** | [**[RelativeDifferenceRep]**](RelativeDifferenceRep.md) | A list of the ranges of the metric that you should have 90% confidence in, for each treatment ID. For example, if the range of the relative differences is [-1%, 4%], you can have 90% confidence that the population difference is a number between 1% lower and 4% higher than the control. | [optional] 
**units** | **int** | The number of experiment users for this variation | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


