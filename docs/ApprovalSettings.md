# ApprovalSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | **bool** | If approvals are required for this environment. | 
**bypass_approvals_for_pending_changes** | **bool** |  | 
**min_num_approvals** | **int** | Sets the amount of approvals required before a member can apply a change. The minimum is one and the maximum is five. | 
**can_review_own_request** | **bool** | Allow someone who makes an approval request to apply their own change. | 
**can_apply_declined_changes** | **bool** | Allow applying the change as long as at least one person has approved. | 
**service_kind** | **str** | Which service to use for managing approvals. | 
**service_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**required_approval_tags** | **[str]** | Require approval only on flags with the provided tags. Otherwise all flags will require approval. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


