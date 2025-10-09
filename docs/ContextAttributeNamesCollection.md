# ContextAttributeNamesCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ContextAttributeNames]**](ContextAttributeNames.md) | A collection of context attribute name data grouped by kind. | 

## Example

```python
from launchdarkly_api.models.context_attribute_names_collection import ContextAttributeNamesCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ContextAttributeNamesCollection from a JSON string
context_attribute_names_collection_instance = ContextAttributeNamesCollection.from_json(json)
# print the JSON string representation of the object
print(ContextAttributeNamesCollection.to_json())

# convert the object into a dict
context_attribute_names_collection_dict = context_attribute_names_collection_instance.to_dict()
# create an instance of ContextAttributeNamesCollection from a dict
context_attribute_names_collection_from_dict = ContextAttributeNamesCollection.from_dict(context_attribute_names_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


