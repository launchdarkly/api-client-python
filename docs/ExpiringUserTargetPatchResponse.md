# ExpiringUserTargetPatchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[ExpiringUserTargetItem]**](ExpiringUserTargetItem.md) | An array of expiring user targets | 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | [optional] 
**total_instructions** | **int** | The total count of instructions sent in the PATCH request | [optional] 
**successful_instructions** | **int** | The total count of successful instructions sent in the PATCH request | [optional] 
**failed_instructions** | **int** | The total count of the failed instructions sent in the PATCH request | [optional] 
**errors** | [**[ExpiringTargetError]**](ExpiringTargetError.md) | An array of error messages for the failed instructions | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


