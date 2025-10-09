# MigrationSettingsPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_kind** | **str** | Context kind for a migration with 6 stages, where data is being moved | [optional] 
**stage_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.migration_settings_post import MigrationSettingsPost

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationSettingsPost from a JSON string
migration_settings_post_instance = MigrationSettingsPost.from_json(json)
# print the JSON string representation of the object
print(MigrationSettingsPost.to_json())

# convert the object into a dict
migration_settings_post_dict = migration_settings_post_instance.to_dict()
# create an instance of MigrationSettingsPost from a dict
migration_settings_post_from_dict = MigrationSettingsPost.from_dict(migration_settings_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


