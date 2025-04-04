# CustomRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the custom role | 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | 
**key** | **str** | The key of the custom role | 
**name** | **str** | The name of the custom role | 
**policy** | [**[Statement]**](Statement.md) | An array of the policies that comprise this custom role | 
**access** | [**Access**](Access.md) |  | [optional] 
**description** | **str** | The description of the custom role | [optional] 
**base_permissions** | **str** |  | [optional] 
**resource_category** | **str** |  | [optional] 
**assigned_to** | [**AssignedToRep**](AssignedToRep.md) |  | [optional] 
**preset_bundle_version** | **int** | If created from a preset, the preset bundle version | [optional] 
**preset_statements** | [**[Statement]**](Statement.md) | If created from a preset, the read-only statements copied from the preset | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


