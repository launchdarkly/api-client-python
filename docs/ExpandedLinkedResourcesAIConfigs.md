# ExpandedLinkedResourcesAIConfigs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpandedAIConfig]**](ExpandedAIConfig.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.expanded_linked_resources_ai_configs import ExpandedLinkedResourcesAIConfigs

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedLinkedResourcesAIConfigs from a JSON string
expanded_linked_resources_ai_configs_instance = ExpandedLinkedResourcesAIConfigs.from_json(json)
# print the JSON string representation of the object
print(ExpandedLinkedResourcesAIConfigs.to_json())

# convert the object into a dict
expanded_linked_resources_ai_configs_dict = expanded_linked_resources_ai_configs_instance.to_dict()
# create an instance of ExpandedLinkedResourcesAIConfigs from a dict
expanded_linked_resources_ai_configs_from_dict = ExpandedLinkedResourcesAIConfigs.from_dict(expanded_linked_resources_ai_configs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


