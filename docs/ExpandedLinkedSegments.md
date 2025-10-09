# ExpandedLinkedSegments

Details on linked segments for a view - requires passing the 'allSegments' expand field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpandedSegment]**](ExpandedSegment.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.expanded_linked_segments import ExpandedLinkedSegments

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedLinkedSegments from a JSON string
expanded_linked_segments_instance = ExpandedLinkedSegments.from_json(json)
# print the JSON string representation of the object
print(ExpandedLinkedSegments.to_json())

# convert the object into a dict
expanded_linked_segments_dict = expanded_linked_segments_instance.to_dict()
# create an instance of ExpandedLinkedSegments from a dict
expanded_linked_segments_from_dict = ExpandedLinkedSegments.from_dict(expanded_linked_segments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


