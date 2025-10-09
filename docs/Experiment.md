# Experiment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The experiment ID | [optional] 
**key** | **str** | The experiment key | 
**name** | **str** | The experiment name | 
**description** | **str** | The experiment description | [optional] 
**maintainer_id** | **str** | The ID of the member who maintains this experiment. | 
**creation_date** | **int** |  | 
**environment_key** | **str** |  | 
**archived_date** | **int** |  | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**holdout_id** | **str** | The holdout ID | [optional] 
**current_iteration** | [**IterationRep**](IterationRep.md) |  | [optional] 
**draft_iteration** | [**IterationRep**](IterationRep.md) |  | [optional] 
**previous_iterations** | [**List[IterationRep]**](IterationRep.md) | Details on the previous iterations for this experiment. | [optional] 

## Example

```python
from launchdarkly_api.models.experiment import Experiment

# TODO update the JSON string below
json = "{}"
# create an instance of Experiment from a JSON string
experiment_instance = Experiment.from_json(json)
# print the JSON string representation of the object
print(Experiment.to_json())

# convert the object into a dict
experiment_dict = experiment_instance.to_dict()
# create an instance of Experiment from a dict
experiment_from_dict = Experiment.from_dict(experiment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


