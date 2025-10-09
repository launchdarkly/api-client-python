# ContextAttributeValuesCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ContextAttributeValues]**](ContextAttributeValues.md) | A collection of context attribute value data grouped by kind. | 

## Example

```python
from launchdarkly_api.models.context_attribute_values_collection import ContextAttributeValuesCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ContextAttributeValuesCollection from a JSON string
context_attribute_values_collection_instance = ContextAttributeValuesCollection.from_json(json)
# print the JSON string representation of the object
print(ContextAttributeValuesCollection.to_json())

# convert the object into a dict
context_attribute_values_collection_dict = context_attribute_values_collection_instance.to_dict()
# create an instance of ContextAttributeValuesCollection from a dict
context_attribute_values_collection_from_dict = ContextAttributeValuesCollection.from_dict(context_attribute_values_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


