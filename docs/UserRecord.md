# UserRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_ping** | **datetime** | Timestamp of the last time this user was seen | [optional] 
**environment_id** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**sort_value** | **bool, date, datetime, dict, float, int, list, str, none_type** | If this record is returned as part of a list, the value used to sort the list. This is only included when the &lt;code&gt;sort&lt;/code&gt; query parameter is specified. It is a time, in Unix milliseconds, if the sort is by &lt;code&gt;lastSeen&lt;/code&gt;. It is a user key if the sort is by &lt;code&gt;userKey&lt;/code&gt;. | [optional] 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


