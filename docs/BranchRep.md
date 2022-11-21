# BranchRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The branch name | 
**head** | **str** | An ID representing the branch HEAD. For example, a commit SHA. | 
**sync_time** | **int** |  | 
**links** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The location and content type of related resources | 
**update_sequence_id** | **int** | An optional ID used to prevent older data from overwriting newer data | [optional] 
**references** | [**[ReferenceRep]**](ReferenceRep.md) | An array of flag references found on the branch | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


