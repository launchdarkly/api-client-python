# Metrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_tokens** | **int** |  | [optional] 
**output_tokens** | **int** |  | [optional] 
**total_tokens** | **int** |  | [optional] 
**generation_count** | **int** | Number of attempted generations | [optional] 
**generation_success_count** | **int** | Number of successful generations | [optional] 
**generation_error_count** | **int** | Number of generations with errors | [optional] 
**thumbs_up** | **int** |  | [optional] 
**thumbs_down** | **int** |  | [optional] 
**duration_ms** | **int** |  | [optional] 
**time_to_first_token_ms** | **int** |  | [optional] 
**satisfaction_rating** | **float** | A value between 0 and 1 representing satisfaction rating | [optional] 
**input_cost** | **float** | Cost of input tokens in USD | [optional] 
**output_cost** | **float** | Cost of output tokens in USD | [optional] 
**judge_accuracy** | **float** | Average accuracy judge score (0.0-1.0) | [optional] 
**judge_relevance** | **float** | Average relevance judge score (0.0-1.0) | [optional] 
**judge_toxicity** | **float** | Average toxicity judge score (0.0-1.0) | [optional] 

## Example

```python
from launchdarkly_api.models.metrics import Metrics

# TODO update the JSON string below
json = "{}"
# create an instance of Metrics from a JSON string
metrics_instance = Metrics.from_json(json)
# print the JSON string representation of the object
print(Metrics.to_json())

# convert the object into a dict
metrics_dict = metrics_instance.to_dict()
# create an instance of Metrics from a dict
metrics_from_dict = Metrics.from_dict(metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


