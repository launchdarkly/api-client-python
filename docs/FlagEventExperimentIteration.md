# FlagEventExperimentIteration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The experiment iteration ID | 
**status** | **str** |  | 
**started_at** | **int** |  | 
**ended_at** | **int** |  | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.flag_event_experiment_iteration import FlagEventExperimentIteration

# TODO update the JSON string below
json = "{}"
# create an instance of FlagEventExperimentIteration from a JSON string
flag_event_experiment_iteration_instance = FlagEventExperimentIteration.from_json(json)
# print the JSON string representation of the object
print(FlagEventExperimentIteration.to_json())

# convert the object into a dict
flag_event_experiment_iteration_dict = flag_event_experiment_iteration_instance.to_dict()
# create an instance of FlagEventExperimentIteration from a dict
flag_event_experiment_iteration_from_dict = FlagEventExperimentIteration.from_dict(flag_event_experiment_iteration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


