# Environment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{str: (Link,)}**](Link.md) | Links to other resources within the API. Includes the URL and content type of those resources | 
**id** | **str** |  | 
**key** | **str** | A project-unique key for the new environment. | 
**name** | **str** | A human-friendly name for the new environment. | 
**api_key** | **str** | API key to use with client-side SDKs. | 
**mobile_key** | **str** | API key to use with mobile SDKs. | 
**color** | **str** | The color used to indicate this environment in the UI. | 
**default_ttl** | **int** | The default time (in minutes) that the PHP SDK can cache feature flag rules locally. | 
**secure_mode** | **bool** | Ensures that one end user of the client-side SDK cannot inspect the variations for another end user. | 
**default_track_events** | **bool** | Enables tracking detailed information for new flags by default. | 
**require_comments** | **bool** | Whether members who modify flags and segments through the LaunchDarkly user interface are required to add a comment | 
**confirm_changes** | **bool** | Whether members who modify flags and segments through the LaunchDarkly user interface are required to confirm those changes | 
**tags** | **[str]** | A list of tags for this environment | 
**approval_settings** | [**ApprovalSettings**](ApprovalSettings.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


