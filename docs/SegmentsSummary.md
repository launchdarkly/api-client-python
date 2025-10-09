# SegmentsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**linked_segments** | [**ExpandedDirectlyLinkedSegments**](ExpandedDirectlyLinkedSegments.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.segments_summary import SegmentsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentsSummary from a JSON string
segments_summary_instance = SegmentsSummary.from_json(json)
# print the JSON string representation of the object
print(SegmentsSummary.to_json())

# convert the object into a dict
segments_summary_dict = segments_summary_instance.to_dict()
# create an instance of SegmentsSummary from a dict
segments_summary_from_dict = SegmentsSummary.from_dict(segments_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


