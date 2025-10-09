# ContextAttributeValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The kind associated with this collection of context attribute values. | 
**values** | [**List[ContextAttributeValue]**](ContextAttributeValue.md) | A collection of context attribute values. | 

## Example

```python
from launchdarkly_api.models.context_attribute_values import ContextAttributeValues

# TODO update the JSON string below
json = "{}"
# create an instance of ContextAttributeValues from a JSON string
context_attribute_values_instance = ContextAttributeValues.from_json(json)
# print the JSON string representation of the object
print(ContextAttributeValues.to_json())

# convert the object into a dict
context_attribute_values_dict = context_attribute_values_instance.to_dict()
# create an instance of ContextAttributeValues from a dict
context_attribute_values_from_dict = ContextAttributeValues.from_dict(context_attribute_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


