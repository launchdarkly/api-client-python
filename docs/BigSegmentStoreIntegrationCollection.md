# BigSegmentStoreIntegrationCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**BigSegmentStoreIntegrationCollectionLinks**](BigSegmentStoreIntegrationCollectionLinks.md) |  | 
**items** | [**List[BigSegmentStoreIntegration]**](BigSegmentStoreIntegration.md) | An array of persistent store integration configurations | 

## Example

```python
from launchdarkly_api.models.big_segment_store_integration_collection import BigSegmentStoreIntegrationCollection

# TODO update the JSON string below
json = "{}"
# create an instance of BigSegmentStoreIntegrationCollection from a JSON string
big_segment_store_integration_collection_instance = BigSegmentStoreIntegrationCollection.from_json(json)
# print the JSON string representation of the object
print(BigSegmentStoreIntegrationCollection.to_json())

# convert the object into a dict
big_segment_store_integration_collection_dict = big_segment_store_integration_collection_instance.to_dict()
# create an instance of BigSegmentStoreIntegrationCollection from a dict
big_segment_store_integration_collection_from_dict = BigSegmentStoreIntegrationCollection.from_dict(big_segment_store_integration_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


