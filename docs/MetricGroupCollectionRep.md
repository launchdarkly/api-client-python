# MetricGroupCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MetricGroupRep]**](MetricGroupRep.md) | An array of metric groups | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.metric_group_collection_rep import MetricGroupCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of MetricGroupCollectionRep from a JSON string
metric_group_collection_rep_instance = MetricGroupCollectionRep.from_json(json)
# print the JSON string representation of the object
print(MetricGroupCollectionRep.to_json())

# convert the object into a dict
metric_group_collection_rep_dict = metric_group_collection_rep_instance.to_dict()
# create an instance of MetricGroupCollectionRep from a dict
metric_group_collection_rep_from_dict = MetricGroupCollectionRep.from_dict(metric_group_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


