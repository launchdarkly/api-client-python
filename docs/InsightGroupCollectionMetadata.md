# InsightGroupCollectionMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_by_indicator** | [**InsightGroupsCountByIndicator**](InsightGroupsCountByIndicator.md) |  | 

## Example

```python
from launchdarkly_api.models.insight_group_collection_metadata import InsightGroupCollectionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of InsightGroupCollectionMetadata from a JSON string
insight_group_collection_metadata_instance = InsightGroupCollectionMetadata.from_json(json)
# print the JSON string representation of the object
print(InsightGroupCollectionMetadata.to_json())

# convert the object into a dict
insight_group_collection_metadata_dict = insight_group_collection_metadata_instance.to_dict()
# create an instance of InsightGroupCollectionMetadata from a dict
insight_group_collection_metadata_from_dict = InsightGroupCollectionMetadata.from_dict(insight_group_collection_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


