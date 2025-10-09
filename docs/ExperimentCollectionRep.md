# ExperimentCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Experiment]**](Experiment.md) | An array of experiments | 
**total_count** | **int** | The total number of experiments in this project and environment. Does not include legacy experiments. | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.experiment_collection_rep import ExperimentCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentCollectionRep from a JSON string
experiment_collection_rep_instance = ExperimentCollectionRep.from_json(json)
# print the JSON string representation of the object
print(ExperimentCollectionRep.to_json())

# convert the object into a dict
experiment_collection_rep_dict = experiment_collection_rep_instance.to_dict()
# create an instance of ExperimentCollectionRep from a dict
experiment_collection_rep_from_dict = ExperimentCollectionRep.from_dict(experiment_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


