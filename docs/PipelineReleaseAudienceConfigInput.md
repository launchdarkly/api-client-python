# PipelineReleaseAudienceConfigInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_id** | **str** | UUID of the audience. | [optional] 
**release_guardian_configuration** | [**PipelineReleaseGuardianConfigurationInput**](PipelineReleaseGuardianConfigurationInput.md) |  | [optional] 
**notify_member_ids** | **List[str]** | An array of member IDs. These members are notified to review the approval request. | [optional] 
**notify_team_keys** | **List[str]** | An array of team keys. The members of these teams are notified to review the approval request. | [optional] 

## Example

```python
from launchdarkly_api.models.pipeline_release_audience_config_input import PipelineReleaseAudienceConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineReleaseAudienceConfigInput from a JSON string
pipeline_release_audience_config_input_instance = PipelineReleaseAudienceConfigInput.from_json(json)
# print the JSON string representation of the object
print(PipelineReleaseAudienceConfigInput.to_json())

# convert the object into a dict
pipeline_release_audience_config_input_dict = pipeline_release_audience_config_input_instance.to_dict()
# create an instance of PipelineReleaseAudienceConfigInput from a dict
pipeline_release_audience_config_input_from_dict = PipelineReleaseAudienceConfigInput.from_dict(pipeline_release_audience_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


