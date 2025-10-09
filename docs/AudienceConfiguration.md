# AudienceConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_strategy** | **str** |  | 
**require_approval** | **bool** | Whether or not the audience requires approval | 
**notify_member_ids** | **List[str]** | An array of member IDs. These members are notified to review the approval request. | [optional] 
**notify_team_keys** | **List[str]** | An array of team keys. The members of these teams are notified to review the approval request. | [optional] 
**release_guardian_configuration** | [**ReleaseGuardianConfiguration**](ReleaseGuardianConfiguration.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.audience_configuration import AudienceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AudienceConfiguration from a JSON string
audience_configuration_instance = AudienceConfiguration.from_json(json)
# print the JSON string representation of the object
print(AudienceConfiguration.to_json())

# convert the object into a dict
audience_configuration_dict = audience_configuration_instance.to_dict()
# create an instance of AudienceConfiguration from a dict
audience_configuration_from_dict = AudienceConfiguration.from_dict(audience_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


