# MetricInGroupRep


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
**name_in_group** | **str** | Name of the metric when used within the associated metric group. Can be different from the original name of the metric. Required if and only if the metric group is a &lt;code&gt;funnel&lt;/code&gt;. | [optional] 
**randomization_units** | **List[str]** | The randomization units for the metric | [optional] 

## Example

```python
from launchdarkly_api.models.metric_in_group_rep import MetricInGroupRep

# TODO update the JSON string below
json = "{}"
# create an instance of MetricInGroupRep from a JSON string
metric_in_group_rep_instance = MetricInGroupRep.from_json(json)
# print the JSON string representation of the object
print(MetricInGroupRep.to_json())

# convert the object into a dict
metric_in_group_rep_dict = metric_in_group_rep_instance.to_dict()
# create an instance of MetricInGroupRep from a dict
metric_in_group_rep_from_dict = MetricInGroupRep.from_dict(metric_in_group_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


