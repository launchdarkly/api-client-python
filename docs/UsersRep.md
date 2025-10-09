# UsersRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**total_count** | **int** | The total number of users in the environment | 
**items** | [**List[UserRecord]**](UserRecord.md) | Details on the users | 

## Example

```python
from launchdarkly_api.models.users_rep import UsersRep

# TODO update the JSON string below
json = "{}"
# create an instance of UsersRep from a JSON string
users_rep_instance = UsersRep.from_json(json)
# print the JSON string representation of the object
print(UsersRep.to_json())

# convert the object into a dict
users_rep_dict = users_rep_instance.to_dict()
# create an instance of UsersRep from a dict
users_rep_from_dict = UsersRep.from_dict(users_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


