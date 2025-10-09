# ExperimentInfoRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline_idx** | **int** |  | 
**items** | [**List[LegacyExperimentRep]**](LegacyExperimentRep.md) |  | 

## Example

```python
from launchdarkly_api.models.experiment_info_rep import ExperimentInfoRep

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentInfoRep from a JSON string
experiment_info_rep_instance = ExperimentInfoRep.from_json(json)
# print the JSON string representation of the object
print(ExperimentInfoRep.to_json())

# convert the object into a dict
experiment_info_rep_dict = experiment_info_rep_instance.to_dict()
# create an instance of ExperimentInfoRep from a dict
experiment_info_rep_from_dict = ExperimentInfoRep.from_dict(experiment_info_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


