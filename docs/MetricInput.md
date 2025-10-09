# MetricInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The metric key | 
**is_group** | **bool** | Whether this is a metric group (true) or a metric (false). Defaults to false | [optional] 
**primary** | **bool** | Deprecated, use &lt;code&gt;primarySingleMetricKey&lt;/code&gt; and &lt;code&gt;primaryFunnelKey&lt;/code&gt;. Whether this is a primary metric (true) or a secondary metric (false) | [optional] 

## Example

```python
from launchdarkly_api.models.metric_input import MetricInput

# TODO update the JSON string below
json = "{}"
# create an instance of MetricInput from a JSON string
metric_input_instance = MetricInput.from_json(json)
# print the JSON string representation of the object
print(MetricInput.to_json())

# convert the object into a dict
metric_input_dict = metric_input_instance.to_dict()
# create an instance of MetricInput from a dict
metric_input_from_dict = MetricInput.from_dict(metric_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


