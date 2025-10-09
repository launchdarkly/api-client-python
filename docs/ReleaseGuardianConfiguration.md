# ReleaseGuardianConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitoring_window_milliseconds** | **int** | The monitoring window in milliseconds | 
**rollout_weight** | **int** | The rollout weight percentage | 
**rollback_on_regression** | **bool** | Whether or not to roll back on regression | 
**randomization_unit** | **str** | The randomization unit for the measured rollout | [optional] 

## Example

```python
from launchdarkly_api.models.release_guardian_configuration import ReleaseGuardianConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseGuardianConfiguration from a JSON string
release_guardian_configuration_instance = ReleaseGuardianConfiguration.from_json(json)
# print the JSON string representation of the object
print(ReleaseGuardianConfiguration.to_json())

# convert the object into a dict
release_guardian_configuration_dict = release_guardian_configuration_instance.to_dict()
# create an instance of ReleaseGuardianConfiguration from a dict
release_guardian_configuration_from_dict = ReleaseGuardianConfiguration.from_dict(release_guardian_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


