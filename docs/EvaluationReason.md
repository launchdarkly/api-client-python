# EvaluationReason


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Describes the general reason that LaunchDarkly selected this variation. | 
**rule_index** | **int** | The positional index of the matching rule if the kind is &#39;RULE_MATCH&#39;. The index is 0-based. | [optional] 
**rule_id** | **str** | The unique identifier of the matching rule if the kind is &#39;RULE_MATCH&#39;. | [optional] 
**prerequisite_key** | **str** | The key of the flag that failed if the kind is &#39;PREREQUISITE_FAILED&#39;. | [optional] 
**in_experiment** | **bool** | Indicates whether the user was evaluated as part of an experiment. | [optional] 
**error_kind** | **str** | The specific error type if the kind is &#39;ERROR&#39;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


