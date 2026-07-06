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
**methodology** | **str** | The results analysis approach. | [optional] 
**data_source** | **str** | The source of metric data in order to analyze results. Defaults to \&quot;launchdarkly\&quot; when not provided. | [optional] 
**archived_date** | **int** |  | [optional] 
**tags** | **List[str]** | Tags for the experiment | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**holdout_id** | **str** | The holdout ID | [optional] 
**current_iteration** | [**IterationRep**](IterationRep.md) |  | [optional] 
**type** | **str** | The experiment type | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**draft_iteration** | [**IterationRep**](IterationRep.md) |  | [optional] 
**previous_iterations** | [**List[IterationRep]**](IterationRep.md) | Details on the previous iterations for this experiment. | [optional] 
**analysis_config** | [**AnalysisConfigRep**](AnalysisConfigRep.md) |  | [optional] 
**mutable_fields_by_status** | [**MutableFieldsByStatusRep**](MutableFieldsByStatusRep.md) |  | [optional] 

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


