# RepositoryRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The repository name | 
**type** | **str** | The type of repository | 
**default_branch** | **str** | The repository&#39;s default branch | 
**enabled** | **bool** | Whether or not a repository is enabled for code reference scanning | 
**version** | **int** | The version of the repository&#39;s saved information | 
**links** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**source_link** | **str** | A URL to access the repository | [optional] 
**commit_url_template** | **str** | A template for constructing a valid URL to view the commit | [optional] 
**hunk_url_template** | **str** | A template for constructing a valid URL to view the hunk | [optional] 
**branches** | [**[BranchRep]**](BranchRep.md) | An array of the repository&#39;s branches that have been scanned for code references | [optional] 
**access** | [**AccessRep**](AccessRep.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


