# InsightsMetricIndicatorRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** | The minimum value for the indicator range | 
**max** | **int** | The maximum value for the indicator range | 

## Example

```python
from launchdarkly_api.models.insights_metric_indicator_range import InsightsMetricIndicatorRange

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsMetricIndicatorRange from a JSON string
insights_metric_indicator_range_instance = InsightsMetricIndicatorRange.from_json(json)
# print the JSON string representation of the object
print(InsightsMetricIndicatorRange.to_json())

# convert the object into a dict
insights_metric_indicator_range_dict = insights_metric_indicator_range_instance.to_dict()
# create an instance of InsightsMetricIndicatorRange from a dict
insights_metric_indicator_range_from_dict = InsightsMetricIndicatorRange.from_dict(insights_metric_indicator_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


