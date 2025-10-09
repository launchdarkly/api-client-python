# Rollout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variations** | [**List[WeightedVariation]**](WeightedVariation.md) |  | 
**experiment_allocation** | [**ExperimentAllocationRep**](ExperimentAllocationRep.md) |  | [optional] 
**seed** | **int** |  | [optional] 
**bucket_by** | **str** |  | [optional] 
**context_kind** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.rollout import Rollout

# TODO update the JSON string below
json = "{}"
# create an instance of Rollout from a JSON string
rollout_instance = Rollout.from_json(json)
# print the JSON string representation of the object
print(Rollout.to_json())

# convert the object into a dict
rollout_dict = rollout_instance.to_dict()
# create an instance of Rollout from a dict
rollout_from_dict = Rollout.from_dict(rollout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


