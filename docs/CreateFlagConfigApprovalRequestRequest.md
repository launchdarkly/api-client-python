# CreateFlagConfigApprovalRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment describing the approval request | [optional] 
**description** | **str** | A brief description of the changes you&#39;re requesting | 
**instructions** | **List[Dict[str, object]]** |  | 
**notify_member_ids** | **List[str]** | An array of member IDs. These members are notified to review the approval request. | [optional] 
**notify_team_keys** | **List[str]** | An array of team keys. The members of these teams are notified to review the approval request. | [optional] 
**execution_date** | **int** |  | [optional] 
**operating_on_id** | **str** | The ID of a scheduled change. Include this if your &lt;code&gt;instructions&lt;/code&gt; include editing or deleting a scheduled change. | [optional] 
**integration_config** | **Dict[str, object]** |  | [optional] 

## Example

```python
from launchdarkly_api.models.create_flag_config_approval_request_request import CreateFlagConfigApprovalRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFlagConfigApprovalRequestRequest from a JSON string
create_flag_config_approval_request_request_instance = CreateFlagConfigApprovalRequestRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFlagConfigApprovalRequestRequest.to_json())

# convert the object into a dict
create_flag_config_approval_request_request_dict = create_flag_config_approval_request_request_instance.to_dict()
# create an instance of CreateFlagConfigApprovalRequestRequest from a dict
create_flag_config_approval_request_request_from_dict = CreateFlagConfigApprovalRequestRequest.from_dict(create_flag_config_approval_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


