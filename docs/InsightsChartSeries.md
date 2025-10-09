# InsightsChartSeries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**InsightsChartSeriesMetadata**](InsightsChartSeriesMetadata.md) |  | 
**data** | [**List[InsightsChartSeriesDataPoint]**](InsightsChartSeriesDataPoint.md) | Data points for the series | 

## Example

```python
from launchdarkly_api.models.insights_chart_series import InsightsChartSeries

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsChartSeries from a JSON string
insights_chart_series_instance = InsightsChartSeries.from_json(json)
# print the JSON string representation of the object
print(InsightsChartSeries.to_json())

# convert the object into a dict
insights_chart_series_dict = insights_chart_series_instance.to_dict()
# create an instance of InsightsChartSeries from a dict
insights_chart_series_from_dict = InsightsChartSeries.from_dict(insights_chart_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


