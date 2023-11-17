# ApplicationVersionRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_added** | **bool** | Whether the application version was automatically created, because it was included in a context when a LaunchDarkly SDK evaluated a feature flag, or if the application version was created through the LaunchDarkly UI or REST API.  | 
**key** | **str** | The unique identifier of this application version | 
**name** | **str** | The name of this version | 
**access** | [**Access**](Access.md) |  | [optional] 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | [optional] 
**version** | **int** | Version of the application version | [optional] 
**creation_date** | **int** |  | [optional] 
**supported** | **bool** | Whether this version is supported. Only applicable if the application &lt;code&gt;kind&lt;/code&gt; is &lt;code&gt;mobile&lt;/code&gt;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


