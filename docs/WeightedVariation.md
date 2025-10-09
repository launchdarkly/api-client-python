# WeightedVariation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation** | **int** |  | 
**weight** | **int** |  | 
**untracked** | **bool** |  | [optional] 

## Example

```python
from launchdarkly_api.models.weighted_variation import WeightedVariation

# TODO update the JSON string below
json = "{}"
# create an instance of WeightedVariation from a JSON string
weighted_variation_instance = WeightedVariation.from_json(json)
# print the JSON string representation of the object
print(WeightedVariation.to_json())

# convert the object into a dict
weighted_variation_dict = weighted_variation_instance.to_dict()
# create an instance of WeightedVariation from a dict
weighted_variation_from_dict = WeightedVariation.from_dict(weighted_variation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


