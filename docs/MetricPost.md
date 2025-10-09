# MetricPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key to reference the metric | 
**name** | **str** | A human-friendly name for the metric | [optional] 
**description** | **str** | Description of the metric | [optional] 
**kind** | **str** | The kind of event your metric will track | 
**selector** | **str** | One or more CSS selectors. Required for click metrics only. | [optional] 
**urls** | [**List[UrlPost]**](UrlPost.md) | One or more target URLs. Required for click and pageview metrics only. | [optional] 
**is_numeric** | **bool** | Whether to track numeric changes in value against a baseline (&lt;code&gt;true&lt;/code&gt;) or to track a conversion when an end user takes an action (&lt;code&gt;false&lt;/code&gt;). Required for custom metrics only. | [optional] 
**unit** | **str** | The unit of measure. Applicable for numeric custom metrics only. | [optional] 
**event_key** | **str** | The event key to use in your code. Required for custom conversion/binary and custom numeric metrics only. | [optional] 
**success_criteria** | **str** | Success criteria. Required for custom numeric metrics, optional for custom conversion metrics. | [optional] 
**tags** | **List[str]** | Tags for the metric | [optional] 
**randomization_units** | **List[str]** | An array of randomization units allowed for this metric | [optional] 
**maintainer_id** | **str** | The ID of the member who maintains this metric | [optional] 
**unit_aggregation_type** | **str** | The method by which multiple unit event values are aggregated | [optional] 
**analysis_type** | **str** | The method for analyzing metric events | [optional] 
**percentile_value** | **int** | The percentile for the analysis method. An integer denoting the target percentile between 0 and 100. Required when &lt;code&gt;analysisType&lt;/code&gt; is &lt;code&gt;percentile&lt;/code&gt;. | [optional] 
**event_default** | [**MetricEventDefaultRep**](MetricEventDefaultRep.md) |  | [optional] 
**data_source** | [**MetricDataSourceRefRep**](MetricDataSourceRefRep.md) |  | [optional] 
**filters** | [**EventFilter**](EventFilter.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.metric_post import MetricPost

# TODO update the JSON string below
json = "{}"
# create an instance of MetricPost from a JSON string
metric_post_instance = MetricPost.from_json(json)
# print the JSON string representation of the object
print(MetricPost.to_json())

# convert the object into a dict
metric_post_dict = metric_post_instance.to_dict()
# create an instance of MetricPost from a dict
metric_post_from_dict = MetricPost.from_dict(metric_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


