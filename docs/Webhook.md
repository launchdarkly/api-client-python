# Webhook


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{str: (Link,)}**](Link.md) | Links to other resources within the API. Includes the URL and content type of those resources. | 
**id** | **str** | The ID of this webhook | 
**url** | **str** | The URL to which LaunchDarkly sends an HTTP POST payload for this webhook | 
**on** | **bool** | Whether or not this webhook is enabled | 
**tags** | **[str]** | List of tags for this webhook | 
**name** | **str** | A human-readable name for this webhook | [optional] 
**secret** | **str** | The secret for this webhook | [optional] 
**statements** | [**[Statement]**](Statement.md) | Represents a Custom role policy, defining a resource kinds filter the webhook responds to. | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


