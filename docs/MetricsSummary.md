# MetricsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.metrics_summary import MetricsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsSummary from a JSON string
metrics_summary_instance = MetricsSummary.from_json(json)
# print the JSON string representation of the object
print(MetricsSummary.to_json())

# convert the object into a dict
metrics_summary_dict = metrics_summary_instance.to_dict()
# create an instance of MetricsSummary from a dict
metrics_summary_from_dict = MetricsSummary.from_dict(metrics_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


