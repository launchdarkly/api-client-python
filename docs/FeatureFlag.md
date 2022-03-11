# FeatureFlag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the feature flag | 
**kind** | **str** | Kind of feature flag | 
**key** | **str** | A unique key used to reference the flag in your code | 
**version** | **int** | Version of the feature flag | 
**creation_date** | **int** |  | 
**variations** | [**[Variation]**](Variation.md) | An array of possible variations for the flag | 
**temporary** | **bool** | Whether or not the flag is a temporary flag | 
**tags** | **[str]** | Tags for the feature flag | 
**links** | [**{str: (Link,)}**](Link.md) |  | 
**experiments** | [**ExperimentInfoRep**](ExperimentInfoRep.md) |  | 
**custom_properties** | [**CustomProperties**](CustomProperties.md) |  | 
**archived** | **bool** | Boolean indicating if the feature flag is archived | 
**environments** | [**{str: (FeatureFlagConfig,)}**](FeatureFlagConfig.md) |  | 
**description** | **str** | Description of the feature flag | [optional] 
**include_in_snippet** | **bool** | Deprecated, use clientSideAvailability. Whether or not this flag should be made available to the client-side JavaScript SDK | [optional] 
**client_side_availability** | [**ClientSideAvailability**](ClientSideAvailability.md) |  | [optional] 
**variation_json_schema** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**maintainer_id** | **str** | Associated maintainerId for the feature flag | [optional] 
**maintainer** | [**MemberSummary**](MemberSummary.md) |  | [optional] 
**goal_ids** | **[str]** |  | [optional] 
**archived_date** | **int** |  | [optional] 
**defaults** | [**Defaults**](Defaults.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


