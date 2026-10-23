# PipelineReleaseGuardianConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitoring_window_milliseconds** | **int** | The monitoring window in milliseconds | 
**rollout_weight** | **int** | The rollout weight percentage | 
**rollback_on_regression** | **bool** | Whether or not to roll back on regression | 
**randomization_unit** | **str** | The randomization unit for the measured rollout | [optional] 

## Example

```python
from launchdarkly_api.models.pipeline_release_guardian_configuration import PipelineReleaseGuardianConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineReleaseGuardianConfiguration from a JSON string
pipeline_release_guardian_configuration_instance = PipelineReleaseGuardianConfiguration.from_json(json)
# print the JSON string representation of the object
print(PipelineReleaseGuardianConfiguration.to_json())

# convert the object into a dict
pipeline_release_guardian_configuration_dict = pipeline_release_guardian_configuration_instance.to_dict()
# create an instance of PipelineReleaseGuardianConfiguration from a dict
pipeline_release_guardian_configuration_from_dict = PipelineReleaseGuardianConfiguration.from_dict(pipeline_release_guardian_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


