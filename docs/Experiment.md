# Experiment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The experiment key | 
**name** | **str** | The experiment name | 
**maintainer_id** | **str** | The ID of the member who maintains this experiment. | 
**creation_date** | **int** |  | 
**environment_key** | **str** |  | 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | 
**id** | **str** | The experiment ID | [optional] 
**description** | **str** | The experiment description | [optional] 
**archived_date** | **int** |  | [optional] 
**holdout_id** | **str** | The holdout ID | [optional] 
**current_iteration** | [**IterationRep**](IterationRep.md) |  | [optional] 
**draft_iteration** | [**IterationRep**](IterationRep.md) |  | [optional] 
**previous_iterations** | [**[IterationRep]**](IterationRep.md) | Details on the previous iterations for this experiment. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


