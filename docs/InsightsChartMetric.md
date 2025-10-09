# InsightsChartMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indicator** | **str** | Metric indicator tier | 
**value** | **float** | Metric value | 
**unit** | **str** | Metric unit | 
**modifier** | **str** | Metric modifier | 
**tiers** | [**List[InsightsMetricTierDefinition]**](InsightsMetricTierDefinition.md) | Metric indicator tiers | 

## Example

```python
from launchdarkly_api.models.insights_chart_metric import InsightsChartMetric

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsChartMetric from a JSON string
insights_chart_metric_instance = InsightsChartMetric.from_json(json)
# print the JSON string representation of the object
print(InsightsChartMetric.to_json())

# convert the object into a dict
insights_chart_metric_dict = insights_chart_metric_instance.to_dict()
# create an instance of InsightsChartMetric from a dict
insights_chart_metric_from_dict = InsightsChartMetric.from_dict(insights_chart_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


