# HoldoutsCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SimpleHoldoutRep]**](SimpleHoldoutRep.md) |  | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**total_count** | **int** | The total number of holdouts in this project and environment. | [optional] 

## Example

```python
from launchdarkly_api.models.holdouts_collection_rep import HoldoutsCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of HoldoutsCollectionRep from a JSON string
holdouts_collection_rep_instance = HoldoutsCollectionRep.from_json(json)
# print the JSON string representation of the object
print(HoldoutsCollectionRep.to_json())

# convert the object into a dict
holdouts_collection_rep_dict = holdouts_collection_rep_instance.to_dict()
# create an instance of HoldoutsCollectionRep from a dict
holdouts_collection_rep_from_dict = HoldoutsCollectionRep.from_dict(holdouts_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


