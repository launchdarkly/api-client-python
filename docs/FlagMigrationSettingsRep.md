# FlagMigrationSettingsRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_kind** | **str** | The context kind targeted by this migration flag. Only applicable for six-stage migrations. | [optional] 
**stage_count** | **int** | The number of stages for this migration flag | [optional] 

## Example

```python
from launchdarkly_api.models.flag_migration_settings_rep import FlagMigrationSettingsRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagMigrationSettingsRep from a JSON string
flag_migration_settings_rep_instance = FlagMigrationSettingsRep.from_json(json)
# print the JSON string representation of the object
print(FlagMigrationSettingsRep.to_json())

# convert the object into a dict
flag_migration_settings_rep_dict = flag_migration_settings_rep_instance.to_dict()
# create an instance of FlagMigrationSettingsRep from a dict
flag_migration_settings_rep_from_dict = FlagMigrationSettingsRep.from_dict(flag_migration_settings_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


