# InsightGroupScores


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall** | [**InsightsMetricScore**](InsightsMetricScore.md) |  | 
**deployment_frequency** | [**InsightsMetricScore**](InsightsMetricScore.md) |  | 
**deployment_failure_rate** | [**InsightsMetricScore**](InsightsMetricScore.md) |  | 
**lead_time** | [**InsightsMetricScore**](InsightsMetricScore.md) |  | 
**impact_size** | [**InsightsMetricScore**](InsightsMetricScore.md) |  | 
**experimentation_coverage** | [**InsightsMetricScore**](InsightsMetricScore.md) |  | 
**flag_health** | [**InsightsMetricScore**](InsightsMetricScore.md) |  | 
**velocity** | [**InsightsMetricScore**](InsightsMetricScore.md) |  | 
**risk** | [**InsightsMetricScore**](InsightsMetricScore.md) |  | 
**efficiency** | [**InsightsMetricScore**](InsightsMetricScore.md) |  | 
**creation_ratio** | [**InsightsMetricScore**](InsightsMetricScore.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.insight_group_scores import InsightGroupScores

# TODO update the JSON string below
json = "{}"
# create an instance of InsightGroupScores from a JSON string
insight_group_scores_instance = InsightGroupScores.from_json(json)
# print the JSON string representation of the object
print(InsightGroupScores.to_json())

# convert the object into a dict
insight_group_scores_dict = insight_group_scores_instance.to_dict()
# create an instance of InsightGroupScores from a dict
insight_group_scores_from_dict = InsightGroupScores.from_dict(insight_group_scores_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


