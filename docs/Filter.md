# Filter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Filter type. One of [contextAttribute, eventProperty, group] | 
**attribute** | **str** | If not a group node, the context attribute name or event property name to filter on | [optional] 
**op** | **str** |  | 
**values** | **List[object]** | The context attribute / event property values or group member nodes | 
**context_kind** | **str** | For context attribute filters, the context kind. | [optional] 
**negate** | **bool** | If set, then take the inverse of the operator. &#39;in&#39; becomes &#39;not in&#39;. | 

## Example

```python
from launchdarkly_api.models.filter import Filter

# TODO update the JSON string below
json = "{}"
# create an instance of Filter from a JSON string
filter_instance = Filter.from_json(json)
# print the JSON string representation of the object
print(Filter.to_json())

# convert the object into a dict
filter_dict = filter_instance.to_dict()
# create an instance of Filter from a dict
filter_from_dict = Filter.from_dict(filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


