# AiConfigsLegacyExperimentRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_key** | **str** |  | [optional] 
**metric** | [**AiConfigsMetricListingRep**](AiConfigsMetricListingRep.md) |  | [optional] 
**environments** | **List[str]** |  | [optional] 
**environment_settings** | [**Dict[str, AiConfigsExperimentEnvironmentSettingRep]**](AiConfigsExperimentEnvironmentSettingRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.ai_configs_legacy_experiment_rep import AiConfigsLegacyExperimentRep

# TODO update the JSON string below
json = "{}"
# create an instance of AiConfigsLegacyExperimentRep from a JSON string
ai_configs_legacy_experiment_rep_instance = AiConfigsLegacyExperimentRep.from_json(json)
# print the JSON string representation of the object
print(AiConfigsLegacyExperimentRep.to_json())

# convert the object into a dict
ai_configs_legacy_experiment_rep_dict = ai_configs_legacy_experiment_rep_instance.to_dict()
# create an instance of AiConfigsLegacyExperimentRep from a dict
ai_configs_legacy_experiment_rep_from_dict = AiConfigsLegacyExperimentRep.from_dict(ai_configs_legacy_experiment_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


