# FeatureFlagScheduledChange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**creation_date** | **int** |  | 
**maintainer_id** | **str** | The ID of the scheduled change maintainer | 
**version** | **int** | Version of the scheduled change | 
**execution_date** | **int** |  | 
**instructions** | [**Instructions**](Instructions.md) |  | 
**conflicts** | **bool, date, datetime, dict, float, int, list, str, none_type** | Details on any conflicting scheduled changes | [optional] 
**links** | [**{str: (Link,)}**](Link.md) | Links to other resources within the API. Includes the URL and content type of those resources. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


