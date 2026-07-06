# ExpandedExperimentRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the experiment | 
**name** | **str** | The name of the experiment | 
**access** | [**Access**](Access.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.expanded_experiment_rep import ExpandedExperimentRep

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedExperimentRep from a JSON string
expanded_experiment_rep_instance = ExpandedExperimentRep.from_json(json)
# print the JSON string representation of the object
print(ExpandedExperimentRep.to_json())

# convert the object into a dict
expanded_experiment_rep_dict = expanded_experiment_rep_instance.to_dict()
# create an instance of ExpandedExperimentRep from a dict
expanded_experiment_rep_from_dict = ExpandedExperimentRep.from_dict(expanded_experiment_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


