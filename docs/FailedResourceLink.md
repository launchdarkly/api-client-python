# FailedResourceLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_key** | **str** | The key of the resource that failed to link. | 
**environment_id** | **str** | Environment ID of the resource (only present for segments) | [optional] 
**resource_type** | **str** | The type of the resource that failed to link. | 
**error_message** | **str** | The reason why linking this resource failed. | 

## Example

```python
from launchdarkly_api.models.failed_resource_link import FailedResourceLink

# TODO update the JSON string below
json = "{}"
# create an instance of FailedResourceLink from a JSON string
failed_resource_link_instance = FailedResourceLink.from_json(json)
# print the JSON string representation of the object
print(FailedResourceLink.to_json())

# convert the object into a dict
failed_resource_link_dict = failed_resource_link_instance.to_dict()
# create an instance of FailedResourceLink from a dict
failed_resource_link_from_dict = FailedResourceLink.from_dict(failed_resource_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


