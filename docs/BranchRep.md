# BranchRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The branch name | 
**head** | **str** | An ID representing the branch HEAD. For example, a commit SHA. | 
**update_sequence_id** | **int** | An optional ID used to prevent older data from overwriting newer data | [optional] 
**sync_time** | **int** |  | 
**references** | [**List[ReferenceRep]**](ReferenceRep.md) | An array of flag references found on the branch | [optional] 
**links** | **Dict[str, object]** | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.branch_rep import BranchRep

# TODO update the JSON string below
json = "{}"
# create an instance of BranchRep from a JSON string
branch_rep_instance = BranchRep.from_json(json)
# print the JSON string representation of the object
print(BranchRep.to_json())

# convert the object into a dict
branch_rep_dict = branch_rep_instance.to_dict()
# create an instance of BranchRep from a dict
branch_rep_from_dict = BranchRep.from_dict(branch_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


