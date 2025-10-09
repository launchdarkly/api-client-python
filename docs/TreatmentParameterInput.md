# TreatmentParameterInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flag_key** | **str** | The flag key | 
**variation_id** | **str** | The ID of the flag variation | 

## Example

```python
from launchdarkly_api.models.treatment_parameter_input import TreatmentParameterInput

# TODO update the JSON string below
json = "{}"
# create an instance of TreatmentParameterInput from a JSON string
treatment_parameter_input_instance = TreatmentParameterInput.from_json(json)
# print the JSON string representation of the object
print(TreatmentParameterInput.to_json())

# convert the object into a dict
treatment_parameter_input_dict = treatment_parameter_input_instance.to_dict()
# create an instance of TreatmentParameterInput from a dict
treatment_parameter_input_from_dict = TreatmentParameterInput.from_dict(treatment_parameter_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


