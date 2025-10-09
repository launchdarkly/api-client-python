# ExpandedLinkedResourcesMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpandedMetric]**](ExpandedMetric.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.expanded_linked_resources_metrics import ExpandedLinkedResourcesMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedLinkedResourcesMetrics from a JSON string
expanded_linked_resources_metrics_instance = ExpandedLinkedResourcesMetrics.from_json(json)
# print the JSON string representation of the object
print(ExpandedLinkedResourcesMetrics.to_json())

# convert the object into a dict
expanded_linked_resources_metrics_dict = expanded_linked_resources_metrics_instance.to_dict()
# create an instance of ExpandedLinkedResourcesMetrics from a dict
expanded_linked_resources_metrics_from_dict = ExpandedLinkedResourcesMetrics.from_dict(expanded_linked_resources_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


