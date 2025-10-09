# MetricInMetricGroupInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The metric key | 
**name_in_group** | **str** | Name of the metric when used within the associated metric group. Can be different from the original name of the metric | 

## Example

```python
from launchdarkly_api.models.metric_in_metric_group_input import MetricInMetricGroupInput

# TODO update the JSON string below
json = "{}"
# create an instance of MetricInMetricGroupInput from a JSON string
metric_in_metric_group_input_instance = MetricInMetricGroupInput.from_json(json)
# print the JSON string representation of the object
print(MetricInMetricGroupInput.to_json())

# convert the object into a dict
metric_in_metric_group_input_dict = metric_in_metric_group_input_instance.to_dict()
# create an instance of MetricInMetricGroupInput from a dict
metric_in_metric_group_input_from_dict = MetricInMetricGroupInput.from_dict(metric_in_metric_group_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


