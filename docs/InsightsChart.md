# InsightsChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**InsightsChartMetadata**](InsightsChartMetadata.md) |  | 
**series** | [**List[InsightsChartSeries]**](InsightsChartSeries.md) | Series data for the chart | 

## Example

```python
from launchdarkly_api.models.insights_chart import InsightsChart

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsChart from a JSON string
insights_chart_instance = InsightsChart.from_json(json)
# print the JSON string representation of the object
print(InsightsChart.to_json())

# convert the object into a dict
insights_chart_dict = insights_chart_instance.to_dict()
# create an instance of InsightsChart from a dict
insights_chart_from_dict = InsightsChart.from_dict(insights_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


