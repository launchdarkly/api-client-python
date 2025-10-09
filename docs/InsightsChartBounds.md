# InsightsChartBounds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the bound | 
**value** | **int** | Value of the bound | 

## Example

```python
from launchdarkly_api.models.insights_chart_bounds import InsightsChartBounds

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsChartBounds from a JSON string
insights_chart_bounds_instance = InsightsChartBounds.from_json(json)
# print the JSON string representation of the object
print(InsightsChartBounds.to_json())

# convert the object into a dict
insights_chart_bounds_dict = insights_chart_bounds_instance.to_dict()
# create an instance of InsightsChartBounds from a dict
insights_chart_bounds_from_dict = InsightsChartBounds.from_dict(insights_chart_bounds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


