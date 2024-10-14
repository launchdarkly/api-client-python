# HoldoutDetailRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** |  | 
**holdout_amount** | **str** | The percentage of traffic allocated to this holdout. | 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 
**base_experiment** | [**Experiment**](Experiment.md) |  | 
**description** | **str** |  | [optional] 
**is_dirty** | **bool** | Indicates if the holdout experiment is running and if any related experiments are running. | [optional] 
**related_experiments** | [**[Experiment]**](Experiment.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


