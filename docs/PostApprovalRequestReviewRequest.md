# PostApprovalRequestReviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The type of review for this approval request | [optional] 
**comment** | **str** | Optional comment about the approval request | [optional] 

## Example

```python
from launchdarkly_api.models.post_approval_request_review_request import PostApprovalRequestReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostApprovalRequestReviewRequest from a JSON string
post_approval_request_review_request_instance = PostApprovalRequestReviewRequest.from_json(json)
# print the JSON string representation of the object
print(PostApprovalRequestReviewRequest.to_json())

# convert the object into a dict
post_approval_request_review_request_dict = post_approval_request_review_request_instance.to_dict()
# create an instance of PostApprovalRequestReviewRequest from a dict
post_approval_request_review_request_from_dict = PostApprovalRequestReviewRequest.from_dict(post_approval_request_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


