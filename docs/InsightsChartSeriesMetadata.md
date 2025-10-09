# InsightsChartSeriesMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the series | 
**count** | **int** | Aggregate count of the series values | [optional] 
**bounds** | [**List[InsightsChartBounds]**](InsightsChartBounds.md) | Bounds for the series data | [optional] 

## Example

```python
from launchdarkly_api.models.insights_chart_series_metadata import InsightsChartSeriesMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsChartSeriesMetadata from a JSON string
insights_chart_series_metadata_instance = InsightsChartSeriesMetadata.from_json(json)
# print the JSON string representation of the object
print(InsightsChartSeriesMetadata.to_json())

# convert the object into a dict
insights_chart_series_metadata_dict = insights_chart_series_metadata_instance.to_dict()
# create an instance of InsightsChartSeriesMetadata from a dict
insights_chart_series_metadata_from_dict = InsightsChartSeriesMetadata.from_dict(insights_chart_series_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


