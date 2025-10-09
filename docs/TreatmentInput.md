# TreatmentInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The treatment name | 
**baseline** | **bool** | Whether this treatment is the baseline to compare other treatments against | 
**allocation_percent** | **str** | The percentage of traffic allocated to this treatment during the iteration | 
**parameters** | [**List[TreatmentParameterInput]**](TreatmentParameterInput.md) | Details on the flag and variation to use for this treatment | 

## Example

```python
from launchdarkly_api.models.treatment_input import TreatmentInput

# TODO update the JSON string below
json = "{}"
# create an instance of TreatmentInput from a JSON string
treatment_input_instance = TreatmentInput.from_json(json)
# print the JSON string representation of the object
print(TreatmentInput.to_json())

# convert the object into a dict
treatment_input_dict = treatment_input_instance.to_dict()
# create an instance of TreatmentInput from a dict
treatment_input_from_dict = TreatmentInput.from_dict(treatment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


