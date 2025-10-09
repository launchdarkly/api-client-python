# ParameterRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation_id** | **str** |  | [optional] 
**flag_key** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.parameter_rep import ParameterRep

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterRep from a JSON string
parameter_rep_instance = ParameterRep.from_json(json)
# print the JSON string representation of the object
print(ParameterRep.to_json())

# convert the object into a dict
parameter_rep_dict = parameter_rep_instance.to_dict()
# create an instance of ParameterRep from a dict
parameter_rep_from_dict = ParameterRep.from_dict(parameter_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


