# RandomizationUnitInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**randomization_unit** | **str** | The unit of randomization. Must match the key of an existing context kind in this project. | 
**default** | **bool** | If true, any experiment iterations created within this project will default to using this randomization unit. A project can only have one default randomization unit. | [optional] 
**standard_randomization_unit** | **str** | (deprecated) This field is deprecated and will be removed. Use randomizationUnit instead. | [optional] 

## Example

```python
from launchdarkly_api.models.randomization_unit_input import RandomizationUnitInput

# TODO update the JSON string below
json = "{}"
# create an instance of RandomizationUnitInput from a JSON string
randomization_unit_input_instance = RandomizationUnitInput.from_json(json)
# print the JSON string representation of the object
print(RandomizationUnitInput.to_json())

# convert the object into a dict
randomization_unit_input_dict = randomization_unit_input_instance.to_dict()
# create an instance of RandomizationUnitInput from a dict
randomization_unit_input_from_dict = RandomizationUnitInput.from_dict(randomization_unit_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


