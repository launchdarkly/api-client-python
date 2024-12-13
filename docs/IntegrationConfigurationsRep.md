# IntegrationConfigurationsRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | 
**id** | **str** | The unique identifier for this integration configuration | 
**name** | **str** | A human-friendly name for the integration | 
**created_at** | **int** |  | [optional] 
**integration_key** | **str** | The type of integration | [optional] 
**tags** | **[str]** | An array of tags for this integration | [optional] 
**enabled** | **bool** | Whether the integration is currently active | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**config_values** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Details on configuration for an integration of this type. Refer to the &lt;code&gt;formVariables&lt;/code&gt; field in the corresponding &lt;code&gt;manifest.json&lt;/code&gt; for a full list of fields for each integration. | [optional] 
**capability_config** | [**CapabilityConfigRep**](CapabilityConfigRep.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


