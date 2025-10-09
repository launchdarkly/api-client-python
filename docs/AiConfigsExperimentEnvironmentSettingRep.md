# AiConfigsExperimentEnvironmentSettingRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **int** |  | [optional] 
**stop_date** | **int** |  | [optional] 
**enabled_periods** | [**List[AiConfigsExperimentEnabledPeriodRep]**](AiConfigsExperimentEnabledPeriodRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.ai_configs_experiment_environment_setting_rep import AiConfigsExperimentEnvironmentSettingRep

# TODO update the JSON string below
json = "{}"
# create an instance of AiConfigsExperimentEnvironmentSettingRep from a JSON string
ai_configs_experiment_environment_setting_rep_instance = AiConfigsExperimentEnvironmentSettingRep.from_json(json)
# print the JSON string representation of the object
print(AiConfigsExperimentEnvironmentSettingRep.to_json())

# convert the object into a dict
ai_configs_experiment_environment_setting_rep_dict = ai_configs_experiment_environment_setting_rep_instance.to_dict()
# create an instance of AiConfigsExperimentEnvironmentSettingRep from a dict
ai_configs_experiment_environment_setting_rep_from_dict = AiConfigsExperimentEnvironmentSettingRep.from_dict(ai_configs_experiment_environment_setting_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


