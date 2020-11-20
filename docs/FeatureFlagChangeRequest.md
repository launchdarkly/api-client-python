# FeatureFlagChangeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**Id**](Id.md) |  | [optional] 
**version** | **int** |  | [optional] 
**creation_date** | **int** | A unix epoch time in milliseconds specifying the date the change request was requested | [optional] 
**requestor_id** | **str** | The id of the member that requested the change | [optional] 
**review_status** | [**FeatureFlagChangeRequestReviewStatus**](FeatureFlagChangeRequestReviewStatus.md) |  | [optional] 
**status** | **str** | | Name     | Description | | --------:| ----------- | | pending  | the feature flag change request has not been applied yet | | completed| the feature flag change request has been applied successfully | | failed   | the feature flag change request has been applied but the changes were not applied successfully |  | [optional] 
**applied_by_member_id** | **str** | The id of the member that applied the change request | [optional] 
**applied_date** | **int** | A unix epoch time in milliseconds specifying the date the change request was applied | [optional] 
**current_reviews_by_member_id** | [**FeatureFlagChangeRequestReview**](FeatureFlagChangeRequestReview.md) |  | [optional] 
**all_reviews** | [**list[FeatureFlagChangeRequestReview]**](FeatureFlagChangeRequestReview.md) |  | [optional] 
**notify_member_ids** | **list[str]** |  | [optional] 
**instructions** | [**SemanticPatchInstruction**](SemanticPatchInstruction.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


