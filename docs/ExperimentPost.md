# ExperimentPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The experiment name | 
**description** | **str** | The experiment description | [optional] 
**maintainer_id** | **str** | The ID of the member who maintains this experiment | [optional] 
**key** | **str** | The experiment key | 
**iteration** | [**IterationInput**](IterationInput.md) |  | 
**holdout_id** | **str** | The ID of the holdout | [optional] 

## Example

```python
from launchdarkly_api.models.experiment_post import ExperimentPost

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentPost from a JSON string
experiment_post_instance = ExperimentPost.from_json(json)
# print the JSON string representation of the object
print(ExperimentPost.to_json())

# convert the object into a dict
experiment_post_dict = experiment_post_instance.to_dict()
# create an instance of ExperimentPost from a dict
experiment_post_from_dict = ExperimentPost.from_dict(experiment_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


