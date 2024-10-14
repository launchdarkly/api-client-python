# ReleasePhase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The phase ID | 
**name** | **str** | The release phase name | 
**complete** | **bool** | Whether this phase is complete | 
**creation_date** | **int** |  | 
**audiences** | [**[ReleaseAudience]**](ReleaseAudience.md) | A logical grouping of one or more environments that share attributes for rolling out changes | 
**completion_date** | **int** |  | [optional] 
**completed_by** | [**CompletedBy**](CompletedBy.md) |  | [optional] 
**status** | **str** |  | [optional] 
**started** | **bool** | Whether or not this phase has started | [optional] 
**started_date** | **int** |  | [optional] 
**configuration** | [**PhaseConfiguration**](PhaseConfiguration.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


