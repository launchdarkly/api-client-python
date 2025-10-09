# ContextAttributeValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | A value for a context attribute. | 
**weight** | **int** | A relative estimate of the number of contexts seen recently that have a matching value for a given attribute. | 

## Example

```python
from launchdarkly_api.models.context_attribute_value import ContextAttributeValue

# TODO update the JSON string below
json = "{}"
# create an instance of ContextAttributeValue from a JSON string
context_attribute_value_instance = ContextAttributeValue.from_json(json)
# print the JSON string representation of the object
print(ContextAttributeValue.to_json())

# convert the object into a dict
context_attribute_value_dict = context_attribute_value_instance.to_dict()
# create an instance of ContextAttributeValue from a dict
context_attribute_value_from_dict = ContextAttributeValue.from_dict(context_attribute_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


