# FlagConfigMigrationSettingsRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_ratio** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.flag_config_migration_settings_rep import FlagConfigMigrationSettingsRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagConfigMigrationSettingsRep from a JSON string
flag_config_migration_settings_rep_instance = FlagConfigMigrationSettingsRep.from_json(json)
# print the JSON string representation of the object
print(FlagConfigMigrationSettingsRep.to_json())

# convert the object into a dict
flag_config_migration_settings_rep_dict = flag_config_migration_settings_rep_instance.to_dict()
# create an instance of FlagConfigMigrationSettingsRep from a dict
flag_config_migration_settings_rep_from_dict = FlagConfigMigrationSettingsRep.from_dict(flag_config_migration_settings_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


