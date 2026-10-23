# DependentReleasePhaseRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The guarded rollout release phase ID | 
**flag_key** | **str** | The guarded rollout flag key  | 
**flag_name** | **str** | The guarded rollout flag name  | 
**flag_purpose** | **str** | The guarded rollout flag purpose | [optional] 
**environment_key** | **str** | The guarded rollout environment key | 
**environment_name** | **str** | The guarded rollout environment name | 
**status** | **str** | The guarded rollout status | 
**creation_date** | **int** |  | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.dependent_release_phase_rep import DependentReleasePhaseRep

# TODO update the JSON string below
json = "{}"
# create an instance of DependentReleasePhaseRep from a JSON string
dependent_release_phase_rep_instance = DependentReleasePhaseRep.from_json(json)
# print the JSON string representation of the object
print(DependentReleasePhaseRep.to_json())

# convert the object into a dict
dependent_release_phase_rep_dict = dependent_release_phase_rep_instance.to_dict()
# create an instance of DependentReleasePhaseRep from a dict
dependent_release_phase_rep_from_dict = DependentReleasePhaseRep.from_dict(dependent_release_phase_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


