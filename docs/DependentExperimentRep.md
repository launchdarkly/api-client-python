# DependentExperimentRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The experiment key | 
**name** | **str** | The experiment name | 
**environment_id** | **str** | The environment ID | 
**environment_key** | **str** | The environment key | 
**creation_date** | **int** |  | 
**archived_date** | **int** |  | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.dependent_experiment_rep import DependentExperimentRep

# TODO update the JSON string below
json = "{}"
# create an instance of DependentExperimentRep from a JSON string
dependent_experiment_rep_instance = DependentExperimentRep.from_json(json)
# print the JSON string representation of the object
print(DependentExperimentRep.to_json())

# convert the object into a dict
dependent_experiment_rep_dict = dependent_experiment_rep_instance.to_dict()
# create an instance of DependentExperimentRep from a dict
dependent_experiment_rep_from_dict = DependentExperimentRep.from_dict(dependent_experiment_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


