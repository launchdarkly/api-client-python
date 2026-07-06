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
**tags** | **List[str]** | Tags for the experiment | [optional] 
**methodology** | **str** | The results analysis approach. | [optional] 
**analysis_config** | [**AnalysisConfigInput**](AnalysisConfigInput.md) |  | [optional] 
**data_source** | **str** | The source of metric data in order to analyze results. Defaults to \&quot;launchdarkly\&quot; when not provided. | [optional] 
**type** | **str** | The type of experiment. | [optional] 

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


