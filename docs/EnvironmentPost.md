# EnvironmentPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the new environment. | 
**key** | **str** | A project-unique key for the new environment. | 
**color** | **str** | A color to indicate this environment in the UI. | 
**default_ttl** | **int** | The default time (in minutes) that the PHP SDK can cache feature flag rules locally. | [optional] 
**secure_mode** | **bool** | Secure mode ensures that a user of the client-side SDK cannot impersonate another user. | [optional] 
**default_track_events** | **bool** | Enables tracking detailed information for new flags by default. | [optional] 
**confirm_changes** | **bool** | Require confirmation for all flag and segment changes via the UI in this environment. | [optional] 
**require_comments** | **bool** | Require comments for all flag and segment changes via the UI in this environment. | [optional] 
**tags** | **[str]** | Tags to apply to the new environment. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


