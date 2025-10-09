# ApprovalRequestSettingsPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_apply_approved_changes** | **bool** | Automatically apply changes that have been approved by all reviewers. This field is only applicable for approval services other than LaunchDarkly.  | [optional] 
**bypass_approvals_for_pending_changes** | **bool** | Whether to skip approvals for pending changes | [optional] 
**can_apply_declined_changes** | **bool** | Allow applying the change as long as at least one person has approved | [optional] 
**can_review_own_request** | **bool** | Allow someone who makes an approval request to apply their own change | [optional] 
**environment_key** | **str** |  | 
**min_num_approvals** | **int** | Sets the amount of approvals required before a member can apply a change. The minimum is one and the maximum is five.  | [optional] 
**required** | **bool** | If approvals are required for this environment | [optional] 
**required_approval_tags** | **List[str]** | Require approval only on flags with the provided tags. Otherwise all flags will require approval.  | [optional] 
**resource_kind** | **str** |  | 
**service_config** | **Dict[str, object]** | Arbitrary service-specific configuration | [optional] 
**service_kind** | **str** | Which service to use for managing approvals | [optional] 
**service_kind_configuration_id** | **str** | Optional integration configuration ID of a custom approval integration. This is an Enterprise-only feature.  | [optional] 

## Example

```python
from launchdarkly_api.models.approval_request_settings_patch import ApprovalRequestSettingsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalRequestSettingsPatch from a JSON string
approval_request_settings_patch_instance = ApprovalRequestSettingsPatch.from_json(json)
# print the JSON string representation of the object
print(ApprovalRequestSettingsPatch.to_json())

# convert the object into a dict
approval_request_settings_patch_dict = approval_request_settings_patch_instance.to_dict()
# create an instance of ApprovalRequestSettingsPatch from a dict
approval_request_settings_patch_from_dict = ApprovalRequestSettingsPatch.from_dict(approval_request_settings_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


