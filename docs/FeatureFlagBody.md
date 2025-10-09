# FeatureFlagBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the feature flag | 
**key** | **str** | A unique key used to reference the flag in your code | 
**description** | **str** | Description of the feature flag. Defaults to an empty string. | [optional] 
**include_in_snippet** | **bool** | Deprecated, use &lt;code&gt;clientSideAvailability&lt;/code&gt;. Whether this flag should be made available to the client-side JavaScript SDK. Defaults to &lt;code&gt;false&lt;/code&gt;. | [optional] 
**client_side_availability** | [**ClientSideAvailabilityPost**](ClientSideAvailabilityPost.md) |  | [optional] 
**variations** | [**List[Variation]**](Variation.md) | An array of possible variations for the flag. The variation values must be unique. If omitted, two boolean variations of &lt;code&gt;true&lt;/code&gt; and &lt;code&gt;false&lt;/code&gt; will be used. | [optional] 
**temporary** | **bool** | Whether the flag is a temporary flag. Defaults to &lt;code&gt;true&lt;/code&gt;. | [optional] 
**tags** | **List[str]** | Tags for the feature flag. Defaults to an empty array. | [optional] 
**custom_properties** | [**Dict[str, CustomProperty]**](CustomProperty.md) |  | [optional] 
**defaults** | [**Defaults**](Defaults.md) |  | [optional] 
**purpose** | **str** | Purpose of the flag | [optional] 
**migration_settings** | [**MigrationSettingsPost**](MigrationSettingsPost.md) |  | [optional] 
**maintainer_id** | **str** | The ID of the member who maintains this feature flag | [optional] 
**maintainer_team_key** | **str** | The key of the team that maintains this feature flag | [optional] 
**initial_prerequisites** | [**List[FlagPrerequisitePost]**](FlagPrerequisitePost.md) | Initial set of prerequisite flags for all environments | [optional] 
**is_flag_on** | **bool** | Whether to automatically turn the flag on across all environments at creation. Defaults to &lt;code&gt;false&lt;/code&gt;. | [optional] 

## Example

```python
from launchdarkly_api.models.feature_flag_body import FeatureFlagBody

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlagBody from a JSON string
feature_flag_body_instance = FeatureFlagBody.from_json(json)
# print the JSON string representation of the object
print(FeatureFlagBody.to_json())

# convert the object into a dict
feature_flag_body_dict = feature_flag_body_instance.to_dict()
# create an instance of FeatureFlagBody from a dict
feature_flag_body_from_dict = FeatureFlagBody.from_dict(feature_flag_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


