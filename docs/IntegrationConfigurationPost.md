# IntegrationConfigurationPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the integration configuration | 
**config_values** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The unique set of fields required to configure the integration. Refer to the &lt;code&gt;formVariables&lt;/code&gt; field in the corresponding &lt;code&gt;manifest.json&lt;/code&gt; at https://github.com/launchdarkly/integration-framework/tree/main/integrations for a full list of fields for the integration you wish to configure. | 
**enabled** | **bool** | Whether the integration configuration is enabled. If omitted, defaults to true | [optional] 
**tags** | **[str]** | Tags for the integration | [optional] 
**capability_config** | [**CapabilityConfigPost**](CapabilityConfigPost.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


