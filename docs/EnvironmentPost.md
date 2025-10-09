# EnvironmentPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the new environment | 
**key** | **str** | A project-unique key for the new environment | 
**color** | **str** | A color to indicate this environment in the UI | 
**default_ttl** | **int** | The default time (in minutes) that the PHP SDK can cache feature flag rules locally | [optional] 
**secure_mode** | **bool** | Ensures that one end user of the client-side SDK cannot inspect the variations for another end user | [optional] 
**default_track_events** | **bool** | Enables tracking detailed information for new flags by default | [optional] 
**confirm_changes** | **bool** | Requires confirmation for all flag and segment changes via the UI in this environment | [optional] 
**require_comments** | **bool** | Requires comments for all flag and segment changes via the UI in this environment | [optional] 
**tags** | **List[str]** | Tags to apply to the new environment | [optional] 
**source** | [**SourceEnv**](SourceEnv.md) |  | [optional] 
**critical** | **bool** | Whether the environment is critical | [optional] 

## Example

```python
from launchdarkly_api.models.environment_post import EnvironmentPost

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentPost from a JSON string
environment_post_instance = EnvironmentPost.from_json(json)
# print the JSON string representation of the object
print(EnvironmentPost.to_json())

# convert the object into a dict
environment_post_dict = environment_post_instance.to_dict()
# create an instance of EnvironmentPost from a dict
environment_post_from_dict = EnvironmentPost.from_dict(environment_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


