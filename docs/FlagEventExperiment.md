# FlagEventExperiment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The experiment key | 
**name** | **str** | The experiment name | 
**iteration** | [**FlagEventExperimentIteration**](FlagEventExperimentIteration.md) |  | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.flag_event_experiment import FlagEventExperiment

# TODO update the JSON string below
json = "{}"
# create an instance of FlagEventExperiment from a JSON string
flag_event_experiment_instance = FlagEventExperiment.from_json(json)
# print the JSON string representation of the object
print(FlagEventExperiment.to_json())

# convert the object into a dict
flag_event_experiment_dict = flag_event_experiment_instance.to_dict()
# create an instance of FlagEventExperiment from a dict
flag_event_experiment_from_dict = FlagEventExperiment.from_dict(flag_event_experiment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


