# ExpandableApprovalRequestsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpandableApprovalRequestResponse]**](ExpandableApprovalRequestResponse.md) | An array of approval requests | 
**total_count** | **int** | Total number of approval requests | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.expandable_approval_requests_response import ExpandableApprovalRequestsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandableApprovalRequestsResponse from a JSON string
expandable_approval_requests_response_instance = ExpandableApprovalRequestsResponse.from_json(json)
# print the JSON string representation of the object
print(ExpandableApprovalRequestsResponse.to_json())

# convert the object into a dict
expandable_approval_requests_response_dict = expandable_approval_requests_response_instance.to_dict()
# create an instance of ExpandableApprovalRequestsResponse from a dict
expandable_approval_requests_response_from_dict = ExpandableApprovalRequestsResponse.from_dict(expandable_approval_requests_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


