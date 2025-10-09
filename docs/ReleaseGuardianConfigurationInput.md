# ReleaseGuardianConfigurationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitoring_window_milliseconds** | **int** | The monitoring window in milliseconds | [optional] 
**rollout_weight** | **int** | The rollout weight | [optional] 
**rollback_on_regression** | **bool** | Whether or not to rollback on regression | [optional] 
**randomization_unit** | **str** | The randomization unit for the measured rollout | [optional] 

## Example

```python
from launchdarkly_api.models.release_guardian_configuration_input import ReleaseGuardianConfigurationInput

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseGuardianConfigurationInput from a JSON string
release_guardian_configuration_input_instance = ReleaseGuardianConfigurationInput.from_json(json)
# print the JSON string representation of the object
print(ReleaseGuardianConfigurationInput.to_json())

# convert the object into a dict
release_guardian_configuration_input_dict = release_guardian_configuration_input_instance.to_dict()
# create an instance of ReleaseGuardianConfigurationInput from a dict
release_guardian_configuration_input_from_dict = ReleaseGuardianConfigurationInput.from_dict(release_guardian_configuration_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


