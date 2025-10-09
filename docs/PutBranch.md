# PutBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The branch name | 
**head** | **str** | An ID representing the branch HEAD. For example, a commit SHA. | 
**update_sequence_id** | **int** | An optional ID used to prevent older data from overwriting newer data. If no sequence ID is included, the newly submitted data will always be saved. | [optional] 
**sync_time** | **int** |  | 
**references** | [**List[ReferenceRep]**](ReferenceRep.md) | An array of flag references found on the branch | [optional] 
**commit_time** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.put_branch import PutBranch

# TODO update the JSON string below
json = "{}"
# create an instance of PutBranch from a JSON string
put_branch_instance = PutBranch.from_json(json)
# print the JSON string representation of the object
print(PutBranch.to_json())

# convert the object into a dict
put_branch_dict = put_branch_instance.to_dict()
# create an instance of PutBranch from a dict
put_branch_from_dict = PutBranch.from_dict(put_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


