# ModelImport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The import ID | 
**segment_key** | **str** | The segment key | 
**creation_time** | **int** |  | 
**mode** | **str** | The import mode used, either &lt;code&gt;merge&lt;/code&gt; or &lt;code&gt;replace&lt;/code&gt; | 
**status** | **str** | The import status | 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | 
**files** | [**[FileRep]**](FileRep.md) | The imported files and their status | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


