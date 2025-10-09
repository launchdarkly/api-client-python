# InsightsMetricTierDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indicator** | **str** | Metric indicator tier | 
**description** | **str** | Metric indicator description | 

## Example

```python
from launchdarkly_api.models.insights_metric_tier_definition import InsightsMetricTierDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsMetricTierDefinition from a JSON string
insights_metric_tier_definition_instance = InsightsMetricTierDefinition.from_json(json)
# print the JSON string representation of the object
print(InsightsMetricTierDefinition.to_json())

# convert the object into a dict
insights_metric_tier_definition_dict = insights_metric_tier_definition_instance.to_dict()
# create an instance of InsightsMetricTierDefinition from a dict
insights_metric_tier_definition_from_dict = InsightsMetricTierDefinition.from_dict(insights_metric_tier_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


