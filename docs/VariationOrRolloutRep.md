# VariationOrRolloutRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation** | **int** | The index of the variation, from the array of variations for this flag | [optional] 
**rollout** | [**Rollout**](Rollout.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.variation_or_rollout_rep import VariationOrRolloutRep

# TODO update the JSON string below
json = "{}"
# create an instance of VariationOrRolloutRep from a JSON string
variation_or_rollout_rep_instance = VariationOrRolloutRep.from_json(json)
# print the JSON string representation of the object
print(VariationOrRolloutRep.to_json())

# convert the object into a dict
variation_or_rollout_rep_dict = variation_or_rollout_rep_instance.to_dict()
# create an instance of VariationOrRolloutRep from a dict
variation_or_rollout_rep_from_dict = VariationOrRolloutRep.from_dict(variation_or_rollout_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


