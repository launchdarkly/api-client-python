# ViewLinkedResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ViewsPaginatedLinks**](ViewsPaginatedLinks.md) |  | [optional] 
**items** | [**List[ViewLinkedResource]**](ViewLinkedResource.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.view_linked_resources import ViewLinkedResources

# TODO update the JSON string below
json = "{}"
# create an instance of ViewLinkedResources from a JSON string
view_linked_resources_instance = ViewLinkedResources.from_json(json)
# print the JSON string representation of the object
print(ViewLinkedResources.to_json())

# convert the object into a dict
view_linked_resources_dict = view_linked_resources_instance.to_dict()
# create an instance of ViewLinkedResources from a dict
view_linked_resources_from_dict = ViewLinkedResources.from_dict(view_linked_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


