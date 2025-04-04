# HoldoutPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the holdout | [optional] 
**key** | **str** | A key that identifies the holdout | [optional] 
**description** | **str** | Description of the holdout | [optional] 
**randomizationunit** | **str** | The chosen randomization unit for the holdout base experiment | [optional] 
**attributes** | **[str]** | The attributes that the holdout iteration&#39;s results can be sliced by | [optional] 
**holdoutamount** | **str** | Audience allocation for the holdout | [optional] 
**primarymetrickey** | **str** | The key of the primary metric for this holdout | [optional] 
**metrics** | [**[MetricInput]**](MetricInput.md) | Details on the metrics for this experiment | [optional] 
**prerequisiteflagkey** | **str** | The key of the flag that the holdout is dependent on | [optional] 
**maintainer_id** | **str** | Maintainer id | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


