# PullRequestRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The pull request internal ID | 
**external_id** | **str** | The pull request number | 
**title** | **str** | The pull request title | 
**status** | **str** | The pull request status | 
**author** | **str** | The pull request author | 
**create_time** | **int** |  | 
**base_commit_key** | **str** | The pull request base commit key | 
**head_commit_key** | **str** | The pull request head commit key | 
**files_changed** | **int** | The number of files changed | 
**lines_added** | **int** | The number of lines added | 
**lines_deleted** | **int** | The number of lines deleted | 
**url** | **str** | The pull request URL | 
**merge_time** | **int** |  | [optional] 
**merge_commit_key** | **str** | The pull request merge commit key | [optional] 
**deployments** | [**DeploymentCollectionRep**](DeploymentCollectionRep.md) |  | [optional] 
**flag_references** | [**FlagReferenceCollectionRep**](FlagReferenceCollectionRep.md) |  | [optional] 
**lead_time** | [**PullRequestLeadTimeRep**](PullRequestLeadTimeRep.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


