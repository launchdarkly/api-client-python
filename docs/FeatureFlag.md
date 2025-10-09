# FeatureFlag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the feature flag | 
**kind** | **str** | Kind of feature flag | 
**description** | **str** | Description of the feature flag | [optional] 
**key** | **str** | A unique key used to reference the flag in your code | 
**version** | **int** | Version of the feature flag | 
**creation_date** | **int** |  | 
**include_in_snippet** | **bool** | Deprecated, use &lt;code&gt;clientSideAvailability&lt;/code&gt;. Whether this flag should be made available to the client-side JavaScript SDK | [optional] 
**client_side_availability** | [**ClientSideAvailability**](ClientSideAvailability.md) |  | [optional] 
**variations** | [**List[Variation]**](Variation.md) | An array of possible variations for the flag | 
**temporary** | **bool** | Whether the flag is a temporary flag | 
**tags** | **List[str]** | Tags for the feature flag | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**maintainer_id** | **str** | Associated maintainerId for the feature flag | [optional] 
**maintainer** | [**MemberSummary**](MemberSummary.md) |  | [optional] 
**maintainer_team_key** | **str** | The key of the associated team that maintains this feature flag | [optional] 
**maintainer_team** | [**MaintainerTeam**](MaintainerTeam.md) |  | [optional] 
**goal_ids** | **List[str]** | Deprecated, use &lt;code&gt;experiments&lt;/code&gt; instead | [optional] 
**experiments** | [**ExperimentInfoRep**](ExperimentInfoRep.md) |  | 
**custom_properties** | [**Dict[str, CustomProperty]**](CustomProperty.md) |  | 
**archived** | **bool** | Boolean indicating if the feature flag is archived | 
**archived_date** | **int** |  | [optional] 
**deprecated** | **bool** | Boolean indicating if the feature flag is deprecated | [optional] 
**deprecated_date** | **int** |  | [optional] 
**defaults** | [**Defaults**](Defaults.md) |  | [optional] 
**purpose** | **str** |  | [optional] 
**migration_settings** | [**FlagMigrationSettingsRep**](FlagMigrationSettingsRep.md) |  | [optional] 
**environments** | [**Dict[str, FeatureFlagConfig]**](FeatureFlagConfig.md) | Details on the environments for this flag. Only returned if the request is filtered by environment, using the &lt;code&gt;filterEnv&lt;/code&gt; query parameter. | [optional] 

## Example

```python
from launchdarkly_api.models.feature_flag import FeatureFlag

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlag from a JSON string
feature_flag_instance = FeatureFlag.from_json(json)
# print the JSON string representation of the object
print(FeatureFlag.to_json())

# convert the object into a dict
feature_flag_dict = feature_flag_instance.to_dict()
# create an instance of FeatureFlag from a dict
feature_flag_from_dict = FeatureFlag.from_dict(feature_flag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


