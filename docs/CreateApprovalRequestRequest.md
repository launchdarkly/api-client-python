# CreateApprovalRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | String representation of the resource specifier | 
**comment** | **str** | Optional comment describing the approval request | [optional] 
**description** | **str** | A brief description of the changes you&#39;re requesting | 
**instructions** | **List[Dict[str, object]]** |  | 
**notify_member_ids** | **List[str]** | An array of member IDs. These members are notified to review the approval request. | [optional] 
**notify_team_keys** | **List[str]** | An array of team keys. The members of these teams are notified to review the approval request. | [optional] 
**integration_config** | **Dict[str, object]** |  | [optional] 

## Example

```python
from launchdarkly_api.models.create_approval_request_request import CreateApprovalRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApprovalRequestRequest from a JSON string
create_approval_request_request_instance = CreateApprovalRequestRequest.from_json(json)
# print the JSON string representation of the object
print(CreateApprovalRequestRequest.to_json())

# convert the object into a dict
create_approval_request_request_dict = create_approval_request_request_instance.to_dict()
# create an instance of CreateApprovalRequestRequest from a dict
create_approval_request_request_from_dict = CreateApprovalRequestRequest.from_dict(create_approval_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


