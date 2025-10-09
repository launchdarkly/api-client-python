# PullRequestCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of pull requests | 
**items** | [**List[PullRequestRep]**](PullRequestRep.md) | A list of pull requests | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.pull_request_collection_rep import PullRequestCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestCollectionRep from a JSON string
pull_request_collection_rep_instance = PullRequestCollectionRep.from_json(json)
# print the JSON string representation of the object
print(PullRequestCollectionRep.to_json())

# convert the object into a dict
pull_request_collection_rep_dict = pull_request_collection_rep_instance.to_dict()
# create an instance of PullRequestCollectionRep from a dict
pull_request_collection_rep_from_dict = PullRequestCollectionRep.from_dict(pull_request_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


