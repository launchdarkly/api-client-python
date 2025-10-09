# InsightsChartSeriesDataPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **int** | X-axis value | 
**y** | **int** | Y-axis value | 
**values** | **Dict[str, object]** | Additional values for the data point | [optional] 

## Example

```python
from launchdarkly_api.models.insights_chart_series_data_point import InsightsChartSeriesDataPoint

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsChartSeriesDataPoint from a JSON string
insights_chart_series_data_point_instance = InsightsChartSeriesDataPoint.from_json(json)
# print the JSON string representation of the object
print(InsightsChartSeriesDataPoint.to_json())

# convert the object into a dict
insights_chart_series_data_point_dict = insights_chart_series_data_point_instance.to_dict()
# create an instance of InsightsChartSeriesDataPoint from a dict
insights_chart_series_data_point_from_dict = InsightsChartSeriesDataPoint.from_dict(insights_chart_series_data_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


