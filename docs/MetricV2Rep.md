# MetricV2Rep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The metric key | 
**version_id** | **str** | The version ID of the metric | [optional] 
**name** | **str** | The metric name | 
**kind** | **str** | The kind of event the metric tracks | 
**is_numeric** | **bool** | For custom metrics, whether to track numeric changes in value against a baseline (&lt;code&gt;true&lt;/code&gt;) or to track a conversion when an end user takes an action (&lt;code&gt;false&lt;/code&gt;). | [optional] 
**unit_aggregation_type** | **str** | The type of unit aggregation to use for the metric | [optional] 
**event_key** | **str** | The event key sent with the metric. Only relevant for custom metrics. | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.metric_v2_rep import MetricV2Rep

# TODO update the JSON string below
json = "{}"
# create an instance of MetricV2Rep from a JSON string
metric_v2_rep_instance = MetricV2Rep.from_json(json)
# print the JSON string representation of the object
print(MetricV2Rep.to_json())

# convert the object into a dict
metric_v2_rep_dict = metric_v2_rep_instance.to_dict()
# create an instance of MetricV2Rep from a dict
metric_v2_rep_from_dict = MetricV2Rep.from_dict(metric_v2_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


