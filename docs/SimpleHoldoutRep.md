# SimpleHoldoutRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**experiments** | [**List[RelatedExperimentRep]**](RelatedExperimentRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.simple_holdout_rep import SimpleHoldoutRep

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleHoldoutRep from a JSON string
simple_holdout_rep_instance = SimpleHoldoutRep.from_json(json)
# print the JSON string representation of the object
print(SimpleHoldoutRep.to_json())

# convert the object into a dict
simple_holdout_rep_dict = simple_holdout_rep_instance.to_dict()
# create an instance of SimpleHoldoutRep from a dict
simple_holdout_rep_from_dict = SimpleHoldoutRep.from_dict(simple_holdout_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


