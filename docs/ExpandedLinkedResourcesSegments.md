# ExpandedLinkedResourcesSegments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpandedSegment]**](ExpandedSegment.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.expanded_linked_resources_segments import ExpandedLinkedResourcesSegments

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedLinkedResourcesSegments from a JSON string
expanded_linked_resources_segments_instance = ExpandedLinkedResourcesSegments.from_json(json)
# print the JSON string representation of the object
print(ExpandedLinkedResourcesSegments.to_json())

# convert the object into a dict
expanded_linked_resources_segments_dict = expanded_linked_resources_segments_instance.to_dict()
# create an instance of ExpandedLinkedResourcesSegments from a dict
expanded_linked_resources_segments_from_dict = ExpandedLinkedResourcesSegments.from_dict(expanded_linked_resources_segments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


