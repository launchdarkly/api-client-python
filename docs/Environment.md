# Environment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**id** | **str** | The ID for the environment. Use this as the client-side ID for authorization in some client-side SDKs, and to associate LaunchDarkly environments with CDN integrations in edge SDKs. | 
**key** | **str** | A project-unique key for the new environment | 
**name** | **str** | A human-friendly name for the new environment | 
**api_key** | **str** | The SDK key for the environment. Use this for authorization in server-side SDKs. | 
**mobile_key** | **str** | The mobile key for the environment. Use this for authorization in mobile SDKs. | 
**color** | **str** | The color used to indicate this environment in the UI | 
**default_ttl** | **int** | The default time (in minutes) that the PHP SDK can cache feature flag rules locally | 
**secure_mode** | **bool** | Ensures that one end user of the client-side SDK cannot inspect the variations for another end user | 
**access** | [**Access**](Access.md) |  | [optional] 
**default_track_events** | **bool** | Enables tracking detailed information for new flags by default | 
**require_comments** | **bool** | Whether members who modify flags and segments through the LaunchDarkly user interface are required to add a comment | 
**confirm_changes** | **bool** | Whether members who modify flags and segments through the LaunchDarkly user interface are required to confirm those changes | 
**tags** | **List[str]** | A list of tags for this environment | 
**approval_settings** | [**ApprovalSettings**](ApprovalSettings.md) |  | [optional] 
**resource_approval_settings** | [**Dict[str, ApprovalSettings]**](ApprovalSettings.md) | Details on the approval settings for this environment for each resource kind | [optional] 
**critical** | **bool** | Whether the environment is critical | 

## Example

```python
from launchdarkly_api.models.environment import Environment

# TODO update the JSON string below
json = "{}"
# create an instance of Environment from a JSON string
environment_instance = Environment.from_json(json)
# print the JSON string representation of the object
print(Environment.to_json())

# convert the object into a dict
environment_dict = environment_instance.to_dict()
# create an instance of Environment from a dict
environment_from_dict = Environment.from_dict(environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


