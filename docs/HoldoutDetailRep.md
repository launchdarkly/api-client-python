# HoldoutDetailRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** |  | 
**description** | **str** |  | [optional] 
**holdout_amount** | **str** | The percentage of traffic allocated to this holdout. | 
**is_dirty** | **bool** | Indicates if the holdout experiment is running and if any related experiments are running. | [optional] 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 
**base_experiment** | [**Experiment**](Experiment.md) |  | 
**related_experiments** | [**List[Experiment]**](Experiment.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.holdout_detail_rep import HoldoutDetailRep

# TODO update the JSON string below
json = "{}"
# create an instance of HoldoutDetailRep from a JSON string
holdout_detail_rep_instance = HoldoutDetailRep.from_json(json)
# print the JSON string representation of the object
print(HoldoutDetailRep.to_json())

# convert the object into a dict
holdout_detail_rep_dict = holdout_detail_rep_instance.to_dict()
# create an instance of HoldoutDetailRep from a dict
holdout_detail_rep_from_dict = HoldoutDetailRep.from_dict(holdout_detail_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


