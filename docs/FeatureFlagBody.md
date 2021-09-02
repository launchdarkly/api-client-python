# FeatureFlagBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the feature flag | 
**key** | **str** | A unique key to reference the flag in your code | 
**description** | **str** | Description of the feature flag | [optional] 
**include_in_snippet** | **bool** | Deprecated, use clientSideAvailability. Whether or not this flag should be made available to the client-side JavaScript SDK | [optional] 
**client_side_availability** | [**ClientSideAvailabilityPost**](ClientSideAvailabilityPost.md) |  | [optional] 
**variations** | [**[Variate]**](Variate.md) | An array of possible variations for the flag | [optional] 
**variation_json_schema** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**temporary** | **bool** | Whether or not the flag is a temporary flag | [optional] 
**tags** | **[str]** | Tags for the feature flag | [optional] 
**custom_properties** | [**CustomProperties**](CustomProperties.md) |  | [optional] 
**defaults** | [**Defaults**](Defaults.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


