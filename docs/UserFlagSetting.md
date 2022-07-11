# UserFlagSetting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources. | 
**value** | **bool, date, datetime, dict, float, int, list, str, none_type** | The value of the flag variation that the user receives. If there is no defined default rule, this is null. | 
**setting** | **bool, date, datetime, dict, float, int, list, str, none_type** | Whether the user is explicitly targeted to receive a particular variation. The setting is false if you have turned off a feature flag for a user. It is null if you haven&#39;t assigned that user to a specific variation. | 
**reason** | [**EvaluationReason**](EvaluationReason.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


