# TreatmentResultRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**treatment_id** | **str** | The ID of the treatment | [optional] 
**treatment_name** | **str** | The name of the treatment | [optional] 
**mean** | **float** | The average value of the variation in this sample. It doesn’t capture the uncertainty in the measurement, so it should not be the only measurement you use to make decisions. | [optional] 
**credible_interval** | [**CredibleIntervalRep**](CredibleIntervalRep.md) |  | [optional] 
**p_best** | **float** | The likelihood that this variation has the biggest effect on the primary metric. The variation with the highest probability is likely the best of the variations you&#39;re testing | [optional] 
**relative_differences** | [**[RelativeDifferenceRep]**](RelativeDifferenceRep.md) | Estimates of the relative difference between this treatment&#39;s mean and the mean of each other treatment | [optional] 
**units** | **int** | The number of end users in this variation of the experiment | [optional] 
**distribution** | [**Distribution**](Distribution.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


