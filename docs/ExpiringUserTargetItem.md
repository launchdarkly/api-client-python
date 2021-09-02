# ExpiringUserTargetItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **int** |  | 
**expiration_date** | **int** |  | 
**user_key** | **str** | A unique key used to represent the user | 
**resource_id** | [**ResourceIDResponse**](ResourceIDResponse.md) |  | 
**target_type** | **str** | A segment&#39;s target type. Included when expiring user targets are updated on a user segment. | [optional] 
**variation_id** | **str** | A unique key used to represent the flag variation. Included when expiring user targets are updated on a feature flag. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


