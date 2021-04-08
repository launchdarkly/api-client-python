# ApprovalRequestConfigBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A name that describes the changes you would like to apply to a feature flag configuration | 
**instructions** | [**SemanticPatchInstruction**](SemanticPatchInstruction.md) |  | 
**notify_member_ids** | **list[str]** |  | 
**comment** | **str** | comment will be included in audit log item for change. | [optional] 
**execution_date** | **int** | Timestamp for when instructions will be executed | [optional] 
**operating_on_id** | **str** | ID of scheduled change to edit or delete | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


