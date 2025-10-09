# InsightsChartMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **Dict[str, object]** |  | 
**name** | **str** | Name of the chart | [optional] 
**metrics** | [**Dict[str, InsightsChartMetric]**](InsightsChartMetric.md) |  | [optional] 
**x_axis** | [**InsightsChartSeriesMetadataAxis**](InsightsChartSeriesMetadataAxis.md) |  | 
**y_axis** | [**InsightsChartSeriesMetadataAxis**](InsightsChartSeriesMetadataAxis.md) |  | 

## Example

```python
from launchdarkly_api.models.insights_chart_metadata import InsightsChartMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsChartMetadata from a JSON string
insights_chart_metadata_instance = InsightsChartMetadata.from_json(json)
# print the JSON string representation of the object
print(InsightsChartMetadata.to_json())

# convert the object into a dict
insights_chart_metadata_dict = insights_chart_metadata_instance.to_dict()
# create an instance of InsightsChartMetadata from a dict
insights_chart_metadata_from_dict = InsightsChartMetadata.from_dict(insights_chart_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


