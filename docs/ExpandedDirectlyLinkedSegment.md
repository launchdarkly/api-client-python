# ExpandedDirectlyLinkedSegment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**name** | **str** |  | 
**environment_id** | **str** |  | 
**links** | [**ViewsSelfLink**](ViewsSelfLink.md) |  | 

## Example

```python
from launchdarkly_api.models.expanded_directly_linked_segment import ExpandedDirectlyLinkedSegment

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedDirectlyLinkedSegment from a JSON string
expanded_directly_linked_segment_instance = ExpandedDirectlyLinkedSegment.from_json(json)
# print the JSON string representation of the object
print(ExpandedDirectlyLinkedSegment.to_json())

# convert the object into a dict
expanded_directly_linked_segment_dict = expanded_directly_linked_segment_instance.to_dict()
# create an instance of ExpandedDirectlyLinkedSegment from a dict
expanded_directly_linked_segment_from_dict = ExpandedDirectlyLinkedSegment.from_dict(expanded_directly_linked_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


