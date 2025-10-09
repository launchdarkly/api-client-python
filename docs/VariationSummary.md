# VariationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | **int** |  | 
**null_rules** | **int** |  | 
**targets** | **int** |  | 
**context_targets** | **int** |  | 
**is_fallthrough** | **bool** |  | [optional] 
**is_off** | **bool** |  | [optional] 
**rollout** | **int** |  | [optional] 
**bucket_by** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.variation_summary import VariationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of VariationSummary from a JSON string
variation_summary_instance = VariationSummary.from_json(json)
# print the JSON string representation of the object
print(VariationSummary.to_json())

# convert the object into a dict
variation_summary_dict = variation_summary_instance.to_dict()
# create an instance of VariationSummary from a dict
variation_summary_from_dict = VariationSummary.from_dict(variation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


