# FeatureFlagBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the feature flag | 
**key** | **str** | A unique key used to reference the flag in your code | 
**description** | **str** | Description of the feature flag | [optional] 
**include_in_snippet** | **bool** | Deprecated, use &lt;code&gt;clientSideAvailability&lt;/code&gt;. Whether this flag should be made available to the client-side JavaScript SDK. | [optional] 
**client_side_availability** | [**ClientSideAvailabilityPost**](ClientSideAvailabilityPost.md) |  | [optional] 
**variations** | [**[Variation]**](Variation.md) | An array of possible variations for the flag. The variation values must be unique. | [optional] 
**temporary** | **bool** | Whether the flag is a temporary flag. Defaults to true. | [optional] 
**tags** | **[str]** | Tags for the feature flag | [optional] 
**custom_properties** | [**CustomProperties**](CustomProperties.md) |  | [optional] 
**defaults** | [**Defaults**](Defaults.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


