# ExpandedLinkedResources

Details on linked resources for a view - requires passing the 'allResources' expand field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**ExpandedLinkedResourcesItems**](ExpandedLinkedResourcesItems.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.expanded_linked_resources import ExpandedLinkedResources

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedLinkedResources from a JSON string
expanded_linked_resources_instance = ExpandedLinkedResources.from_json(json)
# print the JSON string representation of the object
print(ExpandedLinkedResources.to_json())

# convert the object into a dict
expanded_linked_resources_dict = expanded_linked_resources_instance.to_dict()
# create an instance of ExpandedLinkedResources from a dict
expanded_linked_resources_from_dict = ExpandedLinkedResources.from_dict(expanded_linked_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


