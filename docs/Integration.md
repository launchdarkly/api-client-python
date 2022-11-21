# Integration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | [optional] 
**id** | **str** | The ID for this integration audit log subscription | [optional] 
**kind** | **str** | The type of integration | [optional] 
**name** | **str** | A human-friendly name for the integration | [optional] 
**config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Details on configuration for an integration of this type. Refer to the &lt;code&gt;formVariables&lt;/code&gt; field in the corresponding &lt;code&gt;manifest.json&lt;/code&gt; for a full list of fields for each integration. | [optional] 
**statements** | [**[Statement]**](Statement.md) | Represents a Custom role policy, defining a resource kinds filter the integration audit log subscription responds to. | [optional] 
**on** | **bool** | Whether the integration is currently active | [optional] 
**tags** | **[str]** | An array of tags for this integration | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**status** | [**IntegrationSubscriptionStatusRep**](IntegrationSubscriptionStatusRep.md) |  | [optional] 
**url** | **str** | Slack webhook receiver URL. Only used for legacy Slack webhook integrations. | [optional] 
**api_key** | **str** | Datadog API key. Only used for legacy Datadog webhook integrations. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


