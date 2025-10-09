# ExpandedDirectlyLinkedFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpandedDirectlyLinkedFlag]**](ExpandedDirectlyLinkedFlag.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.expanded_directly_linked_flags import ExpandedDirectlyLinkedFlags

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedDirectlyLinkedFlags from a JSON string
expanded_directly_linked_flags_instance = ExpandedDirectlyLinkedFlags.from_json(json)
# print the JSON string representation of the object
print(ExpandedDirectlyLinkedFlags.to_json())

# convert the object into a dict
expanded_directly_linked_flags_dict = expanded_directly_linked_flags_instance.to_dict()
# create an instance of ExpandedDirectlyLinkedFlags from a dict
expanded_directly_linked_flags_from_dict = ExpandedDirectlyLinkedFlags.from_dict(expanded_directly_linked_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


