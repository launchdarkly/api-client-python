# EvaluationReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Describes the general reason that LaunchDarkly selected this variation. | 
**rule_index** | **int** | The positional index of the matching rule if the kind is &#39;RULE_MATCH&#39;. The index is 0-based. | [optional] 
**rule_id** | **str** | The unique identifier of the matching rule if the kind is &#39;RULE_MATCH&#39;. | [optional] 
**prerequisite_key** | **str** | The key of the flag that failed if the kind is &#39;PREREQUISITE_FAILED&#39;. | [optional] 
**in_experiment** | **bool** | Indicates whether the evaluation occurred as part of an experiment. | [optional] 
**error_kind** | **str** | The specific error type if the kind is &#39;ERROR&#39;. | [optional] 

## Example

```python
from launchdarkly_api.models.evaluation_reason import EvaluationReason

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluationReason from a JSON string
evaluation_reason_instance = EvaluationReason.from_json(json)
# print the JSON string representation of the object
print(EvaluationReason.to_json())

# convert the object into a dict
evaluation_reason_dict = evaluation_reason_instance.to_dict()
# create an instance of EvaluationReason from a dict
evaluation_reason_from_dict = EvaluationReason.from_dict(evaluation_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


