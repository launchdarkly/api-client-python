# RepositoryRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The repository name | 
**source_link** | **str** | A URL to access the repository | [optional] 
**commit_url_template** | **str** | A template for constructing a valid URL to view the commit | [optional] 
**hunk_url_template** | **str** | A template for constructing a valid URL to view the hunk | [optional] 
**type** | **str** | The type of repository | 
**default_branch** | **str** | The repository&#39;s default branch | 
**enabled** | **bool** | Whether or not a repository is enabled for code reference scanning | 
**version** | **int** | The version of the repository&#39;s saved information | 
**branches** | [**List[BranchRep]**](BranchRep.md) | An array of the repository&#39;s branches that have been scanned for code references | [optional] 
**links** | **Dict[str, object]** |  | 
**access** | [**Access**](Access.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.repository_rep import RepositoryRep

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRep from a JSON string
repository_rep_instance = RepositoryRep.from_json(json)
# print the JSON string representation of the object
print(RepositoryRep.to_json())

# convert the object into a dict
repository_rep_dict = repository_rep_instance.to_dict()
# create an instance of RepositoryRep from a dict
repository_rep_from_dict = RepositoryRep.from_dict(repository_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


