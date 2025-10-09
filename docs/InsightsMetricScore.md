# InsightsMetricScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** | The score for the metric | 
**aggregate_of** | **List[str]** | The keys of the metrics that were aggregated to calculate this score | [optional] 
**diff_vs_last_period** | **int** |  | [optional] 
**indicator** | **str** |  | 
**indicator_range** | [**InsightsMetricIndicatorRange**](InsightsMetricIndicatorRange.md) |  | 
**last_period** | [**InsightsMetricScore**](InsightsMetricScore.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.insights_metric_score import InsightsMetricScore

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsMetricScore from a JSON string
insights_metric_score_instance = InsightsMetricScore.from_json(json)
# print the JSON string representation of the object
print(InsightsMetricScore.to_json())

# convert the object into a dict
insights_metric_score_dict = insights_metric_score_instance.to_dict()
# create an instance of InsightsMetricScore from a dict
insights_metric_score_from_dict = InsightsMetricScore.from_dict(insights_metric_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


