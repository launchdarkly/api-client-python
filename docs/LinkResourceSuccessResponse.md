# LinkResourceSuccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_count** | **int** | The number of resources successfully linked. | 
**failure_count** | **int** | The number of resources that failed to link. | 
**linked_resources** | [**ViewLinkedResources**](ViewLinkedResources.md) |  | [optional] 
**failed_resources** | [**List[FailedResourceLink]**](FailedResourceLink.md) | Details of resources that failed to link. | [optional] 

## Example

```python
from launchdarkly_api.models.link_resource_success_response import LinkResourceSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkResourceSuccessResponse from a JSON string
link_resource_success_response_instance = LinkResourceSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(LinkResourceSuccessResponse.to_json())

# convert the object into a dict
link_resource_success_response_dict = link_resource_success_response_instance.to_dict()
# create an instance of LinkResourceSuccessResponse from a dict
link_resource_success_response_from_dict = LinkResourceSuccessResponse.from_dict(link_resource_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


