# ApplicationRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_added** | **bool** | Whether the application was automatically created because it was included in a context when a LaunchDarkly SDK evaluated a feature flag, or was created through the LaunchDarkly UI or REST API. | 
**key** | **str** | The unique identifier of this application | 
**kind** | **str** | To distinguish the kind of application | 
**name** | **str** | The name of the application | 
**flags** | [**ApplicationFlagCollectionRep**](ApplicationFlagCollectionRep.md) |  | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | [optional] 
**version** | **int** | Version of the application | [optional] 
**creation_date** | **int** |  | [optional] 
**description** | **str** | The application description | [optional] 
**maintainer** | [**MaintainerRep**](MaintainerRep.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


