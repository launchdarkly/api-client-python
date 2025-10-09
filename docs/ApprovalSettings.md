# ApprovalSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | **bool** | If approvals are required for this environment | 
**bypass_approvals_for_pending_changes** | **bool** | Whether to skip approvals for pending changes | 
**min_num_approvals** | **int** | Sets the amount of approvals required before a member can apply a change. The minimum is one and the maximum is five. | 
**can_review_own_request** | **bool** | Allow someone who makes an approval request to apply their own change | 
**can_apply_declined_changes** | **bool** | Allow applying the change as long as at least one person has approved | 
**auto_apply_approved_changes** | **bool** | Automatically apply changes that have been approved by all reviewers. This field is only applicable for approval services other than LaunchDarkly. | [optional] 
**service_kind** | **str** | Which service to use for managing approvals | 
**service_config** | **Dict[str, object]** |  | 
**required_approval_tags** | **List[str]** | Require approval only on flags with the provided tags. Otherwise all flags will require approval. | 
**service_kind_configuration_id** | **str** | Optional field for integration configuration ID of a custom approval integration. This is an Enterprise-only feature. | [optional] 
**resource_kind** | **str** | The kind of resource for which the approval settings apply, for example, flag or segment | [optional] 

## Example

```python
from launchdarkly_api.models.approval_settings import ApprovalSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalSettings from a JSON string
approval_settings_instance = ApprovalSettings.from_json(json)
# print the JSON string representation of the object
print(ApprovalSettings.to_json())

# convert the object into a dict
approval_settings_dict = approval_settings_instance.to_dict()
# create an instance of ApprovalSettings from a dict
approval_settings_from_dict = ApprovalSettings.from_dict(approval_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


