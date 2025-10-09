# AiConfigsExperimentInfoRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline_idx** | **int** |  | 
**items** | [**List[AiConfigsLegacyExperimentRep]**](AiConfigsLegacyExperimentRep.md) |  | 

## Example

```python
from launchdarkly_api.models.ai_configs_experiment_info_rep import AiConfigsExperimentInfoRep

# TODO update the JSON string below
json = "{}"
# create an instance of AiConfigsExperimentInfoRep from a JSON string
ai_configs_experiment_info_rep_instance = AiConfigsExperimentInfoRep.from_json(json)
# print the JSON string representation of the object
print(AiConfigsExperimentInfoRep.to_json())

# convert the object into a dict
ai_configs_experiment_info_rep_dict = ai_configs_experiment_info_rep_instance.to_dict()
# create an instance of AiConfigsExperimentInfoRep from a dict
ai_configs_experiment_info_rep_from_dict = AiConfigsExperimentInfoRep.from_dict(ai_configs_experiment_info_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


