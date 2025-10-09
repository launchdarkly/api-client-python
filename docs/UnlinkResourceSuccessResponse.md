# UnlinkResourceSuccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_count** | **int** | The number of resources successfully unlinked. | 
**failure_count** | **int** | The number of resources that failed to unlink. | 
**failed_resources** | [**List[FailedResourceLink]**](FailedResourceLink.md) | Details of resources that failed to unlink. | [optional] 

## Example

```python
from launchdarkly_api.models.unlink_resource_success_response import UnlinkResourceSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnlinkResourceSuccessResponse from a JSON string
unlink_resource_success_response_instance = UnlinkResourceSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(UnlinkResourceSuccessResponse.to_json())

# convert the object into a dict
unlink_resource_success_response_dict = unlink_resource_success_response_instance.to_dict()
# create an instance of UnlinkResourceSuccessResponse from a dict
unlink_resource_success_response_from_dict = UnlinkResourceSuccessResponse.from_dict(unlink_resource_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


