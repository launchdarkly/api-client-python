# ExpandedLinkedResourcesItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | [**ExpandedLinkedResourcesFlags**](ExpandedLinkedResourcesFlags.md) |  | 
**segments** | [**ExpandedLinkedResourcesSegments**](ExpandedLinkedResourcesSegments.md) |  | [optional] 
**ai_configs** | [**ExpandedLinkedResourcesAIConfigs**](ExpandedLinkedResourcesAIConfigs.md) |  | [optional] 
**metrics** | [**ExpandedLinkedResourcesMetrics**](ExpandedLinkedResourcesMetrics.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.expanded_linked_resources_items import ExpandedLinkedResourcesItems

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedLinkedResourcesItems from a JSON string
expanded_linked_resources_items_instance = ExpandedLinkedResourcesItems.from_json(json)
# print the JSON string representation of the object
print(ExpandedLinkedResourcesItems.to_json())

# convert the object into a dict
expanded_linked_resources_items_dict = expanded_linked_resources_items_instance.to_dict()
# create an instance of ExpandedLinkedResourcesItems from a dict
expanded_linked_resources_items_from_dict = ExpandedLinkedResourcesItems.from_dict(expanded_linked_resources_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


