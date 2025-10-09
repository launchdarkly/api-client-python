# FormVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**placeholder** | **str** |  | [optional] 
**is_optional** | **bool** |  | [optional] 
**default_value** | **object** |  | [optional] 
**allowed_values** | **List[str]** |  | [optional] 
**dynamic_options** | [**DynamicOptions**](DynamicOptions.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.form_variable import FormVariable

# TODO update the JSON string below
json = "{}"
# create an instance of FormVariable from a JSON string
form_variable_instance = FormVariable.from_json(json)
# print the JSON string representation of the object
print(FormVariable.to_json())

# convert the object into a dict
form_variable_dict = form_variable_instance.to_dict()
# create an instance of FormVariable from a dict
form_variable_from_dict = FormVariable.from_dict(form_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


