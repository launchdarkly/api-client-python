# ExpandedDirectlyLinkedSegments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpandedDirectlyLinkedSegment]**](ExpandedDirectlyLinkedSegment.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.expanded_directly_linked_segments import ExpandedDirectlyLinkedSegments

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedDirectlyLinkedSegments from a JSON string
expanded_directly_linked_segments_instance = ExpandedDirectlyLinkedSegments.from_json(json)
# print the JSON string representation of the object
print(ExpandedDirectlyLinkedSegments.to_json())

# convert the object into a dict
expanded_directly_linked_segments_dict = expanded_directly_linked_segments_instance.to_dict()
# create an instance of ExpandedDirectlyLinkedSegments from a dict
expanded_directly_linked_segments_from_dict = ExpandedDirectlyLinkedSegments.from_dict(expanded_directly_linked_segments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


