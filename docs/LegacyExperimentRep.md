# LegacyExperimentRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_key** | **str** |  | [optional] 
**metric** | [**MetricListingRep**](MetricListingRep.md) |  | [optional] 
**environments** | **List[str]** |  | [optional] 
**environment_settings** | [**Dict[str, ExperimentEnvironmentSettingRep]**](ExperimentEnvironmentSettingRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.legacy_experiment_rep import LegacyExperimentRep

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyExperimentRep from a JSON string
legacy_experiment_rep_instance = LegacyExperimentRep.from_json(json)
# print the JSON string representation of the object
print(LegacyExperimentRep.to_json())

# convert the object into a dict
legacy_experiment_rep_dict = legacy_experiment_rep_instance.to_dict()
# create an instance of LegacyExperimentRep from a dict
legacy_experiment_rep_from_dict = LegacyExperimentRep.from_dict(legacy_experiment_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


