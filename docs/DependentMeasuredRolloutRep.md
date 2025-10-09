# DependentMeasuredRolloutRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The guarded rollout measured rollout Id | 
**flag_key** | **str** | The guarded rollout flag key  | 
**flag_name** | **str** | The guarded rollout flag name  | 
**environment_key** | **str** | The guarded rollout environment key | 
**environment_name** | **str** | The guarded rollout environment name | 
**status** | **str** | The guarded rollout status | 
**creation_date** | **int** |  | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.dependent_measured_rollout_rep import DependentMeasuredRolloutRep

# TODO update the JSON string below
json = "{}"
# create an instance of DependentMeasuredRolloutRep from a JSON string
dependent_measured_rollout_rep_instance = DependentMeasuredRolloutRep.from_json(json)
# print the JSON string representation of the object
print(DependentMeasuredRolloutRep.to_json())

# convert the object into a dict
dependent_measured_rollout_rep_dict = dependent_measured_rollout_rep_instance.to_dict()
# create an instance of DependentMeasuredRolloutRep from a dict
dependent_measured_rollout_rep_from_dict = DependentMeasuredRolloutRep.from_dict(dependent_measured_rollout_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


