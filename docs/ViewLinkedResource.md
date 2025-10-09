# ViewLinkedResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | 
**resource_key** | **str** | Key of the resource (flag, segment, AI config or metric) | 
**environment_id** | **str** | Environment ID of the resource (only present for segments) | [optional] 
**environment_key** | **str** | Environment Key of the resource (only present for segments) | [optional] 
**resource_type** | **str** |  | 
**linked_at** | **int** |  | 
**resource_details** | [**ViewLinkedResourceDetails**](ViewLinkedResourceDetails.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.view_linked_resource import ViewLinkedResource

# TODO update the JSON string below
json = "{}"
# create an instance of ViewLinkedResource from a JSON string
view_linked_resource_instance = ViewLinkedResource.from_json(json)
# print the JSON string representation of the object
print(ViewLinkedResource.to_json())

# convert the object into a dict
view_linked_resource_dict = view_linked_resource_instance.to_dict()
# create an instance of ViewLinkedResource from a dict
view_linked_resource_from_dict = ViewLinkedResource.from_dict(view_linked_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


