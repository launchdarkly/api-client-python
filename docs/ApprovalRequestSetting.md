# ApprovalRequestSetting

Configuration that controls how changes to a resource are gated by approvals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | **bool** | If approvals are required for this environment | 
**bypass_approvals_for_pending_changes** | **bool** | Whether to skip approvals for pending changes | 
**min_num_approvals** | **int** | Sets the amount of approvals required before a member can apply a change. The minimum is one and the maximum is five.  | 
**can_review_own_request** | **bool** | Allow someone who makes an approval request to apply their own change | 
**can_apply_declined_changes** | **bool** | Allow applying the change as long as at least one person has approved | 
**auto_apply_approved_changes** | **bool** | Automatically apply changes that have been approved by all reviewers. This field is only applicable for approval services other than LaunchDarkly.  | [optional] 
**service_kind** | **str** | Which service to use for managing approvals | 
**service_config** | **Dict[str, object]** | Arbitrary service-specific configuration | 
**required_approval_tags** | **List[str]** | Require approval only on flags with the provided tags. Otherwise all flags will require approval.  | 
**service_kind_configuration_id** | **str** | Optional integration configuration ID of a custom approval integration. This is an Enterprise-only feature.  | [optional] 

## Example

```python
from launchdarkly_api.models.approval_request_setting import ApprovalRequestSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalRequestSetting from a JSON string
approval_request_setting_instance = ApprovalRequestSetting.from_json(json)
# print the JSON string representation of the object
print(ApprovalRequestSetting.to_json())

# convert the object into a dict
approval_request_setting_dict = approval_request_setting_instance.to_dict()
# create an instance of ApprovalRequestSetting from a dict
approval_request_setting_from_dict = ApprovalRequestSetting.from_dict(approval_request_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


