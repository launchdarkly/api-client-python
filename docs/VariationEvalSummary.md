# VariationEvalSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** | The variation value | [optional] 
**before** | **int** | The number of evaluations in the ten minutes before the flag event | [optional] 
**after** | **int** | The number of evaluations in the ten minutes after the flag event | [optional] 

## Example

```python
from launchdarkly_api.models.variation_eval_summary import VariationEvalSummary

# TODO update the JSON string below
json = "{}"
# create an instance of VariationEvalSummary from a JSON string
variation_eval_summary_instance = VariationEvalSummary.from_json(json)
# print the JSON string representation of the object
print(VariationEvalSummary.to_json())

# convert the object into a dict
variation_eval_summary_dict = variation_eval_summary_instance.to_dict()
# create an instance of VariationEvalSummary from a dict
variation_eval_summary_from_dict = VariationEvalSummary.from_dict(variation_eval_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


