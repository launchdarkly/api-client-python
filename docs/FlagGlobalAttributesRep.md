# FlagGlobalAttributesRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the feature flag | 
**kind** | **str** | Kind of feature flag | 
**key** | **str** | A unique key used to reference the flag in your code | 
**version** | **int** | Version of the feature flag | 
**creation_date** | **int** |  | 
**variations** | [**[Variation]**](Variation.md) | An array of possible variations for the flag | 
**temporary** | **bool** | Whether the flag is a temporary flag | 
**tags** | **[str]** | Tags for the feature flag | 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | 
**experiments** | [**ExperimentInfoRep**](ExperimentInfoRep.md) |  | 
**custom_properties** | [**CustomProperties**](CustomProperties.md) |  | 
**archived** | **bool** | Boolean indicating if the feature flag is archived | 
**description** | **str** | Description of the feature flag | [optional] 
**include_in_snippet** | **bool** | Deprecated, use &lt;code&gt;clientSideAvailability&lt;/code&gt;. Whether this flag should be made available to the client-side JavaScript SDK | [optional] 
**client_side_availability** | [**ClientSideAvailability**](ClientSideAvailability.md) |  | [optional] 
**maintainer_id** | **str** | Associated maintainerId for the feature flag | [optional] 
**maintainer** | [**MemberSummary**](MemberSummary.md) |  | [optional] 
**maintainer_team_key** | **str** | The key of the associated team that maintains this feature flag | [optional] 
**maintainer_team** | [**MaintainerTeam**](MaintainerTeam.md) |  | [optional] 
**goal_ids** | **[str]** | Deprecated, use &lt;code&gt;experiments&lt;/code&gt; instead | [optional] 
**archived_date** | **int** |  | [optional] 
**defaults** | [**Defaults**](Defaults.md) |  | [optional] 
**purpose** | **str** |  | [optional] 
**migration_settings** | [**FlagMigrationSettingsRep**](FlagMigrationSettingsRep.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


