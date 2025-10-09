# ExpandedLinkedResourcesFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpandedFlag]**](ExpandedFlag.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.expanded_linked_resources_flags import ExpandedLinkedResourcesFlags

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedLinkedResourcesFlags from a JSON string
expanded_linked_resources_flags_instance = ExpandedLinkedResourcesFlags.from_json(json)
# print the JSON string representation of the object
print(ExpandedLinkedResourcesFlags.to_json())

# convert the object into a dict
expanded_linked_resources_flags_dict = expanded_linked_resources_flags_instance.to_dict()
# create an instance of ExpandedLinkedResourcesFlags from a dict
expanded_linked_resources_flags_from_dict = ExpandedLinkedResourcesFlags.from_dict(expanded_linked_resources_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


