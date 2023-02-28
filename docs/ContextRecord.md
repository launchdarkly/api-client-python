# ContextRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **bool, date, datetime, dict, float, int, list, str, none_type** | The context, including its kind and attributes | 
**last_seen** | **datetime** | Timestamp of the last time an evaluation occurred for this context | [optional] 
**application_id** | **str** | An identifier representing the application where the LaunchDarkly SDK is running | [optional] 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**associated_contexts** | **int** | The total number of associated contexts. Associated contexts are contexts that have appeared in the same context instance, that is, they were part of the same flag evaluation. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


