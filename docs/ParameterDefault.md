# ParameterDefault


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** | The default value for the given parameter | [optional] 
**boolean_variation_value** | **bool** | Variation value for boolean flags. Not applicable for non-boolean flags. | [optional] 
**rule_clause** | [**RuleClause**](RuleClause.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.parameter_default import ParameterDefault

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterDefault from a JSON string
parameter_default_instance = ParameterDefault.from_json(json)
# print the JSON string representation of the object
print(ParameterDefault.to_json())

# convert the object into a dict
parameter_default_dict = parameter_default_instance.to_dict()
# create an instance of ParameterDefault from a dict
parameter_default_from_dict = ParameterDefault.from_dict(parameter_default_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


