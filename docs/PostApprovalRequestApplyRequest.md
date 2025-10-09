# PostApprovalRequestApplyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment about the approval request | [optional] 

## Example

```python
from launchdarkly_api.models.post_approval_request_apply_request import PostApprovalRequestApplyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostApprovalRequestApplyRequest from a JSON string
post_approval_request_apply_request_instance = PostApprovalRequestApplyRequest.from_json(json)
# print the JSON string representation of the object
print(PostApprovalRequestApplyRequest.to_json())

# convert the object into a dict
post_approval_request_apply_request_dict = post_approval_request_apply_request_instance.to_dict()
# create an instance of PostApprovalRequestApplyRequest from a dict
post_approval_request_apply_request_from_dict = PostApprovalRequestApplyRequest.from_dict(post_approval_request_apply_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


