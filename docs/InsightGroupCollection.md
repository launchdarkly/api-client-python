# InsightGroupCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of insight groups | 
**items** | [**List[InsightGroup]**](InsightGroup.md) | A list of insight groups | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**metadata** | [**InsightGroupCollectionMetadata**](InsightGroupCollectionMetadata.md) |  | [optional] 
**score_metadata** | [**InsightGroupCollectionScoreMetadata**](InsightGroupCollectionScoreMetadata.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.insight_group_collection import InsightGroupCollection

# TODO update the JSON string below
json = "{}"
# create an instance of InsightGroupCollection from a JSON string
insight_group_collection_instance = InsightGroupCollection.from_json(json)
# print the JSON string representation of the object
print(InsightGroupCollection.to_json())

# convert the object into a dict
insight_group_collection_dict = insight_group_collection_instance.to_dict()
# create an instance of InsightGroupCollection from a dict
insight_group_collection_from_dict = InsightGroupCollection.from_dict(insight_group_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


