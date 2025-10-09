# ExpandedLinkedMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpandedMetric]**](ExpandedMetric.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.expanded_linked_metrics import ExpandedLinkedMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedLinkedMetrics from a JSON string
expanded_linked_metrics_instance = ExpandedLinkedMetrics.from_json(json)
# print the JSON string representation of the object
print(ExpandedLinkedMetrics.to_json())

# convert the object into a dict
expanded_linked_metrics_dict = expanded_linked_metrics_instance.to_dict()
# create an instance of ExpandedLinkedMetrics from a dict
expanded_linked_metrics_from_dict = ExpandedLinkedMetrics.from_dict(expanded_linked_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


