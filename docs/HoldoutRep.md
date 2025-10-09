# HoldoutRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** |  | 
**description** | **str** |  | [optional] 
**holdout_amount** | **str** | The percentage of traffic allocated to this holdout. | 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 
**base_experiment** | [**Experiment**](Experiment.md) |  | 
**experiments** | [**List[RelatedExperimentRep]**](RelatedExperimentRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.holdout_rep import HoldoutRep

# TODO update the JSON string below
json = "{}"
# create an instance of HoldoutRep from a JSON string
holdout_rep_instance = HoldoutRep.from_json(json)
# print the JSON string representation of the object
print(HoldoutRep.to_json())

# convert the object into a dict
holdout_rep_dict = holdout_rep_instance.to_dict()
# create an instance of HoldoutRep from a dict
holdout_rep_from_dict = HoldoutRep.from_dict(holdout_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


