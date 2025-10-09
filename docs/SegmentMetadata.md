# SegmentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env_id** | **str** |  | [optional] 
**segment_id** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**included_count** | **int** |  | [optional] 
**excluded_count** | **int** |  | [optional] 
**last_modified** | **int** |  | [optional] 
**deleted** | **bool** |  | [optional] 

## Example

```python
from launchdarkly_api.models.segment_metadata import SegmentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentMetadata from a JSON string
segment_metadata_instance = SegmentMetadata.from_json(json)
# print the JSON string representation of the object
print(SegmentMetadata.to_json())

# convert the object into a dict
segment_metadata_dict = segment_metadata_instance.to_dict()
# create an instance of SegmentMetadata from a dict
segment_metadata_from_dict = SegmentMetadata.from_dict(segment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


