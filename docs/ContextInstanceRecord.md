# ContextInstanceRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_seen** | **datetime** | Timestamp of the last time an evaluation occurred for this context instance | [optional] 
**id** | **str** | The context instance ID | 
**application_id** | **str** | An identifier representing the application where the LaunchDarkly SDK is running | [optional] 
**anonymous_kinds** | **List[str]** | A list of the context kinds this context was associated with that the SDK removed because they were marked as anonymous at flag evaluation | [optional] 
**context** | **object** | The context, including its kind and attributes | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.context_instance_record import ContextInstanceRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ContextInstanceRecord from a JSON string
context_instance_record_instance = ContextInstanceRecord.from_json(json)
# print the JSON string representation of the object
print(ContextInstanceRecord.to_json())

# convert the object into a dict
context_instance_record_dict = context_instance_record_instance.to_dict()
# create an instance of ContextInstanceRecord from a dict
context_instance_record_from_dict = ContextInstanceRecord.from_dict(context_instance_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


