# StatisticCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | **Dict[str, List[StatisticRep]]** | A map of flag keys to a list of code reference statistics for each code repository in which the flag key appears | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.statistic_collection_rep import StatisticCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticCollectionRep from a JSON string
statistic_collection_rep_instance = StatisticCollectionRep.from_json(json)
# print the JSON string representation of the object
print(StatisticCollectionRep.to_json())

# convert the object into a dict
statistic_collection_rep_dict = statistic_collection_rep_instance.to_dict()
# create an instance of StatisticCollectionRep from a dict
statistic_collection_rep_from_dict = StatisticCollectionRep.from_dict(statistic_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


