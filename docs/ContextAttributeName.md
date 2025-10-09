# ContextAttributeName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A context attribute&#39;s name. | 
**weight** | **int** | A relative estimate of the number of contexts seen recently that have an attribute with the associated name. | 
**redacted** | **bool** | Whether or not the attribute has one or more redacted values. | [optional] 

## Example

```python
from launchdarkly_api.models.context_attribute_name import ContextAttributeName

# TODO update the JSON string below
json = "{}"
# create an instance of ContextAttributeName from a JSON string
context_attribute_name_instance = ContextAttributeName.from_json(json)
# print the JSON string representation of the object
print(ContextAttributeName.to_json())

# convert the object into a dict
context_attribute_name_dict = context_attribute_name_instance.to_dict()
# create an instance of ContextAttributeName from a dict
context_attribute_name_from_dict = ContextAttributeName.from_dict(context_attribute_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


