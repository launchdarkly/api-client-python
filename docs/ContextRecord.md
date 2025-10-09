# ContextRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_seen** | **datetime** | Timestamp of the last time an evaluation occurred for this context | [optional] 
**application_id** | **str** | An identifier representing the application where the LaunchDarkly SDK is running | [optional] 
**context** | **object** | The context, including its kind and attributes | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**associated_contexts** | **int** | The total number of associated contexts. Associated contexts are contexts that have appeared in the same context instance, that is, they were part of the same flag evaluation. | [optional] 

## Example

```python
from launchdarkly_api.models.context_record import ContextRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ContextRecord from a JSON string
context_record_instance = ContextRecord.from_json(json)
# print the JSON string representation of the object
print(ContextRecord.to_json())

# convert the object into a dict
context_record_dict = context_record_instance.to_dict()
# create an instance of ContextRecord from a dict
context_record_from_dict = ContextRecord.from_dict(context_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


