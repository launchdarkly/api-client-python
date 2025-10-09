# ExperimentEnabledPeriodRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **int** |  | [optional] 
**stop_date** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.experiment_enabled_period_rep import ExperimentEnabledPeriodRep

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentEnabledPeriodRep from a JSON string
experiment_enabled_period_rep_instance = ExperimentEnabledPeriodRep.from_json(json)
# print the JSON string representation of the object
print(ExperimentEnabledPeriodRep.to_json())

# convert the object into a dict
experiment_enabled_period_rep_dict = experiment_enabled_period_rep_instance.to_dict()
# create an instance of ExperimentEnabledPeriodRep from a dict
experiment_enabled_period_rep_from_dict = ExperimentEnabledPeriodRep.from_dict(experiment_enabled_period_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


