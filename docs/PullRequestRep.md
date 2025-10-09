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
**merge_time** | **int** |  | [optional] 
**merge_commit_key** | **str** | The pull request merge commit key | [optional] 
**base_commit_key** | **str** | The pull request base commit key | 
**head_commit_key** | **str** | The pull request head commit key | 
**files_changed** | **int** | The number of files changed | 
**lines_added** | **int** | The number of lines added | 
**lines_deleted** | **int** | The number of lines deleted | 
**url** | **str** | The pull request URL | 
**deployments** | [**DeploymentCollectionRep**](DeploymentCollectionRep.md) |  | [optional] 
**flag_references** | [**FlagReferenceCollectionRep**](FlagReferenceCollectionRep.md) |  | [optional] 
**lead_time** | [**PullRequestLeadTimeRep**](PullRequestLeadTimeRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.pull_request_rep import PullRequestRep

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestRep from a JSON string
pull_request_rep_instance = PullRequestRep.from_json(json)
# print the JSON string representation of the object
print(PullRequestRep.to_json())

# convert the object into a dict
pull_request_rep_dict = pull_request_rep_instance.to_dict()
# create an instance of PullRequestRep from a dict
pull_request_rep_from_dict = PullRequestRep.from_dict(pull_request_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


