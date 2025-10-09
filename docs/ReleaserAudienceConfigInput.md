# ReleaserAudienceConfigInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_id** | **str** | UUID of the audience. | [optional] 
**release_guardian_configuration** | [**ReleaseGuardianConfigurationInput**](ReleaseGuardianConfigurationInput.md) |  | [optional] 
**notify_member_ids** | **List[str]** | An array of member IDs. These members are notified to review the approval request. | [optional] 
**notify_team_keys** | **List[str]** | An array of team keys. The members of these teams are notified to review the approval request. | [optional] 

## Example

```python
from launchdarkly_api.models.releaser_audience_config_input import ReleaserAudienceConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaserAudienceConfigInput from a JSON string
releaser_audience_config_input_instance = ReleaserAudienceConfigInput.from_json(json)
# print the JSON string representation of the object
print(ReleaserAudienceConfigInput.to_json())

# convert the object into a dict
releaser_audience_config_input_dict = releaser_audience_config_input_instance.to_dict()
# create an instance of ReleaserAudienceConfigInput from a dict
releaser_audience_config_input_from_dict = ReleaserAudienceConfigInput.from_dict(releaser_audience_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


