# EventFilter


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
from launchdarkly_api.models.event_filter import EventFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EventFilter from a JSON string
event_filter_instance = EventFilter.from_json(json)
# print the JSON string representation of the object
print(EventFilter.to_json())

# convert the object into a dict
event_filter_dict = event_filter_instance.to_dict()
# create an instance of EventFilter from a dict
event_filter_from_dict = EventFilter.from_dict(event_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


