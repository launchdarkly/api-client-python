# TreatmentRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The treatment ID. This is the variation ID from the flag. | [optional] 
**name** | **str** | The treatment name. This is the variation name from the flag. | 
**allocation_percent** | **str** | The percentage of traffic allocated to this treatment during the iteration | 
**baseline** | **bool** | Whether this treatment is the baseline to compare other treatments against | [optional] 
**parameters** | [**List[ParameterRep]**](ParameterRep.md) | Details on the flag and variation used for this treatment | [optional] 

## Example

```python
from launchdarkly_api.models.treatment_rep import TreatmentRep

# TODO update the JSON string below
json = "{}"
# create an instance of TreatmentRep from a JSON string
treatment_rep_instance = TreatmentRep.from_json(json)
# print the JSON string representation of the object
print(TreatmentRep.to_json())

# convert the object into a dict
treatment_rep_dict = treatment_rep_instance.to_dict()
# create an instance of TreatmentRep from a dict
treatment_rep_from_dict = TreatmentRep.from_dict(treatment_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


