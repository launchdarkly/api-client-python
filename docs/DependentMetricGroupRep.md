# DependentMetricGroupRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key to reference the metric group | 
**name** | **str** | A human-friendly name for the metric group | 
**kind** | **str** | The type of the metric group | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.dependent_metric_group_rep import DependentMetricGroupRep

# TODO update the JSON string below
json = "{}"
# create an instance of DependentMetricGroupRep from a JSON string
dependent_metric_group_rep_instance = DependentMetricGroupRep.from_json(json)
# print the JSON string representation of the object
print(DependentMetricGroupRep.to_json())

# convert the object into a dict
dependent_metric_group_rep_dict = dependent_metric_group_rep_instance.to_dict()
# create an instance of DependentMetricGroupRep from a dict
dependent_metric_group_rep_from_dict = DependentMetricGroupRep.from_dict(dependent_metric_group_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


