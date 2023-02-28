# Rule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clauses** | [**[Clause]**](Clause.md) | An array of clauses used for individual targeting based on attributes | 
**track_events** | **bool** | Whether LaunchDarkly tracks events for this rule | 
**id** | **str** | The flag rule ID | [optional] 
**variation** | **int** | The index of the variation, from the array of variations for this flag | [optional] 
**rollout** | [**Rollout**](Rollout.md) |  | [optional] 
**description** | **str** | The rule description | [optional] 
**ref** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


