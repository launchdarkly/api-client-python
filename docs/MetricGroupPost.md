# MetricGroupPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key to reference the metric group | [optional] 
**name** | **str** | A human-friendly name for the metric group | 
**kind** | **str** | The type of the metric group | 
**description** | **str** | Description of the metric group | [optional] 
**maintainer_id** | **str** | The ID of the member who maintains this metric group | 
**tags** | **List[str]** | Tags for the metric group | 
**metrics** | [**List[MetricInMetricGroupInput]**](MetricInMetricGroupInput.md) | An ordered list of the metrics in this metric group | 

## Example

```python
from launchdarkly_api.models.metric_group_post import MetricGroupPost

# TODO update the JSON string below
json = "{}"
# create an instance of MetricGroupPost from a JSON string
metric_group_post_instance = MetricGroupPost.from_json(json)
# print the JSON string representation of the object
print(MetricGroupPost.to_json())

# convert the object into a dict
metric_group_post_dict = metric_group_post_instance.to_dict()
# create an instance of MetricGroupPost from a dict
metric_group_post_from_dict = MetricGroupPost.from_dict(metric_group_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


