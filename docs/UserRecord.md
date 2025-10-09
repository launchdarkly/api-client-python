# UserRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_ping** | **datetime** | Timestamp of the last time this user was seen | [optional] 
**environment_id** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**sort_value** | **object** | If this record is returned as part of a list, the value used to sort the list. This is only included when the &lt;code&gt;sort&lt;/code&gt; query parameter is specified. It is a time, in Unix milliseconds, if the sort is by &lt;code&gt;lastSeen&lt;/code&gt;. It is a user key if the sort is by &lt;code&gt;userKey&lt;/code&gt;. | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.user_record import UserRecord

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecord from a JSON string
user_record_instance = UserRecord.from_json(json)
# print the JSON string representation of the object
print(UserRecord.to_json())

# convert the object into a dict
user_record_dict = user_record_instance.to_dict()
# create an instance of UserRecord from a dict
user_record_from_dict = UserRecord.from_dict(user_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


