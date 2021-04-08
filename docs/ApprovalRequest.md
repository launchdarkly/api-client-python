# ApprovalRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Id**](Id.md) |  | [optional] 
**version** | **int** |  | [optional] 
**creation_date** | **int** | A unix epoch time in milliseconds specifying the date the approval request was requested | [optional] 
**requestor_id** | **str** | The id of the member that requested the change | [optional] 
**review_status** | [**ApprovalRequestReviewStatus**](ApprovalRequestReviewStatus.md) |  | [optional] 
**status** | **str** | | Name      | Description | | ---------:| ----------- | | pending   | the approval request has not been applied yet | | completed | the approval request has been applied successfully | | scheduled | the approval request for a scheduled change has been applied successfully | | failed    | the approval request has been applied but the changes were not applied successfully |  | [optional] 
**applied_by_member_id** | **str** | The id of the member that applied the approval request | [optional] 
**applied_date** | **int** | A unix epoch time in milliseconds specifying the date the approval request was applied | [optional] 
**all_reviews** | [**list[ApprovalRequestReview]**](ApprovalRequestReview.md) |  | [optional] 
**notify_member_ids** | **list[str]** |  | [optional] 
**instructions** | [**SemanticPatchInstruction**](SemanticPatchInstruction.md) |  | [optional] 
**execution_date** | **int** | Timestamp for when instructions will be executed | [optional] 
**operating_on_id** | **str** | ID of scheduled change to edit or delete | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


