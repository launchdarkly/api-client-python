# MetricCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MetricListingRep]**](MetricListingRep.md) | An array of metrics | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.metric_collection_rep import MetricCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of MetricCollectionRep from a JSON string
metric_collection_rep_instance = MetricCollectionRep.from_json(json)
# print the JSON string representation of the object
print(MetricCollectionRep.to_json())

# convert the object into a dict
metric_collection_rep_dict = metric_collection_rep_instance.to_dict()
# create an instance of MetricCollectionRep from a dict
metric_collection_rep_from_dict = MetricCollectionRep.from_dict(metric_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


