# FlagConfigApprovalRequestsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FlagConfigApprovalRequestResponse]**](FlagConfigApprovalRequestResponse.md) | An array of approval requests | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.flag_config_approval_requests_response import FlagConfigApprovalRequestsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlagConfigApprovalRequestsResponse from a JSON string
flag_config_approval_requests_response_instance = FlagConfigApprovalRequestsResponse.from_json(json)
# print the JSON string representation of the object
print(FlagConfigApprovalRequestsResponse.to_json())

# convert the object into a dict
flag_config_approval_requests_response_dict = flag_config_approval_requests_response_instance.to_dict()
# create an instance of FlagConfigApprovalRequestsResponse from a dict
flag_config_approval_requests_response_from_dict = FlagConfigApprovalRequestsResponse.from_dict(flag_config_approval_requests_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


