# ExperimentEnvironmentSettingRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **int** |  | [optional] 
**stop_date** | **int** |  | [optional] 
**enabled_periods** | [**List[ExperimentEnabledPeriodRep]**](ExperimentEnabledPeriodRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.experiment_environment_setting_rep import ExperimentEnvironmentSettingRep

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentEnvironmentSettingRep from a JSON string
experiment_environment_setting_rep_instance = ExperimentEnvironmentSettingRep.from_json(json)
# print the JSON string representation of the object
print(ExperimentEnvironmentSettingRep.to_json())

# convert the object into a dict
experiment_environment_setting_rep_dict = experiment_environment_setting_rep_instance.to_dict()
# create an instance of ExperimentEnvironmentSettingRep from a dict
experiment_environment_setting_rep_from_dict = ExperimentEnvironmentSettingRep.from_dict(experiment_environment_setting_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


