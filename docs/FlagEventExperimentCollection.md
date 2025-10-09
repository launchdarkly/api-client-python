# FlagEventExperimentCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of experiments | 
**items** | [**List[FlagEventExperiment]**](FlagEventExperiment.md) | A list of experiments | 

## Example

```python
from launchdarkly_api.models.flag_event_experiment_collection import FlagEventExperimentCollection

# TODO update the JSON string below
json = "{}"
# create an instance of FlagEventExperimentCollection from a JSON string
flag_event_experiment_collection_instance = FlagEventExperimentCollection.from_json(json)
# print the JSON string representation of the object
print(FlagEventExperimentCollection.to_json())

# convert the object into a dict
flag_event_experiment_collection_dict = flag_event_experiment_collection_instance.to_dict()
# create an instance of FlagEventExperimentCollection from a dict
flag_event_experiment_collection_from_dict = FlagEventExperimentCollection.from_dict(flag_event_experiment_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


