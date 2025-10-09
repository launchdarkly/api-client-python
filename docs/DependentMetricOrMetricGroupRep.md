# DependentMetricOrMetricGroupRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key to reference the metric or metric group | 
**version_id** | **str** | The version ID of the metric or metric group | 
**name** | **str** | A human-friendly name for the metric or metric group | 
**kind** | **str** | If this is a metric, then it represents the kind of event the metric tracks. If this is a metric group, then it represents the group type | 
**is_numeric** | **bool** | For custom metrics, whether to track numeric changes in value against a baseline (&lt;code&gt;true&lt;/code&gt;) or to track a conversion when an end user takes an action (&lt;code&gt;false&lt;/code&gt;). | [optional] 
**event_key** | **str** | The event key sent with the metric. Only relevant for custom metrics. | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**is_group** | **bool** | Whether this is a metric group or a metric | 
**metrics** | [**List[MetricInGroupRep]**](MetricInGroupRep.md) | An ordered list of the metrics in this metric group | [optional] 

## Example

```python
from launchdarkly_api.models.dependent_metric_or_metric_group_rep import DependentMetricOrMetricGroupRep

# TODO update the JSON string below
json = "{}"
# create an instance of DependentMetricOrMetricGroupRep from a JSON string
dependent_metric_or_metric_group_rep_instance = DependentMetricOrMetricGroupRep.from_json(json)
# print the JSON string representation of the object
print(DependentMetricOrMetricGroupRep.to_json())

# convert the object into a dict
dependent_metric_or_metric_group_rep_dict = dependent_metric_or_metric_group_rep_instance.to_dict()
# create an instance of DependentMetricOrMetricGroupRep from a dict
dependent_metric_or_metric_group_rep_from_dict = DependentMetricOrMetricGroupRep.from_dict(dependent_metric_or_metric_group_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


