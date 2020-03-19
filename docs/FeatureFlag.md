# FeatureFlag

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**name** | **str** | Name of the feature flag. | [optional] 
**description** | **str** | Description of the feature flag. | [optional] 
**kind** | **str** | Whether the feature flag is a boolean flag or multivariate. | [optional] 
**creation_date** | **float** | A unix epoch time in milliseconds specifying the creation time of this flag. | [optional] 
**include_in_snippet** | **bool** |  | [optional] 
**temporary** | **bool** | Whether or not this flag is temporary. | [optional] 
**maintainer_id** | **str** | The ID of the member that should maintain this flag. | [optional] 
**tags** | **list[str]** | An array of tags for this feature flag. | [optional] 
**variations** | [**list[Variation]**](Variation.md) | The variations for this feature flag. | [optional] 
**goal_ids** | **list[str]** | An array goals from all environments associated with this feature flag | [optional] 
**version** | **int** |  | [optional] 
**custom_properties** | [**dict(str, CustomProperty)**](CustomProperty.md) | A mapping of keys to CustomProperty entries. | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**maintainer** | [**Member**](Member.md) |  | [optional] 
**environments** | [**dict(str, FeatureFlagConfig)**](FeatureFlagConfig.md) |  | [optional] 
**archived_date** | **float** | A unix epoch time in milliseconds specifying the archived time of this flag. | [optional] 
**archived** | **bool** | Whether or not this flag is archived. | [optional] 
**defaults** | [**Defaults**](Defaults.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


