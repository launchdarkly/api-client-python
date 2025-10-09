# DependentMetricGroupRepWithMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key to reference the metric group | 
**name** | **str** | A human-friendly name for the metric group | 
**kind** | **str** | The type of the metric group | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**metrics** | [**List[MetricInGroupRep]**](MetricInGroupRep.md) | The metrics in the metric group | [optional] 

## Example

```python
from launchdarkly_api.models.dependent_metric_group_rep_with_metrics import DependentMetricGroupRepWithMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of DependentMetricGroupRepWithMetrics from a JSON string
dependent_metric_group_rep_with_metrics_instance = DependentMetricGroupRepWithMetrics.from_json(json)
# print the JSON string representation of the object
print(DependentMetricGroupRepWithMetrics.to_json())

# convert the object into a dict
dependent_metric_group_rep_with_metrics_dict = dependent_metric_group_rep_with_metrics_instance.to_dict()
# create an instance of DependentMetricGroupRepWithMetrics from a dict
dependent_metric_group_rep_with_metrics_from_dict = DependentMetricGroupRepWithMetrics.from_dict(dependent_metric_group_rep_with_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


