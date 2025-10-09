# ContextAttributeNames


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The kind associated with this collection of context attribute names. | 
**names** | [**List[ContextAttributeName]**](ContextAttributeName.md) | A collection of context attribute names. | 

## Example

```python
from launchdarkly_api.models.context_attribute_names import ContextAttributeNames

# TODO update the JSON string below
json = "{}"
# create an instance of ContextAttributeNames from a JSON string
context_attribute_names_instance = ContextAttributeNames.from_json(json)
# print the JSON string representation of the object
print(ContextAttributeNames.to_json())

# convert the object into a dict
context_attribute_names_dict = context_attribute_names_instance.to_dict()
# create an instance of ContextAttributeNames from a dict
context_attribute_names_from_dict = ContextAttributeNames.from_dict(context_attribute_names_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


