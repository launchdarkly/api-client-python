# ExperimentAllocationRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_variation** | **int** |  | 
**can_reshuffle** | **bool** |  | 

## Example

```python
from launchdarkly_api.models.experiment_allocation_rep import ExperimentAllocationRep

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentAllocationRep from a JSON string
experiment_allocation_rep_instance = ExperimentAllocationRep.from_json(json)
# print the JSON string representation of the object
print(ExperimentAllocationRep.to_json())

# convert the object into a dict
experiment_allocation_rep_dict = experiment_allocation_rep_instance.to_dict()
# create an instance of ExperimentAllocationRep from a dict
experiment_allocation_rep_from_dict = ExperimentAllocationRep.from_dict(experiment_allocation_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


