# InsightGroupCollectionScoreMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | [**InsightPeriod**](InsightPeriod.md) |  | 
**last_period** | [**InsightPeriod**](InsightPeriod.md) |  | 

## Example

```python
from launchdarkly_api.models.insight_group_collection_score_metadata import InsightGroupCollectionScoreMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of InsightGroupCollectionScoreMetadata from a JSON string
insight_group_collection_score_metadata_instance = InsightGroupCollectionScoreMetadata.from_json(json)
# print the JSON string representation of the object
print(InsightGroupCollectionScoreMetadata.to_json())

# convert the object into a dict
insight_group_collection_score_metadata_dict = insight_group_collection_score_metadata_instance.to_dict()
# create an instance of InsightGroupCollectionScoreMetadata from a dict
insight_group_collection_score_metadata_from_dict = InsightGroupCollectionScoreMetadata.from_dict(insight_group_collection_score_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


