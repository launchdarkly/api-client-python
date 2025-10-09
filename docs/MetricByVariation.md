# MetricByVariation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation_key** | **str** |  | [optional] 
**metrics** | [**Metrics**](Metrics.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.metric_by_variation import MetricByVariation

# TODO update the JSON string below
json = "{}"
# create an instance of MetricByVariation from a JSON string
metric_by_variation_instance = MetricByVariation.from_json(json)
# print the JSON string representation of the object
print(MetricByVariation.to_json())

# convert the object into a dict
metric_by_variation_dict = metric_by_variation_instance.to_dict()
# create an instance of MetricByVariation from a dict
metric_by_variation_from_dict = MetricByVariation.from_dict(metric_by_variation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


