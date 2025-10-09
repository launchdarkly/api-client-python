# EvaluationsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variations** | [**List[VariationEvalSummary]**](VariationEvalSummary.md) | A list of variation evaluations | [optional] 

## Example

```python
from launchdarkly_api.models.evaluations_summary import EvaluationsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluationsSummary from a JSON string
evaluations_summary_instance = EvaluationsSummary.from_json(json)
# print the JSON string representation of the object
print(EvaluationsSummary.to_json())

# convert the object into a dict
evaluations_summary_dict = evaluations_summary_instance.to_dict()
# create an instance of EvaluationsSummary from a dict
evaluations_summary_from_dict = EvaluationsSummary.from_dict(evaluations_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


